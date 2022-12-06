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
	elf1 = c_line.strip()
	c_line = f.readline()
	elf2 = c_line.strip()
	c_line = f.readline()
	elf3 = c_line.strip()

	common_12 = ''.join(set(elf1).intersection(elf2))
	common_chars = ''.join(set(common_12).intersection(elf3))

	if (ord(common_chars) < 97):
		t_points += ord(common_chars) - 64 + 26
	else:
		t_points += ord(common_chars) - 96
	c_line = f.readline()

print (t_points)
exit(0)
