from scrapy import cmdline

from utils import  create_chrome_driver
if '__main__' == __name__:
    browser = create_chrome_driver()
    browser.get('http://quotes.toscrape.com/')
