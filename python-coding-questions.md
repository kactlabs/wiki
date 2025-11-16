/ [Home](index.md)

## Python Coding Questions

**Note:** tbd



### Q0. Instance vs Class

### simple_print.py

```python
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
```

### simple_2.py:
```python
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

### Questions
1. Explain the code
2. Tell me whether it will execute or not
3. If it is buggy, fix it

<br>

---

## Q1. Temperature Converter

### converter.py

```python
class TemperatureConverter:

    factor = 1.8   # class variable

    def __init__(self, celsius):
        self.celsius = celsius

    def to_fahrenheit(self):
        return (self.celsius * TemperatureConverter.factor) + 32

    def show(self):
        print("Celsius:", self.celsius)
        print("Fahrenheit:", self.to_fahrenheit())
```

### test_converter.py

```python
import converter

t = converter.TemperatureConverter(25)
t.show()

x = converter.TemperatureConverter
x.show()
```

### Questions

1. Explain what this code is intended to do.
2. Will it run without errors? Why or why not?
3. Provide the corrected version if needed.

---

## Q2. Bank Account

### bank.py

```python
class BankAccount:

    def __init__():
        self.balance = 0

    def deposit(self, amount):
        self.balance = self.balance + amount

    def show_balance(self):
        print("Balance:", self.balance)
```

### test_bank.py

```python
from bank import BankAccount

acc = BankAccount()
acc.deposit(100)
acc.show_balance()
```

### Questions

1. Explain what the code is trying to implement.
2. Will the program execute?
3. Fix any issues and provide the corrected version.

---

## Q3. Shopping Cart

### cart.py

```python
class ShoppingCart:

    def __init__(self, items=[]):
        self.items = items

    def add_item(item, price):
        item['price'] = price
        self.items.append(item)

    def show_items(self):
        print(self.items)
```

### test_cart.py

```python
from cart import ShoppingCart

cart = ShoppingCart()
cart.add_item({"name": "Book"}, 300)
cart.add_item({"name": "Pen"}, 20)

cart.show_items()
```

### Questions

1. Why will add_item cause an error?
2. Identify all design issues in this class.
3. Rewrite the class correctly.

---

## **Q4**

### reverse_lines.py

```python
def reverse_lines(filename):
    reversed_lines = []
    with open(filename, "r") as f:
        lines = f.readlines()

    for line in lines:
        # remove newline and reverse characters
        s = line.strip()
        rev = ""
        for ch in s:
            rev = ch + rev
        reversed_lines.append(rev)

    # write results to a new file
    out_name = filename + "_reversed"
    with open(out_name, "w") as out:
        for line in reversed_lines:
            out.write(line + "\n")

if __name__ == "__main__":
    fname = "sample.txt"
    reverse_lines(fname)
    print("Done")
```

### Questions

1. What does this program attempt to do?
2. Will it always work? Identify any problems that may occur when running it.
3. Propose and implement a fix.

---

## **Q5**

### vowel_stats.py

```python
def vowel_stats(text):
    vowels = "aeiou"
    counts = {'a':0, 'e':0, 'i':0, 'o':0, 'u':0}
    total = 0

    for ch in text:
        if ch.lower() in vowels:
            counts[ch.lower()] += 1
            total += 1

    stats = {}
    for k, v in counts.items():
        stats[k] = (v, v / total * 100)  # (count, percentage)

    return stats

if __name__ == "__main__":
    sample = "This is an Example sentence to count Vowels."
    res = vowel_stats(sample)
    for k in sorted(res):
        print(k, res[k])
```

### Questions

1. Describe expected output and whether division by zero or other errors are possible.
2. Identify the bug(s) and explain why they happen with certain inputs.
3. Provide corrected code and show sample output for the given `sample`.

---

## **Q6**

### max_in_matrix.py

```python
def max_in_matrix(matrix):
    max_val = matrix[0][0]
    for row in matrix:
        for val in row:
            if val > max_val:
                max_val = val
    return max_val

