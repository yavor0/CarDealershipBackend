import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from thefuzz import process
from thefuzz import fuzz
from selenium.webdriver.support.ui import Select

# ------------Only for development------------
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument(r"user-data-dir=C:\Users\Yavor\Desktop\CarDealershipBackend\mobile_upload_tests\user_data")
# -------------------------------------------


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
driver.get("https://www.mobile.bg/pcgi/mobile.cgi?pubtype=1&act=1")



print("------------------------------------------------------------------\n")



def fill_car_make(car_make):
    all_car_makes_element = driver.find_element(by=By.XPATH, value='//*[@class="sw145new"][@name="f5"]')
    all_car_makes = all_car_makes_element.text.split("\n")
    dropdown_with_car_makes = Select(all_car_makes_element)
    closest_car_make = process.extractOne(car_make, all_car_makes)
    dropdown_with_car_makes.select_by_value(closest_car_make[0])

def fill_car_model(car_model):
    all_car_models_element = driver.find_element(by=By.XPATH, value='//*[@class="sw145new"][@name="f6"]')
    all_car_models = all_car_models_element.text.split("\n")
    dropdown_with_car_makes = Select(all_car_models_element)
    closest_car_model = process.extractOne(car_model, all_car_models)
    dropdown_with_car_makes.select_by_value(closest_car_model[0])

my_car_make = "Alfa Romeo"
my_car_model = "164"
fill_car_make(my_car_make)
fill_car_model(my_car_model)

print("\n------------------------------------------------------------------")