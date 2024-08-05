from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import csv
import re

chrome_options = Options()
chrome_options.add_argument("--headless")  # To run Chrome in headless mode
chrome_options.add_argument("--no-sandbox")  # Bypass OS security model
chrome_options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems
chrome_service = Service('chromedriver.exe')  # Provide path to your ChromeDriver executable
driver = webdriver.Chrome(service=chrome_service, options=chrome_options) 

    
# Function to extract data from a single page
def extract_data_from_page(url):

    
    driver.get(url)
    html_content = driver.page_source
    

    soup = BeautifulSoup(html_content, 'html.parser')

    items = soup.find_all('div', class_='col-lg-6 col-md-6 wrap-item')
    
    data = []
    for item in items:
        name_data = re.split(r'\s{2,}', item.find('div', class_='solder-name').text.strip())
        rank = name_data[0]
        name = name_data[1]
        additional_info = item.find('div', class_='sub-counter').text.strip()
        if item.find('p'):
            date_up = item.find('p').text.strip()
        else:
            date_up = ''
        image = "https://www.idf.il/" + item.find('div', class_='soldier-image').find('img')['src'].split('?')[0]
        data.append([rank, name, additional_info, date_up, image])
    return data

# Main function to scrape all pages
def scrape_all_pages(base_url, num_pages):
    all_data = []    
    for page_num in range(1, num_pages+1):
        url = f"{base_url}?page={page_num}"
        print(f"Scraping page {page_num}...")
        page_data = extract_data_from_page(url)
        all_data.extend(page_data)
    
    
    return all_data

# URL of the first page
base_url = "https://www.idf.il/%D7%A0%D7%95%D7%A4%D7%9C%D7%99%D7%9D/%D7%97%D7%9C%D7%9C%D7%99-%D7%94%D7%9E%D7%9C%D7%97%D7%9E%D7%94/"
num_pages = 60

# Scrape all pages
all_data = scrape_all_pages(base_url, num_pages)
driver.quit()

# Write data to CSV
with open('idf_soldiers_data.csv', 'w', newline='', encoding='utf-8-sig') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Rank', 'Name', 'Additional Info', 'Date of Death', 'Image'])
    writer.writerows(all_data)

print("Scraping complete. Data saved to idf_soldiers_data.csv")
