from configs.urls import Urls
from selenium import webdriver
import pytest
import random as r

@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.get(Urls.HOME_PAGE_URL)
    yield driver
    driver.quit()

@pytest.fixture(scope='function')
def user():
    name = ('mike', 'john', 'nick', 'alex')
    surname = ('smith', 'jackson', 'brown', 'luke')
    email = r.choice(name) + r.choice(surname) + '18' + str(r.randint(100, 999)) + '@yandex.ru'
    psw = r.randint(100000, 999999)
    new_psw = r.randint(100000, 999999)
    return {
        'name': r.choice(name),
        'surname': r.choice(surname),
        'email': email,
        'password': psw,
        'new_password': new_psw
    }
