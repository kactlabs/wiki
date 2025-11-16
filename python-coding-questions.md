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




## Q24

### power_table.py

```python
def power_table(n, power=2):
    """
    Return a list of strings showing i^power for i from 1..n
    Example entry: "3^2 = 9"
    """
    rows = []
    for i in range(1, n + 1):
        val = i ** power
        rows.append(f"{i}^{power} = {val}")
    return rows

def print_table(rows):
    for r in rows:
        print(r)

if __name__ == "__main__":
    table = power_table(10, 3)
    print_table(table)
    # Write to file
    with open("power_table.txt", "w") as f:
        for r in table:
            f.write(r + "\n")
```

### Questions

1. What output does this program produce when run as-is?
2. Is there any issue when `n` is zero or negative? How should the function behave?
3. Modify `power_table` so it returns an empty list for `n <= 0` and raise a `TypeError` if `n` is not an integer.

---

## Q25

### flatten_dict.py

```python
def flatten_dict(d, parent_key="", sep="."):
    items = []
    for k, v in d.items():
        new_key = parent_key + sep + k if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)

if __name__ == "__main__":
    nested = {
        "a": 1,
        "b": {"c": 2, "d": {"e": 3}},
        "f": 4
    }
    print(flatten_dict(nested))
```

### Questions

1. Describe the transformation `flatten_dict` performs on `nested`.
2. Will this function handle keys that are not strings (e.g., integers)? Explain.
3. Rewrite `flatten_dict` to preserve non-string keys by converting them to strings only in the composed keys, and ensure `sep` can be any character.

---

## Q26

### json_lines_writer.py

```python
import json

def write_json_lines(items, path):
    with open(path, "w") as f:
        for it in items:
            json_str = json.dumps(it)
            f.write(json_str)

if __name__ == "__main__":
    data = [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]
    write_json_lines(data, "out.jsonl")
```

### Questions

1. What file format is this intended to produce? Is the implementation correct for that format?
2. Identify any bug(s) that would make the output invalid or hard to parse.
3. Fix the function so it writes a valid JSON Lines file.

---

## Q27

### finder.py

```python
def find_substring_positions(s, sub):
    """
    Return list of starting indices where `sub` appears in `s`.
    Overlapping occurrences should be included.
    """
    results = []
    i = 0
    while True:
        idx = s.find(sub, i)
        if idx == -1:
            break
        results.append(idx)
        i = idx + len(sub)
    return results

if __name__ == "__main__":
    text = "abababa"
    sub = "aba"
    print(find_substring_positions(text, sub))
```

### Questions

1. What does this program print for the example and why?
2. Does the function include overlapping matches? Explain.
3. Modify the code so overlapping occurrences are included.

---

## Q28

### file_stats.py

```python
import os

def file_stats(path):
    stats = {}
    stats['size'] = os.path.getsize(path)
    stats['lines'] = 0
    with open(path, "r") as f:
        for _ in f:
            stats['lines'] += 1
    stats['words'] = 0
    with open(path, "r") as f:
        for line in f:
            stats['words'] += len(line.split())
    return stats

if __name__ == "__main__":
    p = "sample.txt"
    print(file_stats(p))
```

### Questions

1. What information does `file_stats` collect about `path`?
2. What errors or edge cases might occur when running this on a binary file or on a missing file?
3. Improve `file_stats` to (a) handle missing files gracefully, (b) open files in a mode appropriate for text only, and (c) return `None` or raise a clear exception for non-text files.

---

## Q29

### fibonacci_gen.py

```python
def fibonacci(n):
    """
    Return first n Fibonacci numbers as a list.
    """
    if n <= 0:
        return []
    if n == 1:
        return [0]
    seq = [0, 1]
    while len(seq) < n:
        seq.append(seq[-1] + seq[-2])
    return seq

if __name__ == "__main__":
    print(fibonacci(10))
    # print as generator example
    for x in fibonacci(5):
        print(x)
```

### Questions

1. Explain what `fibonacci(10)` returns.
2. The comment says "print as generator example" — is the function a generator? If not, convert it to one.
3. Write a memory-efficient generator `fibonacci_generator()` that yields Fibonacci numbers indefinitely, and show how to take the first `n` elements from it.

---

## Q30

### validate_email.py

```python
import re

EMAIL_RE = re.compile(r'^[\w\.-]+@[\w\.-]+\.\w+$')

def is_valid_email(email):
    return EMAIL_RE.match(email) is not None

if __name__ == "__main__":
    tests = ["alice@example.com", "bob@localhost", "carol@domain.co.uk", "bad@@x.com"]
    for t in tests:
        print(t, is_valid_email(t))
```

### Questions

1. For each test case, which will pass the regex and which will not?
2. Explain weaknesses of this regular expression for validating emails.
3. Improve `is_valid_email` so it allows common internationalized domain labels and multiple domain parts (e.g., `.co.uk`) while still being reasonably strict. (You do not need to implement full RFC compliance.)

---

## Q31

### merge_sorted.py

```python
def merge_sorted(a, b):
    """Merge two sorted lists into a single sorted list."""
    i, j = 0, 0
    out = []
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            out.append(a[i])
            i += 1
        else:
            out.append(b[j])
            j += 1
    # append remaining
    out.extend(a[i:])
    out.extend(b[j:])
    return out

if __name__ == "__main__":
    x = [1, 3, 5]
    y = [2, 4, 6]
    print(merge_sorted(x, y))
```

### Questions

1. What is the output of merging `x` and `y` in the example?
2. Is the function stable and does it preserve duplicates? Explain.
3. Modify `merge_sorted` to accept any iterable (not just lists) and return a generator that yields values one-by-one.

