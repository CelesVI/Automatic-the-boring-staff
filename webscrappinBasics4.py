from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://automatetheboringstuff.com/')
elem = browser.find_elements_by_css_selector('img')
print(elem)
