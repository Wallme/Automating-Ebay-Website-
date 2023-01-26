import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select
import pytest

class Testsample():
    @pytest.fixture()
    def test_setup(self):
        global driver
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        yield
        driver.close()
        print('Test Completed Successfully')





#LOGIN TO EBAY WEBSITE....(USING ID LOCATORS MOSTLY SHOULD BE DONE)
    def test_login(self,test_setup):

        driver.get("https://www.ebay.com/")
        driver.find_element(By.XPATH,'//span[@id="gh-ug"]//a[contains(text(),"Sign in")]').click()
        #time.sleep(30)
        driver.find_element(By.ID,'userid').send_keys('abcdefgh')
        driver.find_element(By.ID,'signin-continue-btn').click()
        time.sleep(4)
        driver.find_element(By.ID,'pass').send_keys('********')
        driver.find_element(By.ID,'sgnBt').click()
        #time.sleep(30)
        time.sleep(4)
#NAVIGATE TO THE NEW ADDRESS AND UPDATE NEW ADDRESS....(USING ID LOCATORS MOSTLY SHOULD BE DONE)
        # # driver.maximize_window()
        ven = driver.find_element(By.ID,'gh-ug')
        achains = ActionChains(driver)
        achains.move_to_element(ven).perform()
        time.sleep(4)
        driver.find_element(By.LINK_TEXT,'Account settings').click()
        time.sleep(4)
        driver.maximize_window()
        driver.find_element(By.XPATH,"//a[normalize-space()='Addresses']").click()
        time.sleep(4)
        driver.find_element(By.XPATH,"//a[@aria-label='Edit Shipping address opens in new window or tab.']").click()
        time.sleep(4)
        # driver.find_element(By.ID,'pass').send_keys('********')
        # time.sleep(4)
        # driver.find_element(By.ID,'sgnBt').click()
        # time.sleep(4)
        driver.find_element(By.XPATH,"//a[normalize-space()='Edit']").click()
        time.sleep(4)
        driver.find_element(By.ID,'s0-0-17-6-addressLine2-field-addressLine2-field').send_keys('Your Street Address 2')
        time.sleep(4)
        driver.find_element(By.XPATH,"//button[normalize-space()='Save']").click()
        time.sleep(4)
        driver.back()
        driver.back()
        driver.back()
        driver.back()

        # driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        # driver.get("https://www.ebay.com/")
        # actions = ActionChains(driver)
        # sign_in = driver.find_element(By.XPATH,'//b[normalize-space()="********"]').click()
        # actions.move_to_element(sign_in).perform()
        driver.find_element(By.XPATH, "//input[@id='gh-ac']").click()
        driver.find_element(By.XPATH, "//input[@id='gh-ac']").send_keys('Samsung A73')
        time.sleep(4)
        driver.find_element(By.XPATH, "//input[@id='gh-btn']").click()
        time.sleep(4)

        #selecting a item using xpath:

        driver.find_element(By.XPATH,"//span[contains(text(),'For Samsung Galaxy A53 A73 A33 5G Case Soft Liquid')]").click()
        fHandle = driver.current_window_handle
        print(fHandle)
        time.sleep(4)
        handles = []
        handles = driver.window_handles
        for handle in handles:
            print(handle)


        #VIEWING THE CART
        newHandle = handles[1]
        driver.switch_to.window(newHandle)
        addinp = driver.find_element(By.XPATH, "//input[@id='gh-ac']").click()
        driver.switch_to.default_content()
        driver.switch_to.window(handles[0])
        vie = driver.find_element(By.ID,'gh-cart-n')
        achains = ActionChains(driver)
        achains.move_to_element(vie).perform()
        time.sleep(4)
        driver.find_element(By.LINK_TEXT,'View cart').click()
        time.sleep(4)


        #SIGNOUT
        sio = driver.find_element(By.ID,'gh-ug')
        achains = ActionChains(driver)
        achains.move_to_element(sio).perform()
        time.sleep(4)
        driver.find_element(By.LINK_TEXT,'Sign out').click()
        time.sleep(4)

























