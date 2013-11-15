import os,json
from bs4 import BeautifulSoup
from datacleaner import DataClean

def update_occurences(type, text):
	for t in text:
		try:
			type[t] += 1
		except:
			type[t] = 1

dirlist = os.listdir("data")
for l in dirlist[:len(dirlist)/3]:	#1/3 for training
	cons = {}
	pros = {}

	f = open("data/"+l, "r")
	soup = BeautifulSoup(f.read())
	f.close()

	for review in soup.findAll("review"):
		update_occurences(cons, DataClean(review.cons.get_text()).getData())
		update_occurences(pros, DataClean(review.pros.get_text()).getData())
	f = open("processed-data/"+l.split('.')[0]+".json", "w")
	f.write(json.dumps({"cons": cons, "pros" : cons}))
	f.close()