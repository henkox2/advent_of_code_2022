#!/usr/bin/python3
#coding: utf-8

from requests import get, put, post, delete
from time import sleep
from xml.sax.saxutils import escape
import random, json, xml.etree.ElementTree as ET, ftplib, datetime, sys, re, urllib, getopt, os, time, logging

f = open("input.txt", "r")


c_line = f.readline()
d_list = {}
cdir = []
num = 0

while (c_line):
	if (c_line.split(" ")[0] == "$"):
		if (c_line.split(" ")[1] == "cd"):
			if c_line.split(" ")[2].strip() == "..":
				cdir.pop()
			else:
				cdir.append(c_line.split(" ")[2].strip())
				key = ""
				for k in cdir:
					key = key + k
				print (key)
				print (''.join(cdir))
				if (''.join(cdir)) not in d_list.keys():
					d_list[key] = 0
	else:
		if (c_line.split(" ")[0] != "dir"):
			key = ""
			for k in cdir:
				key = key + k
				d_list[key] += int(c_line.split(" ")[0].strip())
	c_line = f.readline()

for itm in d_list:
	if d_list[itm] <= 100000:
		num += d_list[itm] 

print (num)
exit(0)
