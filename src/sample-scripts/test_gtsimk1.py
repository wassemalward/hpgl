from sys import *
from geo import *
from numpy import *
from scipy import *
import os

def test_gtsim(prop1,prop2):
	n = 0
	prop_size = 0
	for i in xrange(prop1.size()):
		if(prop1.is_informed(i) == True):
			prop_size = prop_size + 1
			if (prop1.get_at(i)<>prop2.get_at(i)):
				n = n+1
				#print prop1.get_at(i)-prop2.get_at(i)
	if (n>0):
		print "error ", n
	if (n==0):
		print "ok"
	print prop_size

def ind_ver (prop, indicator):
	ind_count = zeros( (indicator), dtype=float)
	ind_prob = zeros( (indicator), dtype=float)
	prop_size = 0
	for i in xrange(prop.size()):
		for j in xrange(indicator):
			if (prop.get_at(i) == j):
				ind_count[j] = ind_count[j] + 1.0
		if (prop.is_informed(i) == True):
			prop_size = prop_size + 1.0
	for j in xrange(indicator):
		ind_prob[j] = ind_count[j]/(prop_size)
	print ind_prob

prop1 = load_cont_property("test_data/BIG_SOFT_DATA_166_141_20.INC", -99)
prop2 = load_cont_property("results\GTSIM_TRUNC_RESULT.INC", -99)
test_gtsim(prop1,prop2)
ind_ver(prop2,3)
ind_ver(prop1,3)
stdin.readline()
