# How to time your code
import timeit

a_dict = {}


def create_test_dict(size):
    for i in range(size):
        a_dict[str(i)] = i


def test1():
    values = [v for v in a_dict.values()][1:]
    return len(values)


def test2():
    values = list(a_dict.values())[1:]
    return len(values)


create_test_dict(100000)


# To test a function
res1 = timeit.timeit('test1()', setup='from  __main__ import test1', number=1)
print('result1: %s' % res1)

res2 = timeit.timeit('test2()', setup='from  __main__ import test2', number=1)
print('result2: %s' % res2)

# To test some code
timeit.timeit('values = [v for v in list()][1:]', number=1)
timeit.timeit('values = [v for v in list(range(100))][1:]', number=1)
