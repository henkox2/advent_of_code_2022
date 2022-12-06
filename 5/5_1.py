#!/usr/bin/python3
#coding: utf-8

from requests import get, put, post, delete
from time import sleep
from xml.sax.saxutils import escape
import random, json, xml.etree.ElementTree as ET, ftplib, datetime, sys, re, urllib, getopt, os, time, logging

f = open("input.txt", "r")


c_line = f.readline()

stackrows = []
num_stacks = 0
stacks = []

while (c_line):
	if not num_stacks and (c_line.split(' ')[1]) != '1':
		stackrows.append(c_line)
		c_line = f.readline()
		continue
	elif not num_stacks and (c_line.split(' ')[1].strip()) == '1':
		for pos in c_line.split(' '):
			if len(pos.strip()):
				stack = []
				stacks.append(stack)
				num_stacks = int(pos)
		for row in stackrows:
			for i in range(num_stacks):
				if row[1+i*4] != ' ':
					stacks[i].insert(0,row[1+i*4])
		c_line = f.readline()
	
	if c_line.split(' ')[0] == "move":
		for i in range(int(c_line.split(' ')[1])):
			stacks[int(c_line.split(' ')[5].strip())-1].append(stacks[int(c_line.split(' ')[3].strip())-1].pop())
	c_line = f.readline()
print (stacks)
exit(0)