if __name__ == "__main__":
    mat = [
        [3, 5, 2],
        [10, 6, 7],
        [1, 0, -1]
    ]
    print("Maximum is:", max_in_matrix(mat))
```

### Questions

1. What is the purpose of this function?
2. What edge cases should be considered (empty inputs, ragged rows)?
3. Modify `max_in_matrix` to safely handle an empty matrix and rows of variable length.

---

## **Q7**

### bank_account.py

```python
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("deposit must be positive")
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("insufficient funds")
        self.balance -= amount

    def transfer_to(self, other, amount):
        # transfer amount to another account
        self.withdraw(amount)
        other.deposit(amount)

    def __str__(self):
        return f"BankAccount(owner={self.owner}, balance={self.balance})"

if __name__ == "__main__":
    a = BankAccount("Alice", 100)
    b = BankAccount("Bob", 50)
    a.transfer_to(b, 30)
    print(a)
    print(b)
```

### Questions

1. Is this implementation correct? If so, why? If not, identify any hidden problems.
2. How does the `transfer_to` method behave in presence of exceptions? Is it atomic? Explain.
3. Suggest and implement an improvement to make transfers safer in case of errors.

---

## **Q8**

### cart.py

```python
class ShoppingCart:
    def __init__(self, items=[]):
        self.items = items

    def add_item(item_name, price, quantity=1):
        item = {"name": item_name, "price": price, "qty": quantity}
        self.items.append(item)

    def total(self):
        t = 0
        for it in self.items:
            t += it["price"] * it["qty"]
        return t

    def show(self):
        for it in self.items:
            print(f'{it["name"]} x{it["qty"]} = {it["price"] * it["qty"]}')
        print("Total:", self.total())

if __name__ == "__main__":
    c = ShoppingCart()
    c.add_item("Book", 200, 2)
    c.add_item("Pen", 15)
    c.show()
```

### Questions

1. Identify the problems in this class and explain what behavior they cause.
2. Which lines will raise exceptions or behave unexpectedly?
3. Provide corrected code and explain your changes.

---

## **Q9**

### primes_list.py

```python
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def primes_up_to(n):
    primes = []
    for num in range(2, n + 1):
        if is_prime(num):
            primes.append(num)
    return primes

if __name__ == "__main__":
    print(primes_up_to(50))
```

### Questions

1. Explain how `is_prime` is optimized compared to checking all divisors.
2. Is the `primes_up_to` function correct and efficient for moderate `n`? Why or why not?
3. Suggest a faster approach and outline (no need to implement) how you would change `primes_up_to` for large `n`.

---

## **Q10**

### file_copy.py

```python
def copy_file(src, dst):
    buffer = []
    with open(src, "r") as s:
        for line in s:
            buffer.append(line)

    with open(dst, "w") as d:
        for part in buffer:
            d.write(part)

if __name__ == "__main__":
    src_file = "data.bin"
    dst_file = "data_copy.bin"
    copy_file(src_file, dst_file)
    print("Copied")
```

### Questions

1. Will this code work for both text and binary files? Explain.
2. Identify the bug and its consequences for certain file types.
3. Provide corrected code that safely copies arbitrary files.

---

## **Q11**

### flatten.py

```python
def flatten(nested):
    result = []
    for item in nested:
        if isinstance(item, list):
            for sub in item:
                result.extend(flatten(sub))
        else:
            result.append(item)
    return result

if __name__ == "__main__":
    data = [1, [2, [3, 4], 5], 6]
    print(flatten(data))
```

### Questions

1. Does this `flatten` implementation work for arbitrarily nested lists? Explain any recursion issues.
2. Identify any bug(s) in how nested lists are handled. Give an example where it fails or causes an error.
3. Fix the implementation and demonstrate it on the provided `data`.

---

## **Q12**

### schedule.py

```python
from datetime import datetime, timedelta

def upcoming_dates(start_date_str, days, count):
    start = datetime.strptime(start_date_str, "%Y-%m-%d")
    results = []
    for i in range(count):
        d = start + timedelta(days=days * i)
        results.append(d.strftime("%Y-%m-%d"))
    return results

