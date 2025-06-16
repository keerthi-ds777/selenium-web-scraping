from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By 
import pandas as pd

from dotenv import load_dotenv
import os
from sqlalchemy import create_engine
load_dotenv()

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

engine = create_engine(
    f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)





class redbus:
    @staticmethod
    def getting_link(file_path: str, df_name: str):
        driver = webdriver.Chrome()
        driver.get(file_path)
        wait = WebDriverWait(driver, 20)
        links = []
        routes = []

        for i in range(1, 3):
            paths = driver.find_elements(By.XPATH, '//a[@class="route"]')
            for link in paths:
                d = link.get_attribute('href')
                links.append(d)
                routes.append(link.text)
            try:
                pagination = wait.until(ec.presence_of_element_located((By.XPATH, '//*[@class="DC_117_paginationtable"]')))
                next_page = pagination.find_element(By.XPATH, f'//div[@class="DC_117_page_tabs" and text()={i + 1}]')
                next_page.click()
            except Exception as e:
                print(f'No more pages to paginate to at step {i}. Exception: {e}')
                break

        df = pd.DataFrame({'Routes': routes, 'Links': links})
        df.to_sql(df_name, con=engine, if_exists="replace", index=False)
        driver.quit()

    @staticmethod
    def scrape_bus_data(df, df_name: str):
      pass