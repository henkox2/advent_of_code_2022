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
		treerow.append([tree, False])
	forest.append(treerow)
	c_line = f.readline()

	
for v in range(1, len(forest)-1):
	ch = int(forest[v][0][0])
	for h in range(1, len(forest[v])-1):
		if ch < int(forest[v][h][0]):
			ch = int(forest[v][h][0])
			forest[v][h][1] = True

	ch = int(forest[v][len(forest[v])-1][0])
	for h in range(len(forest[v])-2, 0, -1):
		if ch < int(forest[v][h][0]):
			ch = int(forest[v][h][0])
			forest[v][h][1] = True

for h in range(1, len(forest[0])-1):
	cv = int(forest[0][h][0])
	for v in range(1, len(forest)-1):
		if cv < int(forest[v][h][0]):
			cv = int(forest[v][h][0])
			forest[v][h][1] = True

	cv = int(forest[len(forest)-1][h][0])
	for v in range(len(forest)-2, 0, -1):
		if cv < int(forest[v][h][0]):
			cv = int(forest[v][h][0])
			forest[v][h][1] = True

for v in range(1, len(forest)-1):
	for h in range(1, len(forest[v])-1):
		if forest[v][h][1]:
			num += 1

print (num + len(forest)*2 + (len(forest[0])-2)*2)
exit(0)
