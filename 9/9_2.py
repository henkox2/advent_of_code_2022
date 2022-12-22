#!/usr/bin/python3
#coding: utf-8

import random as ET, datetime, sys, re, os, time, logging

f = open("input.txt", "r")

size = 1000
t_map = [[]]
t_map = [[0 for i in range(size)] for j in range(size)]

v_start = int(size/2)-1
h_start = int(size/2)-1

w_pos = [[]]
w_pos = [[v_start, h_start] for i in range(10)] 

c_line = f.readline()
while (c_line):
	if (c_line.split(" ")[0] == "R"):
		for s in range(int(c_line.split(" ")[1].strip())):
			w_pos[0][1] += 1
			for i in range(1, len(w_pos)):	
				if abs(w_pos[i-1][1]-w_pos[i][1]) > 1:
					w_pos[i][1] = int((w_pos[i][1]+w_pos[i-1][1])/2)
					if abs(w_pos[i-1][0] - w_pos[i][0]) == 1:
						w_pos[i][0] = w_pos[i-1][0]
					elif abs(w_pos[i-1][0] - w_pos[i][0]) > 1:
						w_pos[i][0] = int((w_pos[i][0]+w_pos[i-1][0])/2)
				elif abs(w_pos[i-1][0]-w_pos[i][0]) > 1:
					w_pos[i][0] = int((w_pos[i][0]+w_pos[i-1][0])/2)
					if abs(w_pos[i-1][1] - w_pos[i][1]) == 1:
						w_pos[i][1] = w_pos[i-1][1]
					elif abs(w_pos[i-1][1] - w_pos[i][1]) > 1:
						w_pos[i][1] = int((w_pos[i][1]+w_pos[i-1][1])/2)
			t_map[w_pos[9][0]][w_pos[9][1]] = 1
	elif (c_line.split(" ")[0] == "L"):
		for s in range(int(c_line.split(" ")[1].strip())):
			w_pos[0][1] -= 1
			for i in range(1, len(w_pos)):	
				if abs(w_pos[i-1][1]-w_pos[i][1]) > 1:
					w_pos[i][1] = int((w_pos[i][1]+w_pos[i-1][1])/2)
					if abs(w_pos[i-1][0] - w_pos[i][0]) == 1:
						w_pos[i][0] = w_pos[i-1][0]
					elif abs(w_pos[i-1][0] - w_pos[i][0]) > 1:
						w_pos[i][0] = int((w_pos[i][0]+w_pos[i-1][0])/2)
				elif abs(w_pos[i-1][0]-w_pos[i][0]) > 1:
					w_pos[i][0] = int((w_pos[i][0]+w_pos[i-1][0])/2)
					if abs(w_pos[i-1][1] - w_pos[i][1]) == 1:
						w_pos[i][1] = w_pos[i-1][1]
					if abs(w_pos[i-1][1] - w_pos[i][1]) > 1:
						w_pos[i][1] = int((w_pos[i][1]+w_pos[i-1][1])/2)
			t_map[w_pos[9][0]][w_pos[9][1]] = 1
	elif (c_line.split(" ")[0] == "U"):
		for s in range(int(c_line.split(" ")[1].strip())):
			w_pos[0][0] -= 1
			for i in range(1, len(w_pos)):	
				if abs(w_pos[i-1][0]-w_pos[i][0]) > 1:
					w_pos[i][0] = int((w_pos[i][0]+w_pos[i-1][0])/2)
					if abs(w_pos[i-1][1] - w_pos[i][1]) == 1:
						w_pos[i][1] = w_pos[i-1][1]
					elif abs(w_pos[i-1][1] - w_pos[i][1]) > 1:
						w_pos[i][1] = int((w_pos[i][1]+w_pos[i-1][1])/2)
				elif abs(w_pos[i-1][1]-w_pos[i][1]) > 1:
					w_pos[i][1] = int((w_pos[i][1]+w_pos[i-1][1])/2)
					if abs(w_pos[i-1][0] - w_pos[i][0]) == 1:
						w_pos[i][0] = w_pos[i-1][0]
					elif abs(w_pos[i-1][0] - w_pos[i][0]) > 1:
						w_pos[i][0] = int((w_pos[i][0]+w_pos[i-1][0])/2)
			t_map[w_pos[9][0]][w_pos[9][1]] = 1
	else:
		for s in range(int(c_line.split(" ")[1].strip())):
			w_pos[0][0] += 1
			for i in range(1, len(w_pos)):	
				if abs(w_pos[i-1][0]-w_pos[i][0]) > 1:
					w_pos[i][0] = int((w_pos[i][0]+w_pos[i-1][0])/2)
					if abs(w_pos[i-1][1] - w_pos[i][1]) == 1:
						w_pos[i][1] = w_pos[i-1][1]
					elif abs(w_pos[i-1][1] - w_pos[i][1]) > 1:
						w_pos[i][1] = int((w_pos[i][1]+w_pos[i-1][1])/2)
				elif abs(w_pos[i-1][1]-w_pos[i][1]) > 1:
					w_pos[i][1] = int((w_pos[i][1]+w_pos[i-1][1])/2)
					if abs(w_pos[i-1][0] - w_pos[i][0]) == 1:
						w_pos[i][0] = w_pos[i-1][0]
					elif abs(w_pos[i-1][0] - w_pos[i][0]) > 1:
						w_pos[i][0] = int((w_pos[i][0]+w_pos[i-1][0])/2)
			t_map[w_pos[9][0]][w_pos[9][1]] = 1
	c_line = f.readline()

num = 0
for row in t_map:
	num += row.count(1)
print(num)
exit(0)
