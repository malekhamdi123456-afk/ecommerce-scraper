from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
import time
import sys
import csv
import logging

logging.basicConfig(
    filename="scraping.log",
    level=logging.INFO,
    format="%(asctime)s-%(levelname)s-%(message)s"
)

driver=webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
with open ("prod.csv","w",newline="") as f:
    writer=csv.writer(f,delimiter=";")
    writer.writerow(["Sort Option", "Product Name", "Price", "Status"])

    wait=WebDriverWait(driver,10)

    #login

    try:
        username=driver.find_element(By.NAME,"user-name")
        username.send_keys("standard_user")
    except:
        print("WRONG USERNAME")
        
        logging.error("WRONG USERNAME")
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        driver.save_screenshot(f"error_{timestamp}.png")
        driver.quit()
        sys.exit()
    try:
        password=driver.find_element(By.NAME,"password")
        password.send_keys("secret_sauce")
    except:
        print("WRONG PASSWORD")
        logging.error("WRONG PASSWORD")
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        driver.save_screenshot(f"error_{timestamp}.png")
        driver.quit()
        sys.exit()


    button=driver.find_element(By.NAME,"login-button")
    button.click()
    time.sleep(3)
    logging.info("Logged in")

    #dropdown

    for i in range(1,3):
        try:
            dropdown=driver.find_element(By.CLASS_NAME,"product_sort_container")
            select=Select(dropdown)
            select.select_by_index(i)
            if (i==1):
                print("Name Z to A selected")
                logging.info("Sort selected: Name Z to A")
            elif(i==2):
                print("price low to high selected")
                logging.info("Sort selected: Price low to high")
            time.sleep(3)
        except Exception as e:
            print(e)
            timestamp = time.strftime("%Y%m%d_%H%M%S")
            driver.save_screenshot(f"error_{timestamp}.png")                                                                                                
            driver.quit()
            logging.error("PAGE NOT FOUND")
            sys.exit()
    ##scraping articles

        try:
            articles=wait.until(
                EC.presence_of_all_elements_located((By.CLASS_NAME,"inventory_item"))

            )
        except:
            print("ERROR no product available")
            timestamp = time.strftime("%Y%m%d_%H%M%S")
            driver.save_screenshot(f"error_{timestamp}.png")
            driver.quit()
            logging.error("PRODUCT NOT AVAILABLE")
            sys.exit()
        select=Select(driver.find_element(By.CLASS_NAME,"product_sort_container"))
        sort=select.first_selected_option.text
        try:
            for article in articles[:3]:
                name=article.find_element(By.CLASS_NAME,"inventory_item_name")
                price=article.find_element(By.CLASS_NAME,"inventory_item_price")
                try:
                    status=article.find_element(By.CLASS_NAME,"status").text
                except:
                    status=("status not found")
                print(sort,name.text,price.text,status)
                logging.info("SUCCESS")
                writer.writerow([sort,name.text,price.text,status])
        except:
            print("error!!!!! item not found")
            timestamp = time.strftime("%Y%m%d_%H%M%S")
            driver.save_screenshot(f"error_{timestamp}.png")
            driver.quit()
            logging.error("PRODUCT NOT AVAILABLE")
            sys.exit()



driver.quit()