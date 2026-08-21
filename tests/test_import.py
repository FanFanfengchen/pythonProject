from utils.calculator import my_adder
print('Module imported successfully!')
print('Module attributes:', dir(my_adder))
print('Has my_adder:', hasattr(my_adder, '__call__'))
if hasattr(my_adder, '__call__'):
    print('my_adder function:', my_adder)
    print('my_adder(5, 3):', my_adder(5, 3))
