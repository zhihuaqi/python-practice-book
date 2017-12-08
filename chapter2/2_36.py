#!/usr/bin/env python
def anagrams(lst):
	d ={}
	for i in lst:
		value = "".join(sorted(i))
		d[i] = value
	#print d.values()
	new_dict={}
	#print(d)
	for k, v in d.iteritems():
		if v in new_dict:
			new_dict[v].append(k)
		else:
			new_dict[v] = [k]
	new_list= new_dict.values()			
	return new_list
