#!/usr/bin/python3
#coding: utf-8

from requests import get, put, post, delete
from time import sleep
from xml.sax.saxutils import escape
import random, json, xml.etree.ElementTree as ET, ftplib, datetime, sys, re, urllib, getopt, os, time, logging

f = open("input", "r")

elfs = []
elf_cal = 0

c_line = f.readline()
while (c_line):
	if (c_line == '\n'):
		elfs.append(elf_cal)
		elf_cal = 0
	else:
		elf_cal += int(c_line)
	c_line = f.readline()

print(max(elfs))

elfs.sort(reverse=True)

print(elfs[0] + elfs[1] + elfs[2])

exit(0)
