from unittest import TestCase
from selenium.webdriver.common.by import By
from initialise_tests import Initialise
from models.profile import Profile
from models.account import Account
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
import multiprocessing
import time
from selenium.webdriver.support.ui import Select
import random
import string


class SeleniumTest(TestCase, Initialise):
    def setUp(self):
        self.init_app()
        self.account_id = self.create_account()

        # setup selenium
        options = ChromeOptions()
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--no-sandbox')
        options.add_argument("use-fake-ui-for-media-stream")
        options.add_argument('--headless')

        service = ChromeService(executable_path=ChromeDriverManager().install())
        self.driver = webdriver.Chrome(options=options, service=service)

        self.process = multiprocessing.get_context('fork').Process(target=self.flask_app.run, args=())
        self.process.start()

    def tearDown(self):
        Account.objects().delete()
        Profile.objects().delete()
        self.driver.close()
        self.process.kill()

    def test_login(self):
        self.driver.get("http://127.0.0.1:5000/")
        time.sleep(1)

        self.driver.find_element(By.XPATH,
                                 "/html/body/main/div/div[2]/div/a[1]/button").click()

        self.driver.find_element(By.ID, "email").send_keys("test@test.com")
        self.driver.find_element(By.ID, "password").send_keys("test")
        self.driver.find_element(By.ID, "submit").click()
        assert "Welcome" in self.driver.page_source


    def test_register_funnel(self):
        characters = string.ascii_letters + string.digits
        email = ''.join(random.choice(characters) for i in range(20)) + "@test.com"

        self.driver.get("http://127.0.0.1:5000/")
        time.sleep(1)

        # Index page
        self.driver.find_element(By.XPATH,
                                 "/html/body/main/div/div[2]/div/a[2]/button").click()

        # Register page
        self.driver.find_element(By.ID, "forename").send_keys("forename")
        self.driver.find_element(By.ID, "surname").send_keys("surname")
        self.driver.find_element(By.ID, "email").send_keys("test_email@gmail.com")
        self.driver.find_element(By.ID, "password").send_keys("password")
        self.driver.find_element(By.ID, "confirm_psw").send_keys("password")
        self.driver.find_element(By.ID, "submit").click()

        # Create Profile page
        self.driver.find_element(By.ID, "bio").send_keys("test")
        self.driver.find_element(By.ID, "email").send_keys("test@test.com")
        self.driver.find_element(By.ID, "job").send_keys("test")
        self.driver.find_element(By.ID, "field").send_keys("test")
        self.driver.find_element(By.ID, "phone").send_keys(98463920)
        self.driver.find_element(By.ID, "hours").send_keys("test")
        self.driver.find_element(By.ID, "location").send_keys("test")
        self.driver.find_element(By.ID, "registration").send_keys("test")
        self.driver.find_element(By.ID, "years").send_keys("2")
        self.driver.find_element(By.ID, "fee").send_keys("2")
        self.driver.find_element(By.XPATH, '/html/body/main/div/div[2]/div/form/div[11]/div[1]/input').send_keys("test")
        self.driver.find_element(By.XPATH, '/html/body/main/div/div[2]/div/form/div[12]/div[1]/input').send_keys("test")
        self.driver.find_element(By.XPATH, '/html/body/main/div/div[2]/div/form/div[13]/div[1]/input').send_keys("test")
        self.driver.find_element(By.XPATH, '/html/body/main/div/div[2]/div/form/div[14]/div[1]/input').send_keys("test")
        self.driver.find_element(By.XPATH, '/html/body/main/div/div[2]/div/form/div[15]/div[1]/input').send_keys("test")
        self.driver.find_element(By.ID, "submit").click()

        # Create Avatar page
        select = Select(self.driver.find_element(By.NAME, 'avatar'))
        select.select_by_value('doctor_m1')

        select = Select(self.driver.find_element(By.NAME, 'voice'))
        select.select_by_value('male')

        self.driver.find_element(By.XPATH, '/html/body/main/div/div[2]/div/form/button').click()

        # Finish page
        assert "Your card's AR experience" in self.driver.page_source



    def test_ar(self):
        self.driver.get("http://127.0.0.1:5000/ar2/62e6f4e8d1d8472cf1002c40")

        self.driver.switch_to.frame(self.driver.find_element(By.ID, "app-frame"))
        time.sleep(3)

        assert self.driver.find_element(By.ID, "application-canvas")
