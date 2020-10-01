#!/usr/bin/env python
# -*- coding: utf-8 -*-


import math
import copy
import itertools


def get_even_keys(dictionary):
	return {k for k in dictionary.keys() if k % 2 == 0}

def join_dictionaries(dictionaries):
	# Il existe aussi la fonction .update()
	return {key : value for d in dictionaries for key, value in d.items()}

def dictionary_from_lists(keys, values):
	longueur = min(len(keys), len(values))
	dictionary = {}
	for i in range(0, longueur):
		dict = {keys[i]:values[i]}
		dictionary.update(dict)
	return dictionary
	#return {keys[i]:values[i] for i in range(min(len(keys, len(values))))}

def get_greatest_values(dictionary, num_values):
	result = []
	dict = sorted(dictionary.values(), reverse=True)
	for i in range(0, num_values):
		result.append(dict[i])
	return result

def get_sum_values_from_key(dictionaries, key):
	sum = 0
	for d in dictionaries:
		if d.get(key) is not None:
			sum += d.get(key)
	return sum


if __name__ == "__main__":
	yeet = {
		69: "Yeet",
		420: "YeEt",
		9000: "YEET",
	}
	print(get_even_keys(yeet))
	print()

	yeet = {
		69: "Yeet",
		420: "YeEt",
		9000: "YEET",
	}
	doot = {
		0xBEEF: "doot",
		0xDEAD: "DOOT",
		0xBABE: "dOoT"
	}
	print(join_dictionaries([yeet, doot]))
	print()
	
	doh = [
		"D'OH!",
		"d'oh",
		"DOH!"
	]
	nice = [
		"NICE!",
		"nice",
		"nIcE",
		"NAIIIIICE!"
	]
	print(dictionary_from_lists(doh, nice))
	print()
	
	nums = {
		"nice": 69,
		"nice bro": 69420,
		"AGH!": 9000,
		"dude": 420,
		"git gud": 1337
	}
	print(get_greatest_values(nums, 1))
	print(get_greatest_values(nums, 3))
	print()

	bro1 = {
		"money": 12,
		"problems": 14,
		"trivago": 1
	}
	bro2 = {
		"money": 56,
		"problems": 406
	}
	bro3 = {
		"money": 1,
		"chichis": 1,
		"power-level": 9000
	}
	print(get_sum_values_from_key([bro1, bro2, bro3], "problems"))
	print(get_sum_values_from_key([bro1, bro2, bro3], "money"))
	print()
