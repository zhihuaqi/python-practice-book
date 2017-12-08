#!/usr/bin/env python
def word_frequency(words):
	frequency = {}
	for w in words:
		frequency[w] = frequency.get(w,0) + 1
	return frequency
def read_word(filename):
	return open(filename).read().split()
def main(filename):
	frequency=word_frequency(read_word(filename))
	for word, count in sorted(frequency.items(), key=lambda x:x[1], reverse = True):
		print word, count

import sys
main(sys.argv[1])

	
