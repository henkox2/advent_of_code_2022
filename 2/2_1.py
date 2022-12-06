#!/usr/bin/python3
#coding: utf-8

from requests import get, put, post, delete
from time import sleep
from xml.sax.saxutils import escape
import random, json, xml.etree.ElementTree as ET, ftplib, datetime, sys, re, urllib, getopt, os, time, logging

f = open("input.txt", "r")

c_line = f.readline()
t_points = 0

while (c_line):
	opp = c_line.split(" ")[0].strip()
	me = c_line.split(" ")[1].strip()

	if me == 'X':
		t_points += 1
		if opp == "A":
			t_points += 3
		elif opp == "B":
			t_points += 0
		elif opp == "C":
			t_points += 6
	elif me == "Y":
		t_points += 2
		if opp == "A":
			t_points += 6
		elif opp == "B":
			t_points += 3
		elif opp == "C":
			t_points += 0
	elif me == "Z":
		t_points += 3
		if opp == "A":
			t_points += 0
		elif opp == "B":
			t_points += 6
		elif opp == "C":
			t_points += 3
	c_line = f.readline()

print (t_points)
exit(0)
