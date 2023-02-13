import json
import time

from allure_commons._allure import attach
from allure_commons.types import AttachmentType
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from Pages.BasePage import BasePage
from Pages.BmiPage import BmiPage

data = json.load(open("Resources/config.json"))


# This environment page is used as hooks page. Here we can notice that we have used before, after hooks along side with some step hooks.


def before_scenario(context, scenario):
    context.driver = webdriver.Chrome(ChromeDriverManager().install())
    time.sleep(5)
    basepage = BasePage(context.driver)
    context.bmipage = BmiPage(basepage)
    context.stepid = 1
    context.driver.get(data['BMIWEBURL'])
    context.driver.maximize_window()
    context.driver.implicitly_wait(3)


def after_step(context, step):
    attach(context.driver.get_screenshot_as_png(), name=context.stepid, attachment_type=AttachmentType.PNG)
    context.stepid = context.stepid + 1


def after_scenario(context, scenario):
    context.driver.close()



