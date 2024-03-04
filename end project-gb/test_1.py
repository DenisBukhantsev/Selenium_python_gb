import pytest
import yaml

import logging
from test_page import OperationsHelper


with open("./testdata.yaml") as f:
    testdata = yaml.safe_load(f)


def test_step1(browser):
    logging.info("Test login_negative Starting")
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login("test")
    testpage.enter_pass("test")
    testpage.click_login_button()
    assert testpage.get_error_text() == "401", "test_login_negative FAILED"


def test_contact_us(browser):
    logging.info("Test add_post Starting")
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login(testdata["login"])
    testpage.enter_pass(testdata["password"])
    testpage.click_login_button()
    testpage.click_contact_button()
    testpage.add_name(testdata["u_name"])
    testpage.add_email(testdata["u_email"])
    testpage.add_contact_content(testdata["content_contact"])
    testpage.click_contact_us_button()
    assert testpage.get_alert_message() == "Form successfully submitted", "test contact us FAILED!"


def test_about_us(browser):
    logging.info("Test add_post Starting")
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login(testdata["login"])
    testpage.enter_pass(testdata["password"])
    testpage.click_login_button()
    testpage.click_about_us()
    testpage.get_about_page_text()
    testpage.check_about_page_title_font_size()
    assert testpage.check_about_page_title_font_size() == "32px"

