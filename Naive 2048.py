"""
This program is a naive 2048 AI that plays by moving up, down left and then right.
Inspired by the python programming tutorial Automate the Boring Stuff with Python by Al Sweigart
Created by Matthew Chu: 18/9/20
Last edited: on 18/9/20
"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
if __name__=="__main__":
    # Initialize browser
    browser = webdriver.Chrome("C:\\Web Drivers\\chromedriver.exe")
    browser.get("https://gabrielecirulli.github.io/2048/")

    html_element = browser.find_element_by_tag_name("html")
    retry_button = browser.find_element_by_class_name("retry-button")

    # Play until retry button appears
    while not retry_button.is_displayed():
        html_element.send_keys(Keys.LEFT)
        html_element.send_keys(Keys.RIGHT)
        html_element.send_keys(Keys.UP)
        html_element.send_keys(Keys.DOWN)
    browser.close()