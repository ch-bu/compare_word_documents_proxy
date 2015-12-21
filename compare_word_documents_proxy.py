#!/usr/bin/python
# -*- coding: utf-8 -*-

from difflib import unified_diff
import numpy as np


def calc_num_changes(text1, text2):
	"""
	Calculates the number of changes to a document. The results
	are close to the compare-documents tool in Microsoft Word.

	Args: 
		text1: String containing the draft
		text2: String containing the revised draft

	Returns: 
		Integer -> Number of changes to the document

	"""

	if isinstance(text1, basestring) and isinstance(text2, basestring):

		# Number of changes to document
		n_changes = 0

		# Last character of line
		last_char = None

		# Loop over every line of function unified_diff
		for line in unified_diff(text1.split(), text2.split(), lineterm=''):
			
			# Current character of line
			curr_char = line[0]

			for prefix in ('---', '+++', '@@'):
				if line.startswith(prefix):
					break
			else:
				# Check for changes in lines
				if (last_char == '-' and curr_char == ' ') or \
					(last_char == '-' and curr_char == '+') or \
					(last_char == '+' and curr_char == ' ') or \
					(last_char == '+' and curr_char == '-'):
					n_changes = n_changes + 1
			
				# Update last_char
				last_char = curr_char

		return n_changes
	else:
		return None


