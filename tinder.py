#from userDetails import ph, password
from selenium import webdriver
from time import sleep
from random import random

class Tinder():
	def __init__(self):
		self.driver = webdriver.Chrome(executable_path='/usr/bin/chromedriver_newer')
		#self.phone = ph
		#self.password = password


	def get_tinder_page(self):
		self.driver.get('https://www.tinder.com')
		sleep(5)
		self.press_login_button()

	def press_login_button(self):
		self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a').click()
		self.login_with_facebook()

	def like_user(self):
		self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[4]/div/div[4]/button').click()
		sleep(3)

	def dislike_user(self):
		self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[4]/div/div[2]/button').click()
		sleep(3)

	def login_with_facebook(self):
		sleep(3)
		self.driver.find_element_by_xpath('/html/body/div[2]/main/div/div[1]/div/div/div[3]/span/div[2]/button').click()
		sleep(4)
		login_window = self.driver.window_handles[1]
		self.driver.switch_to.window(login_window)
	
		self.driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/div/div[3]/button[1]').click()


		self.driver.find_element_by_xpath('/html/body/div/div[2]/div[1]/form/div/div[1]/div/input').send_keys('')
		self.driver.find_element_by_xpath('/html/body/div/div[2]/div[1]/form/div/div[2]/div/input').send_keys('')
		self.driver.find_element_by_xpath('/html/body/div/div[2]/div[1]/form/div/div[3]/label[2]/input').click()
		
		sleep(15)
		prev_win = self.driver.window_handles[0]
		self.driver.switch_to.window(prev_win)
		sleep(60)
		#self.driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div/div/div/div/div[1]/div[2]/div[2]/div[1]/div/div/div').click()
		accept_location = self.driver.find_element_by_xpath('/html/body/div[2]/main/div/div/div/div[3]/button[1]').click()
		#return
		sleep(15)
		accept_cookies = self.driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/div[1]/div[1]/button').click()
		
		sleep(15)
		click_not_interested = self.driver.find_element_by_xpath('/html/body/div[2]/main/div/div/div/div[3]/button[2]').click()
		sleep(15)
		close_dark_mode = self.driver.find_element_by_xpath('/html/body/div[2]/main/div/div[2]/button').click()
		sleep(15)
		maybe_later = self.driver.find_element_by_xpath('/html/body/div[2]/main/div/div/div[3]/button[2]').click()
		sleep(15)
		like_or_dislike = int(random()*2)
		while True:
			if like_or_dislike == 0:
				self.like_user()
			else:
				self.dislike_user()

