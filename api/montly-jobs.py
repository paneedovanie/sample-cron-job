from http.server import BaseHTTPRequestHandler
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def run_scraper():
    # Path to your custom Chromium binary
    CHROMIUM_PATH = 'https://github.com/Sparticuz/chromium/releases/download/v116.0.0/chromium-v116.0.0-pack.tar'

    # Set up Chrome options
    chrome_options = Options()
    # chrome_options.binary_location = CHROMIUM_PATH
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--headless')  # Optional: Run in headless mode

    # Set up WebDriver service using ChromeDriverManager
    service = Service(ChromeDriverManager().install())

    # Initialize WebDriver
    driver = webdriver.Chrome(service=service, options=chrome_options)

    # Example usage
    driver.get('https://example.com')
    print(driver.title)
    driver.quit()
 
class handler(BaseHTTPRequestHandler):
 
    def do_GET(self):

        run_scraper()

        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        self.wfile.write('Hello, world!'.encode('utf-8'))
        return
    


run_scraper()