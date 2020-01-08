import requests
import json

from bs4 import BeautifulSoup


class Company(object):
	"""docstring for Company"""
	def __init__(self, url, posClass, locClass, urlClass):
		super(Company, self).__init__()
		self.url = url

		res = requests.get(url)
		contents = res.content

		parsedHTML = BeautifulSoup(contents, "lxml")

		self.positions = [element.text for element in parsedHTML.find_all(class_=posClass)]
		self.locations = [element.text for element in parsedHTML.find_all(class_=locClass)]
		self.urls = [element.attrs['href'] for element in parsedHTML.find_all(class_=urlClass)]

		

url = "https://www.facebook.com/careers/students-and-grads/?teams[0]=Internship%20-%20Engineering%2C%20Tech%20%26%20Design&teams[1]=Internship%20-%20Business&teams[2]=Internship%20-%20PhD&teams[3]=University%20Grad%20-%20PhD%20%26%20Postdoc&teams[4]=University%20Grad%20-%20Engineering%2C%20Tech%20%26%20Design&teams[5]=University%20Grad%20-%20Business&roles[0]=full-time&sub_teams[0]=Engineering"
Facebook = Company(url, '_8sel', '_8sen', '_8sef')

print(Facebook.locations)
'''
url = "https://www.facebook.com/careers/students-and-grads/?teams[0]=Internship%20-%20Engineering%2C%20Tech%20%26%20Design&teams[1]=Internship%20-%20Business&teams[2]=Internship%20-%20PhD&teams[3]=University%20Grad%20-%20PhD%20%26%20Postdoc&teams[4]=University%20Grad%20-%20Engineering%2C%20Tech%20%26%20Design&teams[5]=University%20Grad%20-%20Business&roles[0]=full-time&sub_teams[0]=Engineering"
res = requests.get(url)
contents = res.content

#file = open("test.html", 'wb')
#print(contents)
parsedHTML = BeautifulSoup(contents, "lxml")

positions = [element.text for element in parsedHTML.find_all(class_='_8sel')]

locations = [element.text for element in parsedHTML.find_all(class_='_8sen')]

urls = [element.attrs['href'] for element in parsedHTML.find_all(class_='_8sef')]


print(positions)
print(locations)
print(urls)
'''


#file.write(contents)
#file.close()
