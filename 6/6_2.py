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
	sub_s = list(c_line[i:i+14])
	dup_flag = 0
	while len(sub_s):
		pos = sub_s.pop()
		try:
			sub_s.index(pos)
			dup_flag = 1
			break
		except:
			continue
		
	if not dup_flag:
		num = i + 14
		break
print (num)
exit(0)
