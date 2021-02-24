from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

passwords = ['gndadsa', 'gndadsa',  'gndadsa', 'gndadsa',
             'gndadsa', 'gndadsa', 'gndadsa', 'gndadsa',
             'gndadsa', 'gndadsa', 'dsfsd', 'gndadsa',
             ]
is_autotization = False
options = Options()
options.headless = True
driver = webdriver.Firefox(options=options, executable_path=r'C:\_install\geckodriver.exe')
for password in passwords:
    if is_autotization:
        print("break")
        break
    driver.get("http://192.168.1.1/cgi-bin/luci")
    print("try password:", password)
    assert "BerlogaOpenWrt" in driver.title
    elem = driver.find_element_by_name("luci_password")
    submit = driver.find_element_by_class_name("cbi-button-apply")


    elem.clear()
    elem.send_keys(password)
    #elem.send_keys(Keys.RETURN)
    submit.click()

    if "Invalid username and/or password!" not in driver.page_source:
        is_autotization = True
        print("password is good:", password)
       # print(driver.page_source)

#assert "Invalid username and/or password!" not in driver.page_source
#driver.close()