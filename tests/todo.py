from http.server import HTTPServer, SimpleHTTPRequestHandler
from threading import Thread
from selenium import webdriver
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.keys import Keys
from percy import percy_snapshot

# start the example app in another thread

httpd2 = HTTPServer(('localhost', 8000), SimpleHTTPRequestHandler)

thread2 = Thread(target=httpd2.serve_forever)
thread2.setDaemon(True)
thread2.start()

# launch firefox headless
#ff_options = ChromeOptions()
#ff_options.add_argument('-headless')
browser=webdriver.Chrome("/Users/aayushi/Desktop/AmazonSearch/main/chromedriver")
#browser = Chrome(options=ff_options)

# go to the example app
browser.get('https://www.browserstack.com:443')
browser.implicitly_wait(10)

# snapshot empty state
#percy_snapshot(browser, 'Empty Todo State')
percy_snapshot(browser, 'Home Page')

# snapshot with a new todo
#new_todo_input = browser.find_element_by_class_name('new-todo')
#new_todo_input.send_keys('Try Percy')
#new_todo_input.send_keys(Keys.ENTER)
#percy_snapshot(browser, 'With a Todo')
# go to the example app
browser.get('https://www.browserstack.com/pricing')
browser.implicitly_wait(10)
percy_snapshot(browser, 'Pricing Page')

# snapshot with a completed todo
#todo_toggle = browser.find_element_by_class_name('toggle')
#todo_toggle.click()
#percy_snapshot(browser, 'Completed Todo')
browser.get('https://www.browserstack.com/integrations/automate')
browser.implicitly_wait(10)
percy_snapshot(browser, 'integrations automate Page')

# clean up
browser.quit()

httpd2.shutdown()
