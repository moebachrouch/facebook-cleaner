from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

# make sure to download chrome driver to your machine
# edit path of chrome driver accordingly
chrome_driver_path = "/Users/mohamedbachrouch/Desktop/dev/facebook-cleaner/facebook-cleaner/chromedriver"

driver = webdriver.Chrome(chrome_driver_path)

# open facebook

driver.get("https://www.facebook.com/")

####################################################

# prompt user for email and pw in command line

# search for login information input and login to fb
email_input = driver.find_element_by_id("email")
user_email = input("Enter your email: ") 
email_input.send_keys(user_email)

pw_input = driver.find_element_by_id("pass")
user_password = input("Enter your password: ") 
pw_input.send_keys(user_password)

# login with button click
login = driver.find_element_by_name("login")
login.click()

####################################################

# find profile
moe = driver.find_element_by_xpath('//a[contains(@class,"_2s25 _606w")]')
moe.send_keys(Keys.RETURN)

wait = WebDriverWait(driver, 10)

# find activity log
try:
	activity = wait.until(EC.visibility_of_element_located((By.XPATH, '//a[contains(@href,"https://www.facebook.com/ottawaThrowaway/allactivity?entry_point=profile_shortcut")]')))
except:
	driver.quit()

activity.send_keys(Keys.RETURN)

####################################################


sections = wait.until(EC.visibility_of_element_located((By.ID, "fbTimelineLogBody")))

year = sections.find_element_by_id("year_2020")

month = year.find_element_by_id("month_2020_8")

fetchstream = wait.until(EC.visibility_of_element_located((By.ID, 'u_fetchstream_2_g')))

button = fetchstream.find_element_by_xpath('//a[contains(@class, "_42ft _42fu _4-s1 _2agf _4o_4 _p _42gx")]')

button.send_keys(Keys.RETURN)

time.sleep(2)


# x = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[2]/div/div/div/div[2]/div[2]/div[2]/div[1]/div[1]/div/div[2]/div/div/div[1]/ul[1]/li[1]/div/table/tbody/tr/td[3]/div/div/button[2]')

while True:
	x = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[4]/div/div/div/ul/li/a')

	time.sleep(1)

	print(x.text)

	# driver.execute_script("arguments[0].click();",x)

	x.send_keys(Keys.RETURN)


	time.sleep(3)

	y = driver.find_element_by_xpath('/html/body/div[23]/div[2]/div/div/form/div[3]/button')

	y.send_keys(Keys.RETURN)

	time.sleep(5)


####################################################
# Scroll through page
#     # Get scroll height
# last_height = driver.execute_script("return document.body.scrollHeight")
# while True:
#         # Scroll down to bottom
# 	driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

# 	        # Wait to load page
# 	time.sleep(2)

# 	        # Calculate new scroll height and compare with last scroll height
# 	new_height = driver.execute_script("return document.body.scrollHeight")
# 	if new_height == last_height:
# 	            # If heights are the same it will exit the function
# 		break
# 	last_height = new_height