---

## Q32

### template_render.py

```python
def render_template(tpl, context):
    """
    Simple template renderer: replace {{key}} in tpl with context[key].
    """
    out = tpl
    for k, v in context.items():
        out = out.replace("{{" + k + "}}", str(v))
    return out

if __name__ == "__main__":
    tpl = "Hello {{name}}, you have {{count}} new messages."
    ctx = {"name": "Alice", "count": 5}
    print(render_template(tpl, ctx))
    # Edge example
    tpl2 = "{{greeting}} {{name}} {{greeting}}"
    print(render_template(tpl2, {"greeting": "Hi", "name": "Bob"}))
```

### Questions

1. For `tpl2`, what is printed and why?
2. Identify potential problems when keys in `context` can be substrings of other keys (e.g., `"a"` and `"ab"`). Provide an example.
3. Rewrite `render_template` to use a regex that replaces only `{{key}}` tokens and leaves other text intact, and ensure multiple occurrences are handled.

---

## Q33

### cpu_bound_sum.py

```python
def sum_of_squares(n):
    """
    Compute sum of squares from 1..n
    """
    total = 0
    for i in range(1, n + 1):
        total += i * i
    return total

if __name__ == "__main__":
    print(sum_of_squares(1000000))
    # naive timing
    import time
    t0 = time.time()
    s = sum_of_squares(2000000)
    t1 = time.time()
    print("Sum:", s)
    print("Elapsed:", t1 - t0)
```

### Questions

1. Explain the time complexity of `sum_of_squares`.
2. Suggest a mathematical formula that computes the same result faster, and implement it.
3. The code uses `time.time()` for timing — is this appropriate for short-running CPU measurements? If not, recommend a better timing function and explain why.

---



## Q34

### unique_paths.py

```python
def unique_paths(grid):
    """
    Count unique paths from top-left to bottom-right in a grid
    where 0 = free cell and 1 = obstacle. Only moves: right or down.
    """
    if not grid or not grid[0]:
        return 0

    rows = len(grid)
    cols = len(grid[0])
    dp = [[0] * cols for _ in range(rows)]

    # start cell
    if grid[0][0] == 0:
        dp[0][0] = 1

    # first column
    for r in range(1, rows):
        if grid[r][0] == 0:
            dp[r][0] = dp[r-1][0]
        else:
            dp[r][0] = 0

    # first row
    for c in range(1, cols):
        if grid[0][c] == 0:
            dp[0][c] = dp[0][c-1]
        else:
            dp[0][c] = 0

    for r in range(1, rows):
        for c in range(1, cols):
            if grid[r][c] == 0:
                dp[r][c] = dp[r-1][c] + dp[r][c-1]
            else:
                dp[r][c] = 0

    return dp[-1][-1]

if __name__ == "__main__":
    g = [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]
    print(unique_paths(g))
```

### Questions

1. What value is printed for the sample grid and why?
2. What edge cases should `unique_paths` handle (e.g., start or end blocked)? Describe behavior.
3. Modify the function to use O(min(rows, cols)) extra space instead of O(rows*cols).

---

## Q35

### config_validator.py

```python
def validate_config(cfg):
    """
    cfg expected to be a dict with keys:
      - name (str)
      - retries (int, >=0)
      - timeout (float, >0)
      - endpoints (list of str)
    Returns True if valid, else raises ValueError.
    """
    if not isinstance(cfg, dict):
        raise ValueError("cfg must be a dict")

    if 'name' not in cfg or not isinstance(cfg['name'], str):
        raise ValueError("name missing or not a string")

    if 'retries' in cfg:
        if not isinstance(cfg['retries'], int) or cfg['retries'] < 0:
            raise ValueError("invalid retries")

    if 'timeout' not in cfg:
        raise ValueError("timeout missing")
    if not (isinstance(cfg['timeout'], int) or isinstance(cfg['timeout'], float)) or cfg['timeout'] <= 0:
        raise ValueError("invalid timeout")

    if 'endpoints' not in cfg or not isinstance(cfg['endpoints'], list):
        raise ValueError("endpoints missing or not a list")
    for e in cfg['endpoints']:
        if not isinstance(e, str) or not e:
            raise ValueError("invalid endpoint in list")

    return True

if __name__ == "__main__":
    example = {
        "name": "svc",
        "retries": 3,
        "timeout": 2.5,
        "endpoints": ["https://a.example", "https://b.example"]
    }
    print(validate_config(example))
```

### Questions

1. Explain all validations performed by `validate_config`. Which inputs will cause exceptions?
2. Suppose `retries` is omitted — is that acceptable? If yes, what semantics does the function enforce?
3. Extend `validate_config` to fill missing optional keys with defaults (`retries=0`) and return a validated copy of the config instead of `True`.

---

## Q36

### parallel_sum.py

```python
from concurrent.futures import ThreadPoolExecutor, as_completed

def chunked_sum(nums, workers=4):
    n = len(nums)
    if n == 0:
        return 0
    size = (n + workers - 1) // workers
    def chunk_sum(start):
        end = min(start + size, n)
        s = 0
        for i in range(start, end):
            s += nums[i]
        return s

    starts = list(range(0, n, size))
    total = 0
    with ThreadPoolExecutor(max_workers=workers) as ex:
        futures = [ex.submit(chunk_sum, st) for st in starts]
        for fut in as_completed(futures):
            total += fut.result()
    return total

if __name__ == "__main__":
    data = list(range(1, 10001))
    print(chunked_sum(data, workers=8))
```

### Questions

