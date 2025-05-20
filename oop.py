from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys
import pandas as pd


class redbus :
   
        
    
    def getting_link(self,link,route,file_path,df_name:str):
        
        driver = webdriver.Chrome()
        driver.get(link)

        
        wait = WebDriverWait(driver, 20)
      
        links = []
        routes = []

        # Retrieve route links
        for i in range(1, 3):
            # Use find_elements to get a list of elements
            paths = driver.find_elements(By.XPATH, route)

            
            # Loop through each link element
            for paths in link :
                # Retrieve the href attribute
                d = link.get_attribute('href')  # Corrected attribute name
                links.append(d)
                
                # Retrieve the text of each link
                routes.append(link.text)
            
            try:
                # Wait for the pagination element to be present
                pagination = wait.until(ec.presence_of_element_located((By.XPATH, '//*[@class="DC_117_paginationtable"]')))
                
                # Click on the next page button
                next_page = pagination.find_element(By.XPATH, f'//div[@class="DC_117_page_tabs" and text()={i + 1}]')
                next_page.click()
            
            except Exception as e:
                print(f'No more pages to paginate to at step {i}. Exception: {e}')
                break
            
            df = pd.DataFrame({'Routes': routes,'Links':links })

            df.to_csv(file_path,r'\df_name')
            

            

            


            