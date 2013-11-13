import urllib2
import hashlib
from bs4 import BeautifulSoup
from string import ascii_lowercase

baseurl = "http://www.glassdoor.com/"

def get_data(url):
	res = urllib2.urlopen(url)
	return res.read()

def get_page_count(char):
	url = baseurl+"Reviews/%s-company-reviews-SRCH_KE0,1_IP1.htm"%c
	soup = BeautifulSoup(get_data(url))
	l = soup.findAll("tt", {"class" : "notranslate"})
	return int(l[2].get_text())/int(l[1].get_text())+2

#results = soup.findAll("div")
for c in ascii_lowercase[1:]:
	f = open("links/temp-"+c, "w")
	for i in range(1,get_page_count(c)):
		url = baseurl+"Reviews/%s-company-reviews-SRCH_KE0,1_IP%d.htm"%(c,i)
		#url = initurl+str(i)+".htm"
		data = get_data(url)
		soup = BeautifulSoup(data)
		results = soup(attrs={"class" : "companySearchResult"}) 
		for r in results:
			s = r.findAll("a", {}, True, "Reviews")
			try:
				print s[0]['href']
				f.write(s[0]['href']+"\n")
			except:
				pass
	f.close()