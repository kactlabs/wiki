/ [Home](index.md)

## Python Coding Questions

**Note:** tbd



### 1
```
simple_print.py:

class NumberPrinter:

    def __init__(self, limit_y = 20):
        print("inside init")
        self.limit = limit_y

    def __del__(self):
        print("inside destructor")

    def print_numbers(self=None):
        print("printing numbers")
        limit = self.limit
        for index in range(limit):
            print(index + 1)

    def print_numbers_double(self):
        print("printing double")
        for index in range(self.limit):
            print(index * 2) 


simple_2.py:
import simple_print

obj = simple_print.NumberPrinter(7)
print(obj)
obj.print_numbers()
obj.print_numbers_double()

obj2 = simple_print.NumberPrinter
print(obj2)
obj2.print_numbers()


python simple_2.py
```

