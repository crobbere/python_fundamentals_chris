import timeit
# --code not optimal--
# list comprehension mechanics are faster than normal for loops.
# list comprehension mechanics use less code lines

test_for_loop = '''
numbers = list(range(0, 100))
def standard_for_loop(n):
    result=[]
    for i in n:
        if i % 2 ==0:
            result.append(i)
    return result
standard_for_loop(numbers)
'''
test_list_comprehension = '''
numbers = list(range(0,100))
def list_comprehension(n):
    return [i for i in n if i % 2 ==0]
list_comprehension(numbers)
'''
print('Time for loop: ', timeit.timeit(test_for_loop))
print('Time list comprehension: ', timeit.timeit(test_list_comprehension))

# as you can see, list comprehensions are faster