#!/usr/bin/python
import subprocess

file = open('html5lib/testdata/tree-construction/tests1.dat')

data = '#data\n'
errors = '#errors\n'
document  = '#document\n'

type = None
testdata = None
testdatas = []

for line in file:
	if line == data:
		if testdata:
			testdatas.append(testdata)
		testdata = {
			data: [],
			errors: [],
			document: [],
		}
		type = data
	elif line in [errors, document]:
		type = line
	else:
		if type == document and line.startswith('|'):
			line = line[1:]
		testdata[type].append(line)

if testdata:
	testdatas.append(testdata)


i = 0;
for testdata in testdatas:
	proc = subprocess.Popen('../html5',
			shell=True,
			stdin=subprocess.PIPE,
			stdout=subprocess.PIPE,
			stderr=subprocess.PIPE,
			)
	print '---'
	print 'Test %d' % i
	print 'Input:'
	print ''.join(testdata[data]), 
	print 'Expected:'
	print ''.join(testdata[document]),
	print 'Output:'
	out, err = proc.communicate(''.join(testdata[data]))
	print out,
	i = i + 1
