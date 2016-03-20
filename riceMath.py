#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Author: 	Ryan Olson
#Last Mod:	20-Mar-2016
#Purpose:	To demonstrate the use of Selenium webdriver within python to drive
#		and answer questions correctly on FreeRice.com

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

class RiceMath(object):
    def __init__(self):
	#Set User Credentials
	self.userName = "exampleUsername"
	self.userPass = "examplePassword"

	#Init Driver attr
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://freerice.com/"

    	#Answer Elements
	self.ansA = ".//*[@id='external-game-container']/div/div[1]/div/div[2]/div[2]/div[2]/div/ul/li[1]/a"
	self.ansB = ".//*[@id='external-game-container']/div/div[1]/div/div[2]/div[2]/div[2]/div/ul/li[2]/a"
	self.ansC = ".//*[@id='external-game-container']/div/div[1]/div/div[2]/div[2]/div[2]/div/ul/li[3]/a"
	self.ansD = ".//*[@id='external-game-container']/div/div[1]/div/div[2]/div[2]/div[2]/div/ul/li[4]/a"
	self.strQuestion = ".//*[@id='question-title']/a/b"

	#Login Elements
	self.loginBtn = ".//*[@id='block-block-8']/div[4]/div/div/ul/li/a[1]"
	self.passBox = "edit-pass"
	self.userBox = "edit-name"
	self.userBoxWatermark = "edit-name_watermark"
	self.submitBtn = "edit-submit"

	#Navigation Elements
	self.homeBtn = "logo-image"
	self.categoryBtn = ".//*[@id='external-game-container']/div/div[1]/div/div[1]/div[1]/a"
	self.mathBtn = ".//*[@id='qtools_ajax_categories_block']/div/div[4]/div[3]/ul/li[1]/a"
	
    def run(self):
	#Create driver
        driver = self.driver
        driver.get(self.base_url)

	#Login to with user creds if entered
	self.login()

	#Navigate to Math section
	self.navToMath()

	while True:
		time.sleep(1)
		#Assign answer elements for each new question
		aText = driver.find_element_by_xpath(self.ansA).text
		bText = driver.find_element_by_xpath(self.ansB).text
		cText = driver.find_element_by_xpath(self.ansC).text
		dText = driver.find_element_by_xpath(self.ansD).text

		#Get parse and solve page question
		question = driver.find_element_by_xpath(self.strQuestion).text	
		answerList = question.split("x")
		val1 = answerList[0].replace(" ", "")
		val1 = int(val1)
		val2 = answerList[1].replace(" ", "")
		val2 = int(val2)
		newAns = val1 * val2
		
		#Select answer based on available optons
		if newAns is int(aText):
			driver.find_element_by_xpath(self.ansA).click()
		elif newAns is int(bText):
			driver.find_element_by_xpath(self.ansB).click()
		elif newAns is int(cText):
			driver.find_element_by_xpath(self.ansC).click()
		else:
			driver.find_element_by_xpath(self.ansD).click()

    def login(self):
	self.driver.find_element_by_xpath(self.loginBtn).click()
        self.driver.find_element_by_id(self.passBox).clear()
        self.driver.find_element_by_id(self.passBox).send_keys(self.userPass)
        self.driver.find_element_by_id(self.userBoxWatermark).clear()
        self.driver.find_element_by_id(self.userBox).send_keys(self.userName)
        self.driver.find_element_by_id(self.submitBtn).click()
	
    def navToMath(self):
        self.driver.find_element_by_id(self.homeBtn).click()
	self.driver.find_element_by_xpath(self.categoryBtn).click()
	self.driver.find_element_by_xpath(self.mathBtn).click()
 
if __name__ == "__main__":
    RiceMath().run()
