# -*- coding: utf-8 -*-
"""
Contem alguns exemplos de usos de funcionalidades em python.
"""

from math import sqrt
import string


# lambda
first_lambda = lambda x,y: (x**2 + y**2)
print 'Lambda = ', first_lambda(1,2)

#map
print 'Map = ', map(sqrt, [1,2,3,4])

#filter
print 'Filter = ', filter(lambda x: not x%2, [1, 2, 3, 4, 5])

#reduce
print 'Reduce = ', reduce(lambda x,y : x+y, xrange(1,101))

# List Comprehension
print [x for x in xrange(25) if not x % 2]

#String format
format_msg = '{0} {1} {2}. You are welcome!'
for message, title, name in [('Good morning', 'Mr.', 'Bruno'), ('Good night', 'Mr.', 'Bruno')]:
	print format_msg.format(message, title, name)



