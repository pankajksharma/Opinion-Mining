import os
from bs4 import BeautifulSoup
from datacleaner import DataClean

def test(comment, pros, cons, count):
	data = DataClean(comment).getData()
	prop = 1
	conp = 1
	for d in data:
		correction = False
		if pros[d]:
			prop *= pros[d]
		else:
			correction = True
		if cons[d] and correction:
			conp *= (cons[d] + 1)
		elif cons[d]:
			conp *= cons[d]
	return 'pro' if prop > conp else 'con'

def get_data(filen):
	di = {}
	f = open(filen, r)
	while True:
		d = f.readline()
		if not d:
			break
		else:
			t = d.split()
			di[t[0]] = t[1]
	return d

def get_pros_cons(pros_file, cons_file):
	return get_data(pros_file), get_data(cons_file)

pros,cons = get_pros_cons("pros", "cons")
count = int(open('no-of-test-cases', 'r').readline())

training_files = os.listdir("preprcessed-data")
testing_files = [a for a in os.listdir("data") if a.split('.')[0]+'.json' not in training_files ]

for t in testing_files:
	f = open("data/"+t, "r")
	soup = BeautifulSoup(f.read())
	tpros = soup.findAll("pros")
	tcons = soup.findAll("cons")
	for p in tpros:
		print test(p.get_text(), pros, cons, count), "pro"
	for c in tcons:
		print test(c.get_text(), pros, cons, count), "con"
	break