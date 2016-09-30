from pytest import raises
from binsearch import binary_search
import numpy as np

 # >>> input = list(range(10))
 #    >>> binary_search(input, 5)
 #    5
 #    >>> binary_search(input, 4.5)
 #    -1
 #    >>> binary_search(input, 10)
 #    -1
 #    >>> binary_search([5], 5)
 #    0
 #    >>> binary_search([5], 4)
 #    -1
 #    >>> import numpy as np
 #    >>> binary_search([1,2,np.inf], 2)
 #    1
 #    >>> binary_search([1,2,np.inf], np.inf)
 #    2
 #    >>> binary_search(input, 5, 1,3)
 #    -1
 #    >>> binary_search(input, 2, 1,3)
 #    2
 #    >>> binary_search(input, 2, 3, 1)
 #    -1
 #    >>> binary_search(input, 2, 2, 2)
 #    2
 #    >>> binary_search(input, 5, 2, 2)

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


	

# def test_mymath_mean():
#     assert myaverage([9,3]) == 6

# def test_char():
#     with raises(TypeError):
#         myaverage(['a',3])

# def test_mymath():
#     assert mymedian([9,3, 6]) == 6
    
# def test_zero_median():
#     with raises(ValueError):
#         mymedian([])
        
# def test_char_median():
#     with raises(TypeError):
#         mymedian(['a', 3])