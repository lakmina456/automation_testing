from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://practicetestautomation.com/practice-test-login")


username_field = driver.find_element("id", "username")
password_field = driver.find_element("id", "password")

username_field.send_keys("student")
password_field.send_keys("Password123")


login_button = driver.find_element("id", "submit")
login_button.click()

try:
    welcome_message = driver.find_element("xpath", "//div[@id='loop-container']")
    print("Login Successful")
except:
    error_message = driver.find_element("xpath", "//div[@id='error']")
    print("Login Failed")
