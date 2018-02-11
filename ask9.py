#!/usr/bin/python

import sys

f = open(sys.argv[1],"r") #anoigma tou arxeiou pou periexei to keimeno se brainfuck (mono gia anagnwsh)

p = f.read() #program
f.close()

ppos = 0 #program position
m = [0] #memory
mpos = 0  #memory position

while ppos < len(p):
	if p[ppos] == ">":	
		mpos += 1
		if len(m) <= mpos:
			m.append(0)

	elif p[ppos] == "<":
		mpos -= 1
		if mpos < 0:
			print("Exete maetakhnithei ekso apo to orio")	
			sys.exit(0)

	elif p[ppos] == "+":
		m[mpos] += 1
		if m[mpos] >= 255:
			m[mpos] = 0

	elif p[ppos] == "-":
		m[mpos] -= 1
		if m[mpos] <= -1:
			m[mpos] = 255

	elif p[ppos] == ".":
		sys.stdout.write(chr(m[mpos]) )
		sys.stdout.flush()
	elif p[ppos] == ",":
		n=input("to programma zhtaei ena input: ")
		m[mpos] = ord(inp[0])

	elif p[ppos] == "[":
		if m[mpos] == 0:
			i=0 
			ppos += 1
			while ppos < len(p):
				if p[ppos] == "]" and i==0:
					break
				elif p[ppos] =="[":
					i+=1
				elif p[ppos] =="]":
					i-=1
				ppos +=1

	elif p[ppos] == "]":
		if m[mpos] != 0:
			j=0 
			ppos -= 1
			while ppos >= 0:
				if p[ppos] == "[" and j==0:
					break
				elif p[ppos] =="]":
					j+=1
				elif p[ppos] =="[":
					j-=1
				ppos -=1

	ppos +=1

print("")

#Gia na leitourghsei to programma prepei dipla sthn klish tou apo ton compiler na uparxei to onoma tou arxeiou pou periexei to keimeno se brainfuck p.x.: python ask9.py sample.txt 









