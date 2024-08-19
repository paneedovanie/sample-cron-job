from http.server import BaseHTTPRequestHandler
import asyncio
from pyppeteer import launch
 
class handler(BaseHTTPRequestHandler):
 
    async  def do_GET(self):
        browser = await launch()
        page = await browser.newPage()
        await page.goto('https://google.com')
        await browser.close()
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        self.wfile.write('Hello, world!'.encode('utf-8'))
        return