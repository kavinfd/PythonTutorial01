def do_something():
    print "some information"


def do_something_and_return_something():
    print "I am doing something"
    return "Hi there"


def do_something_with_this_values(value1, value2, value3):
    print value1
    print value2
    print value3


def do_something_with_this_values_and_return_something(value1, value2):
    print value1
    print value2
    return value1 + value2


result = do_something()

print result
result2 = do_something_and_return_something()
print result2
do_something_with_this_values("Hi", "Hello", "Fine")
result3 = do_something_with_this_values_and_return_something("Hello", "World")
print result3
