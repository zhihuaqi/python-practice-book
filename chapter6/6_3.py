#!/usr/bin/env python
def unflatten_dict(d):
	result = {}
	for key in d.keys():
		if "." in key:
			parent, child = key.split(".", 1)
			if parent in result.keys():
				result[parent].update(unflatten_dict({child:d[key]}))
			else:
				result.update({parent: unflatten_dict({child:d[key]})})
		else:
			result.update({key:d[key]})
	return result
