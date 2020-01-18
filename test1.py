

import timeit

code_to_test = """

a={}

b=['a','c','d','e','g','2','4','t','Y','A','B']
i=0
for elem in b:
	a[elem]=i




i=a['g']

"""
elapsed_time = timeit.timeit(code_to_test, number=1000000)
print(elapsed_time)