if __name__ == "__main__":
    dates = upcoming_dates("2025-02-28", 1, 5)
    for dt in dates:
        print(dt)
```

### Questions

1. What dates will be printed for the example call? Are there edge cases to be aware of?
2. Suppose we want weekly dates but skip weekends — outline how the function must change.
3. Rewrite the function to handle invalid date formats safely.

---

## **Q13**

### dict_merge.py

```python
def merge_counts(list_of_dicts):
    merged = {}
    for d in list_of_dicts:
        for k, v in d.items():
            merged[k] = merged.get(k, 0) + v
    return merged

if __name__ == "__main__":
    data = [
        {"a": 2, "b": 1},
        {"b": 3, "c": 5},
        {"a": 1, "c": 2}
    ]
    print(merge_counts(data))
```

### Questions

1. What is the expected printed output?
2. What happens if a dictionary contains a non-numeric value?
3. Rewrite `merge_counts` using `collections.Counter`.

---


## Q14

### rotate_list.py

```python
def rotate_right(lst, k):
    if not lst:
        return lst
    n = len(lst)
    k = k % n
    # rotate by slicing
    return lst[-k:] + lst[:-k]

if __name__ == "__main__":
    data = [1, 2, 3, 4, 5, 6]
    k = 2
    print("Original:", data)
    print("Rotated :", rotate_right(data, k))

    # rotate by n should return original
    print("Rotate by n:", rotate_right(data, len(data)))
    # rotate by 0
    print("Rotate by 0:", rotate_right(data, 0))
```

### Questions

1. What output does this program produce for the example runs?
2. Explain how slicing is used to rotate the list.
3. Modify `rotate_right` to rotate in-place without creating a new list.

---

## Q15

### read_json.py

```python
import json

def load_config(path):
    with open(path, "r") as f:
        data = json.load(f)
    return data

def get_database_host(cfg):
    return cfg["database"]["host"]

if __name__ == "__main__":
    cfg = load_config("config.json")
    print("Database host:", get_database_host(cfg))
```

### Questions

1. What will happen if `config.json` does not exist or is not valid JSON?
2. How would you change `get_database_host` to return a default host if the keys are missing?
3. Add exception handling to `load_config` that deals with missing files and JSON errors and returns an empty dict in those cases.

---

## Q16

### unique_words.py

```python
def unique_words(text):
    words = text.split()
    seen = set()
    result = []
    for w in words:
        wclean = w.strip(".,!?;:").lower()
        if wclean not in seen:
            seen.add(wclean)
            result.append(wclean)
    return result

if __name__ == "__main__":
    s = "Hello, world! Hello world. This is a test, a TEST."
    print(unique_words(s))
```

### Questions

1. What does the `unique_words` function return for the sample string?
2. Explain why `.lower()` and `.strip()` are used before checking `seen`.
3. Modify the function to preserve the original casing of the first occurrence while still deduping case-insensitively.

---

## Q17

### stopwatch.py

```python
import time

class Stopwatch:
    def __init__(self):
        self.start_time = None
        self.elapsed = 0

    def start(self):
        if self.start_time is None:
            self.start_time = time.time()

    def stop(self):
        if self.start_time is None:
            return
        self.elapsed += time.time() - self.start_time
        self.start_time = None

    def reset(self):
        self.start_time = None
        self.elapsed = 0

    def elapsed_seconds(self):
        if self.start_time is None:
            return self.elapsed
        return self.elapsed + (time.time() - self.start_time)

if __name__ == "__main__":
    sw = Stopwatch()
    sw.start()
    time.sleep(0.1)
    sw.stop()
    print("Elapsed:", sw.elapsed_seconds())
```

### Questions

1. Explain how this `Stopwatch` handles multiple start/stop cycles.
2. Is there any potential precision or logic issue if `stop` is called twice in a row? Explain.
3. Add a `lap()` method that records lap times without resetting the stopwatch, and show an example usage.

---

## Q18

### calc_stats.py

```python
def mean(nums):
    return sum(nums) / len(nums)

