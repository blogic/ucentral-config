#!/usr/bin/env python3

import json
import time
import sys

serial = sys.argv[1]
merge = {}

def config_merge(path):
	try:
		with open(path) as infile:
			cfg = json.load(infile)
		for k in cfg:
			merge[k] = cfg[k]
		print(f"merged {path}")
	except:
		print(f"failed to merge {path}")
		sys.exit()

def config_override(cfg):
	try:
		for k in cfg:
			merge[k] = cfg[k]
		print(f"merged Overrides")
	except:
		print(f"failed to Override")
		sys.exit()

def config_write():
	try:
		with open(f"{serial}.cfg", 'w') as outfile:
			json.dump(merge, outfile, indent=True)
	except:
		print("failed to write usync.cfg")
		sys.exit()

def config_load():
	try:
		with open(f"{serial}.device") as json_file:
			device = json.load(json_file)
	except:
		print(f"{serial}.device failed to load")
		sys.exit()
	return device

device = config_load()

merge["uuid"] = int(time.time())
config_merge(f"{device['venue']}.venue")
config_merge(f"{device['profile']}.profile")
if "override" in device:
	config_override(device["override"])
config_write()
