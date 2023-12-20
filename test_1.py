import yaml
from module import Site
import pytest

with open("testdata.yaml", encoding="utf-8") as f:
    test_data = yaml.safe_load(f)
site = Site(test_data["address"])
#sccselector = "span.mdc-text-field__ripple"
#print(site.get_element_property("scc", sccselector, "height"))
#x_path = '//*[@id="login"]/div[3]/button/div'
#print(site.get_element_property("xpath", x_path, "color"))

def test_step1():
    x_selector1 = """//*[@id="login"]/div[1]/label/input"""
    input1 = site.find_element("xpath", x_selector1)
    input1.send_keys("test")
    x_selector2 = """//*[@id="login"]/div[2]/label/input"""
    input2 = site.find_element("xpath", x_selector2)
    input2.send_keys("test")
    btn_selector = "button"
    btn = site.find_element("scc", btn_selector)
    btn.click()
    x_selector3 = '//*[@id="app"]/main/div/div/div[2]/h2'
    err_label = site.find_element("xpath", x_selector3)
    assert err_label.text == "401"
    #print(err_label.text)



