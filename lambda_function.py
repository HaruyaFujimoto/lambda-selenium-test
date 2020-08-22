from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def lambda_handler(event, context):
    options = Options()
    options.binary_location = '/opt/chrome/headless-chromium'
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--single-process')
    options.add_argument('--disable-dev-shm-usage')
    browser = webdriver.Chrome('/opt/chrome/chromedriver', chrome_options=options)
    browser.get('https://www.google.com')
    title = browser.title
    browser.close()
    browser.quit()
    return {"title": title}
