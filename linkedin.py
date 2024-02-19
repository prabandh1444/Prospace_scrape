from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv


with open('data.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Name', 'Job Title', 'Company', 'College', 'Location', 'URL'])
    driver = webdriver.Firefox()
    # driver.get('https://linkedin.com/')
    # sleep(1)
    # username = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "session_key")))
    # password = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "session_password")))
    # username.send_keys("prabandhbera@gmail.com")
    # password.send_keys("prabandh007")
    # login_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
    # login_btn.click()
    # driver.get('https://www.google.com')
    # sleep(3)
    # search_query = driver.find_element(By.NAME, 'q')  # Use By.NAME to find element by name
    # search_query.send_keys('site:linkedin.com/in/ AND "software developer"')
    # search_query.send_keys(Keys.RETURN)
    # sleep(10)
    # linkedin_urls = driver.find_elements(By.XPATH, '//div[@class="MjjYud"]/cite')  
    # linkedin_urls = [url.text for url in linkedin_urls]
    # sleep(0.5)
    # print(len(linkedin_urls))
    # print(linkedin_urls)
    driver.get('https://www.linkedin.com')
    input("Please login to LinkedIn manually and press Enter to continue...")
    search_url = 'https://www.linkedin.com/search/results/people/?keywords=software%20development'
    driver.get(search_url)
    elements = driver.find_elements(By.XPATH,"//li[contains(@class, 'reusable-search__entity-result-list')]/a")
    print(elements)
    driver.quit()

