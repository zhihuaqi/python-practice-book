#!/usr/bin/env python
def nearly_equal(x,y):
	import string
	element=list(string.ascii_lowercase)
	length=len(x)
	word_list=[i for i in x]
	full_list=[]
##replac
	list1=[]
	for i in word_list:
		for l in element:
			if l != i:
				replace_word = x.replace(i,l)
				list1.append(replace_word)
				full_list.append(replace_word)
	#print list1
##insert
	list2=[]
	for i in range(length+1):
		for l in element:
			insert_word = x[:i] + l + x[i:]
			list2.append(insert_word)
			full_list.append(insert_word)
	#print list2
##delete
	list3=[]
	for i in range(length):
		x1=[a for a in x]
		x1[i] = ""
		delete_word="".join(x1)
		list3.append(delete_word)
		full_list.append(delete_word)
	#print list3
##swap
	list4=[]
	length1 = length-1
	for i in range(length1):
		test_list=[a for a in x]
		l = i+1
		a = test_list[i]
		b = test_list[l]
		test_list[i] = b
		test_list[l] = a
		swap_word = ''.join(test_list)
		list4.append(swap_word)
		full_list.append(swap_word)
	#print list4
	#print len(full_list)
	if y in full_list:
		return True
	else:
		return False	 
