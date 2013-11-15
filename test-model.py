import os
from bs4 import BeautifulSoup
from datacleaner import DataClean

def test(comment, pros, cons, count):
	data = DataClean(comment).getData()
	prop = 1
	conp = 1
	for d in data:
		correction = False
		if pros.has_key(d):
			prop *= pros[d]
		else:
			correction = True
		if cons.has_key(d) and correction:
			conp *= (cons[d] + 1)
		elif cons.has_key(d):
			conp *= cons[d]
	print prop, conp
	return 'pro' if prop > conp else 'con'

def get_data(filen):
	di = {}
	f = open(filen, 'r')
	while True:
		d = f.readline()
		if not d:
			break
		else:
			t = d.split()
			di[t[0]] = int(t[1])
	return di

def get_pros_cons(pros_file, cons_file):
	return get_data(pros_file), get_data(cons_file)

pros,cons = get_pros_cons("pros", "cons")
count = int(open('no-of-test-cases', 'r').readline())

training_files = os.listdir("processed-data")
testing_files = [a for a in os.listdir("data") if a.split('.')[0]+'.json' not in training_files ]
fo = open("output", "w")
for t in testing_files:
	f = open("data/"+t, "r")
	soup = BeautifulSoup(f.read())
	tpros = soup.findAll("pros")
	tcons = soup.findAll("cons")
	for p in tpros:
		fo.write(test(p.get_text(), pros, cons, count) + " pro\n")
	for c in tcons:
		fo.write(test(c.get_text(), pros, cons, count) + " con\n")
f.close()
