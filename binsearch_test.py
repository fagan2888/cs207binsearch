from pytest import raises
from binsearch import binary_search
import numpy as np

input = list(range(10))

def provided_examples_one():
	assert binary_search(input, 5) == 5
	assert binary_search(input, 4.5) == -1
	assert binary_search(input, 10) == -1
	assert binary_search([5], 5) == 0
	assert binary_search([5], 4) == -1 

def provided_examples_one():
	assert binary_search([1,2,np.inf], 2) == 1
	assert binary_search([1,2,np.inf], np.inf) == 2
	assert binary_search(input, 5, 1,3) == -1
	assert binary_search(input, 2, 2, 2) == 2