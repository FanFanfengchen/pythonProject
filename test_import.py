import my_calculstor
print('Module imported successfully!')
print('Module attributes:', dir(my_calculstor))
print('Has my_adder:', hasattr(my_calculstor, 'my_adder'))
if hasattr(my_calculstor, 'my_adder'):
    print('my_adder function:', my_calculstor.my_adder)
    print('my_adder(5, 3):', my_calculstor.my_adder(5, 3))
