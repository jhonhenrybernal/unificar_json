import csv
import os
import io
import json
import time


CSV_DIR = "D:/unificacion_masiva/"

def init():
	process_json()
	comma_json()
	time.sleep(1)
	structure_json()
	recount_json()



def process_json():

	for top, dirs, files in os.walk("D:/unificacion_masiva"):
		with open("D:/unificacion_masiva/total.json" , 'w') as i:
			for filename in files:
				with open("D:/unificacion_masiva/" + filename,"r+") as f:
					d = json.load(f)
					for obj in d:
						ln = len(d)
						prn = '{0} cant: {1}'.format(filename, ln)
						print(prn)
						json.dump(obj,i, indent=2)
	pass 

def comma_json():

	with open("D:/unificacion_masiva/total.json", "r+") as f:
		old = f.read()
		f.seek(0)  # rewind
		f.write(old.replace('}{', '},{'))
		f.close
	

def structure_json():
	with open("D:/unificacion_masiva/total.json", "r+") as f:
		old = f.read()
	with open("D:/unificacion_masiva/totalFinal.json", "w") as r:
		tmps = '[' + str(old) + ']'
		json_string = json.loads(tmps)

		json.dump(json_string, r, indent=2)
		f.close
	os.remove("D:/unificacion_masiva/total.json")
	print(len(json.load(open("D:/unificacion_masiva/totalFinal.json", 'r'))))



def recount_json():
	print('Recontando')
	with open("D:/unificacion_masiva/totalFinal.json", 'r+') as i:

		d = json.load(i)
		cnt = len(d)
		for x in range(cnt):
			d[x]['count'] = x
			i.seek(0)
			prt = "count :{0}".format(d[x]['count'])
			print(prt)
			json.dump(d, i, indent=3)
				



if __name__ == "__main__":
    init()