def variance(nums):
    m = mean(nums)
    total = 0
    for x in nums:
        total += (x - m) ** 2
    return total / (len(nums) - 1)

def stddev(nums):
    return variance(nums) ** 0.5

if __name__ == "__main__":
    data = [10, 12, 23, 23, 16, 23, 21, 16]
    print("Mean:", mean(data))
    print("Variance:", variance(data))
    print("Stddev:", stddev(data))
```

### Questions

1. What type of variance (population or sample) does this `variance` compute? Explain.
2. What happens if `nums` contains only one element? How would you handle that gracefully?
3. Modify `variance` to accept an argument that chooses between population and sample variance.

---

## Q19

### logger_deco.py

```python
import functools

def log_calls(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args={args} kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper

@log_calls
def multiply(a, b):
    return a * b

@log_calls
def greet(name="World"):
    return "Hello " + name

if __name__ == "__main__":
    print(multiply(3, 4))
    print(greet())
    print(greet(name="Alice"))
```

### Questions

1. Explain what the `log_calls` decorator does and why `functools.wraps` is used.
2. What output is printed when calling `multiply(3, 4)`?
3. Modify the decorator so it logs the execution time of the function as well.

---

## Q20

### sliding_window.py

```python
def sliding_window(seq, k):
    if k <= 0:
        raise ValueError("k must be positive")
    n = len(seq)
    if k > n:
        return []
    result = []
    for i in range(n - k + 1):
        window = []
        for j in range(k):
            window.append(seq[i + j])
        result.append(window)
    return result

if __name__ == "__main__":
    data = [1, 2, 3, 4, 5]
    print(sliding_window(data, 3))
```

### Questions

1. What does `sliding_window([1,2,3,4,5], 3)` return?
2. Rewrite `sliding_window` using list slicing instead of an inner loop.
3. Change `sliding_window` to be a generator that yields each window (so large sequences are handled memory-efficiently).

---

## Q21

### parse_csv.py

```python
def parse_csv_line(line):
    parts = line.split(",")
    return [p.strip() for p in parts]

def read_csv(path):
    rows = []
    with open(path, "r") as f:
        for line in f:
            if not line.strip():
                continue
            rows.append(parse_csv_line(line))
    return rows

if __name__ == "__main__":
    rows = read_csv("data.csv")
    for r in rows:
        print(r)
```

### Questions

1. What issues might arise if a CSV field contains commas inside quotes?
2. How would you modify `read_csv` to skip a header row if present?
3. Rewrite `read_csv` to use Python’s built-in `csv` module to properly handle quoted fields and different delimiters.

---

## Q22

### find_pairs.py

```python
def two_sum(nums, target):
    seen = {}
    for i, v in enumerate(nums):
        need = target - v
        if need in seen:
            return (seen[need], i)
        seen[v] = i
    return None

if __name__ == "__main__":
    arr = [2, 7, 11, 15]
    print(two_sum(arr, 9))
    print(two_sum(arr, 18))
```

### Questions

1. What does `two_sum` return for the two example calls?
2. Explain why `seen` stores indices and how it helps achieve O(n) time.
3. Modify `two_sum` to return all unique index pairs (order of pairs and indices within a pair can be arbitrary).

---

## Q23

### replace_words.py

```python
import re

def replace_words(text, replacements):
    # replacements: dict mapping old_word -> new_word
    pattern = re.compile(r'\b(' + '|'.join(re.escape(k) for k in replacements.keys()) + r')\b')
    return pattern.sub(lambda m: replacements[m.group(0)], text)

if __name__ == "__main__":
    text = "The cat chased the caterpillar. A cat is curious."
    repl = {"cat": "dog", "caterpillar": "butterfly"}
    print(replace_words(text, repl))
```

### Questions

1. What does this program print for the sample `text` and `repl`?
2. Explain why word-boundary `\b` is used in the regex pattern.
3. Make `replace_words` case-insensitive while preserving the case of the first letter of each replaced word (e.g., "Cat" -> "Dog", "cat" -> "dog").

---
