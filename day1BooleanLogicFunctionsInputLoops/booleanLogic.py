print "Not truth table"
print not True
print not False

print "Or truth table"
print True or True
print True or False
print False or True
print False or False

print "And truth table"
print True and True
print True and False
print False and True
print False and False

print "boolean expression"
print True and False or True and False

if True:
    print "I will always get here"


def true_func():
    return True


def false_func():
    return False


if true_func() or false_func():
    print "just to print this"

print 10 < 100
print 10 == 10
print 10 == 1
print 1 <= 0

# if and else are branching statement [expects a condition]
# while is looping statement [expects a condition]
# for is a iterating statement


# following is an example of infinite loop
# while True:
#     print "I will be printed to infinity"

i = 0
while i < 10:
    print "will be printed 10 times"
    i += 1
#
# import sys
# sys.stderr.write("I am wrinting in standard error")