1. What does `chunked_sum` compute and why might you choose a thread pool for it?
2. Are there cases where this approach is slower than a single-threaded sum? Explain.
3. Rewrite `chunked_sum` using `ProcessPoolExecutor` for CPU-bound work and explain trade-offs.

---

## Q37

### regex_groups.py

```python
import re

def extract_dates(text):
    """
    Find dates in YYYY-MM-DD format and return list of tuples (year, month, day)
    """
    pattern = re.compile(r'(\d{4})-(\d{2})-(\d{2})')
    results = []
    for m in pattern.finditer(text):
        year, month, day = m.groups()
        results.append((int(year), int(month), int(day)))
    return results

if __name__ == "__main__":
    s = "Events: 2025-01-01 start, 2025-12-31 end, invalid 2025-13-01"
    print(extract_dates(s))
```

### Questions

1. What tuples will `extract_dates` return for the sample string? Are invalid month values filtered out?
2. Modify the regex (or the code) so that months are validated to 01–12 and days 01–31 (simple validation, no leap-year checks required).
3. Change `extract_dates` to return `datetime.date` objects instead of tuples when valid, and skip invalid matches.

---

## Q38

### settings_merge.py

```python
def merge_defaults(user_cfg, defaults):
    """
    Merge user_cfg onto defaults, but do not modify the originals.
    Nested dicts should be merged recursively.
    """
    def merge(a, b):
        out = {}
        for k, v in b.items():
            out[k] = v
        for k, v in a.items():
            if k in out and isinstance(out[k], dict) and isinstance(v, dict):
                out[k] = merge(v, out[k])
            else:
                out[k] = v
        return out

    return merge(user_cfg, defaults)

if __name__ == "__main__":
    defaults = {"a": 1, "b": {"x": 5, "y": 6}}
    user = {"b": {"y": 20}, "c": 3}
    print(merge_defaults(user, defaults))
```

### Questions

1. What is the printed merged dictionary for the example? Explain order of precedence.
2. Is any of the original input mutated by `merge_defaults`? Justify.
3. Rewrite `merge_defaults` to handle lists by concatenating them when both default and user values are lists (user values appended after defaults).

---

## Q39

### html_text_extractor.py

```python
from html.parser import HTMLParser

class TextExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.parts = []
        self._ignore = False

    def handle_starttag(self, tag, attrs):
        if tag in ("script", "style"):
            self._ignore = True

    def handle_endtag(self, tag):
        if tag in ("script", "style"):
            self._ignore = False

    def handle_data(self, data):
        if not self._ignore:
            self.parts.append(data)

def extract_text(html):
    parser = TextExtractor()
    parser.feed(html)
    return " ".join(p.strip() for p in parser.parts if p.strip())

if __name__ == "__main__":
    sample = "<html><head><style>h{}</style></head><body><h1>Title</h1><p>Hello <b>world</b></p><script>var a=1;</script></body></html>"
    print(extract_text(sample))
```

### Questions

1. What output is produced by `extract_text` for the sample HTML?
2. Identify limitations of this simple extractor (e.g., entity handling, nested tags, preserving whitespace).
3. Modify `TextExtractor` to also ignore the contents of `<noscript>` tags and to unescape HTML entities using `html.unescape`.

---

## Q40

### retry_call.py

```python
import time
import random

def unreliable_operation():
    # simulate transient failure ~50% of the time
    if random.random() < 0.5:
        raise RuntimeError("transient error")
    return "ok"

def retry(func, attempts=3, delay=1.0, backoff=2.0):
    last_exc = None
    for attempt in range(1, attempts + 1):
        try:
            return func()
        except Exception as e:
            last_exc = e
            if attempt == attempts:
                break
            time.sleep(delay)
            delay *= backoff
    raise last_exc

if __name__ == "__main__":
    print(retry(unreliable_operation, attempts=5, delay=0.2))
```

### Questions

1. Explain how `retry` implements retries and exponential backoff. What happens when all attempts fail?
2. Why might catching `Exception` be too broad in some contexts? Suggest how to allow only certain exceptions to be retried.
3. Change `retry` to accept an optional `on_retry` callback that's called with `(attempt, exception)` before sleeping, and demonstrate using it to log retries.

---


## Q41

### unique_chars.py

```python
def first_unique_char(s):
    """
    Return the index of the first non-repeating character in s,
    or -1 if none exists.
    """
    counts = {}
    for ch in s:
        counts[ch] = counts.get(ch, 0) + 1

    for i, ch in enumerate(s):
        if counts.get(ch, 0) == 1:
            return i
    return -1

if __name__ == "__main__":
    tests = ["leetcode", "loveleetcode", "aabb"]
    for t in tests:
        print(t, first_unique_char(t))
```

### Questions

1. What outputs are printed for the sample `tests`?
2. Explain the time and space complexity of `first_unique_char`.
3. Modify the function to return the character itself instead of the index (or `None` if not found).

---

## Q42

### chunked_reader.py

```python
def read_in_chunks(path, chunk_size=1024):
    """
    Yield file contents in chunks of up to chunk_size bytes (text mode).
    """
    with open(path, "r", encoding="utf-8") as f:
        while True:
            data = f.read(chunk_size)
            if not data:
                break
            yield data

if __name__ == "__main__":
    # Example: print first 3 chunks of a large file
    i = 0
    for part in read_in_chunks("large.txt", chunk_size=4096):
        print("Chunk", i, "size", len(part))
        i += 1
        if i >= 3:
            break
```

### Questions

1. What are advantages of reading files in chunks rather than all at once?
2. Is this implementation safe for binary files? Explain.
3. Modify `read_in_chunks` so it can operate in either text or binary mode based on an argument, and ensure proper encoding handling.

