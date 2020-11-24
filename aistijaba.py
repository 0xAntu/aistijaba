#!/usr/bin/env python

import requests
import argparse
from termcolor import colored

__author__ = '4N7U'
#Aistijaba

print(colored("        __         __                 ",'green'))
print(colored("  _____|  |    _  |  |  _     _       ",'green'))
print(colored(" |  _  |  |___| |_|  | |_|___| |_ ___ ",'green'))
print(colored(" |     |__|_ -|  _|__| | | .'| . | .'|",'green'))
print(colored(" |__|__|__|___|_| |__|_| |__,|___|__,|",'green'))
print(colored("                     |___|            ",'green'))
print("") 
print(colored("# Develop by ArMan HoSSa!n     ", 'yellow'))
print(colored("# Twitter: https://twitter.com/0xAntu        ", 'yellow'))
print(colored("# Fast HTTP Response status checker	    ", 'yellow'))               
print("")

parser = argparse.ArgumentParser()
parser.add_argument('-u', help='Target url', dest='url')
parser.add_argument('-f', help='URLs File', dest='url_file')
parser.add_argument('-o', help='Save the results to text file', dest='output_file')
#parser.add_argument('-s', help='If your urllist does not have ssl then use "-s"', dest='For_SSl')
args = parser.parse_args()

url = args.url
url_file = args.url_file
output_file = args.output_file
#For_SSl = args.For_SSl

urls=[]

if url:
	try:
		x = requests.get(url)
		print("[+]",url + " ==> ", x.status_code)
		if output_file:
			with open(output_file, 'a') as out:
				out.write(str(x.status_code) + "  " + url)
	except ConnectionError:
		pass

if url_file:
	file = open(url_file, "r")
	for line in file:
		url = line.strip() 
		try:
			x = requests.get(url)
			print("[+]",url + " ==> ", x.status_code)
			if output_file:
				with open(output_file, 'a') as out:
					out.write(str(x.status_code) + "  " + url+"\n")
		except ConnectionError:
			pass


print()
print(colored("# CopyRight © 0xAntu", 'green'))
print()