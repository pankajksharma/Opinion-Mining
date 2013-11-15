import os
from bs4 import BeautifulSoup

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
training_files = os.listdir("preprcessed-data")
testing_files = [a for a in os.listdir("data") if a.split('.')[0]+'.json' not in training_files ]

for t in testing_files:
	f = open("data/"+t, "r")
	soup = BeautifulSoup(f.read())
	