from selenium import webdriver

from selenium.webdriver.common.by import By

# keep chrome browser open after program finishes

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://amazon.com")







# driver.close()
# driver.quit()