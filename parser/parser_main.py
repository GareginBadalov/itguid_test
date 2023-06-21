
from selenium import webdriver

from pages.raiting_page import RatingPage
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
rating_page = RatingPage(driver)
rating_page.go_to_site()
rating_page.get_top_five()