---

## Q43

### serialize_person.py

```python
import json
from dataclasses import dataclass, asdict

@dataclass
class Person:
    name: str
    age: int
    emails: list

def save_person(p: Person, path):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(asdict(p), f, ensure_ascii=False, indent=2)

def load_person(path):
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return Person(**data)

if __name__ == "__main__":
    p = Person("Alice", 30, ["alice@example.com"])
    save_person(p, "person.json")
    p2 = load_person("person.json")
    print(p2)
```

### Questions

1. Explain how `dataclasses.asdict` is used to serialize `Person`.
2. What issues might arise if `Person` contained non-serializable fields (e.g., `datetime`)?
3. Modify `save_person`/`load_person` to accept and return a list of `Person` objects in one file.

---

## Q44

### matrix_multiply.py

```python
def multiply_matrix(a, b):
    """
    Multiply matrix a (m x p) by b (p x n) and return (m x n) result.
    Matrices are lists of lists, row-major.
    """
    m = len(a)
    p = len(a[0]) if a else 0
    # validate b dimensions
    n = len(b[0]) if b and b[0] else 0

    # initialize result
    res = [[0] * n for _ in range(m)]

    for i in range(m):
        for j in range(n):
            s = 0
            for k in range(p):
                s += a[i][k] * b[k][j]
            res[i][j] = s
    return res

if __name__ == "__main__":
    A = [[1, 2, 3], [4, 5, 6]]
    B = [[7, 8], [9, 10], [11, 12]]
    print(multiply_matrix(A, B))
```

### Questions

1. What is the resulting matrix for the example `A` and `B`?
2. Identify edge cases and potential errors (e.g., empty matrices, incompatible shapes).
3. Add input validation that raises a `ValueError` for incompatible dimensions and handle empty matrices gracefully.

---

## Q45

### balanced_brackets.py

```python
def is_balanced(s):
    pairs = {"(": ")", "[": "]", "{": "}"}
    stack = []
    for ch in s:
        if ch in pairs:
            stack.append(ch)
        elif ch in pairs.values():
            if not stack:
                return False
            top = stack.pop()
            if pairs[top] != ch:
                return False
    return len(stack) == 0

if __name__ == "__main__":
    tests = ["()", "([{}])", "(]", "([)"]
    for t in tests:
        print(t, is_balanced(t))
```

### Questions

1. What are the boolean results for the provided `tests`?
2. Explain why a stack is appropriate for this problem.
3. Modify `is_balanced` to ignore non-bracket characters (so `"a(b)c"` is treated as balanced).

---

## Q46

### top_k_words.py

```python
from collections import Counter

def top_k_words(text, k=3):
    words = [w.strip(".,!?;:()[]\"'").lower() for w in text.split()]
    cnt = Counter(words)
    return [w for w, _ in cnt.most_common(k)]

if __name__ == "__main__":
    sample = "apple banana apple orange banana apple kiwi"
    print(top_k_words(sample, 2))
```

### Questions

1. What does `top_k_words(sample, 2)` return for the sample text?
2. Explain how `Counter.most_common` behaves with ties.
3. Modify the function to return `(word, count)` tuples and to ignore empty strings that may result from stripping punctuation.

---

## Q47

### normalize_path.py

```python
import os

def normalize_paths(paths):
    """
    Given a list of file paths, return a list of normalized absolute paths.
    """
    out = []
    for p in paths:
        # expand user, convert to absolute, and normalize
        expanded = os.path.expanduser(p)
        ab = os.path.abspath(expanded)
        norm = os.path.normpath(ab)
        out.append(norm)
    return out

if __name__ == "__main__":
    paths = ["~/docs/../docs/file.txt", "./script.py", "/tmp//a/b/../c"]
    for p in normalize_paths(paths):
        print(p)
```

### Questions

1. Describe what `normalize_paths` does to each input path and why each step is used.
2. What differences would you expect when running this on Windows vs Unix-like systems?
3. Modify the function to optionally check that each normalized path exists and return a tuple `(path, exists)` for each entry.

---

## Q48

### http_status_summary.py

```python
def summarize_status(codes):
    """
    Given an iterable of HTTP status codes (ints), return a dict summarizing:
      - total: total count
      - by_class: dict mapping '2xx','3xx','4xx','5xx' to counts
      - others: count of codes outside 100-599
    """
    summary = {"total": 0, "by_class": {"2xx": 0, "3xx": 0, "4xx": 0, "5xx": 0}, "others": 0}
    for c in codes:
        summary["total"] += 1
        if 200 <= c < 300:
            summary["by_class"]["2xx"] += 1
        elif 300 <= c < 400:
            summary["by_class"]["3xx"] += 1
        elif 400 <= c < 500:
            summary["by_class"]["4xx"] += 1
        elif 500 <= c < 600:
            summary["by_class"]["5xx"] += 1
        else:
            summary["others"] += 1
    return summary

if __name__ == "__main__":
    sample = [200, 201, 301, 404, 500, 700, 150]
    print(summarize_status(sample))
```

### Questions

1. What is the returned dictionary for the `sample` list?
2. Explain why codes like `150` and `700` are counted in `others`.
3. Extend `summarize_status` to also return the most frequent exact status code (or `None` if list empty).

---

## Q49

### median_of_list.py

```python
def median(nums):
    """
    Return the median of a list of numbers. If list length is even, return the average of two middle values.
    """
    if not nums:
        raise ValueError("empty list")
    sorted_nums = sorted(nums)
    n = len(sorted_nums)
    mid = n // 2
    if n % 2 == 1:
        return sorted_nums[mid]
    else:
        return (sorted_nums[mid - 1] + sorted_nums[mid]) / 2

if __name__ == "__main__":
    print(median([3, 1, 2]))
    print(median([4, 1, 2, 3]))
```

