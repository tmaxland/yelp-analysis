#grab the extended url specific name of the restaurant 

import mechanize
import urllib2
import time
import selenium
from selenium import webdriver
from selenium.common.exceptions import NoSuchAttributeException
from selenium.webdriver.common.keys import Keys
import os
import re
import csv

searchFile = open ("data/countFile.txt")


searchFile = searchFile.read()
searchFileNames = searchFile.split("\n")



br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(False)
br.addheaders = [('User-agent', 'Firefox')]

browser = webdriver.Chrome()


i=0
while i<len(searchFileNames):
	browser.get("http://www.yelp.com/search?find_desc=restaurants&find_loc=los+angeles#start="+searchFileNames[i])
	# extract the first page data at this point
	time.sleep(5)

	#extract restautant url from the website
	try:
		element = browser.find_elements_by_class_name("biz-name")
		#element = browser.find_element_by_link_text('searchFileNames[i]')
		

		for j in element:
			#print j.text
			resLink = browser.find_element_by_link_text(j.text)
			print resLink.get_attribute("href")
			with open("yelpLaResLinks.txt", "a") as file:
				file.write(resLink.get_attribute("href").encode('utf8'+"\n"))
				file.write('\n')
					
	except NoSuchAttributeException:
		assert 0; "cant find the title/url"	
	i+=1