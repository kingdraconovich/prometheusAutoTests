# -*- coding: utf-8 -*-
import unittest
import time
import random
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys


# method to validate all necessary elemens
def verify_courses_elements(self, driver):
    wait = self.wait

    wait.until(lambda driver: driver.current_url.encode('utf-8') == "http://prometheus.org.ua/courses/")

    # verification for main categories: specializations, Available now, Registration open
    wait.until(lambda driver: driver.find_element_by_xpath("//h3[contains(., 'Цикли курсів')]"))
    wait.until(lambda driver: driver.find_element_by_xpath("//h3[contains(., 'Доступні зараз')]"))
    wait.until(lambda driver: driver.find_element_by_xpath("//h3[contains(., 'Відкрито реєстрацію')]"))


# method to attend a random course
def get_random_course_button(self, driver):
    self.wait.until(lambda driver: driver.current_url.encode('utf-8') == "http://prometheus.org.ua/courses/".encode('utf-8'))
    coursesList = driver.find_elements_by_xpath("//div/a[(contains(@href, 'http://courses.') or  contains(@href, 'http://edx.')) and  (contains(@target, 'blank'))]")
    randomCourseButton = coursesList[random.randint(0, (len(coursesList)-1))]
    return randomCourseButton


# method for course submission
def submit_course(self, driver):

    coursesDashboardUrl = "http://courses.prometheus.org.ua/dashboard"

    self.wait.until(lambda driver: driver.find_element_by_xpath("//a[contains(@class, 'register')]"))
    courseRegisterButton = driver.find_element_by_xpath("//a[contains(@class, 'register') and contains(@href, '#')]")
    courseRegisterButton.click()
    time.sleep(1)  # mandatory sleep to give page time to reload
    # checking if it is a pre-paid course and choosing free course submission option
    if driver.current_url.encode('utf-8') == coursesDashboardUrl:
        self.wait.until(lambda driver: driver.current_url.encode('utf-8') == coursesDashboardUrl)

    elif 'course_modes' in driver.current_url.encode('utf-8'):
        submitInHonorModeButton = driver.find_element_by_xpath(
            "//input[contains(@type, 'submit') and contains(@name, 'honor_mode')]")
        self.wait.until(lambda driver: submitInHonorModeButton)
        submitInHonorModeButton.click()
        self.wait.until(lambda driver: driver.current_url.encode('utf-8') == coursesDashboardUrl)
