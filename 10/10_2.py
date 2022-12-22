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
	#print("CPU START " + str(cpu) + " REG: " + str(reg_x) + " CINST: " + str(instr_c))

	if instr_c == 0:		
	#	print(c_line.strip())			

		c_line = f.readline()
		if (c_line.strip() == "noop"):
			instr_c = 1
		elif (c_line.split(" ")[0].strip() == "addx"):
			instr_c = 2

	if (cpu % 40 >= reg_x and cpu % 40 <= reg_x + 2):
		sys.stdout.write("#")
	else:
		sys.stdout.write(".")

	if cpu == 40:
		sys.stdout.write("\n")
	elif cpu == 80:
		sys.stdout.write("\n")
	elif cpu == 120:
		sys.stdout.write("\n")
	elif cpu == 160:
		sys.stdout.write("\n")
	elif cpu == 200:
		sys.stdout.write("\n")
	elif cpu == 240:
		sys.stdout.write("\n")


		
	if (c_line.strip() == "noop"):
		instr_c -= 1
	elif (c_line.split(" ")[0].strip() == "addx"):
		if instr_c == 1:
			reg_x += int(c_line.split(" ")[1].strip())
		instr_c -= 1


sys.stdout.write("\n")

exit(0)
