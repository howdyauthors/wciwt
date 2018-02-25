#!/usr/bin/env python
import requests, json, sys

def wciwt():

	query = '+'.join(sys.argv[1:]).replace(" ", "+")
	if query == "" or query == " ":
		print ('Usage: wciwt "movie or show title"')
		exit()

	try:
		json = (requests.get("https://wciwt.in/api/?format=json&query=" + query))
	except:
		print("Error during requesting, try again after sometime.")
		exit()

	if (json.status_code) != 200:
		print ("Error in request.")
		exit()

	json = json.json()

	if (json['total_results'] == 0):
		print ("No such title in our database.")
	else:
		for service in json['results']:
			if len(json['results'][service]) != 0:
				print ("\n{}:\n{}\n".format(service.upper(), '\n'.join(str((x.encode('utf-8')).decode()) for x in json['results'][service])))

if __name__ == "__main__":
	wciwt()