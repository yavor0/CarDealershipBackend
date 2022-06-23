from email.mime import image
from django.db import close_old_connections
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from thefuzz import process
from thefuzz import fuzz
import random
import os
import time


class MobileUploader():
    def __init__(self):
        # ------------Only for development------------
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        chrome_options.add_argument(r"user-data-dir=C:\Users\Yavor\Desktop\CarDealershipBackend\dealership\mobile_upload\user_data")
        # -------------------------------------------
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
        
        self.dealership_location_region = 'София'
        self.dealership_location_city = 'гр. София'
        self.dealership_phone_number = '0878786309'

    def fill_car_make(self, car_make):
        all_car_makes_element = self.driver.find_element(by=By.XPATH, value='//*[@class="sw145new"][@name="f5"]')
        all_car_makes = all_car_makes_element.text.split("\n")
        dropdown_with_car_makes = Select(all_car_makes_element)
        closest_car_make = process.extractOne(car_make, all_car_makes)
        dropdown_with_car_makes.select_by_value(closest_car_make[0])

    def fill_car_model(self, car_model):
        all_car_models_element = self.driver.find_element(by=By.XPATH, value='//*[@class="sw145new"][@name="f6"]')
        all_car_models = all_car_models_element.text.split("\n")
        dropdown_with_car_models = Select(all_car_models_element)
        closest_car_model = process.extractOne(car_model, all_car_models)
        dropdown_with_car_models.select_by_value(closest_car_model[0])

    def fill_engine_type(self, engine_type):
        all_engine_types = self.driver.find_element(by=By.XPATH, value='//*[@class="sw145new"][@name="f8"]')
        dropdown_with_engine_types = Select(all_engine_types)
        dropdown_with_engine_types.select_by_value(engine_type)

    def fill_horse_power(self, horse_power):
        self.driver.find_element(by=By.XPATH, value='//*[@class="sw145new"][@name="f9"]').send_keys(horse_power)

    def fill_transmission_type(self, transimission_type):
        all_transmission_types = self.driver.find_element(by=By.XPATH, value='//*[@class="sw300new"][@name="f10"]')
        dropdown_with_transmissions_types = Select(all_transmission_types)
        dropdown_with_transmissions_types.select_by_value(transimission_type)

    def fill_category(self, car_category):
        all_categories = self.driver.find_element(by=By.XPATH, value='//*[@class="sw300new"][@name="f11"]')
        dropdown_with_categories = Select(all_categories)
        dropdown_with_categories.select_by_value(car_category)

    def fill_price(self, price):
        self.driver.find_element(by=By.XPATH, value='//*[@class="sw145new"][@name="f12"]').send_keys(price)

    def fill_year(self, year):
        # ------------Select the month------------
        all_months_element = self.driver.find_element(by=By.XPATH, value='//*[@class="sw145new"][@name="f14"]')
        all_months_names = all_months_element.text.split('\n')
        random_month = random.choice(all_months_names)
        dropdown_with_months = Select(all_months_element)
        dropdown_with_months.select_by_value(random_month)
        # --------------------------------------
        
        # ------------Select the year------------
        all_years_element = self.driver.find_element(by=By.XPATH, value='//*[@class="sw145new"][@name="f15"]')
        dropdown_with_years = Select(all_years_element)
        dropdown_with_years.select_by_value(str(year))
        # --------------------------------------

    def fill_mileage(self, mileage):
        self.driver.find_element(by=By.XPATH, value='//*[@class="sw145new"][@name="f16"]').send_keys(mileage)

    def fill_location(self):
        all_regions_element = self.driver.find_element(by=By.XPATH, value='//*[@class="sw145new"][@name="f18"]')
        dropdown_with_regions = Select(all_regions_element)
        dropdown_with_regions.select_by_value(self.dealership_location_region)

        # Wait for the page to reload
        all_cities_element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@class="sw145new"][@name="f19"]')))

        dropdown_with_cities = Select(all_cities_element)
        dropdown_with_cities.select_by_value(self.dealership_location_city)

    def fill_phone_number(self):
        self.driver.find_element(by=By.XPATH, value='//*[@class="sw150new"][@name="f22"]').send_keys(self.dealership_phone_number)


    def get_message_key(self):
        return input("Enter message key: ")

    def fill_images(self, image_paths):
        for image_path in image_paths:
            if not image_path.endswith(".png"):
                self.driver.find_element_by_xpath('/html/body/div[1]/div[5]/div[3]/div/ul/div/input').send_keys(image_path)

    def fill_descriptions(self, description):
        self.driver.find_element(By.XPATH, '//*[@id="mainholder"]/table[3]/tbody/tr/td/form/table[4]/tbody/tr/td[1]/table/tbody/tr[2]/td/textarea').send_keys(description)

    def run(self, car, car_images):
    
        self.driver.get("https://www.mobile.bg/pcgi/mobile.cgi?pubtype=1&act=1")

        # ------------Fill car details------------
        self.fill_car_make(car.make)
        self.fill_car_model(car.model)
        self.fill_engine_type(car.engine_type) 
        self.fill_horse_power(car.power)
        self.fill_transmission_type(car.transmission)
        self.fill_category(car.type)
        self.fill_price(car.price)
        self.fill_year(car.year)
        self.fill_mileage(car.mileage)
        # self.fill_descriptions(car.description) <---------------------- fix for later
        # ----------------------------------------

        # ------------Fill dealership details------------
        self.fill_location()
        self.fill_location()
        self.fill_phone_number()
        # -----------------------------------------------


        # ------------Fill car images------------
        self.driver.execute_script("document.getElementById('pubButton').click()")
        self.fill_images(car_images)
        time.sleep(0.3) # precautionary wait
        self.driver.find_element(By.XPATH, '/html/body/div[1]/div[7]/a').click()


        # ------------Select type of listing and publish------------
        self.driver.find_element(By.XPATH, '/html/body/div[1]/div[4]/div[3]/div/div[2]/form/div[1]/label/input').click()
        self.driver.find_element(By.XPATH, '/html/body/div[1]/div[4]/div[4]/a').click()
