#!/usr/bin/python3
#coding: utf-8

from requests import get, put, post, delete
from time import sleep
from xml.sax.saxutils import escape
import random, json, xml.etree.ElementTree as ET, ftplib, datetime, sys, re, urllib, getopt, os, time, logging

f = open("input.txt", "r")


c_line = f.readline()
num = 0
forest = []

while (c_line):
	treerow = []
	for tree in list(c_line.strip()):
		treerow.append([tree, 0, 0, 0, 0])
	forest.append(treerow)
	c_line = f.readline()

	
for v in range(1, len(forest)-1):
	for h in range(1, len(forest[v])-1):
		for c in range(h+1, len(forest[v])):
			if forest[v][h][0] > forest[v][c][0]:
				forest[v][h][1] += 1
			else:
				forest[v][h][1] += 1
				break

		for c in range(h-1, -1, -1):
			print(str(forest[v][h][0]) + "-" + str(v)+ "," + str(h) + " -- " + str(forest[v][c][0])+ "-" + str(v)+ "," + str(c))
			if forest[v][h][0] > forest[v][c][0]:
				forest[v][h][2] += 1
			else:
				forest[v][h][2] += 1
				break
		print("----------_")
			
		for c in range(v+1, len(forest)):
			if forest[v][h][0] > forest[c][h][0]:
				forest[v][h][3] += 1
			else:
				forest[v][h][3] += 1
				break

		for c in range(v-1, -1, -1):
			if forest[v][h][0] > forest[c][h][0]:
				forest[v][h][4] += 1
			else:
				forest[v][h][4] += 1
				break

for v in range(1, len(forest)-1):
	for h in range(1, len(forest[v])-1):
		if forest[v][h][1] *  forest[v][h][2] * forest[v][h][3] * forest[v][h][4] > num:
			num = forest[v][h][1] *  forest[v][h][2] * forest[v][h][3] * forest[v][h][4]

print (num)
exit(0)
