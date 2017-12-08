#!/usr/bin/env python
def flatten_dict(d, p = ""):
	flat_dict= {}
	for key in d.keys():
		if isinstance(d[key], dict):
			flat_dict.update(flatten_dict(d[key], p = p + key + "."))
		else:
			flat_dict[p + key] = d[key]
	return flat_dict
