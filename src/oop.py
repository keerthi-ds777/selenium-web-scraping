from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By 
import pandas as pd

import os
from sqlalchemy import create_engine
'''load_dotenv()

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

engine = create_engine(
    f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)'''


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import pandas as pd
import time
import os

def scrape_bus_data(df, df_name: str):
    driver = webdriver.Chrome()

    # Initialize lists to collect scraped data
    bus_name = []
    bus_type = []
    start_time = []
    end_time = []
    rating = []
    total_duration = []
    price = []
    seats_available = []
    route_name = []
    route_link = []

    for i, r in df.iterrows():
        routes = r['Routes']
        links = r['Links']

        try:
            driver.get(links)
            time.sleep(2)
        except Exception as e:
            print(f"[Error] Failed to load {links}: {e}")
            continue

        # Try clicking optional elements
        try:
            elements = driver.find_elements(By.XPATH, f'//a[contains(@href, "{links}")]')
            for element in elements:
                element.click()
                time.sleep(2)
        except:
            pass

        try:
            clicks = driver.find_elements(By.XPATH, '//div[@class="button"]')
            for click in clicks:
                click.click()
        except Exception as e:
            print(f"[Warning] Skipping click step on route {routes}: {e}")
            continue

        # Scroll the page to load all bus data
        scrolling = True
        while scrolling:
            old_page_source = driver.page_source
            ActionChains(driver).key_down(Keys.PAGE_DOWN).perform()
            time.sleep(4)
            new_page_source = driver.page_source
            if old_page_source == new_page_source:
                scrolling = False

        # Extract data
        bus_name_elements = driver.find_elements(By.XPATH, "//div[@class='travelsName___950ec8']")
        bus_type_elements = driver.find_elements(By.XPATH, '//p[contains(@class, "busType___675d0a")]')
        start_time_elements = driver.find_elements(By.XPATH, "//p[contains(@class, 'boardingTime___a78ae0')]")
        end_time_elements = driver.find_elements(By.XPATH, "//p[contains(@class, 'droppingTime___c814da')]")
        rating_elements = driver.find_elements(By.XPATH, '//div[contains(@class, "rating___f7ba20")]')
        price_elements = driver.find_elements(By.XPATH, '//p[@class="finalFare___057afc"]')
        total_duration_elements = driver.find_elements(By.XPATH, '//p[@class="duration___b3a515"]')
        seats_available_elements = driver.find_elements(By.XPATH, '//p[contains(@class, "totalSeats___53250b")]')

        total_buses = len(bus_name_elements)

        for idx in range(total_buses):
            bus_name.append(bus_name_elements[idx].text if idx < len(bus_name_elements) else '')
            bus_type.append(bus_type_elements[idx].text if idx < len(bus_type_elements) else '')
            start_time.append(start_time_elements[idx].text if idx < len(start_time_elements) else '')
            end_time.append(end_time_elements[idx].text if idx < len(end_time_elements) else '')
            rating.append(rating_elements[idx].text if idx < len(rating_elements) else '')
            price.append(price_elements[idx].text if idx < len(price_elements) else '')
            total_duration.append(total_duration_elements[idx].text if idx < len(total_duration_elements) else '')
            seats_available.append(seats_available_elements[idx].text if idx < len(seats_available_elements) else '')
            route_name.append(routes)
            route_link.append(links)

    driver.quit()

    # Create DataFrame
    data = {
        'BusName': bus_name,
        'BusType': bus_type,
        'StartTime': start_time,
        'EndTime': end_time,
        'Rating': rating,
        'Price': price,
        'TotalDuration': total_duration,
        'SeatsAvailable': seats_available,
        'RouteName': route_name,
        'Links': route_link
    }

    df_out = pd.DataFrame(data)

    # Save to CSV
    output_dir = "data/bus_details"
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, f"{df_name}.csv")
    df_out.to_csv(output_path, index=False)

    print(f"✅ Scraping complete. Data saved to: {output_path}")



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
        df.to_csv(r'data\link_route\{}.csv'.format(df_name), index=False)

        driver.quit()

    @staticmethod
    def scrape_bus_data(df, df_name: str):
        driver = webdriver.Chrome()

        # Initialize lists to collect scraped data
        bus_name = []
        bus_type = []
        start_time = []
        end_time = []
        rating = []
        total_duration = []
        price = []
        seats_available = []
        route_name = []
        route_link = []

        for i, r in df.iterrows():
            routes = r['Routes']
            links = r['Links']

            try:
                driver.get(links)
                time.sleep(2)
            except Exception as e:
                print(f"[Error] Failed to load {links}: {e}")
                continue

            # Try clicking optional elements
            try:
                elements = driver.find_elements(By.XPATH, f'//a[contains(@href, "{links}")]')
                for element in elements:
                    element.click()
                    time.sleep(2)
            except:
                pass

            try:
                clicks = driver.find_elements(By.XPATH, '//div[@class="button"]')
                for click in clicks:
                    click.click()
            except Exception as e:
                print(f"[Warning] Skipping click step on route {routes}: {e}")
                continue

            # Scroll the page to load all bus data
            scrolling = True
            while scrolling:
                old_page_source = driver.page_source
                ActionChains(driver).key_down(Keys.PAGE_DOWN).perform()
                time.sleep(4)
                new_page_source = driver.page_source
                if old_page_source == new_page_source:
                    scrolling = False

            # Extract data
            bus_name_elements = driver.find_elements(By.XPATH, "//div[@class='travelsName___950ec8']")
            bus_type_elements = driver.find_elements(By.XPATH, '//p[contains(@class, "busType___675d0a")]')
            start_time_elements = driver.find_elements(By.XPATH, "//p[contains(@class, 'boardingTime___a78ae0')]")
            end_time_elements = driver.find_elements(By.XPATH, "//p[contains(@class, 'droppingTime___c814da')]")
            rating_elements = driver.find_elements(By.XPATH, '//div[contains(@class, "rating___f7ba20")]')
            price_elements = driver.find_elements(By.XPATH, '//p[@class="finalFare___057afc"]')
            total_duration_elements = driver.find_elements(By.XPATH, '//p[@class="duration___b3a515"]')
            seats_available_elements = driver.find_elements(By.XPATH, '//p[contains(@class, "totalSeats___53250b")]')

            total_buses = len(bus_name_elements)

            for idx in range(total_buses):
                bus_name.append(bus_name_elements[idx].text if idx < len(bus_name_elements) else '')
                bus_type.append(bus_type_elements[idx].text if idx < len(bus_type_elements) else '')
                start_time.append(start_time_elements[idx].text if idx < len(start_time_elements) else '')
                end_time.append(end_time_elements[idx].text if idx < len(end_time_elements) else '')
                rating.append(rating_elements[idx].text if idx < len(rating_elements) else '')
                price.append(price_elements[idx].text if idx < len(price_elements) else '')
                total_duration.append(total_duration_elements[idx].text if idx < len(total_duration_elements) else '')
                seats_available.append(seats_available_elements[idx].text if idx < len(seats_available_elements) else '')
                route_name.append(routes)
                route_link.append(links)

        driver.quit()

        # Create DataFrame
        data = {
            'BusName': bus_name,
            'BusType': bus_type,
            'StartTime': start_time,
            'EndTime': end_time,
            'Rating': rating,
            'Price': price,
            'TotalDuration': total_duration,
            'SeatsAvailable': seats_available,
            'RouteName': route_name,
            'Links': route_link
        }

        df_out = pd.DataFrame(data)

        # Save to CSV
        output_dir = "data/bus_details"
        os.makedirs(output_dir, exist_ok=True)
        output_path = os.path.join(output_dir, f"{df_name}.csv")
        df_out.to_csv(output_path, index=False)

        print(f"✅ Scraping complete. Data saved to: {output_path}")


