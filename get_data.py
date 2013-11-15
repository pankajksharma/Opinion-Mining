import os
from bs4 import BeautifulSoup

dirlist = os.listdir("processed-data")
count = 0
for d in dirlist:
	f = open("data/"+d.split('.')[0]+'.xml', 'r')
	soup = BeautifulSoup(f.read())
	count += len(soup.findAll("review"))
f = open("no-of-test-cases", "w")
f.write(str(count))
f.close()
print count 