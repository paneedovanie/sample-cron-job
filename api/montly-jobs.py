from http.server import BaseHTTPRequestHandler
import pyppeteer
from pyppeteer import launch
import asyncio

async def scraper():
    browser = await launch(headless=True)
    page = await browser.newPage()
    await page.goto('https://example.com')
    content = await page.content()
    print(content)
    await browser.close()
 
class handler(BaseHTTPRequestHandler):
 
    def do_GET(self):
        asyncio.get_event_loop().run_until_complete(scraper())
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        self.wfile.write('Hello, world!'.encode('utf-8'))
        return