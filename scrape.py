from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import csv

def scrape_profiles(driver):
    profile_links = driver.find_elements(By.XPATH, '//a[contains(@href, "/in/")]')
    profile_urls = [link.get_attribute("href") for link in profile_links] 
    print(profile_urls)
    for profile_url in profile_urls:
        try:
            driver.get(profile_url)
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            name = soup.find('h1', {'class': 'text-heading-xlarge inline t-24 v-align-middle break-words'}).text.strip()
            works_at_loc = soup.find("div", {'class': 'text-body-medium'})
            current_position = works_at_loc.get_text().strip()
            skills = [skill.text.strip() for skill in soup.find_all('span', {'class': 'pv-skill-category-entity__name-text'})]
        except:
            continue
        p = {
            'name': name,
            'current_position': current_position,
            'linkedin_url': profile_url,
            'skills': skills
        }
        if p not in profiles:
            profiles.append(p)
        if len(profiles) >= 100:
            break

    return

driver = webdriver.Firefox()
driver.get('https://www.linkedin.com')
input("Please login to LinkedIn manually and press Enter to continue...")
profiles = []
i = 1
while(True):
    search_url = f'https://www.linkedin.com/search/results/people/?keywords=software%20development&origin=SWITCH_SEARCH_VERTICAL&page={i}'
    driver.get(search_url)
    scrape_profiles(driver)
    i = i + 1
    if len(profiles) >= 100:
            break
with open('data.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow([ 'id', 'Name', 'Current Position', 'LinkedIn URL', 'skills'])
    for idx, profile in enumerate(profiles, start=1):
            writer.writerow([idx, profile['name'], profile['current_position'], profile['linkedin_url'], ', '.join(profile['skills'])])
driver.quit()
