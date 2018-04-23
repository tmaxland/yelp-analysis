# get the meta info from each restaurant

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

searchFile = open ("data/yelpLaResLinks.txt")


searchFile = searchFile.read()
searchFileNames = searchFile.split("\n")



br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(False)
br.addheaders = [('User-agent', 'Firefox')]

browser = webdriver.Firefox()


i=0
while i<len(searchFileNames):
	#browser.get("http://www.yelp.com/search?find_desc=restaurants&find_loc=los+angeles#start="+searchFileNames[i])
	browser.get(searchFileNames[i])
	# extract the first page data at this point
	time.sleep(3)
	try:
		#get  longitude and latitude
		resName = browser.find_element_by_class_name("biz-name")
		category = browser.find_element_by_class_name("category-str-list")
		longitude = browser.find_element_by_xpath("//meta[@property='place:location:longitude']")
		latitude = browser.find_element_by_xpath("//meta[@property='place:location:latitude']")
		# address = browser.find_element_by_class_name("address")
		phone = browser.find_element_by_class_name("biz-phone")
		reviews = browser.find_element_by_class_name("review-count")
			
		print "The Restaurant Name is", resName.text
		print "The Restaurant category is", category.text
		print "The longitude is " , longitude.get_attribute("content")
		print "The latitude is " , latitude.get_attribute("content")
		print "The phone no is " , phone.text
		print "No of reviews" , reviews.text
		
		# print "The Restaurant Address is", address.text
		
		with open("data/yelpLaResData.txt", "a") as file:
				file.write(resName.text.encode('utf8'))
				file.write(" ")
				file.write(category.text.encode('utf8'))
				file.write(" ")
				file.write(longitude.get_attribute("content"))
				file.write(" ")
				file.write(latitude.get_attribute("content"))
				file.write(" ")
				file.write(phone.text)
				file.write(" ")
				file.write(reviews.text)
				file.write(" ")
				file.write('\n')
			
	except NoSuchAttributeException:
		assert 0; "cant find the title"
	i+=1


