from selenium import webdriver


browser = webdriver.Firefox()
#browser = webdriver.Chrome()

# Jane has heard about a cool new online todo app and she goes to check out the homepage

browser.get('http://localhost:8000')

# She notices the page title and header mention to-do lists

assert 'To-Do' in browser.title

browser.quit()
