# -*- coding: utf-8 -*-

import random
import time
import unittest

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
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

    '''
    def test_guideBookTourRegister(self):
    #1. User registers and enters site with valid credentials.

        driver = self.driver
        wait = self.wait

        # String variables for new user credentials
        randomID = str(random.randint(1, 1000))
        emailStr = "test_email"+randomID+"@gmail.com"
        passwordStr = "test"
        nameStr = "Test Test"
        usernameStr = "autoTester"+randomID

        #Values for drop-down lists
        educationChoice = "Немає"
        genderChoice = "Інше"
        yobChoice = "1949"

        #Values for text areas
        mailingAdressStr = "Somewhere, over the rainbow"
        goalsStr = "I am just a little robot, trying to test your site"

        register_MenuEntryXpath = "//a[@href='http://edx.prometheus.org.ua/register']"
        registerButton = driver.find_element_by_xpath(register_MenuEntryXpath)
        wait.until(lambda driver: registerButton)

        #unable to get single Register Button object(there are two similar objects for white and black menus),
        #  so just opening a next step  after verification of registration button presence

        driver.get("http://edx.prometheus.org.ua/register")

        #List of Xhath for elements
        emailField = driver.find_element_by_xpath("//li/input[@id='email']")
        passwordField = driver.find_element_by_xpath("//li/input[@id='password']")
        nameField = driver.find_element_by_xpath("//li/input[@id='name']")
        usernameField = driver.find_element_by_xpath("//li/input[@id='username']")
        educationDDList = driver.find_element_by_xpath("//li/div/select[@id='education-level']")
        genderDDList = driver.find_element_by_xpath("//li/div/select[@id='gender']")
        yobDDList = driver.find_element_by_xpath("//li/div/select[@id='yob']")
        mailingAdressField = driver.find_element_by_xpath("//ol/li/textarea[@id='address-mailing']") #notify about this
        goalsAreaField = driver.find_element_by_xpath("//ol/li/textarea[@id='goals']")
        termsOfServiceBox = driver.find_element_by_xpath("//div/input[@id='tos-yes']")
        honorCodeBox = driver.find_element_by_xpath("//div/input[@id='honorcode-yes']")
        submitButton = driver.find_element_by_xpath("//div/button[@id='submit']")

        #Entering credentials

        wait.until(lambda driver: emailField)
        emailField.clear()
        emailField.send_keys(emailStr)
        time.sleep(1)

        wait.until(lambda driver: nameField)
        nameField.clear()
        nameField.send_keys(nameStr)
        time.sleep(1)

        wait.until(lambda driver: usernameField)
        usernameField.clear()
        usernameField.send_keys(usernameStr)
        time.sleep(1)

        wait.until(lambda driver: passwordField)
        passwordField.clear()
        passwordField.send_keys(passwordStr)
        time.sleep(1)

        #Checking education, gender and Birth year drop-down lists

        wait.until(lambda driver: educationDDList)
        Select(educationDDList).select_by_visible_text(educationChoice)
        time.sleep(1)

        wait.until(lambda driver: genderDDList)
        Select(genderDDList).select_by_visible_text(genderChoice)
        time.sleep(1)

        wait.until(lambda driver: yobDDList)
        Select(yobDDList).select_by_visible_text(yobChoice)
        time.sleep(1)

        #Filling text areas: mailing adress and goals for registration

        wait.until(lambda driver: mailingAdressField)
        mailingAdressField.clear()
        mailingAdressField.send_keys(mailingAdressStr)
        time.sleep(1)

        wait.until(lambda driver: goalsAreaField)
        goalsAreaField.clear()
        goalsAreaField.send_keys(goalsStr)
        time.sleep(1)

        #checking honor code and conditions terms checkboxes
        wait.until(lambda driver: termsOfServiceBox)
        termsOfServiceBox.click()
        time.sleep(1)

        wait.until(lambda driver: honorCodeBox)
        honorCodeBox.click()
        time.sleep(1)

        #pressing "Submit" button and ending with test: uncomment this strings for new user registration
        #wait.until(lambda driver: submitButton)
        #submitButton.click()
        #time.sleep(4)

        #assertion that we are at the valid URL
        #assert driver.current_url == "http://courses.prometheus.org.ua/dashboard"
        time.sleep(1)

        #NOTE: if you want to proceed with generated user info, please see the console log for generated info output
        #  and note in down.
        #Later in our tests we will use only one pre-registered and email confirmed account
        #

    '''

    def test_searchAndBrowseCourses(self):
        #2. User is able to login with email and/or username he registered, browse some courses to choose and attend

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

        Dashboard.verify_dashboard_elements(self, emailStr, usernameStr, nameStr, driver)

        # And let's explore couple of courses and decide what to learn

        #checking for empty dashboard
        try:
            findCoursesButton = driver.find_element_by_xpath("//section/a[@href='/courses']")
            wait.until(lambda driver: findCoursesButton)
            findCoursesButton.click()

        #if it's not empty then initiating clean-up script
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

        #short checkout on specialization page
        # for WP web-interface the string current_url should be decoded to utf-8 in order to verification work properly
        wait.until(lambda driver: driver.current_url == "http://prometheus.org.ua/civileducation/".decode('utf-8'))
        titleElement = driver.find_element_by_tag_name('h1')
        assert titleElement.text == "Громадянська освіта".decode('utf-8')

        #closing specialization tab and proceeding with cources page
        driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 'w')
        driver.switch_to_window(driver.window_handles[0])

        #Choosing some random course to attend
        singleCourseButton = Courses.get_random_course_button(self, driver)
        courseUrl = singleCourseButton.get_attribute("href")
        singleCourseButton.click()


        #some courses are leading to edx. subdomain and others are leading to cources. subdomain. At the first case
        # browser anyway redirects user to .courses subdomain but we are unable to verify that we are leading to desired
        # page: driver.current_url is courses... but courseUrl is edx... To fix this issue we are editing the
        # mismatching string(courseUrl) to be matched as courses. subdomain instance

        if "edx" in courseUrl.encode('utf-8'):
            courseUrl = BasicActions.convert_subdomains(self, courseUrl)

        driver.switch_to_window(driver.window_handles[-1])
        wait.until(lambda driver: driver.current_url.encode('utf-8') == courseUrl.encode('utf-8'))

        #submitting under the course
        Courses.submit_course(self, driver)

        time.sleep(2)

    def tearDown(self):
        self.driver.quit()

    if __name__ == "__main__":
        unittest.main()
