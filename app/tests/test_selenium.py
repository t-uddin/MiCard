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


class SeleniumTest(TestCase, Initialise):
    def setUp(self):
        self.init_app()
        self.account_id = self.create_account()

        # setup selenium
        options = ChromeOptions()
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--no-sandbox')
        # options.add_argument('--headless')
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

