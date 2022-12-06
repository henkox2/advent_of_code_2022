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
	comp1 = slice(0,len(c_line)//2)
	comp2 = slice(len(c_line)//2,len(c_line))
	comp1_t = c_line[comp1].strip()
	comp2_t = c_line[comp2].strip()

	common_chars = ''.join(set(comp1_t).intersection(comp2_t))

	if (ord(common_chars) < 97):
		t_points += ord(common_chars) - 64 + 26
	else:
		t_points += ord(common_chars) - 96
	c_line = f.readline()

print (t_points)
exit(0)
