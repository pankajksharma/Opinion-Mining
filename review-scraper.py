import re
import urllib2
import hashlib
from bs4 import BeautifulSoup
from string import ascii_lowercase

baseurl = "http://www.glassdoor.com"

def get_data(url):
	res = urllib2.urlopen(url)
	return res.read()

def get_review_page_count(url):
	data = get_data(url)
	soup = BeautifulSoup(data)
	rc = soup.findAll("div", {"class" : "counts h3 floatLt"})[0].tt
	return int(rc.get_text())/10+1 if int(rc.get_text())%10 == 0 else int(rc.get_text())/10+2

def get_name(url):
	data = get_data(url)
	soup = BeautifulSoup(data)
	return str(soup.title.get_text().split('|')[0])

def get_file_name(url):
	return url.split('-')[-1].replace('htm\n', 'xml')

for c in ascii_lowercase:
	try:
		f = open('links/temp-'+c, 'r')

		while True:
			rl = f.readline()
			if not rl:
				break
			initurl = baseurl + rl
			fw = open('data/'+get_file_name(initurl), 'w')
			print get_file_name(initurl)
			
			fw.write('<name>%s</name>\n' %get_name(initurl).encode('utf8'))
			fw.write('<url>%s</url>\n' %initurl)
			fw.write('<reviews>\n')

			pc = get_review_page_count(initurl)

			for i in range(1, pc):
				url = initurl.split('.htm')[0]+'_P%d.htm' %i
				data = get_data(url)
				soup = BeautifulSoup(data)
				reviews = soup.findAll("div", {"class" : "employerReview"})
				# print reviews
				for r in reviews:
					body = r(attrs={"class" : "reviewBody"})[0]
					auth = r(attrs={"class" : "authorJobTitle"})[0]
					desc = r(attrs={"class" : "description"})[0]
					ps = desc.findAll("p")
					# print auth
					fw.write('<review>\n')
					fw.write('<date>%s</date>\n' %r.time['datetime'])
					fw.write('<rating>%s</rating>\n' %r.span.span.span['title'].encode('utf8'))
					try:
						fw.write('<upvote>%s</upvote>\n' %body.p.span.span.get_text())
					except:
						fw.write('<upvote>0</upvote>\n')
					fw.write('<employee-type>%s</employee-type>\n' %str(auth.get_text()))
					fw.write('<title>%s</title>' %body.h2.get_text().encode('utf8'))
					fw.write('<pros>%s</pros>\n' %ps[1].get_text().encode('utf8'))
					fw.write('<cons>%s</cons>\n' %ps[2].get_text().encode('utf8'))
					fw.write('<advice-to-management>%s</advice-to-management>\n' %ps[3].get_text().encode('utf8'))
					fw.write('<recommended>%s</recommended>\n' %ps[4].get_text().split(',')[0].encode('utf8'))
					fw.write('</review>\n\n')
			fw.write('</reviews>')
	except Exception,e:
		print str(e)