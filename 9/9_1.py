#!/usr/bin/python3
#coding: utf-8

import random as ET, datetime, sys, re, os, time, logging

f = open("input.txt", "r")

size = 1000
t_map = [[]]
t_map = [[0 for i in range(size)] for j in range(size)]

t_pos = [int(size/2)-1,0]
h_pos = [int(size/2)-1,0]

c_line = f.readline()
while (c_line):
	print(c_line.strip())
				
	if (c_line.split(" ")[0] == "R"):
		for i in range(int(c_line.split(" ")[1].strip())):
			h_pos[1] += 1
			if abs(h_pos[1]-t_pos[1]) > 1:
				if h_pos[0] != t_pos[0]:
					t_pos[0] = h_pos[0]
				t_pos[1] = int((t_pos[1]+h_pos[1])/2)

			t_map[t_pos[0]][t_pos[1]] = 1

	elif (c_line.split(" ")[0] == "L"):
		for i in range(int(c_line.split(" ")[1].strip())):
			h_pos[1] -= 1
			if abs(h_pos[1]-t_pos[1]) > 1:
				if h_pos[0] != t_pos[0]:
					t_pos[0] = h_pos[0]
				t_pos[1] = int((t_pos[1]+h_pos[1])/2)

			t_map[t_pos[0]][t_pos[1]] = 1

	elif (c_line.split(" ")[0] == "U"):
		for i in range(int(c_line.split(" ")[1].strip())):
			h_pos[0] -= 1
			if abs(h_pos[0]-t_pos[0]) > 1:
				if (h_pos[1] != t_pos[1]):
					t_pos[1] = h_pos[1]
				t_pos[0] = int((t_pos[0]+h_pos[0])/2)

			t_map[t_pos[0]][t_pos[1]] = 1

	else:
		for i in range(int(c_line.split(" ")[1].strip())):
			h_pos[0] += 1
			if abs(h_pos[0]-t_pos[0]) > 1:
				if h_pos[1] != t_pos[1]:
					t_pos[1] = h_pos[1]
				t_pos[0] = int((t_pos[0]+h_pos[0])/2)

			t_map[t_pos[0]][t_pos[1]] = 1

	c_line = f.readline()

num = 0
for row in t_map:
	num += row.count(1)
print(num)
exit(0)
