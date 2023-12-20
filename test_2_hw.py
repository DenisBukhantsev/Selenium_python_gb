import yaml
from module import Site
import pytest
import  time
with open("testdata.yaml", encoding="utf-8") as f:
    test_data = yaml.safe_load(f)

site = Site(test_data["address"])

def test_step1(x_selector1, x_selector2, btn_selector, add_post_selector, add_title, add_content, add_description,
               save_post, check_title, title_name):

    input1 = site.find_element("xpath", x_selector1)
    input1.send_keys(test_data["login"])

    input2 = site.find_element("xpath", x_selector2)
    input2.send_keys(test_data["password"])

    btn = site.find_element("scc", btn_selector)
    btn.click()

    time.sleep(test_data["sleep_time"])

    btn = site.find_element("xpath", add_post_selector)
    btn.click()

    input3 = site.find_element("xpath", add_title)
    input3.send_keys(test_data["title"])

    input4 = site.find_element("xpath", add_description)
    input4.send_keys(test_data["description"])

    input5 = site.find_element("xpath", add_content)
    input5.send_keys(test_data["content"])

    btn = site.find_element("xpath", save_post)
    btn.click()

    time.sleep(test_data["sleep_time"])

    code_label = site.find_element("xpath", check_title).text
    assert code_label == title_name, "test 'add post' Failed"

    site.driver.close()







