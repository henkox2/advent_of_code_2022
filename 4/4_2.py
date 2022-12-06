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
	elf1 = c_line.split(',')[0].strip()
	elf2 = c_line.split(',')[1].strip()
	elf1_low = int(elf1.split('-')[0])
	elf1_high = int(elf1.split('-')[1])
	elf2_low = int(elf2.split('-')[0])
	elf2_high = int(elf2.split('-')[1])
	
	if (elf1_low <= elf2_low and elf1_high >= elf2_low):
		t_points += 1
		c_line = f.readline()
		continue
	
	if (elf2_low <= elf1_low and elf2_high >= elf1_low):
		t_points += 1
		c_line = f.readline()
		continue
	c_line = f.readline()
print (t_points)
exit(0)
