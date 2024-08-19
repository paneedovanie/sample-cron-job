from http.server import BaseHTTPRequestHandler
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time

def setup_selenium():
    options = Options()
    options.headless = True  # Run in headless mode (no GUI)
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    return driver

def scrape_website(url):
    driver = setup_selenium()
    driver.get(url)

    # Optional: Wait for JavaScript to load (if necessary)
    time.sleep(5)  # Adjust this time based on how long the page needs to load

    # Get page source and use BeautifulSoup for parsing
    page_source = driver.page_source
    soup = BeautifulSoup(page_source, 'html.parser')

    # Example: Extract and print all <h1> tags
    for h1 in soup.find_all('h1'):
        print(h1.get_text())

    driver.quit()
 
class handler(BaseHTTPRequestHandler):
 
    def do_GET(self):
        scrape_website('https://www.governmentjobs.com')
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        self.wfile.write('Hello, world!'.encode('utf-8'))
        return