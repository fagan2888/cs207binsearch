from pytest import raises
from binsearch import binary_search
import numpy as np

input = list(range(100))

def test_one():
	#Basic binary search operations 
	assert binary_search(input, 5) == 5
	assert binary_search(input, 75) == 75
	assert binary_search(input, 9.5) == -1
	assert binary_search(input, 100) == -1
	assert binary_search([5], 5) == 0
	assert binary_search([5], 4) == -1 

def tests_two():
	#with Numpy
	assert binary_search([1,2,np.inf], 2) == 1
	assert binary_search([1,2,np.inf], np.inf) == 2
	assert binary_search(input, 5, 1,3) == -1
	assert binary_search(input, 2, 2, 2) == 2

def tests_thee():
	# Test a case with odd len
	assert binary_search(list(range(99)), 5) == 5
	# Odd structure 
	input = [0] * 99
	input[20] = 5
	assert binary_search(input, 5) == -1
	



def test_input_type():
	#error conditions
	with raises(TypeError):
		binary_search(['Chars',5])

def test_blank_array():
	with raises(TypeError):
		binary_search([[],3])