#!/usr/bin/python3
#coding: utf-8

import random as ET, datetime, sys, re, os, time, logging

f = open("input-12.txt", "r")

reg_x = 1
cpu = 0
max_c = 1000
instr_c = 0
num = 0 


#c_line = f.readline()
c_line = "START"
while (c_line):
	cpu += 1

	if instr_c == 0:		
	
		c_line = f.readline()
		if (c_line.strip() == "noop"):
			instr_c = 1
		elif (c_line.split(" ")[0].strip() == "addx"):
			instr_c = 2

	if cpu == 20:
		num += cpu * reg_x
	elif cpu == 60:
		num += cpu * reg_x
	elif cpu == 100:
		num += cpu * reg_x
	elif cpu == 140:
		num += cpu * reg_x
	elif cpu == 180:
		num += cpu * reg_x
	elif cpu == 220:
		num += cpu * reg_x

	if (c_line.strip() == "noop"):
		instr_c -= 1
	elif (c_line.split(" ")[0].strip() == "addx"):
		if instr_c == 1:
			reg_x += int(c_line.split(" ")[1].strip())
		instr_c -= 1

print (num)
exit(0)
