#!/bin/python

from bs4 import BeautifulSoup
import requests
import smtplib

def send_to_pocket(fromaddr, toaddrs, username, password, msg):

	server = smtplib.SMTP("smtp.gmail.com", 587)
	server.starttls()
	server.login(username,password)
	server.sendmail(fromaddr, toaddrs, msg)
	server.quit()

def get_links(url, headers):
	links=[]
	page = requests.get(url, headers=headers)
	soup = BeautifulSoup(page.text, 'html.parser')
	section_69 = soup.find(id="section-69")
	for link in section_69.find_all('a'):
		if link.get('class') == [u'node-link']:
			links.append(link.get('href')) 
	return links


if __name__ == '__main__':

	# Config send_to_pocket()
	fromaddr = 'YOUREMAIL@GMAIL.COM'
	toaddrs  = 'add@getpocket.com'
	username = 'YOUREMAIL@GMAIL.COM'
	password = 'YOURPASSWORD'

	# Config get_links()
	url ='http://www.economist.com/printedition/2015-09-12'
	headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'}

	for link in get_links(url, headers):
		send_to_pocket(fromaddr, toaddrs, username, password, 'kikoo http://www.economist.com' + link)
