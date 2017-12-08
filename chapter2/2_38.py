#!/usr/bin/env python
def invertdict(dict):
	new_dict={}
	list1=dict.keys()
	list2=dict.values()
	for i in range(len(list1)):
		new_dict[list2[i]] = list1[i]
	return new_dict
		
