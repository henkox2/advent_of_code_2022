#!/usr/bin/python3
#coding: utf-8

from requests import get, put, post, delete
from time import sleep
from xml.sax.saxutils import escape
import random, json, xml.etree.ElementTree as ET, ftplib, datetime, sys, re, urllib, getopt, os, time, logging

f = open("input.txt", "r")


c_line = f.readline()

ch_list = []
counter = 0 
num = 0

for i in range(len(c_line.strip())):
	try:
		ch_list.index(c_line[i])
		ch_list = []
		counter = 1
	except: 
		counter += 1
	ch_list.append(c_line[i])
	if counter == 4:
		num = i
		break
print (num)
exit(0)