### Questions

1. What are the outputs for the two example calls?
2. Discuss numeric types: what happens if input contains ints vs floats?
3. Modify `median` to accept any iterable (not only lists) and avoid copying the entire data when possible.

---

## Q50

### adaptive_sample.py

```python
import random

def adaptive_sample(population, k):
    """
    Return k unique items sampled from population without replacement.
    If k >= len(population), return a shuffled copy of the population.
    """
    n = len(population)
    if k >= n:
        out = list(population)
        random.shuffle(out)
        return out
    # reservoir sampling when k << n could be used; for simplicity use random.sample here
    return random.sample(population, k)

if __name__ == "__main__":
    data = list(range(10))
    print(adaptive_sample(data, 3))
    print(adaptive_sample(data, 15))
```

### Questions

1. Explain behavior when `k` is less than, equal to, or greater than the population size.
2. Why might reservoir sampling be preferred for streaming or very large populations? Outline how reservoir sampling works.
3. Replace `random.sample` with an explicit reservoir sampling implementation that works on any iterable and returns `k` items.

---





## Q51

### batch_processor.py

```python
def process_item(item):
    # placeholder processing (e.g., transform)
    return item * 2

def process_in_batches(items, batch_size=10):
    """
    Process items in batches and yield results for each batch as a list.
    """
    n = len(items)
    for i in range(0, n, batch_size):
        batch = items[i:i+batch_size]
        out = []
        for it in batch:
            out.append(process_item(it))
        yield out

if __name__ == "__main__":
    data = list(range(1, 35))
    for idx, batch in enumerate(process_in_batches(data, 8)):
        print("Batch", idx, "->", batch)
```

### Questions

1. What does the program print when run as-is?
2. Explain memory characteristics of this design vs returning a single combined list.
3. Modify `process_in_batches` to accept a callable `processor` argument instead of using `process_item` global.

---

## Q52

### csv_to_dicts.py

```python
def csv_to_dicts(path):
    """
    Read a simple CSV (first row headers) and return a list of dicts.
    Assumes no quoted commas and simple format.
    """
    rows = []
    with open(path, "r", encoding="utf-8") as f:
        headers = None
        for line in f:
            line = line.rstrip("\n")
            if not headers:
                headers = [h.strip() for h in line.split(",")]
                continue
            parts = [p.strip() for p in line.split(",")]
            row = {headers[i]: parts[i] if i < len(parts) else "" for i in range(len(headers))}
            rows.append(row)
    return rows

if __name__ == "__main__":
    # example usage (file not actually provided here)
    print(csv_to_dicts("sample.csv"))
```

### Questions

1. What assumptions does `csv_to_dicts` make about the CSV file? Name potential failure modes.
2. How does the code handle rows with fewer fields than headers? More fields than headers?
3. Replace the naive parsing with Python’s `csv.DictReader` to robustly support quoted fields.

---

## Q53

### lowercase_keys.py

```python
def lowercase_keys(d):
    """
    Recursively convert all dictionary keys to lowercase (string keys only).
    Returns a new dict; does not modify input.
    """
    if not isinstance(d, dict):
        return d
    out = {}
    for k, v in d.items():
        new_key = k.lower() if isinstance(k, str) else k
        if isinstance(v, dict):
            out[new_key] = lowercase_keys(v)
        else:
            out[new_key] = v
    return out

if __name__ == "__main__":
    data = {"Name": "Alice", "Meta": {"ID": 1, "Tags": {"TagOne": True}}}
    print(lowercase_keys(data))
```

### Questions

1. What output does this program produce for `data`?
2. How does the function treat non-string keys?
3. Modify the function to also convert keys in lists of dicts (e.g., `{"items":[{"A":1},{"B":2}]}`).

---

## Q54

### angle_converter.py

```python
import math

def deg_to_rad(deg):
    return deg * math.pi / 180.0

def rotate_points(points, angle_deg):
    """
    Rotate a list of (x, y) points by angle_deg around the origin.
    """
    theta = deg_to_rad(angle_deg)
    cos_t = math.cos(theta)
    sin_t = math.sin(theta)
    out = []
    for x, y in points:
        xr = x * cos_t - y * sin_t
        yr = x * sin_t + y * cos_t
        out.append((xr, yr))
    return out

if __name__ == "__main__":
    pts = [(1, 0), (0, 1)]
    print(rotate_points(pts, 90))
```

### Questions

1. What coordinates are produced when rotating `pts` by 90 degrees? Explain sign and rounding considerations.
2. Why use radians internally? What issues arise if degrees are passed directly to `math.cos`?
3. Add an optional `origin` parameter so points can be rotated around an arbitrary origin.

---

## Q55

### dict_filter.py

```python
def filter_dict(d, predicate):
    """
    Return a new dict containing only items where predicate(key, value) is True.
    """
    out = {}
    for k, v in d.items():
        if predicate(k, v):
            out[k] = v
    return out

if __name__ == "__main__":
    items = {"a": 1, "b": 10, "c": 5}
    print(filter_dict(items, lambda k, v: v >= 5))
```

### Questions

1. What output is printed by the example call?
2. How would you implement `filter_dict` using dict comprehensions? Provide the code.
3. Modify `filter_dict` to accept either a predicate or a list of allowed keys; handle both cases.

---

## Q56

### http_client_simple.py

```python
import urllib.request
import json

def fetch_json(url, timeout=5):
    req = urllib.request.Request(url, headers={"Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        data = r.read().decode("utf-8")
        return json.loads(data)

if __name__ == "__main__":
    # Example: won't run here, but illustrates usage
    print(fetch_json("https://api.example.com/info"))
```

