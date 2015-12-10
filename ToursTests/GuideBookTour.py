# -*- coding: utf-8 -*-

import random
import time
import unittest

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException, WebDriverException, \
    NoSuchWindowException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

from BasicElements import *

'''
THE IDEA
The guidebook tour stets the software’s ability to deliver its advertised functionality.
'''


class GuideBookTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("http://prometheus.org.ua")
        self.wait = WebDriverWait(self.driver, 10)

        # preregistered and confirmed user credentials
        self.emailStr = "vlad.belogorodskiy@gmail.com"
        self.passwordStr = "test"
        self.usernameStr = "autoTester"
        self.nameStr = "Test Test"

    def test_guideBookTourRegister(self):
        # 1. User registers and enters site with valid credentials.

        driver = self.driver
        wait = self.wait
        randomID = str(random.randint(1, 1000))

        course_registration = Registration(driver, randomID, "test_email"+randomID+"@gmail.com", "test", "Test Test", "autoTester"+randomID, "Немає", "Інше", "1949", "some adress", "I'ma robot man")

        course_registration.verify_and_register()
        course_registration.enter_email()
        course_registration.enter_name()
        course_registration.enter_username()
        course_registration.enter_password()
        course_registration.fill_education_list()
        course_registration.fill_birth_year_list()
        course_registration.fill_gender_list()
        course_registration.fill_mailing_adress_area()
        course_registration.fill_goals_area()
        course_registration.check_honor_code_box()
        course_registration.check_terms_of_service_box()

        #commented this strings in order to prevent cloning of test users
        #course_registration.registration_submit()
        #wait.until(lambda driver: driver.current_url == "http://courses.prometheus.org.ua/dashboard")
        #assert driver.current_url.encode('utf-8') == "http://courses.prometheus.org.ua/dashboard"


    def test_searchAndBrowseCourses(self):
        # 2. User is able to login with email and/or username he registered, browse some courses to choose and attend

        driver = self.driver
        wait = self.wait

        # again, getting URL directly because of two similar meny entries in WordPress interface and unability to
        # indicate a single element
        driver.get("http://courses.prometheus.org.ua/login")

        # credentials for user
        emailStr = self.emailStr
        passwordStr = self.passwordStr
        usernameStr = self.usernameStr
        nameStr = self.nameStr

        BasicActions.user_login(self, emailStr, passwordStr, driver)

        # waiting to enter Dashboard menu
        wait.until(lambda driver: driver.current_url == "http://courses.prometheus.org.ua/dashboard")

        # verification of key elements for dashboard menu
        for i in range(0,9,1):
            Dashboard.verify_dashboard_elements(self, emailStr, usernameStr, nameStr, driver)

            # And let's explore couple of courses and decide what to learn

            # checking for empty dashboard
            try:
                findCoursesButton = driver.find_element_by_xpath("//section/a[@href='/courses']")
                wait.until(lambda driver: findCoursesButton)
                findCoursesButton.click()

            # if it's not empty then initiating clean-up script
            except(NoSuchElementException):
                Dashboard.dashboard_cleanup(self, driver)
                findCoursesButton = driver.find_element_by_xpath("//section/a[@href='/courses']")
                wait.until(lambda driver: findCoursesButton)
                findCoursesButton.click()

            Courses.verify_courses_elements(self, driver)

            civEduButton = driver.find_element_by_xpath("//div/a[@href='http://prometheus.org.ua/civileducation/']")
            wait.until(lambda driver: civEduButton)
            civEduButton.click()
            driver.switch_to_window(driver.window_handles[-1])

            # short checkout on specialization page
            # for WP web-interface the string current_url should be decoded to utf-8 in order to verification work properly

            # closing specialization tab and proceeding with cources page
            if len(driver.window_handles) > 1:
                driver.switch_to_window(driver.window_handles[-1])
                driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 'w')
                try:
                    driver.switch_to_window(driver.window_handles[0])
                except(NoSuchWindowException):
                    pass

            # Choosing some random course to attend
            driver.switch_to_window(driver.window_handles[-1])
            singleCourseButton = Courses.get_random_course_button(self, driver)

            courseUrl = singleCourseButton.get_attribute("href")
            time.sleep(1)
            singleCourseButton.click()

            # some courses are leading to edx. subdomain and others are leading to cources. subdomain. At the first case
            # browser anyway redirects user to .courses subdomain but we are unable to verify that we are leading to desired
            # page: driver.current_url is courses... but courseUrl is edx... To fix this issue we are editing the
            # mismatching string(courseUrl) to be matched as courses. subdomain instance

            if "edx" in courseUrl.encode('utf-8'):
                courseUrl = BasicActions.convert_subdomains(courseUrl)
            else:
                courseUrl = courseUrl
            driver.switch_to_window(driver.window_handles[-1])
            try:
                wait.until(lambda driver: driver.current_url.encode('utf-8') == courseUrl.encode('utf-8'))
            except(TimeoutException):
                driver.switch_to_window(driver.window_handles[-1])
                wait.until(lambda driver: driver.current_url.encode('utf-8') == courseUrl.encode('utf-8'))
                pass

            # submitting under the course
            Courses.submit_course(self, driver)

        time.sleep(2)


    def tearDown(self):
        self.driver.quit()


    if __name__ == "__main__":
        unittest.main()
