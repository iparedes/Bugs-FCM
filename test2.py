

import timeit



code_to_test = """

a=['a','c','d','e','g','2','4','t','Y','A','B']
a.index('g')

"""
elapsed_time = timeit.timeit(code_to_test, number=1000000)
print(elapsed_time)