### Questions

1. What exceptions might `fetch_json` raise during network failures or invalid responses?
2. How would you add retry logic with exponential backoff for transient HTTP errors? Outline changes.
3. Rewrite `fetch_json` using `requests` (assume it's available) and include a timeout and basic error handling returning `None` on failure.

---

## Q57

### unique_substrings.py

```python
def unique_substrings(s, k):
    """
    Return a sorted list of unique substrings of length k from s.
    """
    if k <= 0:
        return []
    n = len(s)
    seen = set()
    for i in range(0, n - k + 1):
        seen.add(s[i:i+k])
    return sorted(seen)

if __name__ == "__main__":
    print(unique_substrings("ababa", 2))
```

### Questions

1. What substrings are returned for the example and why are they sorted?
2. Explain time and memory complexity for large `s`.
3. Modify the function to return substrings in original order of first appearance (no sorting).

---

## Q58

### throttle.py

```python
import time
from collections import deque

class Throttler:
    """
    Allow up to `limit` actions in any rolling `period` seconds.
    """
    def __init__(self, limit, period=1.0):
        self.limit = limit
        self.period = period
        self.timestamps = deque()

    def allow(self):
        now = time.time()
        while self.timestamps and now - self.timestamps[0] > self.period:
            self.timestamps.popleft()
        if len(self.timestamps) < self.limit:
            self.timestamps.append(now)
            return True
        return False

if __name__ == "__main__":
    t = Throttler(3, period=2.0)
    for i in range(6):
        print(i, t.allow())
        time.sleep(0.5)
```

### Questions

1. Describe the behavior of this throttler for the example loop.
2. Explain the difference between a sliding window (this) and fixed-window rate limiter.
3. Modify `allow` to return the number of seconds the caller should wait before the next allowed action when rate-limited.

---

## Q59

### ping_hosts.py

```python
import subprocess
import platform

def ping(host, count=1, timeout=1):
    system = platform.system()
    if system == "Windows":
        cmd = ["ping", "-n", str(count), "-w", str(timeout * 1000), host]
    else:
        cmd = ["ping", "-c", str(count), "-W", str(timeout), host]
    try:
        subprocess.check_output(cmd, stderr=subprocess.STDOUT)
        return True
    except subprocess.CalledProcessError:
        return False

if __name__ == "__main__":
    hosts = ["8.8.8.8", "example.invalid"]
    for h in hosts:
        print(h, ping(h))
```

### Questions

1. What are portability issues to consider with using system `ping`?
2. Why is `timeout` multiplied by 1000 on Windows? Explain units.
3. Replace subprocess usage with `socket`-based TCP connect checks to port 80 as an alternative reachability test; outline the approach.

---

## Q60

### memoize.py

```python
import functools

def memoize(func):
    cache = {}
    @functools.wraps(func)
    def wrapper(*args):
        if args in cache:
            return cache[args]
        res = func(*args)
        cache[args] = res
        return res
    return wrapper

@memoize
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

if __name__ == "__main__":
    print(fib(30))
```

### Questions

1. Explain how `memoize` speeds up the `fib` function.
2. What limitations exist with using `args` as a cache key? Give examples.
3. Modify `memoize` to accept an optional `maxsize` parameter and implement a simple LRU eviction policy.

---

## Q61

### timestamped_logger.py

```python
import logging
from datetime import datetime

def get_logger(name):
    logger = logging.getLogger(name)
    if not logger.handlers:
        handler = logging.StreamHandler()
        formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)
    return logger

if __name__ == "__main__":
    log = get_logger("myapp")
    log.info("Started")
    log.error("An error occurred")
```

### Questions

1. What will the logger print when run? Explain why the `if not logger.handlers` guard is important.
2. How would you add file logging and log rotation using `logging.handlers.RotatingFileHandler`? Outline changes.
3. Modify `get_logger` to accept a `level` argument and an optional `file_path` to log to a file as well as console.

---

## Q62

### topological_sort.py

```python
from collections import defaultdict, deque

def topological_sort(edges):
    """
    edges: list of (u, v) meaning u -> v
    Returns list of nodes in topological order or raises ValueError for cycles.
    """
    g = defaultdict(list)
    indeg = {}
    nodes = set()
    for u, v in edges:
        g[u].append(v)
        nodes.add(u); nodes.add(v)
        indeg[v] = indeg.get(v, 0) + 1
        indeg.setdefault(u, 0)

    q = deque([n for n in nodes if indeg.get(n, 0) == 0])
    res = []
    while q:
        x = q.popleft()
        res.append(x)
        for nb in g[x]:
            indeg[nb] -= 1
            if indeg[nb] == 0:
                q.append(nb)
    if len(res) != len(nodes):
        raise ValueError("cycle detected")
    return res

if __name__ == "__main__":
    es = [("a","b"), ("b","c"), ("a","c")]
    print(topological_sort(es))
```

### Questions

1. What topological ordering(s) are valid for the example edges?
2. Why does the algorithm detect cycles by comparing lengths? Explain.
3. Modify the function to accept nodes with zero degree even if they don't appear in `edges` (add an optional `nodes` parameter).

---

## Q63

### chunked_writer.py

```python
def write_in_chunks(path, data_iter, chunk_size=1024):
    """
    Write data from an iterator to a file in binary mode. Each item in data_iter is bytes.
    """
    with open(path, "wb") as f:
        buffer = bytearray()
        for chunk in data_iter:
            buffer.extend(chunk)
            if len(buffer) >= chunk_size:
                f.write(buffer[:chunk_size])
                del buffer[:chunk_size]
        if buffer:
            f.write(buffer)

if __name__ == "__main__":
    # Example: simulate streaming bytes of varying sizes
    def gen():
        for i in range(10):
            yield bytes([i]) * (i + 1)
    write_in_chunks("out.bin", gen(), chunk_size=8)
```

### Questions

1. Explain how the buffering logic ensures writes of `chunk_size` bytes when possible.
2. Why open the file with `"wb"` here instead of text mode?
3. Modify `write_in_chunks` to accept both bytes and memoryview objects and to optionally flush after each write.

---

## Q64

### hex_palette.py

```python
def hex_to_rgb(h):
    h = h.lstrip("#")
    if len(h) == 3:
        h = "".join([c*2 for c in h])
    r = int(h[0:2], 16)
    g = int(h[2:4], 16)
    b = int(h[4:6], 16)
    return (r, g, b)

def generate_gradient(start_hex, end_hex, steps):
    s = hex_to_rgb(start_hex)
    e = hex_to_rgb(end_hex)
    res = []
    for i in range(steps):
        t = i / (steps - 1) if steps > 1 else 0
        r = int(round(s[0] + (e[0]-s[0]) * t))
        g = int(round(s[1] + (e[1]-s[1]) * t))
        b = int(round(s[2] + (e[2]-s[2]) * t))
        res.append('#{0:02x}{1:02x}{2:02x}'.format(r, g, b))
    return res

if __name__ == "__main__":
    print(generate_gradient("#ff0000", "#00ff00", 5))
```

### Questions

1. What gradient hex colors are produced for the example?
2. Explain handling of 3-digit hex values in `hex_to_rgb`.
3. Add input validation for hex strings and raise a `ValueError` for invalid formats.

---

## Q65

### retry_queue.py

```python
import time
from collections import deque

class RetryQueue:
    def __init__(self):
        self.queue = deque()

    def push(self, func, max_attempts=3):
        self.queue.append((func, 0, max_attempts))

    def run_once(self):
        """
        Run one attempt for each queued function. If it fails, increment attempt count;
        if attempts remain, keep it for next run.
        """
        n = len(self.queue)
        for _ in range(n):
            func, attempts, max_attempts = self.queue.popleft()
            try:
                func()
            except Exception:
                attempts += 1
                if attempts < max_attempts:
                    self.queue.append((func, attempts, max_attempts))

if __name__ == "__main__":
    def flaky():
        import random
        if random.random() < 0.7:
            raise RuntimeError("fail")
        print("ok")
    rq = RetryQueue()
    rq.push(flaky, max_attempts=5)
    for _ in range(6):
        rq.run_once()
        time.sleep(0.2)
```

### Questions

1. Explain how `RetryQueue` manages retries and when functions are removed.
2. What happens if a function takes a long time or blocks? How would that affect the queue?
3. Modify `push` to accept an optional `delay` parameter (seconds) and ensure a failed function is retried only after its delay has elapsed.

---

## Q66

### semaphore_counter.py

```python
import threading
import time

class Counter:
    def __init__(self):
        self.value = 0
        self.lock = threading.Lock()

    def inc(self):
        with self.lock:
            v = self.value
            time.sleep(0.001)
            self.value = v + 1

def worker(counter, n):
    for _ in range(n):
        counter.inc()

if __name__ == "__main__":
    c = Counter()
    threads = []
    for _ in range(5):
        t = threading.Thread(target=worker, args=(c, 100))
        t.start()
        threads.append(t)
    for t in threads:
        t.join()
    print("Final value:", c.value)
```

### Questions

1. Why is `Lock` used here and is it sufficient to avoid race conditions?
2. What final value is expected and why might it differ without the lock?
3. Modify the class to also support a `decrement` method and implement it safely.

---

## Q67

### sparse_vector.py

```python
class SparseVector:
    def __init__(self, length, data=None):
        self.length = length
        # data: dict index -> value
        self.data = dict(data) if data else {}

    def dot(self, other):
        if self.length != other.length:
            raise ValueError("length mismatch")
        total = 0
        # iterate over smaller dict for efficiency
        a, b = (self.data, other.data) if len(self.data) <= len(other.data) else (other.data, self.data)
        for i, v in a.items():
            total += v * b.get(i, 0)
        return total

if __name__ == "__main__":
    v1 = SparseVector(5, {0:1, 3:2})
    v2 = SparseVector(5, {1:4, 3:3})
    print(v1.dot(v2))
```

### Questions

1. What is the computed dot product for the example vectors?
2. Why iterate over the smaller dictionary? Explain complexity benefits.
3. Add methods for `__add__` and `__sub__` to return new `SparseVector` objects.

---

## Q68

### yaml_loader.py

```python
def load_yaml(path):
    """
    Load YAML file and return Python object.
    Requires pyyaml installed.
    """
    import yaml
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

if __name__ == "__main__":
    # Usage example (file not provided here)
    print(load_yaml("config.yaml"))
```

### Questions

1. What is difference between `yaml.safe_load` and `yaml.load`? Why prefer `safe_load`?
2. How do you handle missing `pyyaml` dependency gracefully so the function raises a clear error?
3. Extend `load_yaml` to validate the YAML against a simple schema (e.g., ensure top-level is a dict and contains a `version` key).

---

## Q69

### batch_delete_files.py

```python
import os
import glob

def delete_matching(pattern):
    """
    Delete files matching the glob pattern. Return list of deleted paths.
    """
    deleted = []
    for p in glob.glob(pattern):
        try:
            os.remove(p)
            deleted.append(p)
        except OSError:
            pass
    return deleted

if __name__ == "__main__":
    print(delete_matching("tmp_*.log"))
```

### Questions

1. What risks exist when executing `delete_matching` and how could you mitigate them?
2. Why catch `OSError` broadly and what information might you want to log instead?
3. Modify the function to accept a `dry_run` flag that returns which files would be deleted without deleting them.

---

## Q70

### date_range.py

```python
from datetime import datetime, timedelta

def date_range(start_str, end_str, fmt="%Y-%m-%d"):
    """
    Yield date strings from start to end inclusive.
    """
    start = datetime.strptime(start_str, fmt)
    end = datetime.strptime(end_str, fmt)
    cur = start
    while cur <= end:
        yield cur.strftime(fmt)
        cur += timedelta(days=1)

if __name__ == "__main__":
    for d in date_range("2025-01-01", "2025-01-05"):
        print(d)
```

### Questions

1. What dates are printed by the example?
2. How would you change `date_range` to accept `datetime.date` objects as well as strings?
3. Modify `date_range` to yield `datetime.date` objects instead of formatted strings and accept an optional `step` (timedelta) parameter.

---

## Q71

### matrix_transpose.py

```python
def transpose(matrix):
    """
    Transpose a matrix represented as list of rows.
    """
    if not matrix:
        return []
    rows = len(matrix)
    cols = len(matrix[0])
    res = [[None] * rows for _ in range(cols)]
    for i in range(rows):
        for j in range(cols):
            res[j][i] = matrix[i][j]
    return res

if __name__ == "__main__":
    M = [[1,2,3],[4,5,6]]
    print(transpose(M))
```

### Questions

1. What is the transposed matrix for `M`?
2. What assumptions does this code make about row lengths? How to handle ragged matrices?
3. Provide an implementation that transposes a rectangular matrix using `zip`.

---

## Q72

### weighted_random_choice.py

```python
import random
import bisect

def weighted_choice(items, weights):
    """
    items: list of values
    weights: list of positive numbers
    Returns a single randomly chosen item based on weights.
    """
    if len(items) != len(weights):
        raise ValueError("items and weights length mismatch")
    cumulative = []
    total = 0
    for w in weights:
        total += w
        cumulative.append(total)
    r = random.random() * total
    idx = bisect.bisect_right(cumulative, r)
    return items[idx]

if __name__ == "__main__":
    print(weighted_choice(["a","b","c"], [0.1, 0.2, 0.7]))
```

### Questions

1. Explain how cumulative sums and binary search enable weighted sampling.
2. Identify an off-by-one or index error that could occur and correct it.
3. Modify `weighted_choice` to return `None` if all weights are zero or negative.

---

## Q73

### yaml_dumper.py

```python
import json

def dump_config_as_yaml(cfg, path):
    """
    Save config (dict) as YAML-like file. If PyYAML available, use it; otherwise write a simple YAML approximation.
    """
    try:
        import yaml
        with open(path, "w", encoding="utf-8") as f:
            yaml.safe_dump(cfg, f)
    except ImportError:
        # fallback: write JSON but with .yaml extension
        with open(path, "w", encoding="utf-8") as f:
            json.dump(cfg, f, indent=2)

if __name__ == "__main__":
    dump_config_as_yaml({"a":1, "b":[1,2,3]}, "out.yaml")
```

### Questions

1. What are pros/cons of the fallback behavior used here?
2. Why might writing JSON to a `.yaml` file be problematic?
3. Modify the fallback to write a simple, human-readable YAML approximation (key: value lines, lists as `- item`).

---

## Q74

### sliding_median.py

```python
import bisect

def sliding_median(seq, k):
    """
    Yield median of each sliding window of size k over seq.
    Uses a sorted list and bisect for insertion/removal.
    """
    if k <= 0:
        raise ValueError("k must be positive")
    window = []
    for i, x in enumerate(seq):
        if i >= k:
            # remove seq[i-k]
            old = seq[i-k]
            idx = bisect.bisect_left(window, old)
            del window[idx]
        bisect.insort(window, x)
        if i >= k - 1:
            mid = k // 2
            if k % 2 == 1:
                yield window[mid]
            else:
                yield (window[mid-1] + window[mid]) / 2.0

if __name__ == "__main__":
    print(list(sliding_median([1,3,2,6,4,5], 3)))
```

### Questions

1. What medians are yielded for the example?
2. Explain time complexity and why more advanced approaches (heaps) are used for large windows.
3. Modify `sliding_median` to support even and odd k consistently when returning numeric types.

---

## Q75

### config_watch.py

```python
import os
import time

def watch_file(path, callback, poll_interval=1.0):
    """
    Poll a file for modification and call callback(path) when it changes.
    """
    last_mtime = None
    if os.path.exists(path):
        last_mtime = os.path.getmtime(path)
    while True:
        try:
            if not os.path.exists(path):
                if last_mtime is not None:
                    last_mtime = None
                    callback(path)
            else:
                m = os.path.getmtime(path)
                if last_mtime is None or m != last_mtime:
                    last_mtime = m
                    callback(path)
        except Exception:
            pass
        time.sleep(poll_interval)

if __name__ == "__main__":
    def cb(p): print("changed:", p)
    # Warning: infinite loop if run directly
    # watch_file("config.yaml", cb)
    print("Example ready")
```

### Questions

1. What are limitations and drawbacks of polling for file changes? Suggest alternatives.
2. Why is the `while True` loop potentially dangerous in scripts, and how would you make it stoppable?
3. Modify `watch_file` to accept a `stop_event` (e.g., `threading.Event`) so the loop can be cleanly terminated.

---

