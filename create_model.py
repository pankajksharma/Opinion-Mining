import json,os

def update_occurences(type, occ):
	for k,v in occ.iteritems():
		try:
			type[k] += v
		except:
			type[k] = v
dirlist = os.listdir("processed-data")
pros = {}
cons = {}
for d in dirlist:
	# print d
	f = open("processed-data/"+d)
	data = f.read().replace('""""', '""').replace(' u"', ' "').replace('{u"', '{"')
	f.close()
	try:
		data = json.loads(data)
	except Exception,e:
		print d
		continue
	update_occurences(cons, data['cons'])
	update_occurences(pros, data['pros'])

f = open("pros", "w")
for k,v in pros.iteritems():
	f.write(k.encode('utf8')+' '+str(v)+'\n')
f.close()
fc = open("cons", "w")
for k,v in cons.iteritems():
	f.write(k.encode('utf8')+' '+str(v)+'\n')
f.close()