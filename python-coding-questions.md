/ [Home](index.md)

## Python Coding Questions

**Note:** tbd

tcode: pyq10092


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



## Q76

### json_diff.py

```python
import json

def json_diff(a, b, path=""):
    """
    Return list of differences between two JSON-like dicts as tuples:
    (path, value_in_a, value_in_b)
    """
    diffs = []
    if a == b:
        return diffs
    if isinstance(a, dict) and isinstance(b, dict):
        keys = set(a.keys()) | set(b.keys())
        for k in keys:
            pa = path + "." + str(k) if path else str(k)
            diffs.extend(json_diff(a.get(k), b.get(k), pa))
    else:
        diffs.append((path, a, b))
    return diffs

if __name__ == "__main__":
    x = {"a": 1, "b": {"c": 2}}
    y = {"a": 1, "b": {"c": 3}, "d": 4}
    for d in json_diff(x, y):
        print(d)
```

### Questions

1. What differences are printed for the example `x` and `y`?
2. How does this function handle nested dictionaries and missing keys?
3. Extend `json_diff` to handle lists by comparing by index and include index in the path.

---

## Q77

### mutex_pool.py

```python
import threading
import time

class MutexPool:
    """
    Simple pool that acquires a lock from a pool of locks for a given key.
    Useful to serialize operations per-key.
    """
    def __init__(self):
        self._locks = {}
        self._global_lock = threading.Lock()

    def _get_lock(self, key):
        with self._global_lock:
            if key not in self._locks:
                self._locks[key] = threading.Lock()
            return self._locks[key]

    def run_with_lock(self, key, func, *args, **kwargs):
        lock = self._get_lock(key)
        with lock:
            return func(*args, **kwargs)

if __name__ == "__main__":
    pool = MutexPool()
    def work(x):
        time.sleep(0.01)
        print("done", x)
    pool.run_with_lock("k", work, 1)
```

### Questions

1. Explain how `MutexPool` ensures serial access per key.
2. Are there any memory or cleanup concerns with the `_locks` dict? How would you mitigate them?
3. Modify `MutexPool` to remove locks for keys when no longer used (weak references or reference counting).

---

## Q78

### pretty_print_table.py

```python
def pretty_print_table(rows, headers=None):
    """
    Print rows (list of lists) as a simple aligned table.
    """
    if headers:
        rows = [headers] + rows
    # compute column widths
    cols = max(len(r) for r in rows)
    widths = [0] * cols
    for r in rows:
        for i, v in enumerate(r):
            widths[i] = max(widths[i], len(str(v)))
    # print rows
    for r in rows:
        parts = []
        for i in range(cols):
            val = str(r[i]) if i < len(r) else ""
            parts.append(val.ljust(widths[i]))
        print(" | ".join(parts))

if __name__ == "__main__":
    data = [[1, "Alice", 3.2], [2, "Bob", 4.5]]
    pretty_print_table(data, headers=["id", "name", "score"])
```

### Questions

1. What output is produced for the example `data`? Describe alignment behavior.
2. How does the code handle rows with missing columns?
3. Add an option to right-align numeric columns while left-aligning text columns.

---

## Q79

### csv_chunker.py

```python
import csv

def chunk_csv(input_path, output_prefix, rows_per_file=1000):
    """
    Split a CSV into multiple files with header preserved.
    """
    with open(input_path, "r", newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        header = next(reader)
        file_idx = 0
        rows = []
        for row in reader:
            rows.append(row)
            if len(rows) >= rows_per_file:
                out_name = f"{output_prefix}_{file_idx}.csv"
                with open(out_name, "w", newline="", encoding="utf-8") as out:
                    writer = csv.writer(out)
                    writer.writerow(header)
                    writer.writerows(rows)
                file_idx += 1
                rows = []
        if rows:
            out_name = f"{output_prefix}_{file_idx}.csv"
            with open(out_name, "w", newline="", encoding="utf-8") as out:
                writer = csv.writer(out)
                writer.writerow(header)
                writer.writerows(rows)

if __name__ == "__main__":
    # example usage (file not provided)
    chunk_csv("big.csv", "part", 500)
```

### Questions

1. Why is `newline=""` used when opening CSV files?
2. How does this preserve the CSV header across chunks?
3. Modify `chunk_csv` to optionally gzip each output file (use `gzip.open` when enabled).

---

## Q80

### html_table_parser.py

```python
from html.parser import HTMLParser

class TableParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.in_td = False
        self.current = []
        self.rows = []
        self._text = []

    def handle_starttag(self, tag, attrs):
        if tag.lower() == "td" or tag.lower() == "th":
            self.in_td = True
            self._text = []

    def handle_endtag(self, tag):
        if tag.lower() in ("td", "th"):
            self.in_td = False
            self.current.append("".join(self._text).strip())
        if tag.lower() == "tr":
            if self.current:
                self.rows.append(self.current)
            self.current = []

    def handle_data(self, data):
        if self.in_td:
            self._text.append(data)

def parse_tables(html):
    parser = TableParser()
    parser.feed(html)
    return parser.rows

if __name__ == "__main__":
    html = "<table><tr><td>A</td><td>B</td></tr><tr><td>1</td><td>2</td></tr></table>"
    print(parse_tables(html))
```

### Questions

1. What list of rows is returned for the sample HTML?
2. Identify limitations of this simple parser (e.g., nested tables, attributes).
3. Extend `TableParser` to optionally capture header rows separately and return `(headers, rows)`.

---

## Q81

### secure_filename.py

```python
import os
import re

def secure_filename(fname):
    """
    Return a filesystem-safe filename by removing dangerous characters and normalizing.
    """
    fname = os.path.basename(fname)
    # replace spaces with underscore
    fname = fname.replace(" ", "_")
    # remove .. sequences
    fname = re.sub(r"\.\.+", ".", fname)
    # allow only safe characters
    fname = re.sub(r"[^A-Za-z0-9._-]", "", fname)
    if not fname:
        raise ValueError("invalid filename")
    return fname

if __name__ == "__main__":
    print(secure_filename("../some dir/fi le!!.txt"))
```

### Questions

1. What does `secure_filename` return for the example input?
2. Discuss whether this approach is safe across different filesystems and locales.
3. Modify `secure_filename` to preserve file extension and limit base name length to 255 characters.

---

## Q82

### lockfile_guard.py

```python
import os
import time

class LockFile:
    def __init__(self, path):
        self.path = path
        self.fd = None

    def acquire(self, timeout=5):
        start = time.time()
        while True:
            try:
                self.fd = os.open(self.path, os.O_CREAT | os.O_EXCL | os.O_RDWR)
                return True
            except FileExistsError:
                if time.time() - start > timeout:
                    return False
                time.sleep(0.1)

    def release(self):
        if self.fd:
            os.close(self.fd)
            try:
                os.unlink(self.path)
            except OSError:
                pass
            self.fd = None

if __name__ == "__main__":
    lk = LockFile("my.lock")
    if lk.acquire():
        print("locked")
        lk.release()
```

### Questions

1. Explain how this lockfile mechanism avoids race conditions.
2. What issues arise if a process crashes while holding the lock? Suggest improvements.
3. Modify `LockFile` to write the PID into the lock file when acquired and add a method to stale-check and break locks older than a threshold.

---

## Q83

### xml_to_dict.py

```python
import xml.etree.ElementTree as ET

def xml_to_dict(xml_str):
    root = ET.fromstring(xml_str)
    def node_to_dict(node):
        d = {}
        for k, v in node.attrib.items():
            d["@" + k] = v
        text = (node.text or "").strip()
        if text:
            d["#text"] = text
        for child in node:
            name = child.tag
            val = node_to_dict(child)
            if name in d:
                if isinstance(d[name], list):
                    d[name].append(val)
                else:
                    d[name] = [d[name], val]
            else:
                d[name] = val
        return d
    return {root.tag: node_to_dict(root)}

if __name__ == "__main__":
    xml = "<person id='1'><name>Alice</name><age>30</age></person>"
    print(xml_to_dict(xml))
```

### Questions

1. What dictionary results from the sample XML?
2. How are attributes and text nodes represented in the output?
3. Modify `xml_to_dict` to handle namespaces by stripping them from tag names.

---

## Q84

### top_k_stream.py

```python
import heapq

def top_k_stream(iterable, k):
    """
    Return k largest items from an iterable in ascending order.
    """
    if k <= 0:
        return []
    heap = []
    for x in iterable:
        if len(heap) < k:
            heapq.heappush(heap, x)
        else:
            if x > heap[0]:
                heapq.heapreplace(heap, x)
    return sorted(heap)

if __name__ == "__main__":
    print(top_k_stream(range(100), 5))
```

### Questions

1. What does `top_k_stream(range(100), 5)` return?
2. Explain why a min-heap of size `k` is used here.
3. Modify `top_k_stream` to accept a key function similar to `heapq.nlargest`.

---

## Q85

### sync_dirs.py

```python
import os
import shutil

def sync_dirs(src, dst):
    """
    Simple directory sync: copy files from src to dst, overwriting if newer or missing.
    """
    if not os.path.isdir(src):
        raise ValueError("src must be a directory")
    os.makedirs(dst, exist_ok=True)
    for root, dirs, files in os.walk(src):
        rel = os.path.relpath(root, src)
        target_dir = os.path.join(dst, rel) if rel != "." else dst
        os.makedirs(target_dir, exist_ok=True)
        for f in files:
            s = os.path.join(root, f)
            d = os.path.join(target_dir, f)
            if not os.path.exists(d) or os.path.getmtime(s) > os.path.getmtime(d):
                shutil.copy2(s, d)

if __name__ == "__main__":
    # example usage (directories not provided)
    sync_dirs("src_dir", "dst_dir")
```

### Questions

1. What behavior does `sync_dirs` implement regarding file modification times?
2. Identify potential pitfalls (symlinks, permissions, deletions) and how to address them.
3. Add an option to delete files in `dst` that are no longer present in `src` (mirror mode).

---

## Q86

### pretty_json.py

```python
import json

def pretty_json(obj, indent=2, sort_keys=True):
    return json.dumps(obj, indent=indent, sort_keys=sort_keys, ensure_ascii=False)

if __name__ == "__main__":
    data = {"b": 1, "a": [3, 2, 1]}
    print(pretty_json(data))
```

### Questions

1. What string is printed for the example `data`?
2. Explain the effect of `ensure_ascii=False`. When is that useful?
3. Modify `pretty_json` to stream a large list to a file in pretty JSON format without building the entire string in memory.

---

## Q87

### encode_decode_base64.py

```python
import base64

def encode_file_to_base64(path):
    with open(path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode("ascii")

def decode_base64_to_file(b64, path):
    data = base64.b64decode(b64.encode("ascii"))
    with open(path, "wb") as f:
        f.write(data)

if __name__ == "__main__":
    # not run here, example only
    b = encode_file_to_base64("image.png")
    decode_base64_to_file(b, "copy.png")
```

### Questions

1. Why are files opened in binary mode for base64 encode/decode?
2. What are memory implications for large files? Suggest an alternative streaming approach.
3. Implement chunked encode/decode functions that operate on file-like objects without loading entire files.

---

## Q88

### rolling_hash.py

```python
def rolling_hash(s, k, base=256, mod=2**32):
    """
    Compute rolling hash for all substrings of length k in s.
    Returns list of hash values in order.
    """
    n = len(s)
    if k <= 0 or k > n:
        return []
    h = 0
    power = 1
    for i in range(k):
        h = (h * base + ord(s[i])) % mod
        if i < k - 1:
            power = (power * base) % mod
    out = [h]
    for i in range(k, n):
        h = (h - ord(s[i-k]) * power) % mod
        h = (h * base + ord(s[i])) % mod
        out.append(h)
    return out

if __name__ == "__main__":
    print(rolling_hash("abcdefg", 3))
```

### Questions

1. What does `rolling_hash("abcdefg", 3)` return conceptually?
2. Explain the role of `power` in the rolling hash update step.
3. Modify the function to return (hash, substring) pairs and handle Unicode characters robustly.

---

## Q89

### file_signature.py

```python
import hashlib

def file_sha256(path, block_size=65536):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for block in iter(lambda: f.read(block_size), b""):
            h.update(block)
    return h.hexdigest()

if __name__ == "__main__":
    # example usage (file not provided)
    print(file_sha256("somefile.bin"))
```

### Questions

1. Why is the file read in blocks instead of all at once?
2. What guarantees does SHA-256 provide for file integrity?
3. Add an option to compute and return both MD5 and SHA-256 in one pass.

---

## Q90

### retry_async.py

```python
import asyncio
import random

async def unreliable_async():
    if random.random() < 0.6:
        raise RuntimeError("fail")
    return "ok"

async def retry_async(func, attempts=3, delay=0.5):
    last = None
    for i in range(attempts):
        try:
            return await func()
        except Exception as e:
            last = e
            if i < attempts - 1:
                await asyncio.sleep(delay)
    raise last

if __name__ == "__main__":
    async def main():
        print(await retry_async(unreliable_async, attempts=5, delay=0.1))
    asyncio.run(main())
```

### Questions

1. How does `retry_async` differ from a synchronous retry implementation regarding sleeping?
2. Why must `retry_async` `await` the function call? What happens if you pass a coroutine object instead of a callable?
3. Modify `retry_async` to accept either a coroutine function or a callable returning a coroutine, and accept an `on_retry` callback.

---

## Q91

### obfuscate_email.py

```python
def obfuscate_email(email):
    """
    Simple obfuscation: keep first char of local part and domain and replace inner chars with '*'
    """
    local, at, domain = email.partition("@")
    if not at:
        raise ValueError("invalid email")
    d_parts = domain.split(".", 1)
    d0 = d_parts[0]
    domain_rest = "." + d_parts[1] if len(d_parts) > 1 else ""
    def mask(s):
        if len(s) <= 2:
            return s[0] + "*" * (len(s)-1)
        return s[0] + "*" * (len(s)-2) + s[-1]
    return mask(local) + "@" + mask(d0) + domain_rest

if __name__ == "__main__":
    print(obfuscate_email("alice@example.com"))
```

### Questions

1. What is the obfuscated result for `alice@example.com`?
2. Are there corner cases where this breaks (short local parts, missing domain)? Give examples.
3. Modify `obfuscate_email` to preserve the overall length and replace with visually distinct characters while keeping first and last characters.

---

## Q92

### cache_bust_url.py

```python
import urllib.parse
import time

def cache_bust(url, t=None):
    """
    Append or update a `_cb` query parameter with current timestamp to bust caches.
    """
    if t is None:
        t = int(time.time())
    p = urllib.parse.urlparse(url)
    q = dict(urllib.parse.parse_qsl(p.query))
    q["_cb"] = str(t)
    new_q = urllib.parse.urlencode(q)
    return urllib.parse.urlunparse((p.scheme, p.netloc, p.path, p.params, new_q, p.fragment))

if __name__ == "__main__":
    print(cache_bust("https://example.com/api?v=1"))
```

### Questions

1. What query string results from the example call?
2. How does this function behave if `_cb` already exists?
3. Modify `cache_bust` to accept a `granularity` parameter (e.g., seconds, minutes) and round the timestamp accordingly.

---

## Q93

### sliding_sum.py

```python
def sliding_sum(seq, k):
    """
    Yield sum of each sliding window of size k.
    """
    n = len(seq)
    if k <= 0 or k > n:
        return
    s = sum(seq[:k])
    yield s
    for i in range(k, n):
        s += seq[i] - seq[i-k]
        yield s

if __name__ == "__main__":
    print(list(sliding_sum([1,2,3,4,5], 3)))
```

### Questions

1. What values are yielded for the example?
2. Explain how constant-time update is achieved for each window.
3. Modify `sliding_sum` to accept an iterator (not just a sequence) and operate with O(k) memory.

---

## Q94

### weighted_median.py

```python
def weighted_median(items, weights):
    """
    items: list of numbers
    weights: same-length list of positive weights
    Returns the weighted median value.
    """
    pairs = sorted(zip(items, weights), key=lambda x: x[0])
    total = sum(weights)
    cum = 0
    for v, w in pairs:
        cum += w
        if cum >= total / 2:
            return v
    return pairs[-1][0] if pairs else None

if __name__ == "__main__":
    print(weighted_median([1,2,3,4], [1,1,1,1]))
```

### Questions

1. What is the weighted median for the example equal weights?
2. Explain behavior when weights sum to an odd or even total and when cumulative equals exactly half.
3. Modify `weighted_median` to return an interpolated value when cumulative weight equals exactly half (average of current and next item).

---

## Q95

### parse_query_string.py

```python
import urllib.parse

def parse_qs(qs):
    """
    Return dict mapping keys to list of values from a query string (without leading '?').
    """
    pairs = urllib.parse.parse_qsl(qs, keep_blank_values=True)
    out = {}
    for k, v in pairs:
        out.setdefault(k, []).append(v)
    return out

if __name__ == "__main__":
    print(parse_qs("a=1&a=2&b="))
```

### Questions

1. What is the returned dict for the example query string?
2. Why might `keep_blank_values=True` be useful?
3. Modify `parse_qs` to also decode plus signs and percent-escapes properly (show usage of `urllib.parse` utilities).

---

## Q96

### sample_without_replacement.py

```python
import random

def sample_without_replacement(iterable, k):
    """
    Reservoir sampling: return k items from iterable without replacement.
    """
    it = iter(iterable)
    reservoir = []
    for i, x in enumerate(it):
        if i < k:
            reservoir.append(x)
        else:
            j = random.randrange(i + 1)
            if j < k:
                reservoir[j] = x
    return reservoir

if __name__ == "__main__":
    print(sample_without_replacement(range(100), 5))
```

### Questions

1. Explain why this reservoir algorithm produces an unbiased sample.
2. What happens if `k` is greater than the population size? How would you handle it?
3. Modify the function to raise `ValueError` when `k` is negative and to return a shuffled copy when `k >= population size` but population length is known.

---

## Q97

### safe_eval.py

```python
import ast

def safe_eval(expr, allowed_names=None):
    """
    Evaluate simple arithmetic expressions using AST to avoid eval().
    allowed_names: dict of allowed names (e.g., math functions)
    """
    if allowed_names is None:
        allowed_names = {}
    node = ast.parse(expr, mode="eval")
    def _eval(n):
        if isinstance(n, ast.Expression):
            return _eval(n.body)
        if isinstance(n, ast.Num):
            return n.n
        if isinstance(n, ast.BinOp):
            left = _eval(n.left); right = _eval(n.right)
            if isinstance(n.op, ast.Add): return left + right
            if isinstance(n.op, ast.Sub): return left - right
            if isinstance(n.op, ast.Mult): return left * right
            if isinstance(n.op, ast.Div): return left / right
            if isinstance(n.op, ast.Pow): return left ** right
        if isinstance(n, ast.UnaryOp) and isinstance(n.op, ast.USub):
            return -_eval(n.operand)
        if isinstance(n, ast.Name):
            if n.id in allowed_names:
                return allowed_names[n.id]
        raise ValueError("unsupported expression")
    return _eval(node)

if __name__ == "__main__":
    print(safe_eval("2 + 3 * 4"))
```

### Questions

1. What does `safe_eval("2 + 3 * 4")` return?
2. Identify expression types that are intentionally disallowed and why.
3. Extend `safe_eval` to allow calling simple math functions (e.g., `sin`, `cos`) passed via `allowed_names`.

---

## Q98

### http_retry_decorator.py

```python
import time
import functools

def http_retry(attempts=3, delay=0.5, exceptions=(Exception,)):
    def deco(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            last = None
            for i in range(attempts):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    last = e
                    if i < attempts - 1:
                        time.sleep(delay * (2 ** i))
            raise last
        return wrapper
    return deco

if __name__ == "__main__":
    @http_retry(attempts=4, delay=0.1, exceptions=(RuntimeError,))
    def flaky():
        import random
        if random.random() < 0.8:
            raise RuntimeError("fail")
        return "ok"
    print(flaky())
```

### Questions

1. How does the decorator implement exponential backoff?
2. Why might catching `Exception` by default be unsafe? How is that addressed here?
3. Modify the decorator to accept an optional `on_retry` callback that is invoked with `(attempt, exception)`.

---

## Q99

### json_schema_check.py

```python
def check_schema(obj, schema):
    """
    Simple schema checker: schema is dict mapping key->type (or nested dict).
    Returns True if obj conforms, else False.
    """
    if not isinstance(obj, dict) or not isinstance(schema, dict):
        return False
    for k, t in schema.items():
        if k not in obj:
            return False
        val = obj[k]
        if isinstance(t, dict):
            if not isinstance(val, dict):
                return False
            if not check_schema(val, t):
                return False
        else:
            if not isinstance(val, t):
                return False
    return True

if __name__ == "__main__":
    s = {"name": str, "age": int, "meta": {"id": int}}
    print(check_schema({"name":"A","age":30,"meta":{"id":1}}, s))
```

### Questions

1. What does the example check return and why?
2. What are limitations of this simple type-based schema approach?
3. Improve `check_schema` to accept optional keys (e.g., by marking schema types as `(type, True)` for optional) and return meaningful error messages.

---

## Q100

### batch_http_get.py

```python
import concurrent.futures
import urllib.request

def fetch(url, timeout=5):
    req = urllib.request.Request(url, headers={"User-Agent": "batch-client"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.getcode(), r.read()[:200]

def batch_fetch(urls, max_workers=5):
    results = {}
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as ex:
        future_to_url = {ex.submit(fetch, u): u for u in urls}
        for fut in concurrent.futures.as_completed(future_to_url):
            url = future_to_url[fut]
            try:
                code, data = fut.result()
                results[url] = (code, len(data))
            except Exception as e:
                results[url] = ("err", str(e))
    return results

if __name__ == "__main__":
    urls = ["https://example.com", "https://httpbin.org/status/404"]
    print(batch_fetch(urls, max_workers=3))
```

### Questions

1. What keys and value types are present in the returned `results` dict?
2. Why use a thread pool for IO-bound HTTP requests instead of a process pool?
3. Modify `batch_fetch` to add timeouts per request and overall cancellation if the total time exceeds a given budget.





## Q101

### flatten_tuple.py

```python
def flatten_tuple(t):
    """
    Flatten a nested tuple structure into a flat list.
    """
    out = []
    for item in t:
        if isinstance(item, tuple):
            out.extend(flatten_tuple(item))
        else:
            out.append(item)
    return out

if __name__ == "__main__":
    data = (1, (2, 3), (4, (5, 6)))
    print(flatten_tuple(data))
```

### Questions

1. What is the output for the sample `data`?
2. Explain recursion depth concerns for very deep nesting.
3. Modify to handle lists inside tuples as well.

---

## Q102

### parse_iso8601.py

```python
from datetime import datetime

def parse_iso8601(s):
    """
    Parse a limited set of ISO-8601 datetime strings like 2025-01-02T15:04:05
    """
    try:
        return datetime.strptime(s, "%Y-%m-%dT%H:%M:%S")
    except ValueError:
        return None

if __name__ == "__main__":
    print(parse_iso8601("2025-07-01T12:30:45"))
    print(parse_iso8601("2025-07-01"))
```

### Questions

1. What does the function return for the two examples?
2. Why might full ISO-8601 parsing need a library?
3. Extend the function to accept optional fractional seconds (e.g., `.123`) when present.

---

## Q103

### char_histogram.py

```python
def char_hist(s):
    """
    Return dict mapping characters to counts.
    """
    d = {}
    for ch in s:
        d[ch] = d.get(ch, 0) + 1
    return d

if __name__ == "__main__":
    print(char_hist("banana"))
```

### Questions

1. What dictionary is printed for `"banana"`?
2. How would you ignore whitespace and case?
3. Rewrite using `collections.Counter`.

---

## Q104

### pluralize.py

```python
def pluralize(word, n):
    """
    Very small pluralizer: naive rules for English (not comprehensive).
    """
    if n == 1:
        return word
    if word.endswith("y") and word[-2] not in "aeiou":
        return word[:-1] + "ies"
    if word.endswith("s") or word.endswith("x") or word.endswith("z") or word.endswith("ch") or word.endswith("sh"):
        return word + "es"
    return word + "s"

if __name__ == "__main__":
    for w in ["box","baby","cat"]:
        print(w, pluralize(w, 2))
```

### Questions

1. What are the outputs for the sample words?
2. Identify words this simplistic approach fails on.
3. Improve function to handle a small exceptions dictionary (e.g., "mouse" -> "mice").

---

## Q105

### sum_digits.py

```python
def sum_digits(n):
    """
    Sum decimal digits of integer n (handles negative).
    """
    s = str(abs(n))
    total = 0
    for ch in s:
        total += ord(ch) - ord('0')
    return total

if __name__ == "__main__":
    print(sum_digits(12345))
    print(sum_digits(-907))
```

### Questions

1. What are printed results for the examples?
2. Could this fail for non-integer input? How to validate?
3. Rewrite using arithmetic (no string conversions).

---

## Q106

### longest_common_prefix.py

```python
def longest_common_prefix(strs):
    if not strs:
        return ""
    prefix = strs[0]
    for s in strs[1:]:
        while not s.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix

if __name__ == "__main__":
    print(longest_common_prefix(["flower", "flow", "flight"]))
```

### Questions

1. What prefix is returned for the example list?
2. Explain complexity in worst case.
3. Modify to use binary search on prefix length for efficiency.

---

## Q107

### pairwise_diff.py

```python
def pairwise_diff(a, b):
    """
    Return list of (i, a[i], b[i]) where elements differ; stops at min length.
    """
    res = []
    n = min(len(a), len(b))
    for i in range(n):
        if a[i] != b[i]:
            res.append((i, a[i], b[i]))
    return res

if __name__ == "__main__":
    print(pairwise_diff([1,2,3], [1,4,3,5]))
```

### Questions

1. What is the output for the sample lists?
2. How would you report extra trailing elements when lengths differ?
3. Modify to optionally compare up to the longer length and use `None` for missing values.

---

## Q108

### safe_int.py

```python
def safe_int(s, default=0):
    try:
        return int(s)
    except (ValueError, TypeError):
        return default

if __name__ == "__main__":
    print(safe_int("10"))
    print(safe_int("x", default=-1))
```

### Questions

1. What do the two example calls return?
2. Why catch `TypeError` in addition to `ValueError`?
3. Extend to accept a `base` parameter (e.g., base=16) and validate inputs.

---

## Q109

### heads_or_tails.py

```python
import random

def flip_n(n):
    """
    Return tuple (heads, tails) counts after n fair flips.
    """
    heads = tails = 0
    for _ in range(n):
        if random.random() < 0.5:
            heads += 1
        else:
            tails += 1
    return heads, tails

if __name__ == "__main__":
    print(flip_n(10))
```

### Questions

1. What is the expected statistical behavior as `n` grows?
2. How to seed the RNG for reproducible tests?
3. Change to use `random.choice([0,1])` and measure performance difference.

---

## Q110

### grep_simple.py

```python
def grep_simple(path, pattern):
    """
    Print lines containing pattern (simple substring search).
    """
    with open(path, "r", encoding="utf-8") as f:
        for i, line in enumerate(f, 1):
            if pattern in line:
                print(f"{i}:{line.rstrip()}")

if __name__ == "__main__":
    # usage example: file must exist
    # grep_simple("sample.txt", "error")
    pass
```

### Questions

1. Why is `enumerate(..., 1)` used?
2. How would you make this case-insensitive?
3. Replace substring search with regex matching and add an option to invert match.

---

## Q111

### int_to_roman.py

```python
def int_to_roman(num):
    vals = [
        (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
        (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
        (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
    ]
    res = []
    for v, sym in vals:
        while num >= v:
            num -= v
            res.append(sym)
    return "".join(res)

if __name__ == "__main__":
    print(int_to_roman(1994))
```

### Questions

1. What Roman numeral does `1994` map to?
2. What input validation might be needed?
3. Implement `roman_to_int` to convert back and validate round-trip.

---

## Q112

### sliding_max.py

```python
from collections import deque

def sliding_max(seq, k):
    if k <= 0:
        raise ValueError("k must be positive")
    dq = deque()
    res = []
    for i, x in enumerate(seq):
        while dq and dq[0] <= i - k:
            dq.popleft()
        while dq and seq[dq[-1]] < x:
            dq.pop()
        dq.append(i)
        if i >= k - 1:
            res.append(seq[dq[0]])
    return res

if __name__ == "__main__":
    print(sliding_max([1,3,-1,-3,5,3,6,7], 3))
```

### Questions

1. What are the sliding maximums for the example?
2. Why store indices in deque rather than values?
3. Modify to handle streaming iterables (yield results).

---

## Q113

### group_by_key.py

```python
from collections import defaultdict

def group_by(items, keyfunc):
    out = defaultdict(list)
    for it in items:
        out[keyfunc(it)].append(it)
    return dict(out)

if __name__ == "__main__":
    people = [{"name":"A","age":20},{"name":"B","age":30},{"name":"C","age":20}]
    print(group_by(people, lambda p: p["age"]))
```

### Questions

1. What grouping does the example produce?
2. Explain why `defaultdict` is convenient here.
3. Modify to accept an optional `valuefunc` to transform stored values.

---

## Q114

### file_tail.py

```python
from collections import deque

def tail(path, n=10):
    with open(path, "r", encoding="utf-8") as f:
        dq = deque(f, maxlen=n)
    return [line.rstrip("\n") for line in dq]

if __name__ == "__main__":
    # tail("large.txt", 5)
    pass
```

### Questions

1. How does `deque` with `maxlen` implement tail efficiently?
2. What happens when file has fewer than `n` lines?
3. Modify to stream lines and yield as they are added (follow/tail -f behavior).

---

## Q115

### histogram_bins.py

```python
def histogram_bins(values, bins):
    """
    Simple histogram: bins is list of bin edges (ascending),
    returns list of counts of length len(bins)-1.
    """
    counts = [0] * (len(bins) - 1)
    for v in values:
        for i in range(len(bins)-1):
            if bins[i] <= v < bins[i+1]:
                counts[i] += 1
                break
    return counts

if __name__ == "__main__":
    print(histogram_bins([1,2,3,4,5], [0,2,4,6]))
```

### Questions

1. What counts are produced for the example?
2. How are values equal to the last edge handled?
3. Optimize using `bisect` for large numbers of bins.

---

## Q116

### almost_equal.py

```python
def almost_equal(a, b, rel_tol=1e-9, abs_tol=0.0):
    return abs(a - b) <= max(rel_tol * max(abs(a), abs(b)), abs_tol)

if __name__ == "__main__":
    print(almost_equal(0.1 + 0.2, 0.3, rel_tol=1e-9))
```

### Questions

1. Why is direct equality unreliable for floats?
2. Explain the meaning of `rel_tol` and `abs_tol`.
3. Provide examples where only `abs_tol` is appropriate.

---

## Q117

### find_anagrams.py

```python
from collections import defaultdict

def group_anagrams(words):
    out = defaultdict(list)
    for w in words:
        key = "".join(sorted(w))
        out[key].append(w)
    return list(out.values())

if __name__ == "__main__":
    print(group_anagrams(["eat","tea","tan","ate","nat","bat"]))
```

### Questions

1. What groups are returned for the sample list?
2. Explain performance considerations for long words.
3. Modify to ignore case and non-letter characters.

---

## Q118

### ping_pong_server.py

```python
import socket

def start_echo_server(host="127.0.0.1", port=9000):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen(1)
    conn, addr = s.accept()
    with conn:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)
    s.close()

if __name__ == "__main__":
    # start_echo_server()  # network code; run manually
    pass
```

### Questions

1. Describe what this server does on a single connection.
2. What security and robustness issues exist (e.g., blocking accept)?
3. Modify to handle multiple clients using `threading.Thread`.

---

## Q119

### chunked_combine.py

```python
def combine_chunks(chunks):
    """
    Given iterable of iterables, flatten one level and return list.
    """
    out = []
    for chunk in chunks:
        for item in chunk:
            out.append(item)
    return out

if __name__ == "__main__":
    print(combine_chunks([[1,2],[3,4],[5]]))
```

### Questions

1. What does the function return for the example?
2. How to implement using `itertools.chain.from_iterable`?
3. Modify to accept generators without exhausting memory (return generator).

---

## Q120

### decode_utf8_safe.py

```python
def read_utf8(path):
    with open(path, "rb") as f:
        data = f.read()
    return data.decode("utf-8", errors="replace")

if __name__ == "__main__":
    # read_utf8("somefile.txt")
    pass
```

### Questions

1. What does `errors="replace"` do on decode errors?
2. Why might you prefer `errors="strict"` in some contexts?
3. Change to stream-read and decode incrementally to handle huge files.

---

## Q121

### localized_format.py

```python
import locale

def format_currency(value, loc="en_US.UTF-8"):
    try:
        locale.setlocale(locale.LC_ALL, loc)
    except locale.Error:
        return str(value)
    return locale.currency(value, grouping=True)

if __name__ == "__main__":
    print(format_currency(12345.67))
```

### Questions

1. Why can `setlocale` raise `locale.Error`?
2. What are portability concerns when using locale names?
3. Modify to not change global locale permanently (use context manager or save/restore).

---

## Q122

### find_cycle_in_list.py

```python
class Node:
    def __init__(self, val, nxt=None):
        self.val = val
        self.next = nxt

def has_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True
    return False

if __name__ == "__main__":
    a = Node(1); b = Node(2); c = Node(3)
    a.next = b; b.next = c; c.next = b
    print(has_cycle(a))
```

### Questions

1. What does the example print and why?
2. Explain Floyd’s cycle-finding algorithm intuition.
3. Modify to return the node where cycle begins.

---

## Q123

### replace_multiple.py

```python
def replace_multiple(s, replacements):
    """
    replacements: dict old->new, apply sequentially using str.replace
    """
    out = s
    for old, new in replacements.items():
        out = out.replace(old, new)
    return out

if __name__ == "__main__":
    print(replace_multiple("abc abc", {"ab":"x", "x":"y"}))
```

### Questions

1. What is the result for the example and why might order matter?
2. How to perform simultaneous non-overlapping replacements safely?
3. Implement with regex that replaces whole-word keys only.

---

## Q124

### unique_id_generator.py

```python
import threading
import time

class IDGen:
    def __init__(self):
        self.lock = threading.Lock()
        self.counter = 0

    def next_id(self):
        with self.lock:
            self.counter += 1
            return f"{int(time.time())}-{self.counter}"

if __name__ == "__main__":
    g = IDGen()
    print(g.next_id())
    print(g.next_id())
```

### Questions

1. Why is locking needed here?
2. What happens if system time changes backwards?
3. Modify to use an epoch-based monotonic counter to avoid collisions.

---

## Q125

### text_wrap.py

```python
def wrap_text(s, width):
    words = s.split()
    lines = []
    cur = []
    curlen = 0
    for w in words:
        if curlen + len(w) + (1 if cur else 0) > width:
            lines.append(" ".join(cur))
            cur = [w]; curlen = len(w)
        else:
            cur.append(w); curlen += (len(w) + (1 if cur and len(cur)>1 else 0))
    if cur:
        lines.append(" ".join(cur))
    return lines

if __name__ == "__main__":
    print(wrap_text("This is a simple wrap example for testing", 10))
```

### Questions

1. What issues exist in the way `curlen` is updated?
2. How does `textwrap.wrap` from stdlib solve this?
3. Fix the bug and handle words longer than `width`.

---

## Q126

### luhn_check.py

```python
def luhn_checksum(card_number):
    digits = [int(d) for d in str(card_number)][::-1]
    total = 0
    for i, d in enumerate(digits):
        if i % 2 == 1:
            d *= 2
            if d > 9:
                d -= 9
        total += d
    return total % 10 == 0

if __name__ == "__main__":
    print(luhn_checksum("4532015112830366"))  # valid Visa example
```

### Questions

1. What does the function validate and what does it return for the example?
2. Why reverse the digits for processing?
3. Add a function to compute the check digit for a partial number.

---

## Q127

### safe_json_loads.py

```python
import json

def safe_json_loads(s):
    try:
        return json.loads(s)
    except json.JSONDecodeError as e:
        return {"_error": str(e)}

if __name__ == "__main__":
    print(safe_json_loads('{"a":1}'))
    print(safe_json_loads('{"a":1'))
```

### Questions

1. What does the function return on invalid JSON?
2. Why might swallowing errors be problematic?
3. Modify to optionally raise the original exception when `raise_on_error=True`.

---

## Q128

### find_missing_number.py

```python
def find_missing(nums):
    """
    Given nums containing unique numbers from 0..n with one missing, find missing.
    """
    n = len(nums)
    total = n * (n + 1) // 2
    return total - sum(nums)

if __name__ == "__main__":
    print(find_missing([3,0,1]))  # missing 2
```

### Questions

1. Why does this formula work?
2. What assumptions must hold about `nums`?
3. Modify to work when numbers are not zero-based but given a min/max.

---

## Q129

### dns_lookup.py

```python
import socket

def resolve(host):
    try:
        return socket.gethostbyname(host)
    except socket.gaierror:
        return None

if __name__ == "__main__":
    print(resolve("localhost"))
    print(resolve("nonexistent.example.invalid"))
```

### Questions

1. What does `gethostbyname` return for `localhost`?
2. How to get all addresses (IPv4/IPv6) for a host?
3. Modify to perform an asynchronous lookup using threads.

---

## Q130

### concat_files.py

```python
def concat_files(paths, out):
    with open(out, "w", encoding="utf-8") as outf:
        for p in paths:
            with open(p, "r", encoding="utf-8") as inf:
                for line in inf:
                    outf.write(line)

if __name__ == "__main__":
    # concat_files(["a.txt","b.txt"], "combined.txt")
    pass
```

### Questions

1. What happens if one input file doesn't exist?
2. How to make this atomic (avoid partial writes)?
3. Modify to support binary files and preserve mode per file.

---

## Q131

### topological_detect_cycle.py

```python
def detect_cycle(edges):
    from collections import defaultdict
    g = defaultdict(list)
    nodes = set()
    for u, v in edges:
        g[u].append(v)
        nodes.add(u); nodes.add(v)
    visited = set()
    stack = set()
    def dfs(u):
        visited.add(u)
        stack.add(u)
        for v in g[u]:
            if v not in visited:
                if dfs(v):
                    return True
            elif v in stack:
                return True
        stack.remove(u)
        return False
    for n in nodes:
        if n not in visited:
            if dfs(n):
                return True
    return False

if __name__ == "__main__":
    print(detect_cycle([("a","b"),("b","c"),("c","a")]))
```

### Questions

1. What does the example print and why?
2. Explain role of `stack` in cycle detection.
3. Modify to return one cycle path when found.

---

## Q132

### url_join.py

```python
from urllib.parse import urljoin

def join_paths(base, *parts):
    url = base
    for p in parts:
        url = urljoin(url.rstrip("/") + "/", p)
    return url

if __name__ == "__main__":
    print(join_paths("https://api.example.com/v1", "users", "123"))
```

### Questions

1. How does `urljoin` handle leading slashes in parts?
2. Why use `rstrip("/") + "/"` in the loop?
3. Modify to preserve query strings if present in final part.

---

## Q133

### max_subarray.py

```python
def max_subarray(nums):
    max_ending = max_so_far = nums[0]
    for x in nums[1:]:
        max_ending = max(x, max_ending + x)
        max_so_far = max(max_so_far, max_ending)
    return max_so_far

if __name__ == "__main__":
    print(max_subarray([-2,1,-3,4,-1,2,1,-5,4]))
```

### Questions

1. What is the maximum subarray sum for the example?
2. Explain Kadane’s algorithm intuition.
3. Modify to return the start and end indices as well.

---

## Q134

### parse_ini.py

```python
def parse_ini(path):
    cfg = {}
    section = None
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith(";") or line.startswith("#"):
                continue
            if line.startswith("[") and line.endswith("]"):
                section = line[1:-1].strip()
                cfg[section] = {}
            elif "=" in line and section is not None:
                k, v = line.split("=", 1)
                cfg[section][k.strip()] = v.strip()
    return cfg

if __name__ == "__main__":
    # parse_ini("config.ini")
    pass
```

### Questions

1. How are comments and sections handled?
2. What happens if `key=value` occurs before any section?
3. Modify to support a global (no-section) area and type conversion for integers/floats.

---

## Q135

### compare_versions.py

```python
def compare_versions(a, b):
    """
    return -1 if a<b, 0 if equal, 1 if a>b for dot-separated numeric versions
    """
    pa = [int(x) for x in a.split(".")]
    pb = [int(x) for x in b.split(".")]
    n = max(len(pa), len(pb))
    for i in range(n):
        va = pa[i] if i < len(pa) else 0
        vb = pb[i] if i < len(pb) else 0
        if va < vb:
            return -1
        if va > vb:
            return 1
    return 0

if __name__ == "__main__":
    print(compare_versions("1.2.3", "1.2"))
```

### Questions

1. What does the example return and why?
2. How to handle pre-release tags like `1.2.3-alpha`?
3. Modify to accept non-numeric parts by comparing alphabetically when numeric parts equal.

---

## Q136

### flatten_dict_values.py

```python
def flatten_values(d):
    """
    Replace any list value with its flattened single-level concatenation of strings.
    """
    out = {}
    for k, v in d.items():
        if isinstance(v, list):
            out[k] = "".join(str(x) for x in v)
        else:
            out[k] = v
    return out

if __name__ == "__main__":
    print(flatten_values({"a":[1,2],"b":"x"}))
```

### Questions

1. What output does the example print?
2. Why might joining list items be lossy?
3. Modify to recursively flatten nested lists and preserve types if requested.

---

## Q137

### find_pairs_sum_k.py

```python
def find_pairs(nums, k):
    seen = set()
    res = set()
    for x in nums:
        if k - x in seen:
            res.add(tuple(sorted((x, k-x))))
        seen.add(x)
    return [list(p) for p in res]

if __name__ == "__main__":
    print(find_pairs([1,2,3,2,4], 4))
```

### Questions

1. What pairs are returned for the example?
2. Why use sorted tuple in `res`?
3. Modify to return indices instead of values.

---

## Q138

### ensure_dir.py

```python
import os

def ensure_dir(path):
    if not os.path.exists(path):
        os.makedirs(path, exist_ok=True)
    elif not os.path.isdir(path):
        raise ValueError(f"{path} exists and is not a directory")

if __name__ == "__main__":
    ensure_dir("tmp/example")
```

### Questions

1. What does `ensure_dir` do if path already exists as file?
2. Why use `exist_ok=True`?
3. Modify to create parent dirs with specific permissions using `os.chmod`.

---

## Q139

### gcd_lcm.py

```python
def gcd(a, b):
    while b:
        a, b = b, a % b
    return abs(a)

def lcm(a, b):
    if a == 0 or b == 0:
        return 0
    return abs(a // gcd(a, b) * b)

if __name__ == "__main__":
    print(gcd(48,18))
    print(lcm(12,15))
```

### Questions

1. What are gcd(48,18) and lcm(12,15)?
2. Why use `abs` and check for zero in lcm?
3. Extend to compute gcd/lcm for a list of numbers.

---

## Q140

### flatten_generator.py

```python
def flatten_generator(nested):
    for item in nested:
        if hasattr(item, "__iter__") and not isinstance(item, (str, bytes)):
            for x in flatten_generator(item):
                yield x
        else:
            yield item

if __name__ == "__main__":
    print(list(flatten_generator([1, [2, (3,4)], "x"])))
```

### Questions

1. What is yielded for the sample input, and why treat strings specially?
2. What issues might arise with infinite iterables?
3. Modify to accept a `max_depth` parameter to limit recursion.

---

## Q141

### time_window_aggregation.py

```python
from collections import deque
import time

class TimeWindow:
    def __init__(self, window_seconds):
        self.window = window_seconds
        self.events = deque()

    def add(self, value):
        self.events.append((time.time(), value))
        self._evict()

    def _evict(self):
        now = time.time()
        while self.events and now - self.events[0][0] > self.window:
            self.events.popleft()

    def sum(self):
        self._evict()
        return sum(v for _, v in self.events)

if __name__ == "__main__":
    tw = TimeWindow(2.0)
    tw.add(1); tw.add(2)
    time.sleep(1); tw.add(3)
    print(tw.sum())
```

### Questions

1. What does `sum()` compute for recent events?
2. Explain why `_evict` is necessary on both add and sum.
3. Modify to return average and count as well.

---

## Q142

### dict_keypath_get.py

```python
def get_path(d, path, sep="."):
    keys = path.split(sep) if path else []
    cur = d
    for k in keys:
        if not isinstance(cur, dict) or k not in cur:
            return None
        cur = cur[k]
    return cur

if __name__ == "__main__":
    cfg = {"a":{"b":{"c":1}}}
    print(get_path(cfg, "a.b.c"))
    print(get_path(cfg, "a.x.c"))
```

### Questions

1. What do the two example calls return?
2. How to modify to raise a `KeyError` instead of returning `None`?
3. Add support to set a value at a key path (creating intermediate dicts).

---

## Q143

### split_on_delimiter.py

```python
def split_once(s, delim):
    idx = s.find(delim)
    if idx == -1:
        return s, ""
    return s[:idx], s[idx+len(delim):]

if __name__ == "__main__":
    print(split_once("a=b=c", "="))
```

### Questions

1. What does the example return?
2. How to make `split_once` split from the right (last occurrence)?
3. Modify to return a tuple with both parts trimmed.

---

## Q144

### flatten_json_keys.py

```python
def flatten_keys(d, parent="", sep="."):
    out = {}
    for k, v in d.items():
        key = parent + sep + k if parent else k
        if isinstance(v, dict):
            out.update(flatten_keys(v, key, sep=sep))
        else:
            out[key] = v
    return out

if __name__ == "__main__":
    print(flatten_keys({"a":{"b":1},"c":2}))
```

### Questions

1. What output does the example produce?
2. How to handle lists by including indices in keys?
3. Modify to optionally ignore `None` values.

---

## Q145

### is_palindrome.py

```python
def is_palindrome(s):
    cleaned = "".join(ch.lower() for ch in s if ch.isalnum())
    return cleaned == cleaned[::-1]

if __name__ == "__main__":
    print(is_palindrome("A man, a plan, a canal: Panama"))
```

### Questions

1. What does the example return and why?
2. Why use `isalnum()`?
3. Modify to check palindrome for linked lists of characters (no string conversion).

---

## Q146

### clamp_values.py

```python
def clamp_list(nums, low, high):
    return [low if x < low else high if x > high else x for x in nums]

if __name__ == "__main__":
    print(clamp_list([1,-2,5,10], 0, 6))
```

### Questions

1. What list does the example produce?
2. How to implement in-place modification?
3. Modify to accept a per-element clamp function instead of scalar bounds.

---

## Q147

### relative_path.py

```python
import os

def relative_path(from_path, to_path):
    return os.path.relpath(to_path, start=os.path.dirname(from_path))

if __name__ == "__main__":
    print(relative_path("/a/b/c/file.txt", "/a/d/x.txt"))
```

### Questions

1. What relative path is produced for the example?
2. How does behavior differ on Windows with drive letters?
3. Modify to return an absolute path if drives differ on Windows.

---

## Q148

### monotone_stack.py

```python
def next_greater_elements(nums):
    """
    Return list of next greater element for each index, -1 if none.
    """
    res = [-1]*len(nums)
    stack = []
    for i, x in enumerate(nums):
        while stack and nums[stack[-1]] < x:
            idx = stack.pop()
            res[idx] = x
        stack.append(i)
    return res

if __name__ == "__main__":
    print(next_greater_elements([2,1,2,4,3]))
```

### Questions

1. What is the output for the example input?
2. Explain why a monotone decreasing stack is used.
3. Modify to handle circular arrays (wrap-around).

---

## Q149

### jinstrument.py

```python
import time

def instrument(func):
    def wrapper(*args, **kwargs):
        t0 = time.perf_counter()
        res = func(*args, **kwargs)
        t1 = time.perf_counter()
        print(f"{func.__name__} took {t1 - t0:.6f}s")
        return res
    return wrapper

@instrument
def compute(n):
    s = 0
    for i in range(n):
        s += i*i
    return s

if __name__ == "__main__":
    compute(100000)
```

### Questions

1. What does the decorator print when `compute` runs?
2. Why use `time.perf_counter()` for timing?
3. Modify decorator to be usable with optional parameters (e.g., `@instrument(enabled=False)`).

---

## Q150

### group_adjacent_by.py

```python
def group_adjacent(seq, keyfunc=lambda x:x):
    """
    Group adjacent equal keys into lists.
    """
    out = []
    cur_key = None
    cur_list = []
    for x in seq:
        k = keyfunc(x)
        if cur_list and k != cur_key:
            out.append(cur_list)
            cur_list = []
        cur_list.append(x)
        cur_key = k
    if cur_list:
        out.append(cur_list)
    return out

if __name__ == "__main__":
    print(group_adjacent([1,1,2,2,2,3,1,1]))
```

### Questions

1. What grouping is produced for the example?
2. How does this differ from grouping all equal values regardless of adjacency?
3. Modify to return `(key, group)` pairs instead of lists.







## Q151

### merge_intervals.py

```python
def merge_intervals(intervals):
    """
    Merge overlapping intervals. Intervals are list of (start, end).
    """
    if not intervals:
        return []
    intervals = sorted(intervals, key=lambda x: x[0])
    out = []
    cur_start, cur_end = intervals[0]
    for s, e in intervals[1:]:
        if s <= cur_end:
            cur_end = max(cur_end, e)
        else:
            out.append((cur_start, cur_end))
            cur_start, cur_end = s, e
    out.append((cur_start, cur_end))
    return out

if __name__ == "__main__":
    print(merge_intervals([(1,3),(2,6),(8,10),(15,18)]))
```

### Questions

1. What merged intervals are produced for the example?
2. Explain why sorting by start is necessary.
3. Modify to merge intervals in-place if the input is large and memory is constrained.

---

## Q152

### random_walk.py

```python
import random

def random_walk(steps):
    """
    Simulate 1D random walk starting at 0 for given number of steps.
    Return list of positions including origin.
    """
    pos = 0
    path = [pos]
    for _ in range(steps):
        step = 1 if random.random() < 0.5 else -1
        pos += step
        path.append(pos)
    return path

if __name__ == "__main__":
    print(random_walk(10))
```

### Questions

1. What is the length of the returned path for `steps=10`?
2. How would you compute mean squared displacement from many trials?
3. Modify to allow biased probability `p` for stepping +1.

---

## Q153

### binary_search.py

```python
def binary_search(a, target):
    lo, hi = 0, len(a) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if a[mid] == target:
            return mid
        if a[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1

if __name__ == "__main__":
    print(binary_search([1,3,5,7,9], 5))
```

### Questions

1. What index is returned for target 5?
2. What precondition must `a` satisfy?
3. Modify to return the insertion index when target is not present.

---

## Q154

### chunked_map.py

```python
def chunked_map(func, iterable, chunk_size=10):
    it = iter(iterable)
    out = []
    while True:
        chunk = []
        try:
            for _ in range(chunk_size):
                chunk.append(next(it))
        except StopIteration:
            pass
        if not chunk:
            break
        out.append([func(x) for x in chunk])
    return out

if __name__ == "__main__":
    print(chunked_map(lambda x: x*x, range(1,21), 7))
```

### Questions

1. How many sublists are returned for range 1..20 with chunk size 7?
2. Explain the StopIteration handling pattern here.
3. Rewrite to yield mapped chunks lazily as a generator.

---

## Q155

### median_stream.py

```python
import heapq

class RunningMedian:
    def __init__(self):
        self.lo = []  # max-heap via negation
        self.hi = []  # min-heap

    def add(self, x):
        if not self.lo or x <= -self.lo[0]:
            heapq.heappush(self.lo, -x)
        else:
            heapq.heappush(self.hi, x)
        # rebalance
        if len(self.lo) > len(self.hi) + 1:
            heapq.heappush(self.hi, -heapq.heappop(self.lo))
        elif len(self.hi) > len(self.lo):
            heapq.heappush(self.lo, -heapq.heappop(self.hi))

    def median(self):
        if not self.lo:
            return None
        if len(self.lo) > len(self.hi):
            return -self.lo[0]
        return (-self.lo[0] + self.hi[0]) / 2.0

if __name__ == "__main__":
    rm = RunningMedian()
    for x in [5,2,3,4,1,6]:
        rm.add(x)
        print("median now:", rm.median())
```

### Questions

1. How does this class maintain the running median?
2. What is output sequence of medians for the sample list?
3. Modify `median` to return integer median when all inputs are ints and an integer median exists.

---

## Q156

### file_diff_lines.py

```python
def diff_lines(a_path, b_path):
    with open(a_path, "r", encoding="utf-8") as fa, open(b_path, "r", encoding="utf-8") as fb:
        a_lines = fa.readlines()
        b_lines = fb.readlines()
    diffs = []
    n = max(len(a_lines), len(b_lines))
    for i in range(n):
        a = a_lines[i].rstrip("\n") if i < len(a_lines) else None
        b = b_lines[i].rstrip("\n") if i < len(b_lines) else None
        if a != b:
            diffs.append((i+1, a, b))
    return diffs

if __name__ == "__main__":
    # example: files not provided
    print(diff_lines("a.txt", "b.txt"))
```

### Questions

1. What does each tuple in `diffs` represent?
2. How are differing lengths handled?
3. Modify to run as a unified diff (context lines) instead of line-by-line tuples.

---

## Q157

### find_cycle_graph.py

```python
from collections import defaultdict

def find_cycle(edges):
    g = defaultdict(list)
    nodes = set()
    for u, v in edges:
        g[u].append(v)
        nodes.add(u); nodes.add(v)

    visited = set()
    stack = []

    def dfs(u):
        visited.add(u)
        stack.append(u)
        for v in g[u]:
            if v not in visited:
                res = dfs(v)
                if res:
                    return res
            elif v in stack:
                # cycle found: return cycle path
                return stack[stack.index(v):] + [v]
        stack.pop()
        return None

    for n in nodes:
        if n not in visited:
            cyc = dfs(n)
            if cyc:
                return cyc
    return None

if __name__ == "__main__":
    print(find_cycle([("a","b"),("b","c"),("c","a")]))
```

### Questions

1. What does the function return for the sample cycle?
2. Explain how the cycle path is reconstructed.
3. Modify to return all cycles up to a given length.

---

## Q158

### sum_matrix.py

```python
def sum_matrix(mat):
    total = 0
    for row in mat:
        for v in row:
            total += v
    return total

if __name__ == "__main__":
    print(sum_matrix([[1,2,3],[4,5,6]]))
```

### Questions

1. What sum does the example return?
2. How would you handle non-rectangular matrices?
3. Modify to accept an iterator of rows (not necessarily list) and compute sum lazily.

---

## Q159

### batch_scheduler.py

```python
import time
import heapq

class Scheduler:
    def __init__(self):
        self.pq = []  # (run_at, func, args, kwargs)

    def schedule(self, delay, func, *args, **kwargs):
        run_at = time.time() + delay
        heapq.heappush(self.pq, (run_at, func, args, kwargs))

    def run_pending(self):
        now = time.time()
        while self.pq and self.pq[0][0] <= now:
            _, func, args, kwargs = heapq.heappop(self.pq)
            try:
                func(*args, **kwargs)
            except Exception:
                pass

if __name__ == "__main__":
    s = Scheduler()
    s.schedule(0.1, print, "hello")
    time.sleep(0.2)
    s.run_pending()
```

### Questions

1. How does `schedule` and `run_pending` coordinate timed execution?
2. What happens if a scheduled function raises an exception?
3. Add a `cancel(func)` method to remove scheduled entries for a given function.

---

## Q160

### count_subarrays_with_sum.py

```python
def count_subarrays_with_sum(nums, target):
    """
    Count contiguous subarrays summing to target using prefix-sum hashmap.
    """
    seen = {0:1}
    s = 0
    count = 0
    for x in nums:
        s += x
        count += seen.get(s - target, 0)
        seen[s] = seen.get(s, 0) + 1
    return count

if __name__ == "__main__":
    print(count_subarrays_with_sum([1,1,1], 2))
```

### Questions

1. What is the returned value for the example?
2. Explain why prefix-sum counts provide O(n) time.
3. Modify to return the actual subarray index ranges instead of count.

---

## Q161

### levenshtein.py

```python
def levenshtein(a, b):
    """
    Compute Levenshtein distance (edit distance) between strings a and b.
    """
    n, m = len(a), len(b)
    if n == 0:
        return m
    if m == 0:
        return n
    prev = list(range(m+1))
    for i in range(1, n+1):
        cur = [i] + [0]*m
        for j in range(1, m+1):
            cost = 0 if a[i-1] == b[j-1] else 1
            cur[j] = min(prev[j] + 1, cur[j-1] + 1, prev[j-1] + cost)
        prev = cur
    return prev[m]

if __name__ == "__main__":
    print(levenshtein("kitten", "sitting"))
```

### Questions

1. What distance does the example compute?
2. Explain memory optimization used (only two rows).
3. Modify to also return the alignment/edits sequence.

---

## Q162

### find_local_extrema.py

```python
def local_extrema(nums):
    """
    Return list of (index, value, type) where type is 'min' or 'max' for strict local extrema.
    """
    out = []
    n = len(nums)
    for i in range(1, n-1):
        if nums[i] > nums[i-1] and nums[i] > nums[i+1]:
            out.append((i, nums[i], 'max'))
        if nums[i] < nums[i-1] and nums[i] < nums[i+1]:
            out.append((i, nums[i], 'min'))
    return out

if __name__ == "__main__":
    print(local_extrema([1,3,2,4,3,5]))
```

### Questions

1. What extrema are identified in the example?
2. How to handle plateaus (equal neighbors)?
3. Modify to optionally include endpoints as extrema based on neighbor.

---

## Q163

### mean_median_mode.py

```python
from collections import Counter
import statistics

def mean_median_mode(nums):
    mean = sum(nums)/len(nums)
    median = statistics.median(nums)
    cnt = Counter(nums)
    mode = cnt.most_common(1)[0][0]
    return mean, median, mode

if __name__ == "__main__":
    print(mean_median_mode([1,2,2,3,4]))
```

### Questions

1. What triple is returned for the example?
2. What if multiple modes exist? How does `most_common` behave?
3. Modify to return all modes in case of ties.

---

## Q164

### find_duplicates_in_file.py

```python
def find_duplicates(path):
    seen = set()
    dups = set()
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.rstrip("\n")
            if line in seen:
                dups.add(line)
            else:
                seen.add(line)
    return sorted(dups)

if __name__ == "__main__":
    # file not provided; example only
    print(find_duplicates("lines.txt"))
```

### Questions

1. What does the function return?
2. How does memory scale with unique lines?
3. Modify to stream and write duplicates to an output file instead of returning list.

---

## Q165

### lru_cache_simple.py

```python
from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key):
        if key not in self.cache:
            return None
        val = self.cache.pop(key)
        self.cache[key] = val
        return val

    def put(self, key, value):
        if key in self.cache:
            self.cache.pop(key)
        elif len(self.cache) >= self.capacity:
            self.cache.popitem(last=False)
        self.cache[key] = value

if __name__ == "__main__":
    c = LRUCache(2)
    c.put(1,1); c.put(2,2)
    print(c.get(1))
    c.put(3,3)
    print(c.get(2))
```

### Questions

1. What outputs are printed by the example?
2. Explain why `OrderedDict` is useful for LRU.
3. Add a `delete(key)` method and thread-safety using a lock.

---

## Q166

### split_sentences.py

```python
import re

def split_sentences(text):
    """
    Naive sentence splitter splitting on .!? followed by space and capital letter.
    """
    parts = re.split(r'([.!?])\s+(?=[A-Z])', text)
    out = []
    for i in range(0, len(parts)-1, 2):
        out.append(parts[i] + parts[i+1])
    if len(parts) % 2 == 1:
        out.append(parts[-1])
    return [s.strip() for s in out if s.strip()]

if __name__ == "__main__":
    print(split_sentences("Hello world. This is a test! Is it ok? yes."))
```

### Questions

1. What sentences are produced by the example?
2. Why is this approach brittle for abbreviations?
3. Modify to use `nltk.sent_tokenize` if available, with fallback to the naive splitter.

---

## Q167

### rotate_matrix.py

```python
def rotate_matrix_90(mat):
    """
    Rotate square matrix 90 degrees clockwise in-place.
    """
    n = len(mat)
    for layer in range(n//2):
        first = layer
        last = n - layer - 1
        for i in range(first, last):
            offset = i - first
            top = mat[first][i]
            # left -> top
            mat[first][i] = mat[last - offset][first]
            # bottom -> left
            mat[last - offset][first] = mat[last][last - offset]
            # right -> bottom
            mat[last][last - offset] = mat[i][last]
            # top -> right
            mat[i][last] = top
    return mat

if __name__ == "__main__":
    M = [[1,2,3],[4,5,6],[7,8,9]]
    print(rotate_matrix_90(M))
```

### Questions

1. What does the rotated matrix look like?
2. Why must matrix be square for this in-place method?
3. Modify to return a rotated copy and support rectangular matrices.

---

## Q168

### cluster_points_kmeans.py

```python
import random
import math

def kmeans(points, k, iterations=10):
    centroids = random.sample(points, k)
    for _ in range(iterations):
        clusters = [[] for _ in range(k)]
        for p in points:
            dists = [math.dist(p, c) for c in centroids]
            idx = dists.index(min(dists))
            clusters[idx].append(p)
        for i in range(k):
            if clusters[i]:
                xs = [p[0] for p in clusters[i]]
                ys = [p[1] for p in clusters[i]]
                centroids[i] = (sum(xs)/len(xs), sum(ys)/len(ys))
    return centroids, clusters

if __name__ == "__main__":
    pts = [(random.random(), random.random()) for _ in range(50)]
    print(kmeans(pts, 3))
```

### Questions

1. What do `centroids` and `clusters` represent?
2. Why is k-means sensitive to initial centroids?
3. Modify to allow `max_restarts` and pick the best clustering by inertia.

---

## Q169

### longest_increasing_subseq.py

```python
import bisect

def lis_length(seq):
    tails = []
    for x in seq:
        i = bisect.bisect_left(tails, x)
        if i == len(tails):
            tails.append(x)
        else:
            tails[i] = x
    return len(tails)

if __name__ == "__main__":
    print(lis_length([10,9,2,5,3,7,101,18]))
```

### Questions

1. What length does the example return?
2. Explain why `tails` does not store an actual subsequence but helps compute length.
3. Modify to reconstruct one actual increasing subsequence (not just length).

---

## Q170

### windowed_average.py

```python
from collections import deque

def windowed_average(seq, k):
    if k <= 0:
        raise ValueError("k positive")
    dq = deque()
    s = 0
    for i, x in enumerate(seq):
        dq.append(x); s += x
        if i >= k:
            s -= dq.popleft()
        if i >= k-1:
            yield s / k

if __name__ == "__main__":
    print(list(windowed_average([1,2,3,4,5], 3)))
```

### Questions

1. What averages are yielded for the example?
2. How does deque help keep O(1) per-step updates?
3. Modify to support variable window sizes per position.

---

## Q171

### snake_case_to_camel.py

```python
def snake_to_camel(s):
    parts = s.split("_")
    return parts[0] + "".join(p.capitalize() for p in parts[1:])

if __name__ == "__main__":
    print(snake_to_camel("this_is_a_test"))
```

### Questions

1. What does the function return for the example?
2. How to handle leading/trailing underscores or multiple underscores?
3. Modify to convert to `PascalCase` optionally.

---

## Q172

### dir_tree_size.py

```python
import os

def dir_size(path):
    total = 0
    for root, dirs, files in os.walk(path):
        for f in files:
            try:
                total += os.path.getsize(os.path.join(root, f))
            except OSError:
                pass
    return total

if __name__ == "__main__":
    # example directory not provided
    print(dir_size("."))
```

### Questions

1. How does this compute directory size?
2. Why catch `OSError` for each file?
3. Modify to skip certain file extensions and optionally follow symlinks.

---

## Q173

### json_path_get.py

```python
import json

def json_get(obj, path):
    """
    Path like 'a.b[2].c' supports dict keys and list indices.
    """
    cur = obj
    for token in path.replace("]", "").split("."):
        if "[" in token:
            key, idx = token.split("[")
            cur = cur[key]
            cur = cur[int(idx)]
        else:
            cur = cur[token]
    return cur

if __name__ == "__main__":
    data = {"a":{"b":[{"c":1},{"c":2}]}}
    print(json_get(data, "a.b[1].c"))
```

### Questions

1. What value is returned by the example?
2. What exceptions can occur for invalid paths?
3. Modify to return a default value instead of raising when path missing.

---

## Q174

### balanced_partition.py

```python
def can_partition(nums):
    total = sum(nums)
    if total % 2 != 0:
        return False
    target = total // 2
    dp = {0}
    for x in nums:
        new = set()
        for s in dp:
            if s + x == target:
                return True
            if s + x < target:
                new.add(s + x)
        dp |= new
    return target in dp

if __name__ == "__main__":
    print(can_partition([1,5,11,5]))
```

### Questions

1. What is returned for the example and why?
2. Explain time complexity and DP state size.
3. Modify to actually return the two partitions if possible.

---

## Q175

### count_inversions.py

```python
def count_inversions(arr):
    """
    Count number of inversions using merge-sort style approach.
    """
    def merge_count(a):
        n = len(a)
        if n <= 1:
            return a, 0
        m = n//2
        left, lc = merge_count(a[:m])
        right, rc = merge_count(a[m:])
        merged = []
        i = j = 0
        inv = lc + rc
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i]); i += 1
            else:
                merged.append(right[j]); j += 1
                inv += len(left) - i
        merged.extend(left[i:]); merged.extend(right[j:])
        return merged, inv
    _, cnt = merge_count(arr)
    return cnt

if __name__ == "__main__":
    print(count_inversions([2,4,1,3,5]))
```

### Questions

1. What inversion count does the example produce?
2. Why is merge-based method O(n log n)?
3. Modify to return the sorted array as well as inversion count.

---

## Q176

### detect_language_simple.py

```python
from collections import Counter
import re

def detect_language(text):
    """
    Very naive language detector using frequency of stopwords for a few languages.
    """
    tokens = re.findall(r"[a-zA-Z]+", text.lower())
    freq = Counter(tokens)
    english = sum(freq[w] for w in ("the","and","is","in","it"))
    french = sum(freq[w] for w in ("le","et","est","dans","il"))
    if english > french:
        return "en"
    if french > english:
        return "fr"
    return "unknown"

if __name__ == "__main__":
    print(detect_language("This is an example in English."))
```

### Questions

1. What language does the example return?
2. Explain why this approach is unreliable.
3. Modify to accept language profiles and compute cosine similarity.

---

## Q177

### sparse_matrix_dot.py

```python
def sparse_dot(A, B):
    """
    A and B are dicts mapping (i,j) -> value. Return dict of product.
    Naive multiplication: for each (i,k) in A and (k,j) in B accumulate.
    """
    res = {}
    B_by_row = {}
    for (k, j), v in B.items():
        B_by_row.setdefault(k, []).append((j, v))
    for (i, k), va in A.items():
        for j, vb in B_by_row.get(k, []):
            res[(i, j)] = res.get((i, j), 0) + va * vb
    return res

if __name__ == "__main__":
    A = {(0,0):1, (1,0):2}
    B = {(0,1):3}
    print(sparse_dot(A,B))
```

### Questions

1. What product dictionary is returned for the sample A and B?
2. Explain why grouping B by row improves efficiency.
3. Modify to accept and return CSR (compressed sparse row) representation.

---

## Q178

### random_subset.py

```python
import random

def random_subset(seq, p):
    """
    Return subset of seq including each element with probability p independently.
    """
    out = []
    for x in seq:
        if random.random() < p:
            out.append(x)
    return out

if __name__ == "__main__":
    print(random_subset(range(10), 0.3))
```

### Questions

1. What is expected length of returned subset in expectation?
2. How to make sampling reproducible?
3. Modify to use numpy for vectorized performance on large arrays.

---

## Q179

### flatten_html_text.py

```python
from html.parser import HTMLParser
import html

class SimpleText(HTMLParser):
    def __init__(self):
        super().__init__()
        self.parts = []

    def handle_data(self, data):
        self.parts.append(data)

def html_to_text(html_str):
    p = SimpleText()
    p.feed(html_str)
    return html.unescape(" ".join(part.strip() for part in p.parts if part.strip()))

if __name__ == "__main__":
    print(html_to_text("<p>Hello &amp; welcome</p>"))
```

### Questions

1. What is the output for the example?
2. Why use `html.unescape`?
3. Modify to collapse multiple whitespace and preserve paragraph breaks as `\n\n`.

---

## Q180

### topological_group.py

```python
from collections import defaultdict, deque

def group_tasks(edges):
    """
    Given dependency edges u->v, return list of task groups that can run in parallel (levels).
    """
    g = defaultdict(list)
    indeg = defaultdict(int)
    nodes = set()
    for u, v in edges:
        g[u].append(v)
        indeg[v] += 1
        nodes.add(u); nodes.add(v)
        indeg.setdefault(u, indeg.get(u,0))
    q = deque([n for n in nodes if indeg[n] == 0])
    groups = []
    while q:
        level_size = len(q)
        level = []
        for _ in range(level_size):
            x = q.popleft()
            level.append(x)
            for nb in g[x]:
                indeg[nb] -= 1
                if indeg[nb] == 0:
                    q.append(nb)
        groups.append(level)
    if sum(len(g) for g in groups) != len(nodes):
        raise ValueError("cycle")
    return groups

if __name__ == "__main__":
    print(group_tasks([("a","b"),("a","c"),("b","d"),("c","d")]))
```

### Questions

1. What groups are produced for the example?
2. Explain how this produces levelized parallel batches.
3. Modify to include nodes with zero degree provided in an optional `nodes` parameter.

---

## Q181

### remove_kth_from_end.py

```python
class ListNode:
    def __init__(self, val=0, nxt=None):
        self.val = val; self.next = nxt

def remove_kth_from_end(head, k):
    dummy = ListNode(0, head)
    slow = fast = dummy
    for _ in range(k):
        if not fast.next:
            return head  # k too large
        fast = fast.next
    while fast.next:
        slow = slow.next
        fast = fast.next
    # remove slow.next
    slow.next = slow.next.next
    return dummy.next

if __name__ == "__main__":
    # example building list omitted
    pass
```

### Questions

1. Explain two-pointer technique used here.
2. What happens if `k` equals list length?
3. Modify to return the removed node's value as well.

---

## Q182

### sparse_lu_solve.py

```python
def forward_sub(L, b):
    n = len(b)
    y = [0]*n
    for i in range(n):
        s = b[i]
        for j, v in L.get(i, []):
            if j < i:
                s -= v * y[j]
        y[i] = s
    return y

def backward_sub(U, y):
    n = len(y)
    x = [0]*n
    for i in range(n-1, -1, -1):
        s = y[i]
        for j, v in U.get(i, []):
            if j > i:
                s -= v * x[j]
        diag = dict(U.get(i, [])).get(i, None)
        if diag is None:
            raise ValueError("missing diagonal")
        x[i] = s / diag
    return x

if __name__ == "__main__":
    # sparse L and U omitted for brevity
    pass
```

### Questions

1. What do forward and backward substitution compute?
2. Why must U have diagonal entries?
3. Modify to accept CSR-like structures for efficiency.

---

## Q183

### unique_prefixes.py

```python
def shortest_unique_prefixes(words):
    """
    For each word, find the shortest prefix distinguishing it from others.
    """
    prefixes = {}
    for i, w in enumerate(words):
        for L in range(1, len(w)+1):
            p = w[:L]
            if sum(1 for x in words if x.startswith(p)) == 1:
                prefixes[w] = p
                break
        else:
            prefixes[w] = w
    return prefixes

if __name__ == "__main__":
    print(shortest_unique_prefixes(["dog","cat","car","cart"]))
```

### Questions

1. What prefixes are returned for the example set?
2. Explain why this naive approach is O(n^2 * m).
3. Modify to build a trie to compute prefixes in O(total chars) time.

---

## Q184

### find_missing_ranges.py

```python
def missing_ranges(nums, lo, hi):
    """
    Given sorted unique nums, return ranges missing in [lo,hi].
    """
    out = []
    prev = lo - 1
    nums = [n for n in nums if lo <= n <= hi]
    for n in nums:
        if n - prev > 1:
            start = prev + 1
            end = n - 1
            out.append((start, end))
        prev = n
    if hi - prev >= 1:
        out.append((prev+1, hi))
    return out

if __name__ == "__main__":
    print(missing_ranges([0,1,3,50,75], 0, 99))
```

### Questions

1. What missing ranges are returned for the example?
2. Why filter nums into [lo,hi]?
3. Modify to format single-number ranges as "x" and multi-number as "x->y" strings.

---

## Q185

### text_stats.py

```python
import re

def text_stats(text):
    words = re.findall(r"\b\w+\b", text)
    num_words = len(words)
    num_chars = len(text)
    avg_word_len = sum(len(w) for w in words)/num_words if num_words else 0
    return {"words": num_words, "chars": num_chars, "avg_word_len": avg_word_len}

if __name__ == "__main__":
    print(text_stats("Hello world!"))
```

### Questions

1. What stats are produced for "Hello world!"?
2. Why use regex `\b\w+\b` instead of `split()`?
3. Modify to also return top 5 most frequent words.

---

## Q186

### find_closest_pair.py

```python
import math

def closest_pair(points):
    """
    Naive O(n^2) closest-pair computation returning distance and pair.
    """
    best = float("inf")
    pair = None
    n = len(points)
    for i in range(n):
        for j in range(i+1, n):
            d = math.dist(points[i], points[j])
            if d < best:
                best = d
                pair = (points[i], points[j])
    return best, pair

if __name__ == "__main__":
    pts = [(0,0),(1,1),(2,2),(0,1)]
    print(closest_pair(pts))
```

### Questions

1. What closest pair is found for the sample points?
2. Explain why O(n log n) divide-and-conquer algorithms are used for large n.
3. Modify to return indices instead of point coordinates.

---

## Q187

### redact_sensitive.py

```python
import re

def redact(text, patterns):
    """
    Replace occurrences of patterns (regex strings) with [REDACTED].
    """
    out = text
    for p in patterns:
        out = re.sub(p, "[REDACTED]", out)
    return out

if __name__ == "__main__":
    print(redact("My card 4111-1111-1111-1111", [r"\b\d{4}(?:-\d{4}){3}\b"]))
```

### Questions

1. How does the example redact the card number?
2. Why must regex be carefully chosen to avoid false positives?
3. Modify to preserve last 4 digits and replace preceding digits with `*`.

---

## Q188

### sliding_window_maximum_generator.py

```python
from collections import deque

def sliding_max_gen(seq, k):
    dq = deque()
    for i, x in enumerate(seq):
        while dq and dq[0] <= i - k:
            dq.popleft()
        while dq and seq[dq[-1]] < x:
            dq.pop()
        dq.append(i)
        if i >= k - 1:
            yield seq[dq[0]]

if __name__ == "__main__":
    print(list(sliding_max_gen([1,3,-1,-3,5,3,6,7], 3)))
```

### Questions

1. What are the yielded maximums for the example?
2. Why is this approach O(n)?
3. Modify to return tuples `(window_start, max_value)`.

---

## Q189

### paginate_list.py

```python
def paginate(items, page_size):
    """
    Yield pages (sublists) of size page_size.
    """
    it = iter(items)
    while True:
        page = []
        try:
            for _ in range(page_size):
                page.append(next(it))
        except StopIteration:
            pass
        if not page:
            break
        yield page

if __name__ == "__main__":
    for p in paginate(range(1,13), 5):
        print(p)
```

### Questions

1. What pages are printed for range 1..12 with page_size 5?
2. How to support a `page_number` parameter to directly fetch a page?
3. Modify to return an iterator object with `.next_page()` and `.has_next()` methods.

---

## Q190

### approximate_percentile.py

```python
import random
import math

def approximate_percentile(seq, q, sample_frac=0.1):
    """
    Approximate q-th percentile by sampling a fraction of seq.
    """
    if not 0 <= q <= 1:
        raise ValueError("q between 0 and 1")
    n = len(seq)
    if n == 0:
        return None
    sample = random.sample(seq, max(1, int(n * sample_frac)))
    sample.sort()
    idx = int(q * (len(sample)-1))
    return sample[idx]

if __name__ == "__main__":
    print(approximate_percentile(list(range(1000)), 0.95, 0.05))
```

### Questions

1. What does this function approximate and what are limitations?
2. Explain trade-offs of sample_frac choice.
3. Modify to use reservoir sampling when seq is an iterator.

---

## Q191

### serialize_tree.py

```python
class Node:
    def __init__(self, val, children=None):
        self.val = val
        self.children = children or []

def serialize(root):
    """
    Preorder serialize with brackets: val [ child1 child2 ... ]
    """
    if root is None:
        return ""
    parts = [str(root.val)]
    if root.children:
        parts.append("[")
        for c in root.children:
            parts.append(serialize(c))
        parts.append("]")
    return " ".join(p for p in parts if p)

if __name__ == "__main__":
    t = Node(1, [Node(2), Node(3, [Node(4)])])
    print(serialize(t))
```

### Questions

1. What string is produced for the sample tree?
2. How to implement `deserialize` corresponding to this format?
3. Modify to produce and consume JSON for portability.

---

## Q192

### bracket_sequence_count.py

```python
def count_valid_sequences(n):
    """
    Count number of valid parentheses sequences of length 2n (Catalan number).
    """
    from math import comb
    return comb(2*n, n) // (n+1)

if __name__ == "__main__":
    print(count_valid_sequences(3))
```

### Questions

1. What is returned for n=3?
2. Explain combinatorial derivation for Catalan numbers.
3. Modify to generate all valid sequences rather than count.

---

## Q193

### multi_key_sort.py

```python
def multi_sort(items, keys):
    """
    Sort items (dicts) by sequence of keys (key, reverse=False) tuples.
    """
    for key, rev in reversed(keys):
        items.sort(key=lambda x: x.get(key, None), reverse=rev)
    return items

if __name__ == "__main__":
    data = [{"a":2,"b":1},{"a":1,"b":5},{"a":2,"b":0}]
    print(multi_sort(data, [("a", False), ("b", True)]))
```

### Questions

1. What sorted order results from the example?
2. Explain why keys are applied in reversed order.
3. Modify to accept key functions instead of key names.

---

## Q194

### nearest_neighbors_bruteforce.py

```python
import math

def k_nearest(points, query, k):
    dists = [(math.dist(p, query), i, p) for i, p in enumerate(points)]
    dists.sort()
    return [p for _, _, p in dists[:k]]

if __name__ == "__main__":
    pts = [(0,0),(1,1),(2,2),(5,5)]
    print(k_nearest(pts, (1.5,1.5), 2))
```

### Questions

1. What two nearest points are returned for the example?
2. When does brute-force become impractical?
3. Modify to use KD-tree (scipy.spatial.KDTree or a simple implementation) for faster queries.

---

## Q195

### safe_open.py

```python
import os

def safe_open(path, mode="r", max_size=None):
    if "w" in mode and os.path.exists(path) and os.path.getsize(path) > (max_size or 0):
        raise ValueError("file too large to overwrite")
    return open(path, mode, encoding="utf-8" if "b" not in mode else None)

if __name__ == "__main__":
    # example only
    pass
```

### Questions

1. What safety check does this provide before opening for write?
2. Why is encoding chosen conditionally?
3. Modify to create parent directories if missing when writing.

---

## Q196

### find_subsequence.py

```python
def is_subsequence(s, t):
    """
    Return True if s is a subsequence of t (characters in order, not necessarily contiguous).
    """
    it = iter(t)
    return all(c in it for c in s)

if __name__ == "__main__":
    print(is_subsequence("ace", "abcde"))
```

### Questions

1. What does the example return and why?
2. Explain why `all(c in it for c in s)` works for subsequence check.
3. Modify to return indices in `t` where subsequence characters were matched.

---

## Q197

### url_normalize.py

```python
from urllib.parse import urlparse, urlunparse

def normalize_url(url):
    p = urlparse(url)
    scheme = p.scheme.lower() or "http"
    netloc = p.netloc.lower().rstrip("/")
    path = p.path or "/"
    return urlunparse((scheme, netloc, path, "", "", ""))

if __name__ == "__main__":
    print(normalize_url("HTTP://Example.COM/Path/"))
```

### Questions

1. What normalized URL is returned for the example?
2. What parts are intentionally dropped? Why?
3. Modify to preserve query string sorted by parameter name.

---

## Q198

### replace_in_file.py

```python
def replace_in_file(path, old, new, inplace=True):
    with open(path, "r", encoding="utf-8") as f:
        data = f.read()
    data2 = data.replace(old, new)
    if inplace:
        with open(path, "w", encoding="utf-8") as f:
            f.write(data2)
    return data2

if __name__ == "__main__":
    # example usage omitted
    pass
```

### Questions

1. What are risks of doing inplace replace (partial write)?
2. How to make operation atomic (avoid data loss on crash)?
3. Modify to write to a temporary file and rename atomically.

---

## Q199

### rank_transform.py

```python
def rank_transform(arr):
    """
    Replace each value by its rank (starting at 1) among unique sorted values.
    """
    uniq = sorted(set(arr))
    ranks = {v: i+1 for i, v in enumerate(uniq)}
    return [ranks[v] for v in arr]

if __name__ == "__main__":
    print(rank_transform([40,10,20,40]))
```

### Questions

1. What transformed array does the example produce?
2. Explain how ties are handled.
3. Modify to use 0-based ranks and to handle streaming input.

---

## Q200

### sliding_window_find_sum.py

```python
def find_window_with_sum(nums, k, target):
    """
    Return starting index of a window of size k whose sum equals target, or -1.
    """
    n = len(nums)
    if k > n:
        return -1
    s = sum(nums[:k])
    if s == target:
        return 0
    for i in range(k, n):
        s += nums[i] - nums[i-k]
        if s == target:
            return i - k + 1
    return -1

if __name__ == "__main__":
    print(find_window_with_sum([1,2,3,4,5], 3, 9))
```

### Questions

1. What index is returned for the example and why?
2. Explain why sliding sum update is O(1) per step.
3. Modify to return all starting indices matching the target instead of first match.






## Q201

### prime_factors.py

```python
def prime_factors(n):
    """
    Return prime factors of n as a list (with multiplicity).
    """
    i = 2
    out = []
    while i * i <= n:
        while n % i == 0:
            out.append(i)
            n //= i
        i += 1 if i == 2 else 2
    if n > 1:
        out.append(n)
    return out

if __name__ == "__main__":
    print(prime_factors(360))
```

### Questions

1. What list is printed for 360?
2. Explain why the loop increments differently after 2.
3. Modify to return factors as `(prime, exponent)` pairs.

---

## Q202

### dict_deep_update.py

```python
def deep_update(a, b):
    """
    Update dict a with dict b recursively (mutates a).
    """
    for k, v in b.items():
        if k in a and isinstance(a[k], dict) and isinstance(v, dict):
            deep_update(a[k], v)
        else:
            a[k] = v
    return a

if __name__ == "__main__":
    a = {"x":1, "y":{"z":2}}
    b = {"y":{"z":3, "w":4}, "k":5}
    print(deep_update(a, b))
```

### Questions

1. What is printed after update?
2. Does `deep_update` mutate `a` or return a new dict? Explain.
3. Modify to optionally produce a new merged dict without mutating inputs.

---

## Q203

### list_rotate_inplace.py

```python
def rotate_inplace(a, k):
    n = len(a)
    if n == 0:
        return a
    k %= n
    # reverse helper
    def rev(l, i, j):
        while i < j:
            l[i], l[j] = l[j], l[i]
            i += 1; j -= 1
    rev(a, 0, n-1)
    rev(a, 0, k-1)
    rev(a, k, n-1)
    return a

if __name__ == "__main__":
    arr = [1,2,3,4,5]
    print(rotate_inplace(arr, 2))
```

### Questions

1. What transformed list is printed?
2. Explain why three reversals achieve rotation.
3. Modify to rotate left by `k` instead of right.

---

## Q204

### file_extension_stats.py

```python
import os
from collections import Counter

def extension_stats(root):
    cnt = Counter()
    for dirpath, _, files in os.walk(root):
        for f in files:
            ext = os.path.splitext(f)[1].lower()
            cnt[ext] += 1
    return cnt

if __name__ == "__main__":
    print(extension_stats("."))
```

### Questions

1. What does the returned Counter represent?
2. How are files without an extension counted?
3. Modify to also report total size per extension.

---

## Q205

### debounce.py

```python
import time
import threading

def debounce(wait):
    def deco(fn):
        timer = None
        lock = threading.Lock()
        def wrapper(*args, **kwargs):
            nonlocal timer
            def call():
                fn(*args, **kwargs)
            with lock:
                if timer:
                    timer.cancel()
                timer = threading.Timer(wait, call)
                timer.start()
        return wrapper
    return deco

if __name__ == "__main__":
    @debounce(0.1)
    def say(x):
        print("say", x)
    say(1); say(2); say(3)
    time.sleep(0.2)
```

### Questions

1. Describe how the decorator debounces calls.
2. What output is expected from the example?
3. Modify to support an option `leading=True` to call immediately on first invocation.

---

## Q206

### table_formatter.py

```python
def format_table(rows, padding=1):
    cols = max(len(r) for r in rows)
    widths = [0]*cols
    for r in rows:
        for i, v in enumerate(r):
            widths[i] = max(widths[i], len(str(v)))
    lines = []
    for r in rows:
        parts = []
        for i in range(cols):
            v = str(r[i]) if i < len(r) else ""
            parts.append(v.ljust(widths[i]+padding))
        lines.append("".join(parts).rstrip())
    return "\n".join(lines)

if __name__ == "__main__":
    print(format_table([["id","name"], ["1","Alice"], ["2","Bob"]]))
```

### Questions

1. How does padding affect alignment?
2. What happens with ragged rows?
3. Modify to allow per-column alignment (left/right/center).

---

## Q207

### build_index.py

```python
def build_inverted_index(docs):
    """
    docs: dict id -> text
    returns dict word -> set(ids)
    """
    idx = {}
    for doc_id, text in docs.items():
        for w in set(text.lower().split()):
            idx.setdefault(w, set()).add(doc_id)
    return idx

if __name__ == "__main__":
    docs = {1:"Hello world", 2:"Hello there"}
    print(build_inverted_index(docs))
```

### Questions

1. What inverted index is produced?
2. Why use `set(text.split())` per doc?
3. Modify to store word frequencies per doc instead of just sets.

---

## Q208

### unique_emails.py

```python
def canonical_email(email):
    local, at, domain = email.partition("@")
    local = local.split("+",1)[0].replace(".", "")
    return local + "@" + domain.lower()

def unique_emails(emails):
    return len({canonical_email(e) for e in emails})

if __name__ == "__main__":
    print(unique_emails(["a.b+x@EX.com","ab@ex.com"]))
```

### Questions

1. What does the example return and why?
2. Which email normalization rules are applied?
3. Modify to handle domains that treat dots as significant (allow override).

---

## Q209

### file_chunk_reader.py

```python
def read_chunks(path, chunk_size=4096):
    with open(path, "rb") as f:
        while True:
            b = f.read(chunk_size)
            if not b:
                break
            yield b

if __name__ == "__main__":
    # example usage omitted
    pass
```

### Questions

1. Why is binary mode used here?
2. How can a caller process text lines using these chunks? Outline approach.
3. Modify to yield overlapping windows of bytes of size `window_size`.

---

## Q210

### flatten_nested_dicts.py

```python
def flatten_nested(d, parent_key="", sep="."):
    items = []
    for k, v in d.items():
        new_key = parent_key + sep + k if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_nested(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)

if __name__ == "__main__":
    print(flatten_nested({"a":{"b":1},"c":2}))
```

### Questions

1. What flattened dict is printed?
2. How are non-dict iterables (lists) treated?
3. Modify to support a max depth parameter.

---

## Q211

### sandbox_exec.py

```python
import ast, types

def safe_exec(expr, allowed_names=None):
    node = ast.parse(expr, mode="exec")
    for n in ast.walk(node):
        if isinstance(n, (ast.Import, ast.ImportFrom, ast.Call)):
            raise ValueError("disallowed construct")
    globs = {"__builtins__": {}}
    if allowed_names:
        globs.update(allowed_names)
    locs = {}
    exec(compile(node, "<string>", "exec"), globs, locs)
    return locs

if __name__ == "__main__":
    print(safe_exec("a=1\nb=2\n", {}))
```

### Questions

1. What constructs are blocked by this simple check?
2. Why is `__builtins__` set to `{}`? What limitations does that impose?
3. Discuss security pitfalls and suggest safer alternatives.

---

## Q212

### overlapping_intervals.py

```python
def has_overlap(intervals):
    intervals = sorted(intervals, key=lambda x: x[0])
    last_end = None
    for s, e in intervals:
        if last_end is not None and s < last_end:
            return True
        last_end = max(last_end, e) if last_end is not None else e
    return False

if __name__ == "__main__":
    print(has_overlap([(1,2),(3,4),(2,5)]))
```

### Questions

1. Will the example return True or False? Explain.
2. Why sort by start time first?
3. Modify to return the overlapping pair when found.

---

## Q213

### frequent_elements.py

```python
from collections import Counter

def top_k(nums, k):
    cnt = Counter(nums)
    return [x for x, _ in cnt.most_common(k)]

if __name__ == "__main__":
    print(top_k([1,1,2,2,2,3], 2))
```

### Questions

1. What does the example return?
2. How does `most_common` order ties?
3. Modify to return elements with counts above a given threshold.

---

## Q214

### nth_prime.py

```python
def nth_prime(n):
    if n < 1:
        return None
    count = 0
    num = 1
    while True:
        num += 1
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                break
        else:
            count += 1
            if count == n:
                return num

if __name__ == "__main__":
    print(nth_prime(10))
```

### Questions

1. What is the 10th prime printed by the example?
2. Explain complexity and possible optimizations.
3. Modify to use a simple sieve for better performance.

---

## Q215

### unique_subseqs.py

```python
def unique_subsequences(s, k):
    """
    Return set of all unique substrings of length k.
    """
    out = set()
    for i in range(len(s)-k+1):
        out.add(s[i:i+k])
    return out

if __name__ == "__main__":
    print(unique_subsequences("aaaa", 2))
```

### Questions

1. What is returned for the example and why?
2. How would the output differ for "ababa"?
3. Modify to count occurrences of each substring instead of unique set.

---

## Q216

### chunked_upload_sim.py

```python
def upload_chunks(chunks, uploader):
    """
    uploader: callable(chunk, idx) -> True/False
    Return list of successful indices.
    """
    successes = []
    for i, c in enumerate(chunks):
        ok = uploader(c, i)
        if ok:
            successes.append(i)
        else:
            break
    return successes

if __name__ == "__main__":
    def fake(c, i): return i != 2
    print(upload_chunks([b"a",b"b",b"c",b"d"], fake))
```

### Questions

1. What indices are returned by the example?
2. Why might you want retries on failure instead of breaking?
3. Modify to resume from last successful chunk given a resume index.

---

## Q217

### sum_of_pairs_count.py

```python
def count_pairs(nums, target):
    seen = {}
    count = 0
    for x in nums:
        need = target - x
        count += seen.get(need, 0)
        seen[x] = seen.get(x, 0) + 1
    return count

if __name__ == "__main__":
    print(count_pairs([1,1,2,3], 4))
```

### Questions

1. What count is printed for the example?
2. Why does the algorithm use a hashmap to count complements?
3. Modify to return unique value pairs (unordered) instead of count.

---

## Q218

### secure_compare.py

```python
import hmac

def secure_equal(a, b):
    return hmac.compare_digest(str(a), str(b))

if __name__ == "__main__":
    print(secure_equal("abc", "abc"))
```

### Questions

1. Why use `compare_digest` instead of `==` for secrets?
2. What types are safe to pass to `compare_digest`?
3. Modify to accept bytes input and document encoding expectations.

---

## Q219

### flatten_generator_depth_limited.py

```python
def flatten_limited(nested, max_depth=1, _depth=0):
    for item in nested:
        if _depth < max_depth and isinstance(item, (list, tuple)):
            for x in flatten_limited(item, max_depth, _depth+1):
                yield x
        else:
            yield item

if __name__ == "__main__":
    print(list(flatten_limited([1,[2,[3]]], max_depth=1)))
```

### Questions

1. What is printed for max_depth=1?
2. How does `max_depth` affect flattening?
3. Modify to accept `max_items` to stop after yielding a limit.

---

## Q220

### json_key_remap.py

```python
def remap_keys(d, mapping):
    """
    mapping: old_key -> new_key
    """
    out = {}
    for k, v in d.items():
        new_k = mapping.get(k, k)
        if isinstance(v, dict):
            out[new_k] = remap_keys(v, mapping)
        else:
            out[new_k] = v
    return out

if __name__ == "__main__":
    print(remap_keys({"a":1,"b":{"a":2}}, {"a":"alpha"}))
```

### Questions

1. What remapped dict is printed?
2. Does mapping apply recursively? Explain.
3. Modify so mapping values can be callables that transform the key or value.

---

## Q221

### quantize_values.py

```python
def quantize(value, step):
    """
    Round value to nearest multiple of step.
    """
    return round(value / step) * step

def quantize_list(lst, step):
    return [quantize(x, step) for x in lst]

if __name__ == "__main__":
    print(quantize_list([0.12, 0.37, 0.89], 0.25))
```

### Questions

1. What quantized list is produced for the example?
2. How does `round` handle ties?
3. Modify `quantize` to always floor or always ceil instead of nearest.

---

## Q222

### url_query_merge.py

```python
from urllib.parse import urlparse, parse_qsl, urlencode, urlunparse

def merge_query(url, params):
    p = urlparse(url)
    q = dict(parse_qsl(p.query))
    q.update(params)
    new_q = urlencode(q)
    return urlunparse((p.scheme, p.netloc, p.path, p.params, new_q, p.fragment))

if __name__ == "__main__":
    print(merge_query("https://a.com/path?x=1", {"y":"2","x":"9"}))
```

### Questions

1. What URL is produced by the example?
2. How are duplicate keys handled?
3. Modify to preserve multiple values per key (lists) instead of overriding.

---

## Q223

### weighted_random_generator.py

```python
import random
import bisect

class WeightedGen:
    def __init__(self, items, weights):
        total = 0
        self.cum = []
        self.items = items
        for w in weights:
            total += w
            self.cum.append(total)
        self.total = total

    def sample(self):
        r = random.random() * self.total
        i = bisect.bisect_right(self.cum, r)
        return self.items[i]

if __name__ == "__main__":
    g = WeightedGen(["a","b"], [0.2, 0.8])
    print(g.sample())
```

### Questions

1. How does `sample()` choose an item probabilistically?
2. What if all weights sum to zero?
3. Modify to produce an iterator yielding infinite samples.

---

## Q224

### event_bus.py

```python
from collections import defaultdict

class EventBus:
    def __init__(self):
        self.handlers = defaultdict(list)

    def subscribe(self, event, fn):
        self.handlers[event].append(fn)

    def publish(self, event, *args, **kwargs):
        for fn in list(self.handlers.get(event, [])):
            fn(*args, **kwargs)

if __name__ == "__main__":
    bus = EventBus()
    bus.subscribe("m", lambda x: print("got", x))
    bus.publish("m", 42)
```

### Questions

1. What will the example print?
2. Why iterate over `list(self.handlers.get(...))` instead of the original list?
3. Modify to support asynchronous handlers (coroutines).

---

## Q225

### sum_digits_base.py

```python
def sum_digits_base(n, base=10):
    n = abs(n)
    s = 0
    while n:
        s += n % base
        n //= base
    return s

if __name__ == "__main__":
    print(sum_digits_base(255, 16))
```

### Questions

1. What is printed for 255 in base 16?
2. How would you represent digits > 9 if needed?
3. Modify to return the digit list instead of their sum.

---

## Q226

### enumerate_recursive.py

```python
def enumerate_recursive(obj, prefix=()):
    """
    Yield (path_tuple, value) for nested dict/list structures.
    """
    if isinstance(obj, dict):
        for k, v in obj.items():
            yield from enumerate_recursive(v, prefix + (k,))
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            yield from enumerate_recursive(v, prefix + (i,))
    else:
        yield prefix, obj

if __name__ == "__main__":
    data = {"a":[1, {"b":2}]}
    for p, v in enumerate_recursive(data):
        print(p, v)
```

### Questions

1. What pairs (path, value) are printed?
2. How are list indices represented in the path?
3. Modify to accept a callback instead of yielding tuples.

---

## Q227

### sparse_prefix_sum.py

```python
class SparsePrefix:
    def __init__(self):
        self.data = {}  # index->value

    def add(self, idx, val):
        self.data[idx] = self.data.get(idx, 0) + val

    def prefix_sum(self, idx):
        s = 0
        for i, v in self.data.items():
            if i <= idx:
                s += v
        return s

if __name__ == "__main__":
    sp = SparsePrefix(); sp.add(2,10); sp.add(5,3)
    print(sp.prefix_sum(4))
```

### Questions

1. What prefix sum is printed for idx=4?
2. Why is this naive approach O(n) per query and how to optimize?
3. Modify to use a Binary Indexed Tree (Fenwick) for faster updates/queries.

---

## Q228

### json_sort_keys.py

```python
import json

def json_sorted(obj):
    return json.dumps(obj, sort_keys=True)

if __name__ == "__main__":
    print(json_sorted({"b":1,"a":2}))
```

### Questions

1. What string is printed and why is sorting useful?
2. How does this affect nested dict ordering?
3. Modify to pretty-print with indentation and stable key order.

---

## Q229

### find_longest_word.py

```python
def longest_word(words):
    if not words:
        return None
    best = words[0]
    for w in words[1:]:
        if len(w) > len(best):
            best = w
    return best

if __name__ == "__main__":
    print(longest_word(["a","abc","ab"]))
```

### Questions

1. What is the longest word returned?
2. How to return all words tied for longest?
3. Modify to handle streaming input (generator of words).

---

## Q230

### normalize_whitespace.py

```python
import re

def normalize_ws(s):
    return re.sub(r'\s+', ' ', s).strip()

if __name__ == "__main__":
    print(normalize_ws("  hello \n\t world  "))
```

### Questions

1. What is printed after normalization?
2. Why use regex instead of `split()` + `join()`?
3. Modify to preserve single newlines while collapsing other whitespace.

---

## Q231

### compute_similarity_jaccard.py

```python
def jaccard(a, b):
    sa, sb = set(a), set(b)
    inter = sa & sb
    union = sa | sb
    return len(inter) / len(union) if union else 1.0

if __name__ == "__main__":
    print(jaccard([1,2,3], [2,3,4]))
```

### Questions

1. What Jaccard similarity does the example produce?
2. How is empty-union handled?
3. Modify to compute weighted Jaccard for multisets.

---

## Q232

### binary_gap.py

```python
def binary_gap(n):
    b = bin(n)[2:].strip('0')
    return max((len(x) for x in b.split('1') if x), default=0)

if __name__ == "__main__":
    print(binary_gap(9))  # 1001 -> gap 2
```

### Questions

1. What value is printed for n=9?
2. Explain why `strip('0')` is used.
3. Modify to return positions (start,end) of the largest gap.

---

## Q233

### stream_word_count.py

```python
from collections import Counter
import sys

def stream_count_words():
    cnt = Counter()
    for line in sys.stdin:
        for w in line.split():
            cnt[w] += 1
    return cnt

if __name__ == "__main__":
    # usage: echo "a b a" | python script.py
    pass
```

### Questions

1. How does the function process streaming input?
2. How to make it memory-bounded (approximate counts)?
3. Modify to report top-K words periodically (e.g., every N lines).

---

## Q234

### sum_two_largest.py

```python
def sum_two_largest(nums):
    if not nums:
        return 0
    a = b = float('-inf')
    for x in nums:
        if x > a:
            b = a; a = x
        elif x > b:
            b = x
    return (a if a!=-float('inf') else 0) + (b if b!=-float('inf') else 0)

if __name__ == "__main__":
    print(sum_two_largest([5,1,3]))
```

### Questions

1. What is printed by the example?
2. How does algorithm handle negative numbers and single-element lists?
3. Modify to return indices of the two largest elements.

---

## Q235

### time_series_resample.py

```python
from datetime import datetime, timedelta

def resample_daily(points):
    """
    points: list of (datetime, value) unsorted. Return dict date->sum.
    """
    out = {}
    for dt, v in points:
        d = dt.date()
        out[d] = out.get(d, 0) + v
    return out

if __name__ == "__main__":
    print(resample_daily([(datetime(2025,1,1,10),1),(datetime(2025,1,1,22),2)]))
```

### Questions

1. What daily sums are produced in the example?
2. How to handle timezone-aware datetimes?
3. Modify to return a complete uninterrupted date range filling missing dates with zero.

---

## Q236

### second_largest.py

```python
def second_largest(nums):
    if len(nums) < 2:
        return None
    first = second = float('-inf')
    for x in nums:
        if x > first:
            second = first; first = x
        elif first > x > second:
            second = x
    return None if second == float('-inf') else second

if __name__ == "__main__":
    print(second_largest([3,1,3,2]))
```

### Questions

1. What second largest value is returned for the example?
2. How are duplicates of the largest value treated?
3. Modify to return the second largest distinct value or `None` if not present.

---

## Q237

### validate_brackets_types.py

```python
def validate(s, pairs={'(':')','[':']','{':'}'}):
    stack = []
    for ch in s:
        if ch in pairs:
            stack.append(ch)
        elif ch in pairs.values():
            if not stack or pairs[stack.pop()] != ch:
                return False
    return not stack

if __name__ == "__main__":
    print(validate("{[()]}"))
```

### Questions

1. What does the example return?
2. Why pop before comparison?
3. Modify to ignore bracket-like characters inside string literals (quotes).

---

## Q238

### escape_html_text.py

```python
import html

def escape_html(s):
    return html.escape(s)

if __name__ == "__main__":
    print(escape_html('<div class="x">Hello & Goodbye</div>'))
```

### Questions

1. What does the example print after escaping?
2. When would you prefer `html.escape(..., quote=False)`?
3. Modify to selectively escape only `<` and `&` but not quotes.

---

## Q239

### k_closest_points_origin.py

```python
import heapq
import math

def k_closest(points, k):
    heap = []
    for x, y in points:
        d = -(x*x + y*y)  # use max-heap via negatives
        if len(heap) < k:
            heapq.heappush(heap, (d, (x,y)))
        else:
            if d > heap[0][0]:
                heapq.heapreplace(heap, (d, (x,y)))
    return [p for _, p in heap]

if __name__ == "__main__":
    print(k_closest([(1,2),(3,4),(0,1)], 2))
```

### Questions

1. What two points are returned for the example?
2. Why use negative squared distance?
3. Modify to return points sorted by increasing distance.

---

## Q240

### parse_key_value_file.py

```python
def parse_kv(path):
    d = {}
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            if not line.strip() or line.strip().startswith("#"):
                continue
            if "=" in line:
                k, v = line.split("=",1)
                d[k.strip()] = v.strip()
    return d

if __name__ == "__main__":
    # usage example omitted
    pass
```

### Questions

1. How does parser handle comments and blank lines?
2. What if a value contains `=` characters?
3. Modify to support quoted values (strip surrounding quotes).

---

## Q241

### group_by_window.py

```python
from collections import defaultdict

def group_by_window(items, window_size):
    out = defaultdict(list)
    for i, x in enumerate(items):
        out[i // window_size].append(x)
    return dict(out)

if __name__ == "__main__":
    print(group_by_window(list(range(10)), 3))
```

### Questions

1. What groups does the example produce?
2. How to handle variable-length final window?
3. Modify to return list of lists instead of dict keyed by window index.

---

## Q242

### float_histogram.py

```python
import bisect

def float_hist(vals, edges):
    counts = [0]*(len(edges)-1)
    for v in vals:
        i = bisect.bisect_right(edges, v) - 1
        if 0 <= i < len(counts):
            counts[i] += 1
    return counts

if __name__ == "__main__":
    print(float_hist([0.5,1.2,3.4], [0,1,2,4]))
```

### Questions

1. What counts are produced for the example?
2. Why use `bisect_right` then -1?
3. Modify to return normalized densities (counts divided by bin width).

---

## Q243

### ordered_unique.py

```python
def ordered_unique(seq):
    seen = set()
    out = []
    for x in seq:
        if x not in seen:
            seen.add(x)
            out.append(x)
    return out

if __name__ == "__main__":
    print(ordered_unique([1,2,1,3,2]))
```

### Questions

1. What list is printed for the example?
2. How does this preserve original order?
3. Modify to allow a key function for uniqueness test.

---

## Q244

### longest_run.py

```python
def longest_run(nums):
    best = cur = nums[0] if nums else None
    best_len = cur_len = 1 if nums else 0
    for i in range(1, len(nums)):
        if nums[i] == nums[i-1]:
            cur_len += 1
        else:
            if cur_len > best_len:
                best_len = cur_len; best = nums[i-1]
            cur_len = 1
    if cur_len > best_len:
        best_len = cur_len; best = nums[-1]
    return best, best_len

if __name__ == "__main__":
    print(longest_run([1,1,2,2,2,3]))
```

### Questions

1. What is the longest run and its length in the example?
2. How would you adapt to find longest increasing run instead?
3. Modify to return start and end indices of the longest run.

---

## Q245

### responsive_sleep.py

```python
import time

def responsive_sleep(total, step=0.1, should_stop=lambda: False):
    elapsed = 0.0
    while elapsed < total:
        if should_stop():
            return False
        time.sleep(min(step, total - elapsed))
        elapsed += step
    return True

if __name__ == "__main__":
    print(responsive_sleep(0.5))
```

### Questions

1. What does the function return when not interrupted?
2. Why sleep in small steps instead of one long sleep?
3. Modify to accept an event object (`threading.Event`) to wait on.

---

## Q246

### detect_duplicates_sorted.py

```python
def has_duplicates_sorted(a):
    for i in range(1, len(a)):
        if a[i] == a[i-1]:
            return True
    return False

if __name__ == "__main__":
    print(has_duplicates_sorted([1,2,2,3]))
```

### Questions

1. What does the example return?
2. What precondition on `a` is required?
3. Modify to return the duplicate value(s) found.

---

## Q247

### chunked_json_write.py

```python
import json

def write_json_array(path, items, chunk_size=1000):
    with open(path, "w", encoding="utf-8") as f:
        f.write("[")
        first = True
        for i, it in enumerate(items):
            if not first:
                f.write(",")
            else:
                first = False
            json.dump(it, f)
        f.write("]")

if __name__ == "__main__":
    # usage example omitted
    pass
```

### Questions

1. How does this avoid building the entire list in memory?
2. What happens if `items` is a generator?
3. Modify to pretty-print with newlines after each item for readability.

---

## Q248

### replace_nth_occurrence.py

```python
def replace_nth(s, old, new, n):
    idx = -1
    for _ in range(n):
        idx = s.find(old, idx+1)
        if idx == -1:
            return s
    return s[:idx] + new + s[idx+len(old):]

if __name__ == "__main__":
    print(replace_nth("a b a b a", "a", "X", 2))
```

### Questions

1. What string is produced by the example?
2. How does the function behave when fewer than `n` occurrences exist?
3. Modify to replace the nth occurrence from the end.

---

## Q249

### rolling_window_stats.py

```python
from collections import deque

def rolling_stats(seq, k):
    dq = deque()
    s = 0
    for x in seq:
        dq.append(x); s += x
        if len(dq) > k:
            s -= dq.popleft()
        if len(dq) == k:
            yield s / k, min(dq), max(dq)

if __name__ == "__main__":
    print(list(rolling_stats([1,2,3,4,5], 3)))
```

### Questions

1. What triples (mean,min,max) are yielded for the example?
2. Why keep deque of size at most k?
3. Modify to return variance in addition to mean.

---

## Q250

### find_triplets_sum_zero.py

```python
def three_sum(nums):
    nums.sort()
    res = []
    n = len(nums)
    for i in range(n):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        l, r = i+1, n-1
        while l < r:
            s = nums[i] + nums[l] + nums[r]
            if s == 0:
                res.append([nums[i], nums[l], nums[r]])
                l += 1; r -= 1
                while l < r and nums[l] == nums[l-1]:
                    l += 1
                while l < r and nums[r] == nums[r+1]:
                    r -= 1
            elif s < 0:
                l += 1
            else:
                r -= 1
    return res

if __name__ == "__main__":
    print(three_sum([-1,0,1,2,-1,-4]))
```

### Questions

1. What triplets are returned for the example?
2. Explain why sorting helps and how duplicates are skipped.
3. Modify to find triplets that sum to a given target instead of zero.







Here are **50 more** Python coding questions, continuing numbering from **Q251** to **Q300**. Each item includes a code file (self-contained) and **three learner questions**. Titles give no hints and there are no emojis.

---

## Q251

### max_heap.py

```python
import heapq

class MaxHeap:
    def __init__(self):
        self._h = []

    def push(self, x):
        heapq.heappush(self._h, -x)

    def pop(self):
        if not self._h:
            raise IndexError("pop from empty heap")
        return -heapq.heappop(self._h)

    def peek(self):
        return -self._h[0] if self._h else None

if __name__ == "__main__":
    h = MaxHeap()
    h.push(3); h.push(1); h.push(4)
    print(h.peek(), h.pop(), h.pop())
```

### Questions

1. What is printed by the example and why?
2. Why does this use negative values internally?
3. Modify to support `push_pop` and `replace` methods analogously to `heapq`.

---

## Q252

### find_duplicates_k.py

```python
def find_duplicates_k(nums, k):
    """
    Return elements that appear more than once within distance k.
    """
    seen = {}
    res = set()
    for i, x in enumerate(nums):
        if x in seen and i - seen[x] <= k:
            res.add(x)
        seen[x] = i
    return list(res)

if __name__ == "__main__":
    print(find_duplicates_k([1,2,3,1,2,3], 3))
```

### Questions

1. What does the example return and why?
2. How does the `seen` dict enforce the distance constraint?
3. Modify to return indices of duplicate pairs instead of values.

---

## Q253

### parallel_map.py

```python
from concurrent.futures import ThreadPoolExecutor

def parallel_map(func, items, max_workers=4):
    with ThreadPoolExecutor(max_workers=max_workers) as ex:
        futures = [ex.submit(func, it) for it in items]
        return [f.result() for f in futures]

if __name__ == "__main__":
    print(parallel_map(lambda x: x*x, range(6), max_workers=3))
```

### Questions

1. What output is produced by the example?
2. Why might ordering of results match input order here? Are there cases it would not?
3. Modify to stream results as they complete using `as_completed`.

---

## Q254

### sliding_min.py

```python
from collections import deque

def sliding_min(seq, k):
    if k <= 0:
        raise ValueError("k must be positive")
    dq = deque()
    res = []
    for i, x in enumerate(seq):
        while dq and dq[0] <= i - k:
            dq.popleft()
        while dq and seq[dq[-1]] > x:
            dq.pop()
        dq.append(i)
        if i >= k - 1:
            res.append(seq[dq[0]])
    return res

if __name__ == "__main__":
    print(sliding_min([2,1,3,4,0,5], 3))
```

### Questions

1. What minima are returned for the example?
2. Explain why indices (not values) are kept in the deque.
3. Modify to yield `(window_start, min_value)` tuples.

---

## Q255

### binary_gap_positions.py

```python
def binary_gap_positions(n):
    b = bin(n)[2:].strip('0')
    gaps = []
    start = 0
    for i, ch in enumerate(b):
        if ch == '1':
            start = i+1
            break
    cur = start
    for i in range(start, len(b)):
        if b[i] == '1':
            if i - cur > 0:
                gaps.append((cur, i-1, i-cur))
            cur = i+1
    return gaps

if __name__ == "__main__":
    print(binary_gap_positions(9))
```

### Questions

1. What list is printed for `9` and what do tuples mean?
2. Why strip trailing zeros before computing gaps?
3. Modify to return gaps relative to original binary string (including leading bits).

---

## Q256

### sparse_add.py

```python
def sparse_add(a, b):
    """
    a, b: dict index->value for sparse vectors. Return new dict.
    """
    res = dict(a)
    for k, v in b.items():
        res[k] = res.get(k, 0) + v
        if res[k] == 0:
            del res[k]
    return res

if __name__ == "__main__":
    print(sparse_add({0:1,2:3}, {1:4,2:-3}))
```

### Questions

1. What is the result for the example?
2. Why delete zero entries? What trade-offs exist?
3. Modify to support in-place addition option.

---

## Q257

### rotate_string_kmp.py

```python
def is_rotation(s, t):
    """
    Check if t is rotation of s by KMP-style trick.
    """
    if len(s) != len(t):
        return False
    return t in (s + s)

if __name__ == "__main__":
    print(is_rotation("waterbottle", "erbottlewat"))
```

### Questions

1. Why does the `s+s` trick work?
2. What complexity does this check have?
3. Modify to return the rotation offset K if present, else -1.

---

## Q258

### topological_order_safe.py

```python
from collections import defaultdict, deque

def topo_sort(edges):
    g = defaultdict(list)
    indeg = defaultdict(int)
    nodes = set()
    for u, v in edges:
        g[u].append(v)
        indeg[v] += 1
        nodes.add(u); nodes.add(v)
    q = deque([n for n in nodes if indeg.get(n,0)==0])
    res = []
    while q:
        n = q.popleft()
        res.append(n)
        for nb in g[n]:
            indeg[nb] -= 1
            if indeg[nb] == 0:
                q.append(nb)
    if len(res) != len(nodes):
        return None  # cycle
    return res

if __name__ == "__main__":
    print(topo_sort([("a","b"),("b","c")]))
```

### Questions

1. What is returned for an acyclic graph?
2. Why return `None` on cycles instead of raising? Pros/cons?
3. Modify to return one detected cycle when present.

---

## Q259

### partition_even_odd.py

```python
def partition_even_odd(nums):
    i = 0
    for j in range(len(nums)):
        if nums[j] % 2 == 0:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
    return nums

if __name__ == "__main__":
    print(partition_even_odd([3,2,4,1,6]))
```

### Questions

1. What in-place rearrangement does the example yield?
2. Is the relative order of evens/pairs preserved? Explain.
3. Modify to partition by a provided predicate function.

---

## Q260

### download_sim.py

```python
import time

def simulate_download(size_kb, speed_kb_s=100):
    downloaded = 0
    chunk = 10
    while downloaded < size_kb:
        time.sleep(chunk / speed_kb_s)
        downloaded += chunk
        yield min(downloaded, size_kb)

if __name__ == "__main__":
    for p in simulate_download(250, 50):
        print("Downloaded KB:", p)
```

### Questions

1. What does the generator yield?
2. How to adapt to display percent complete?
3. Modify to support pausing/resuming via external signal.

---

## Q261

### safe_divide_list.py

```python
def safe_divide_list(a, b):
    """
    Element-wise divide lists a / b, returns list with None where division invalid.
    """
    n = min(len(a), len(b))
    out = []
    for i in range(n):
        try:
            out.append(a[i] / b[i])
        except Exception:
            out.append(None)
    return out

if __name__ == "__main__":
    print(safe_divide_list([4,2,0], [2,0,1]))
```

### Questions

1. What list is produced by the example?
2. Why use `min(len(a), len(b))`? What happens to extra elements?
3. Modify to raise on first invalid division if `strict=True`.

---

## Q262

### windowed_max_indices.py

```python
from collections import deque

def sliding_max_indices(seq, k):
    dq = deque()
    res = []
    for i, x in enumerate(seq):
        while dq and dq[0] <= i - k:
            dq.popleft()
        while dq and seq[dq[-1]] < x:
            dq.pop()
        dq.append(i)
        if i >= k - 1:
            res.append(dq[0])
    return res

if __name__ == "__main__":
    print(sliding_max_indices([1,3,2,5,4], 3))
```

### Questions

1. What indices are returned for the example?
2. How could you use these indices to extract window maxima efficiently?
3. Modify to return all indices that equal the window maximum (ties).

---

## Q263

### format_bytes.py

```python
def human_readable(n):
    units = ["B","KB","MB","GB","TB"]
    i = 0
    while n >= 1024 and i < len(units)-1:
        n /= 1024.0
        i += 1
    return f"{n:.2f}{units[i]}"

if __name__ == "__main__":
    print(human_readable(1234567))
```

### Questions

1. What string does the example produce?
2. Why limit units and what happens past TB?
3. Modify to use powers of 1000 instead of 1024 optionally.

---

## Q264

### json_schema_flatten.py

```python
def flatten_schema(schema, parent=""):
    """
    Given nested dict schema mapping fields -> types, return flat mapping "a.b"->type.
    """
    out = {}
    for k, v in schema.items():
        key = f"{parent}.{k}" if parent else k
        if isinstance(v, dict):
            out.update(flatten_schema(v, key))
        else:
            out[key] = v
    return out

if __name__ == "__main__":
    print(flatten_schema({"a":{"b":int},"c":str}))
```

### Questions

1. What flat mapping does the example produce?
2. How to handle arrays/lists in the schema representation?
3. Modify to accept a separator argument other than '.'.

---

## Q265

### mask_sensitive_json.py

```python
def mask_json(obj, keys=("password","ssn")):
    if isinstance(obj, dict):
        return {k: ("***" if k.lower() in keys else mask_json(v, keys)) for k, v in obj.items()}
    if isinstance(obj, list):
        return [mask_json(x, keys) for x in obj]
    return obj

if __name__ == "__main__":
    print(mask_json({"user":"a","password":"p","info":{"ssn":"123"}}))
```

### Questions

1. What masked structure is printed?
2. Why use case-insensitive matching of keys? Pros/cons?
3. Modify to mask values by pattern (e.g., regex) rather than by key name.

---

## Q266

### rotate_matrix_copy.py

```python
def rotate_matrix_copy(mat):
    rows = len(mat)
    cols = len(mat[0]) if mat else 0
    res = [[None]*rows for _ in range(cols)]
    for i in range(rows):
        for j in range(cols):
            res[j][rows-1-i] = mat[i][j]
    return res

if __name__ == "__main__":
    print(rotate_matrix_copy([[1,2,3],[4,5,6]]))
```

### Questions

1. What rotated matrix is produced for the example (rectangular)?
2. Why is this approach safe for non-square matrices?
3. Modify to rotate 90° counter-clockwise instead.

---

## Q267

### balanced_multiset.py

```python
from collections import Counter

def can_make_equal_by_one_move(a, b):
    ca, cb = Counter(a), Counter(b)
    # simple check: same multiset or one move swap can make equal
    return ca == cb

if __name__ == "__main__":
    print(can_make_equal_by_one_move([1,2,2],[2,1,2]))
```

### Questions

1. What does the function currently check?
2. Why is this insufficient to test "one move"?
3. Modify to check if exchanging a single element from `a` to `b` (and vice versa) can equalize multisets.

---

## Q268

### lexicographic_permutations.py

```python
import itertools

def kth_permutation(s, k):
    perms = itertools.permutations(sorted(s))
    for i, p in enumerate(perms):
        if i == k:
            return "".join(p)
    return None

if __name__ == "__main__":
    print(kth_permutation("bca", 2))
```

### Questions

1. What is returned for the example and why?
2. What are performance issues of this approach?
3. Modify to compute the k-th permutation directly without generating all prior permutations.

---

## Q269

### parse_ranges.py

```python
def parse_ranges(s):
    """
    Parse string like "1-3,5,7-9" into sorted list of ints.
    """
    out = []
    for part in s.split(","):
        if "-" in part:
            a, b = map(int, part.split("-"))
            out.extend(range(a, b+1))
        else:
            out.append(int(part))
    return sorted(set(out))

if __name__ == "__main__":
    print(parse_ranges("1-3,5,2,7-8"))
```

### Questions

1. What list does the example produce?
2. How are duplicates handled?
3. Modify to accept whitespace and validate ranges `a<=b`.

---

## Q270

### find_subarray_with_product.py

```python
def find_subarray_product(nums, target):
    """
    Return any contiguous subarray whose product equals target.
    (Assumes positive integers.)
    """
    n = len(nums)
    for i in range(n):
        prod = 1
        for j in range(i, n):
            prod *= nums[j]
            if prod == target:
                return nums[i:j+1]
            if prod > target:
                break
    return None

if __name__ == "__main__":
    print(find_subarray_product([2,3,1,4], 12))
```

### Questions

1. What subarray does the example return?
2. Why does this assume positive integers? What breaks otherwise?
3. Modify to return start/end indices instead of the slice.

---

## Q271

### flatten_generator_unique.py

```python
def flatten_unique(nested):
    seen = set()
    for item in nested:
        if isinstance(item, (list, tuple)):
            for x in flatten_unique(item):
                if x not in seen:
                    seen.add(x); yield x
        else:
            if item not in seen:
                seen.add(item); yield item

if __name__ == "__main__":
    print(list(flatten_unique([1,[2,1],[3,[2]]])))
```

### Questions

1. What sequence is yielded for the example?
2. How does `seen` interact with nested order?
3. Modify to preserve first occurrence ordering across nested levels.

---

## Q272

### http_status_retry.py

```python
import time
import random

def retry_on_status(fetch, attempts=3, retry_statuses=(500,502,503)):
    last = None
    for i in range(attempts):
        code, data = fetch()
        if code not in retry_statuses:
            return code, data
        last = (code, data)
        time.sleep(0.1 * (2 ** i))
    return last

if __name__ == "__main__":
    def fake(): return (random.choice([200,500,502]), b"")
    print(retry_on_status(fake))
```

### Questions

1. What behavior does `retry_on_status` implement?
2. Why apply exponential backoff between attempts?
3. Modify to accept a function deciding whether to retry given `(code, data)`.

---

## Q273

### merge_sorted_iters.py

```python
import heapq

def merge_sorted_iters(iters):
    heap = []
    for idx, it in enumerate(iters):
        try:
            val = next(it)
            heapq.heappush(heap, (val, idx, it))
        except StopIteration:
            pass
    while heap:
        val, idx, it = heapq.heappop(heap)
        yield val
        try:
            nxt = next(it)
            heapq.heappush(heap, (nxt, idx, it))
        except StopIteration:
            pass

if __name__ == "__main__":
    a = iter([1,4,7])
    b = iter([2,3,8])
    print(list(merge_sorted_iters([a,b])))
```

### Questions

1. What merged list does the example produce?
2. Why include `idx` in heap tuples?
3. Modify to support key functions for custom ordering.

---

## Q274

### longest_common_subsequence.py

```python
def lcs(a, b):
    n, m = len(a), len(b)
    dp = [[0]*(m+1) for _ in range(n+1)]
    for i in range(n-1,-1,-1):
        for j in range(m-1,-1,-1):
            if a[i]==b[j]:
                dp[i][j] = 1 + dp[i+1][j+1]
            else:
                dp[i][j] = max(dp[i+1][j], dp[i][j+1])
    # reconstruct
    i=j=0; res=[]
    while i<n and j<m:
        if a[i]==b[j]:
            res.append(a[i]); i+=1; j+=1
        elif dp[i+1][j] >= dp[i][j+1]:
            i+=1
        else:
            j+=1
    return "".join(res)

if __name__ == "__main__":
    print(lcs("AGGTAB","GXTXAYB"))
```

### Questions

1. What longest common subsequence does the example return?
2. What is the DP time and space complexity?
3. Modify to return length only in O(min(n,m)) space.

---

## Q275

### detect_anagram_pairs.py

```python
from collections import defaultdict

def anagram_pairs(words):
    d = defaultdict(list)
    for w in words:
        key = "".join(sorted(w))
        d[key].append(w)
    res = []
    for group in d.values():
        if len(group) > 1:
            res.extend([(group[i], group[j]) for i in range(len(group)) for j in range(i+1, len(group))])
    return res

if __name__ == "__main__":
    print(anagram_pairs(["eat","tea","tan","ate"]))
```

### Questions

1. What pairs are returned for the example?
2. How does sorting characters serve as a grouping key?
3. Modify to return indices instead of word pairs.

---

## Q276

### median_of_two_sorted.py

```python
def median_two_sorted(a, b):
    merged = []
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            merged.append(a[i]); i+=1
        else:
            merged.append(b[j]); j+=1
    merged.extend(a[i:]); merged.extend(b[j:])
    n = len(merged)
    mid = n//2
    if n % 2:
        return merged[mid]
    return (merged[mid-1]+merged[mid])/2.0

if __name__ == "__main__":
    print(median_two_sorted([1,3],[2]))
```

### Questions

1. What median is returned for the example?
2. What is the time complexity of this merge-based approach?
3. Modify to achieve O(log(min(n,m))) time using partitioning.

---

## Q277

### merge_k_lists.py

```python
import heapq

def merge_k_lists(lists):
    heap = []
    for idx, lst in enumerate(lists):
        if lst:
            heapq.heappush(heap, (lst[0], idx, 0))
    res = []
    while heap:
        val, li, pi = heapq.heappop(heap)
        res.append(val)
        if pi+1 < len(lists[li]):
            heapq.heappush(heap, (lists[li][pi+1], li, pi+1))
    return res

if __name__ == "__main__":
    print(merge_k_lists([[1,4],[2,3],[0,5]]))
```

### Questions

1. What merged list does the example produce?
2. How does the heap keep track of positions?
3. Modify to merge generators (iterators) rather than indexable lists.

---

## Q278

### find_missing_positive.py

```python
def first_missing_positive(nums):
    n = len(nums)
    for i in range(n):
        while 1 <= nums[i] <= n and nums[nums[i]-1] != nums[i]:
            nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]
    for i in range(n):
        if nums[i] != i+1:
            return i+1
    return n+1

if __name__ == "__main__":
    print(first_missing_positive([3,4,-1,1]))
```

### Questions

1. What value does the example return?
2. Explain why this algorithm runs in O(n) time and O(1) extra space.
3. Modify to avoid mutating the original list (use extra array).

---

## Q279

### compress_run_length.py

```python
def run_length_encode(s):
    if not s:
        return ""
    out = []
    cur = s[0]; cnt = 1
    for ch in s[1:]:
        if ch == cur:
            cnt += 1
        else:
            out.append(f"{cur}{cnt}")
            cur = ch; cnt = 1
    out.append(f"{cur}{cnt}")
    return "".join(out)

if __name__ == "__main__":
    print(run_length_encode("aaabbc"))
```

### Questions

1. What encoded string does the example produce?
2. How would you decode such a string?
3. Modify to handle binary data (bytes) and return bytes.

---

## Q280

### graph_bfs_levels.py

```python
from collections import deque, defaultdict

def bfs_levels(graph, start):
    q = deque([start])
    seen = {start}
    levels = defaultdict(list)
    level = 0
    while q:
        for _ in range(len(q)):
            u = q.popleft()
            levels[level].append(u)
            for v in graph.get(u, []):
                if v not in seen:
                    seen.add(v); q.append(v)
        level += 1
    return dict(levels)

if __name__ == "__main__":
    g = {"a":["b","c"], "b":["d"], "c":[]}
    print(bfs_levels(g, "a"))
```

### Questions

1. What level grouping is returned for the example?
2. Why use level-order traversal here?
3. Modify to stop after `max_levels` and return partial result.




## Q281

### compress_run_length.py

```python
def run_length_encode(s):
    if not s:
        return ""
    out = []
    cur = s[0]
    cnt = 1
    for ch in s[1:]:
        if ch == cur:
            cnt += 1
        else:
            out.append(f"{cur}{cnt}")
            cur = ch
            cnt = 1
    out.append(f"{cur}{cnt}")
    return "".join(out)

if __name__ == "__main__":
    print(run_length_encode("aaabbc"))
```

### Questions

1. What encoded string is produced for the example?
2. How would you decode such a string back to the original?
3. Modify the function to accept bytes (return bytes) instead of strings.

---

## Q282

### graph_bfs_levels.py

```python
from collections import deque, defaultdict

def bfs_levels(graph, start):
    q = deque([start])
    seen = {start}
    levels = defaultdict(list)
    level = 0
    while q:
        for _ in range(len(q)):
            u = q.popleft()
            levels[level].append(u)
            for v in graph.get(u, []):
                if v not in seen:
                    seen.add(v)
                    q.append(v)
        level += 1
    return dict(levels)

if __name__ == "__main__":
    g = {"a":["b","c"], "b":["d"], "c":[]}
    print(bfs_levels(g, "a"))
```

### Questions

1. What level grouping is returned for the example?
2. Explain why BFS produces level-order grouping.
3. Modify to stop after `max_levels` and return partial result.

---

## Q283

### find_closest_pair.py

```python
import math

def closest_pair(points):
    best = float("inf")
    pair = None
    n = len(points)
    for i in range(n):
        for j in range(i+1, n):
            d = math.dist(points[i], points[j])
            if d < best:
                best = d
                pair = (points[i], points[j])
    return best, pair

if __name__ == "__main__":
    pts = [(0,0),(1,1),(2,2),(0,1)]
    print(closest_pair(pts))
```

### Questions

1. What closest pair is found for the sample points?
2. Why is this O(n²) and when is that impractical?
3. Modify to return indices of the closest pair instead of coordinates.

---

## Q284

### redact_sensitive.py

```python
import re

def redact(text, patterns):
    out = text
    for p in patterns:
        out = re.sub(p, "[REDACTED]", out)
    return out

if __name__ == "__main__":
    print(redact("My card 4111-1111-1111-1111", [r"\b\d{4}(?:-\d{4}){3}\b"]))
```

### Questions

1. How does the example redact the card number?
2. What are risks of naive regex redaction?
3. Modify to preserve last four digits and replace preceding digits with `*`.

---

## Q285

### sliding_window_maximum_generator.py

```python
from collections import deque

def sliding_max_gen(seq, k):
    dq = deque()
    for i, x in enumerate(seq):
        while dq and dq[0] <= i - k:
            dq.popleft()
        while dq and seq[dq[-1]] < x:
            dq.pop()
        dq.append(i)
        if i >= k - 1:
            yield seq[dq[0]]

if __name__ == "__main__":
    print(list(sliding_max_gen([1,3,-1,-3,5,3,6,7], 3)))
```

### Questions

1. What values are yielded for the example?
2. Why is the deque storing indices rather than values?
3. Modify to yield `(window_start, max_value)` tuples.

---

## Q286

### paginate_list.py

```python
def paginate(items, page_size):
    it = iter(items)
    while True:
        page = []
        try:
            for _ in range(page_size):
                page.append(next(it))
        except StopIteration:
            pass
        if not page:
            break
        yield page

if __name__ == "__main__":
    for p in paginate(range(1,13), 5):
        print(p)
```

### Questions

1. What pages are printed for range 1..12 with page_size=5?
2. How would you add a `page_number` argument to fetch a single page?
3. Modify to return a generator object with `.next_page()` and `.has_next()`.

---

## Q287

### approximate_percentile.py

```python
import random

def approximate_percentile(seq, q, sample_frac=0.1):
    if not 0 <= q <= 1:
        raise ValueError("q between 0 and 1")
    n = len(seq)
    if n == 0:
        return None
    sample = random.sample(seq, max(1, int(n * sample_frac)))
    sample.sort()
    idx = int(q * (len(sample)-1))
    return sample[idx]

if __name__ == "__main__":
    print(approximate_percentile(list(range(1000)), 0.95, 0.05))
```

### Questions

1. What is this function approximating and what are limitations?
2. How does `sample_frac` affect accuracy and cost?
3. Modify to use reservoir sampling when `seq` is an iterator.

---

## Q288

### serialize_tree.py

```python
class Node:
    def __init__(self, val, children=None):
        self.val = val
        self.children = children or []

def serialize(root):
    if root is None:
        return ""
    parts = [str(root.val)]
    if root.children:
        parts.append("[")
        for c in root.children:
            parts.append(serialize(c))
        parts.append("]")
    return " ".join(p for p in parts if p)

if __name__ == "__main__":
    t = Node(1, [Node(2), Node(3, [Node(4)])])
    print(serialize(t))
```

### Questions

1. What string is produced for the sample tree?
2. How would you design a corresponding `deserialize`?
3. Modify to emit JSON instead for portability.

---

## Q289

### bracket_sequence_count.py

```python
from math import comb

def count_valid_sequences(n):
    return comb(2*n, n) // (n+1)

if __name__ == "__main__":
    print(count_valid_sequences(3))
```

### Questions

1. What number is returned for n=3?
2. What combinatorial object does this compute (name)?
3. Modify to generate all valid parentheses sequences (instead of counting).

---

## Q290

### multi_key_sort.py

```python
def multi_sort(items, keys):
    for key, rev in reversed(keys):
        items.sort(key=lambda x: x.get(key, None), reverse=rev)
    return items

if __name__ == "__main__":
    data = [{"a":2,"b":1},{"a":1,"b":5},{"a":2,"b":0}]
    print(multi_sort(data, [("a", False), ("b", True)]))
```

### Questions

1. What order results from the example?
2. Why are keys applied in reversed order when using `sort` repeatedly?
3. Modify to accept key functions instead of key names.

---

## Q291

### nearest_neighbors_bruteforce.py

```python
import math

def k_nearest(points, query, k):
    dists = [(math.dist(p, query), i, p) for i, p in enumerate(points)]
    dists.sort()
    return [p for _, _, p in dists[:k]]

if __name__ == "__main__":
    pts = [(0,0),(1,1),(2,2),(5,5)]
    print(k_nearest(pts, (1.5,1.5), 2))
```

### Questions

1. What two nearest points are returned for the example?
2. When does brute-force approach become impractical?
3. Modify to return indices and distances as well.

---

## Q292

### safe_open.py

```python
import os

def safe_open(path, mode="r", max_size=None):
    if "w" in mode and os.path.exists(path) and os.path.getsize(path) > (max_size or 0):
        raise ValueError("file too large to overwrite")
    return open(path, mode, encoding="utf-8" if "b" not in mode else None)

if __name__ == "__main__":
    pass
```

### Questions

1. What safety check is performed before opening for write?
2. Why conditionally set `encoding`?
3. Modify to create parent directories when writing if missing.

---

## Q293

### find_subsequence.py

```python
def is_subsequence(s, t):
    it = iter(t)
    return all(c in it for c in s)

if __name__ == "__main__":
    print(is_subsequence("ace", "abcde"))
```

### Questions

1. Why does the example return `True`?
2. Explain why `all(c in it for c in s)` works for subsequence checking.
3. Modify to return the indices in `t` where the characters matched.

---

## Q294

### url_normalize.py

```python
from urllib.parse import urlparse, urlunparse

def normalize_url(url):
    p = urlparse(url)
    scheme = p.scheme.lower() or "http"
    netloc = p.netloc.lower().rstrip("/")
    path = p.path or "/"
    return urlunparse((scheme, netloc, path, "", "", ""))

if __name__ == "__main__":
    print(normalize_url("HTTP://Example.COM/Path/"))
```

### Questions

1. What normalized URL is returned for the example?
2. What parts are dropped by this normalization?
3. Modify to preserve and sort query parameters instead of dropping them.

---

## Q295

### replace_in_file.py

```python
def replace_in_file(path, old, new, inplace=True):
    with open(path, "r", encoding="utf-8") as f:
        data = f.read()
    data2 = data.replace(old, new)
    if inplace:
        with open(path, "w", encoding="utf-8") as f:
            f.write(data2)
    return data2

if __name__ == "__main__":
    pass
```

### Questions

1. What risks exist when writing in-place?
2. How would you make this atomic to avoid partial writes?
3. Modify to write to a temp file and rename atomically.

---

## Q296

### rank_transform.py

```python
def rank_transform(arr):
    uniq = sorted(set(arr))
    ranks = {v: i+1 for i, v in enumerate(uniq)}
    return [ranks[v] for v in arr]

if __name__ == "__main__":
    print(rank_transform([40,10,20,40]))
```

### Questions

1. What transformed array is produced by the example?
2. How are ties handled?
3. Modify to return 0-based ranks and to handle streaming input.

---

## Q297

### sliding_window_find_sum.py

```python
def find_window_with_sum(nums, k, target):
    n = len(nums)
    if k > n:
        return -1
    s = sum(nums[:k])
    if s == target:
        return 0
    for i in range(k, n):
        s += nums[i] - nums[i-k]
        if s == target:
            return i - k + 1
    return -1

if __name__ == "__main__":
    print(find_window_with_sum([1,2,3,4,5], 3, 9))
```

### Questions

1. What index is returned for the example and why?
2. Explain why the sliding update is O(1) per step.
3. Modify to return all starting indices matching the target instead of first match.

---

## Q298

### prime_factors.py

```python
def prime_factors(n):
    i = 2
    out = []
    while i * i <= n:
        while n % i == 0:
            out.append(i)
            n //= i
        i += 1 if i == 2 else 2
    if n > 1:
        out.append(n)
    return out

if __name__ == "__main__":
    print(prime_factors(360))
```

### Questions

1. What is the prime factorization list for 360?
2. Why increment `i` by 1 then by 2 (skip even numbers after 2)?
3. Modify to return `(prime, exponent)` pairs instead of repeated primes.

---

## Q299

### dict_deep_update.py

```python
def deep_update(a, b):
    for k, v in b.items():
        if k in a and isinstance(a[k], dict) and isinstance(v, dict):
            deep_update(a[k], v)
        else:
            a[k] = v
    return a

if __name__ == "__main__":
    a = {"x":1, "y":{"z":2}}
    b = {"y":{"z":3, "w":4}, "k":5}
    print(deep_update(a, b))
```

### Questions

1. What is printed after updating `a` with `b`?
2. Does this function mutate `a` or create a new dict? Explain.
3. Modify to optionally return a new merged dict without mutating inputs.

---

## Q300

### list_rotate_inplace.py

```python
def rotate_inplace(a, k):
    n = len(a)
    if n == 0:
        return a
    k %= n
    def rev(l, i, j):
        while i < j:
            l[i], l[j] = l[j], l[i]
            i += 1; j -= 1
    rev(a, 0, n-1)
    rev(a, 0, k-1)
    rev(a, k, n-1)
    return a

if __name__ == "__main__":
    arr = [1,2,3,4,5]
    print(rotate_inplace(arr, 2))
```

### Questions

1. What list is produced for the example rotation by 2?
2. Explain why three reversals perform the rotation in-place.
3. Modify to perform a left-rotation by `k` instead of right-rotation.



## Q301

### palindrome_pairs.py

```python
def is_palindrome(s):
    return s == s[::-1]

def palindrome_pairs(words):
    res = []
    d = {w:i for i,w in enumerate(words)}
    for i, w in enumerate(words):
        for cut in range(len(w)+1):
            left, right = w[:cut], w[cut:]
            if is_palindrome(left) and right[::-1] in d and d[right[::-1]] != i:
                res.append((d[right[::-1]], i))
            if cut != len(w) and is_palindrome(right) and left[::-1] in d and d[left[::-1]] != i:
                res.append((i, d[left[::-1]]))
    return res

if __name__ == "__main__":
    print(palindrome_pairs(["bat","tab","cat"]))
```

Questions:

1. What pair(s) are returned for the sample list and why?
2. Explain purpose of `cut != len(w)` check.
3. Modify to avoid duplicate pairs and return unique pairs only.

---

## Q302

### find_cycle_length.py

```python
def cycle_length(next_fn, start):
    tortoise = next_fn(start)
    hare = next_fn(next_fn(start))
    while tortoise != hare:
        tortoise = next_fn(tortoise)
        hare = next_fn(next_fn(hare))
    # find mu
    mu = 0
    tortoise = start
    while tortoise != hare:
        tortoise = next_fn(tortoise); hare = next_fn(hare); mu += 1
    # find lambda
    lam = 1
    hare = next_fn(tortoise)
    while tortoise != hare:
        hare = next_fn(hare); lam += 1
    return mu, lam

if __name__ == "__main__":
    f = lambda x: (x*2)%7
    print(cycle_length(f, 1))
```

Questions:

1. What do `mu` and `lam` represent?
2. Why use two phases (meeting then locating start)?
3. Adapt `cycle_length` to work on lists using indices as `next_fn`.

---

## Q303

### kth_smallest_heap.py

```python
import heapq

def kth_smallest(nums, k):
    if k <= 0 or k > len(nums):
        return None
    heap = [-x for x in nums[:k]]
    heapq.heapify(heap)
    for x in nums[k:]:
        if -heap[0] > x:
            heapq.heapreplace(heap, -x)
    return -heap[0]

if __name__ == "__main__":
    print(kth_smallest([7,10,4,3,20,15], 3))
```

Questions:

1. What value is returned for the example?
2. Explain why a max-heap of size `k` is used.
3. Modify to return a sorted list of the k smallest values.

---

## Q304

### group_anagram_indices.py

```python
from collections import defaultdict

def group_anagram_indices(words):
    d = defaultdict(list)
    for i, w in enumerate(words):
        key = "".join(sorted(w))
        d[key].append(i)
    return list(d.values())

if __name__ == "__main__":
    print(group_anagram_indices(["eat","tea","tan","ate","nat","bat"]))
```

Questions:

1. What grouping of indices is produced for the example?
2. Why use indices instead of words? When is that useful?
3. Modify to group by normalized form ignoring punctuation and case.

---

## Q305

### round_robin_iterators.py

```python
from collections import deque

def round_robin(*iters):
    dq = deque(iters)
    while dq:
        it = dq.popleft()
        try:
            yield next(it)
            dq.append(it)
        except StopIteration:
            pass

if __name__ == "__main__":
    a = iter([1,2,3]); b = iter(['a','b'])
    print(list(round_robin(a,b)))
```

Questions:

1. What sequence is printed for the sample iterators?
2. Compare memory characteristics vs zipping with `itertools.zip_longest`.
3. Modify to skip empty iterables gracefully and accept an arbitrary iterable of iterables.

---

## Q306

### validate_ip.py

```python
def valid_ipv4(s):
    parts = s.split(".")
    if len(parts) != 4:
        return False
    for p in parts:
        if not p.isdigit() or not 0 <= int(p) <= 255 or (p[0]=='0' and len(p)>1):
            return False
    return True

if __name__ == "__main__":
    print(valid_ipv4("192.168.0.1"), valid_ipv4("256.0.0.1"))
```

Questions:

1. Which inputs in the example are valid and why?
2. Why reject segments with leading zeros? Is that always desirable?
3. Extend to validate IPv6 addresses (outline approach or implement basic check).

---

## Q307

### xor_linked_list_concept.py

```python
class XNode:
    def __init__(self, val, both=0):
        self.val = val
        self.both = both

# Note: This is a conceptual example; Python cannot get raw addresses safely.
def traverse_xor(start, fetch_by_addr):
    prev_addr = 0
    cur = start
    while cur:
        yield cur.val
        next_addr = prev_addr ^ cur.both
        prev_addr = id(cur)  # conceptual
        cur = fetch_by_addr(next_addr)

if __name__ == "__main__":
    print("Conceptual only")
```

Questions:

1. Explain the `both` field and how XOR linked lists work.
2. Why is this approach unsafe/unnatural in Python?
3. Propose a safe Python-compatible emulation of XOR linked list behavior.

---

## Q308

### partition_array_k_equal_sum.py

```python
def can_partition_k_subsets(nums, k):
    total = sum(nums)
    if total % k != 0:
        return False
    target = total // k
    nums.sort(reverse=True)
    if nums[0] > target:
        return False
    buckets = [0]*k
    def dfs(i):
        if i == len(nums):
            return len(set(buckets)) == 1
        v = nums[i]
        for j in range(k):
            if buckets[j]+v <= target:
                buckets[j]+=v
                if dfs(i+1):
                    return True
                buckets[j]-=v
            if buckets[j] == 0:
                break
        return False
    return dfs(0)

if __name__ == "__main__":
    print(can_partition_k_subsets([4,3,2,3,5,2,1], 4))
```

Questions:

1. What does the example indicate (True/False)?
2. Why sort descending before backtracking?
3. Modify to return the actual buckets when possible.

---

## Q309

### phone_number_mnemonics.py

```python
M = {"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
def mnemonics(digits):
    if not digits:
        return [""]
    res = [""]
    for d in digits:
        letters = M.get(d, d)
        res = [r + c for r in res for c in letters]
    return res

if __name__ == "__main__":
    print(mnemonics("23"))
```

Questions:

1. What mnemonics are returned for "23"?
2. How does complexity scale with digit length?
3. Modify to filter mnemonics by a provided dictionary of valid words.

---

## Q310

### detect_peak_element.py

```python
def find_peak(nums):
    lo, hi = 0, len(nums)-1
    while lo < hi:
        mid = (lo+hi)//2
        if nums[mid] > nums[mid+1]:
            hi = mid
        else:
            lo = mid+1
    return lo

if __name__ == "__main__":
    print(find_peak([1,2,3,1]))
```

Questions:

1. What index is returned in the example and why?
2. What assumptions about array shape are required?
3. Modify to return any peak index and explain correctness.

---

## Q311

### compare_two_files_stream.py

```python
def compare_files(a_path, b_path):
    with open(a_path, "rb") as fa, open(b_path, "rb") as fb:
        while True:
            a = fa.read(8192); b = fb.read(8192)
            if a != b:
                return False
            if not a:
                return True

if __name__ == "__main__":
    print("Usage: compare two files")
```

Questions:

1. Why read in blocks instead of whole file?
2. How does this behave for different file lengths?
3. Modify to return the offset of first difference when files differ.

---

## Q312

### permutations_with_repetition.py

```python
def permutations_with_repetition(items, r):
    if r == 0:
        return [[]]
    res = []
    for it in items:
        for tail in permutations_with_repetition(items, r-1):
            res.append([it] + tail)
    return res

if __name__ == "__main__":
    print(permutations_with_repetition([1,2], 3))
```

Questions:

1. What sequences are generated for the example?
2. How does this differ from `itertools.product`?
3. Modify to yield results lazily (generator).

---

## Q313

### longest_common_prefix_array.py

```python
def longest_common_prefix_strs(strs):
    if not strs:
        return ""
    min_s = min(strs); max_s = max(strs)
    for i, ch in enumerate(min_s):
        if ch != max_s[i]:
            return min_s[:i]
    return min_s

if __name__ == "__main__":
    print(longest_common_prefix_strs(["flower","flow","flight"]))
```

Questions:

1. Explain why comparing min and max works.
2. What prefix is returned for the example?
3. Modify to work on bytes arrays instead of strings.

---

## Q314

### majority_element_moore.py

```python
def majority_element(nums):
    count = 0
    candidate = None
    for x in nums:
        if count == 0:
            candidate = x
            count = 1
        elif candidate == x:
            count += 1
        else:
            count -= 1
    # optional verify candidate
    return candidate

if __name__ == "__main__":
    print(majority_element([3,3,4,2,3,3,5]))
```

Questions:

1. What does Moore's voting algorithm find?
2. Why might we need to verify the candidate afterward?
3. Modify to return None if no majority element (> n/2) exists.

---

## Q315

### validate_sudoku.py

```python
def is_valid_sudoku(board):
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    blocks = [set() for _ in range(9)]
    for r in range(9):
        for c in range(9):
            v = board[r][c]
            if v == '.': continue
            b = (r//3)*3 + c//3
            if v in rows[r] or v in cols[c] or v in blocks[b]:
                return False
            rows[r].add(v); cols[c].add(v); blocks[b].add(v)
    return True

if __name__ == "__main__":
    print("Provide 9x9 board to validate")
```

Questions:

1. Which duplicated placements would this detect?
2. Why compute block index `(r//3)*3 + c//3`?
3. Modify to also verify that all digits are between '1' and '9'.

---

## Q316

### word_break_dp.py

```python
def word_break(s, word_dict):
    n = len(s)
    dp = [False]*(n+1)
    dp[0] = True
    for i in range(1,n+1):
        for j in range(i):
            if dp[j] and s[j:i] in word_dict:
                dp[i] = True; break
    return dp[n]

if __name__ == "__main__":
    print(word_break("leetcode", {"leet","code"}))
```

Questions:

1. What does the example return and why?
2. Explain time complexity in worst case.
3. Modify to return one valid segmentation when possible.

---

## Q317

### evaluate_rpn.py

```python
def eval_rpn(tokens):
    stack = []
    for t in tokens:
        if t in {"+","-","*","/"}:
            b = stack.pop(); a = stack.pop()
            if t == "+": stack.append(a+b)
            elif t == "-": stack.append(a-b)
            elif t == "*": stack.append(a*b)
            else: stack.append(int(a/b))
        else:
            stack.append(int(t))
    return stack[0]

if __name__ == "__main__":
    print(eval_rpn(["2","1","+","3","*"]))
```

Questions:

1. What result is produced for the example tokens?
2. Why use `int(a/b)` for division behavior?
3. Modify to support unary operators and error handling.

---

## Q318

### product_except_self.py

```python
def product_except_self(nums):
    n = len(nums)
    res = [1]*n
    left = 1
    for i in range(n):
        res[i] = left
        left *= nums[i]
    right = 1
    for i in range(n-1,-1,-1):
        res[i] *= right
        right *= nums[i]
    return res

if __name__ == "__main__":
    print(product_except_self([1,2,3,4]))
```

Questions:

1. What output is returned for the sample array?
2. Why does this avoid using division?
3. Modify to handle zeros correctly and explain behavior.

---

## Q319

### repeated_substring_pattern.py

```python
def repeated_substring_pattern(s):
    return (s + s).find(s, 1) != len(s)

if __name__ == "__main__":
    print(repeated_substring_pattern("abab"))
```

Questions:

1. Why does `(s+s).find(s,1)` detect repetitions?
2. What does the function return for "aba"?
3. Modify to return the smallest repeating unit when present.

---

## Q320

### kth_largest_stream.py

```python
import heapq

class KthLargest:
    def __init__(self, k, nums):
        self.k = k
        self.heap = nums[:]
        heapq.heapify(self.heap)
        while len(self.heap) > k:
            heapq.heappop(self.heap)
    def add(self, val):
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]

if __name__ == "__main__":
    k = KthLargest(3, [4,5,8,2])
    print(k.add(3), k.add(5), k.add(10))
```

Questions:

1. What values are printed by successive `add` calls?
2. Explain invariant maintained by the heap.
3. Modify to support a removal operation of arbitrary elements.

---

## Q321

### zigzag_conversion.py

```python
def convert_zigzag(s, num_rows):
    if num_rows == 1 or num_rows >= len(s):
        return s
    rows = ['']*num_rows
    cur, step = 0, 1
    for ch in s:
        rows[cur] += ch
        if cur == 0: step = 1
        elif cur == num_rows-1: step = -1
        cur += step
    return ''.join(rows)

if __name__ == "__main__":
    print(convert_zigzag("PAYPALISHIRING", 3))
```

Questions:

1. What converted string is produced for the example?
2. Why handle `num_rows == 1` specially?
3. Modify to return the 2D row layout (list of strings) instead of concatenated result.

---

## Q322

### valid_palindrome_with_removal.py

```python
def valid_palindrome_after_removal(s):
    i, j = 0, len(s)-1
    while i < j:
        if s[i] != s[j]:
            a = s[i+1:j+1]; b = s[i:j]
            return a == a[::-1] or b == b[::-1]
        i += 1; j -= 1
    return True

if __name__ == "__main__":
    print(valid_palindrome_after_removal("abca"))
```

Questions:

1. What does the example return and why?
2. Explain why only two substring checks are needed on mismatch.
3. Modify to return the index of removal that makes it palindrome (or -1).

---

## Q323

### split_array_largest_sum.py

```python
def split_array(nums, m):
    def feasible(cap):
        cnt, cur = 1, 0
        for x in nums:
            if cur + x <= cap:
                cur += x
            else:
                cnt += 1; cur = x
        return cnt <= m
    lo, hi = max(nums), sum(nums)
    while lo < hi:
        mid = (lo+hi)//2
        if feasible(mid):
            hi = mid
        else:
            lo = mid+1
    return lo

if __name__ == "__main__":
    print(split_array([7,2,5,10,8], 2))
```

Questions:

1. What minimal largest subarray sum is returned for the example?
2. Explain role of binary search here.
3. Modify to return the actual partition boundaries.

---

## Q324

### unique_paths_with_obstacles.py

```python
def unique_paths_with_obstacles(obstacle_grid):
    if not obstacle_grid or obstacle_grid[0][0]==1: return 0
    r, c = len(obstacle_grid), len(obstacle_grid[0])
    dp = [0]*c
    dp[0] = 1
    for i in range(r):
        for j in range(c):
            if obstacle_grid[i][j] == 1:
                dp[j] = 0
            elif j > 0:
                dp[j] += dp[j-1]
    return dp[-1]

if __name__ == "__main__":
    grid = [[0,0,0],[0,1,0],[0,0,0]]
    print(unique_paths_with_obstacles(grid))
```

Questions:

1. What number of paths is returned for the sample grid?
2. Explain why single-row DP `dp[j]` suffices.
3. Modify to also return one example path when available.

---

## Q325

### merge_intervals_inplace.py

```python
def merge_intervals_inplace(intervals):
    if not intervals: return []
    intervals.sort()
    res = [intervals[0]]
    for s,e in intervals[1:]:
        last_s, last_e = res[-1]
        if s <= last_e:
            res[-1] = (last_s, max(last_e, e))
        else:
            res.append((s,e))
    return res

if __name__ == "__main__":
    print(merge_intervals_inplace([(1,4),(2,3),(5,6)]))
```

Questions:

1. What merged intervals are returned?
2. Why sort first and what about in-place memory?
3. Modify to merge intervals when they touch (e.g., (1,2) and (2,3)).

---

## Q326

### lowest_common_ancestor_bt.py

```python
class TreeNode:
    def __init__(self,val, left=None, right=None):
        self.val=val; self.left=left; self.right=right

def lca(root, p, q):
    if not root or root==p or root==q:
        return root
    left = lca(root.left, p,q)
    right = lca(root.right,p,q)
    return root if left and right else (left or right)

if __name__ == "__main__":
    print("Provide a tree; function returns LCA node")
```

Questions:

1. How does recursion determine LCA in a binary tree?
2. What is returned when one node is ancestor of the other?
3. Modify to return `None` if either `p` or `q` isn't present in the tree.

---

## Q327

### sum_root_to_leaf_numbers.py

```python
class Node:
    def __init__(self, val, left=None, right=None):
        self.val=val; self.left=left; self.right=right

def sum_numbers(root):
    def dfs(node, cur):
        if not node: return 0
        cur = cur*10 + node.val
        if not node.left and not node.right:
            return cur
        return dfs(node.left, cur) + dfs(node.right, cur)
    return dfs(root, 0)

if __name__ == "__main__":
    print(sum_numbers(Node(1, Node(2), Node(3))))
```

Questions:

1. What sum is returned for the example tree?
2. Explain how `cur` accumulates path numbers.
3. Modify to return the list of all root-to-leaf numbers as well.

---

## Q328

### simulate_calendar_conflicts.py

```python
def can_attend_all(events):
    events.sort()
    for i in range(1, len(events)):
        if events[i][0] < events[i-1][1]:
            return False
    return True

if __name__ == "__main__":
    print(can_attend_all([(0,30),(5,10),(15,20)]))
```

Questions:

1. What does the example return and why?
2. Why is sorting by start time sufficient?
3. Modify to return a conflicting pair when detected.

---

## Q329

### next_permutation.py

```python
def next_permutation(nums):
    i = len(nums)-2
    while i>=0 and nums[i]>=nums[i+1]:
        i-=1
    if i>=0:
        j = len(nums)-1
        while nums[j] <= nums[i]:
            j-=1
        nums[i], nums[j] = nums[j], nums[i]
    nums[i+1:] = reversed(nums[i+1:])
    return nums

if __name__ == "__main__":
    print(next_permutation([1,2,3]))
```

Questions:

1. What is produced for the example?
2. Explain why reversing the tail yields the next permutation.
3. Modify to return `False` and reset to smallest permutation when no next exists.

---

## Q330

### minimum_window_substring.py

```python
from collections import Counter

def min_window(s, t):
    need = Counter(t)
    missing = len(t)
    i = start = end = 0
    for j,ch in enumerate(s,1):
        if need[ch] > 0:
            missing -= 1
        need[ch] -= 1
        if missing == 0:
            while i < j and need[s[i]] < 0:
                need[s[i]] += 1; i += 1
            if end == 0 or j-i < end-start:
                start, end = i, j
            need[s[i]] += 1
            missing += 1
            i += 1
    return s[start:end]

if __name__ == "__main__":
    print(min_window("ADOBECODEBANC","ABC"))
```

Questions:

1. What minimal window is returned for the sample?
2. Explain role of `need` and `missing`.
3. Modify to return indices `(start,end)` instead of substring.

---

## Q331

### find_all_duplicates_array.py

```python
def find_duplicates(nums):
    res = []
    for i in range(len(nums)):
        idx = abs(nums[i]) - 1
        if nums[idx] < 0:
            res.append(idx+1)
        else:
            nums[idx] = -nums[idx]
    return res

if __name__ == "__main__":
    print(find_duplicates([4,3,2,7,8,2,3,1]))
```

Questions:

1. What duplicates are found in the example?
2. Why mutate array sign bits and what are caveats?
3. Modify to restore the array to original values before returning.

---

## Q332

### paint_fence_dp.py

```python
def num_ways(n, k):
    if n == 0: return 0
    same = 0
    diff = k
    for i in range(2, n+1):
        same, diff = diff, (same+diff)*(k-1)
    return same + diff

if __name__ == "__main__":
    print(num_ways(3,2))
```

Questions:

1. What does the function compute for paint fence problem?
2. Explain meanings of `same` and `diff`.
3. Modify to return sequence of number of ways for all lengths up to `n`.

---

## Q333

### reconstruct_itinerary.py

```python
from collections import defaultdict
import heapq

def find_itinerary(tickets):
    graph = defaultdict(list)
    for a,b in tickets:
        heapq.heappush(graph[a], b)
    route = []
    def visit(airport):
        while graph[airport]:
            visit(heapq.heappop(graph[airport]))
        route.append(airport)
    visit("JFK")
    return route[::-1]

if __name__ == "__main__":
    print(find_itinerary([["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]))
```

Questions:

1. What itinerary is produced for the example tickets?
2. Why use a heap to store destinations?
3. Modify to start from a configurable origin instead of "JFK".

---

## Q334

### score_of_parentheses.py

```python
def score_of_parentheses(s):
    stack = [0]
    for ch in s:
        if ch == '(':
            stack.append(0)
        else:
            v = stack.pop()
            stack[-1] += max(2*v, 1)
    return stack.pop()

if __name__ == "__main__":
    print(score_of_parentheses("()()"))
```

Questions:

1. What score does the example return and why?
2. Explain role of stack and `max(2*v,1)` expression.
3. Modify to validate parentheses and raise on invalid input.

---

## Q335

### island_perimeter.py

```python
def island_perimeter(grid):
    rows=len(grid); cols=len(grid[0])
    per=0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c]==1:
                per += 4
                if r>0 and grid[r-1][c]==1: per -=2
                if c>0 and grid[r][c-1]==1: per -=2
    return per

if __name__ == "__main__":
    g=[[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
    print(island_perimeter(g))
```

Questions:

1. What perimeter value is returned for the sample grid?
2. Why subtract 2 for each adjacent pair counted twice?
3. Modify to support multiple disjoint islands and return a dict island_id->perimeter.

---

## Q336

### binary_tree_serialization.py

```python
def serialize(root):
    vals=[]
    def dfs(node):
        if not node:
            vals.append("#"); return
        vals.append(str(node.val))
        dfs(node.left); dfs(node.right)
    dfs(root)
    return ",".join(vals)

def deserialize(s):
    vals = iter(s.split(","))
    def dfs():
        v = next(vals)
        if v == "#": return None
        node = TreeNode(int(v))
        node.left = dfs(); node.right = dfs()
        return node
    return dfs()
```

Questions:

1. Explain preorder serialization with `#` placeholders.
2. How does deserialization reconstruct shape unambiguously?
3. Modify to use level-order (BFS) serialization.

---

## Q337

### multiply_strings.py

```python
def multiply(num1, num2):
    if num1=="0" or num2=="0": return "0"
    m, n = len(num1), len(num2)
    res = [0]*(m+n)
    for i in range(m-1,-1,-1):
        for j in range(n-1,-1,-1):
            res[i+j+1] += int(num1[i])*int(num2[j])
    for k in range(len(res)-1,0,-1):
        res[k-1] += res[k]//10
        res[k] %= 10
    start = 0
    while start < len(res) and res[start]==0:
        start += 1
    return ''.join(map(str,res[start:]))

if __name__ == "__main__":
    print(multiply("123","456"))
```

Questions:

1. What product string is returned for the example?
2. Explain the convolution-like accumulation into `res`.
3. Modify to handle signed numbers with optional leading `-`.

---

## Q338

### longest_palindromic_substring_center.py

```python
def longest_palindrome(s):
    start = 0; maxlen = 0
    for i in range(len(s)):
        for j in (i,i+1):
            l, r = i, j
            while l>=0 and r<len(s) and s[l]==s[r]:
                if r-l+1 > maxlen:
                    start, maxlen = l, r-l+1
                l-=1; r+=1
    return s[start:start+maxlen]

if __name__ == "__main__":
    print(longest_palindrome("babad"))
```

Questions:

1. What is a possible longest palindromic substring for "babad"?
2. Why check both centers `i` and `i+1`?
3. Modify to use Manacher’s algorithm for linear time.

---

## Q339

### validate_bst_iterative.py

```python
def is_valid_bst(root):
    stack=[]; prev=None
    node=root
    while stack or node:
        while node:
            stack.append(node); node=node.left
        node=stack.pop()
        if prev is not None and node.val <= prev:
            return False
        prev = node.val
        node = node.right
    return True
```

Questions:

1. Explain why in-order traversal validates BST ordering.
2. What does `prev` store and why compare `<=`?
3. Modify to return the violating node pair when invalid.

---

## Q340

### count_islands_dfs.py

```python
def num_islands(grid):
    if not grid: return 0
    rows, cols = len(grid), len(grid[0])
    def dfs(r,c):
        if r<0 or c<0 or r>=rows or c>=cols or grid[r][c]=='0': return
        grid[r][c]='0'
        for dr,dc in [(1,0),(-1,0),(0,1),(0,-1)]: dfs(r+dr,c+dc)
    cnt=0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c]=='1':
                cnt+=1; dfs(r,c)
    return cnt

if __name__ == "__main__":
    g=[list("11110"),list("11010"),list("11000"),list("00000")]
    print(num_islands(g))
```

Questions:

1. What island count is returned for the example?
2. Why mark visited cells to avoid revisiting?
3. Modify to compute each island’s area as well.











Sure — here are **Q341–Q350** (complete). Each question includes a code file and three learner questions. No hints in titles and no emojis.

---

## Q341

### top_k_frequent.py

```python
from collections import Counter

def top_k_frequent(nums, k):
    """
    Return k most frequent elements using Counter.most_common.
    """
    if k <= 0:
        return []
    freq = Counter(nums)
    return [num for num, _ in freq.most_common(k)]

if __name__ == "__main__":
    print(top_k_frequent([1,1,1,2,2,3], 2))
```

### Questions

1. What list is returned for the example input and why?
2. Discuss time/space complexity when `k` is much smaller than the number of unique elements.
3. Modify to return the `k` least frequent elements instead.

---

## Q342

### serialize_deserialize_bst.py

```python
# Minimal TreeNode for demo
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val; self.left = left; self.right = right

def serialize(root):
    """Preorder serialize BST with 'N' as null marker."""
    vals = []
    def dfs(node):
        if not node:
            vals.append("N"); return
        vals.append(str(node.val))
        dfs(node.left); dfs(node.right)
    dfs(root)
    return ",".join(vals)

def deserialize(s):
    """Deserialize preorder string into a binary tree."""
    vals = iter(s.split(","))
    def dfs():
        v = next(vals)
        if v == "N":
            return None
        node = TreeNode(int(v))
        node.left = dfs(); node.right = dfs()
        return node
    return dfs()

if __name__ == "__main__":
    root = TreeNode(2, TreeNode(1), TreeNode(3))
    s = serialize(root)
    r2 = deserialize(s)
    print(s, r2.val, r2.left.val, r2.right.val)
```

### Questions

1. Explain how preorder plus null markers allows unambiguous reconstruction.
2. What are trade-offs vs level-order (BFS) serialization?
3. Modify `serialize` to use a compact binary format (outline steps).

---

## Q343

### longest_consecutive_sequence.py

```python
def longest_consecutive(nums):
    """
    Return length of longest consecutive elements sequence in O(n) time.
    """
    num_set = set(nums)
    best = 0
    for n in num_set:
        if n - 1 not in num_set:
            length = 1
            cur = n + 1
            while cur in num_set:
                length += 1
                cur += 1
            best = max(best, length)
    return best

if __name__ == "__main__":
    print(longest_consecutive([100,4,200,1,3,2]))
```

### Questions

1. What value does the example return and why?
2. Explain why checking `n - 1 not in num_set` keeps the algorithm O(n).
3. Modify to return the longest consecutive sequence (list) rather than its length.

---

## Q344

### product_array_except_self.py

```python
def product_except_self(nums):
    n = len(nums)
    res = [1] * n
    left = 1
    for i in range(n):
        res[i] = left
        left *= nums[i]
    right = 1
    for i in range(n-1, -1, -1):
        res[i] *= right
        right *= nums[i]
    return res

if __name__ == "__main__":
    print(product_except_self([1,2,3,4]))
```

### Questions

1. What output does the example produce and why does it avoid division?
2. How do prefix and suffix products build the result?
3. Modify to explicitly handle zeros and explain expected output semantics when zeros are present.

---

## Q345

### minimum_window_substring.py

```python
from collections import Counter

def min_window(s, t):
    if not t or not s:
        return ""
    need = Counter(t)
    missing = len(t)
    left = start = end = 0
    for right, ch in enumerate(s, 1):
        if need[ch] > 0:
            missing -= 1
        need[ch] -= 1
        while missing == 0:
            if end == 0 or right - left < end - start:
                start, end = left, right
            need[s[left]] += 1
            if need[s[left]] > 0:
                missing += 1
            left += 1
    return s[start:end]

if __name__ == "__main__":
    print(min_window("ADOBECODEBANC", "ABC"))
```

### Questions

1. What minimal window substring does the example return and why?
2. Explain roles of `need` and `missing`.
3. Modify to return window indices `(start, end)` instead of the substring.

---

## Q346

### kth_smallest_in_matrix.py

```python
import heapq

def kth_smallest(matrix, k):
    """
    matrix is n x n with rows and cols sorted ascending.
    Use min-heap seeded with first element of each row.
    """
    n = len(matrix)
    heap = []
    for r in range(min(n, k)):
        heapq.heappush(heap, (matrix[r][0], r, 0))
    num = None
    for _ in range(k):
        num, r, c = heapq.heappop(heap)
        if c + 1 < n:
            heapq.heappush(heap, (matrix[r][c+1], r, c+1))
    return num

if __name__ == "__main__":
    m = [[1,5,9],[10,11,13],[12,13,15]]
    print(kth_smallest(m, 8))
```

### Questions

1. What value does the example return and why?
2. Why push at most `min(n,k)` rows initially?
3. Outline how to solve this via binary search on values instead of a heap.

---

## Q347

### word_ladder_bfs.py

```python
from collections import deque

def ladder_length(begin, end, word_list):
    word_set = set(word_list)
    if end not in word_set:
        return 0
    q = deque([(begin, 1)])
    visited = {begin}
    while q:
        word, steps = q.popleft()
        if word == end:
            return steps
        for i in range(len(word)):
            for ch in "abcdefghijklmnopqrstuvwxyz":
                nxt = word[:i] + ch + word[i+1:]
                if nxt in word_set and nxt not in visited:
                    visited.add(nxt)
                    q.append((nxt, steps+1))
    return 0

if __name__ == "__main__":
    print(ladder_length("hit", "cog", ["hot","dot","dog","lot","log","cog"]))
```

### Questions

1. What length does the example produce and what does it represent?
2. Why is BFS appropriate here instead of DFS?
3. Modify to return one transformation path (sequence of words) from `begin` to `end`.

---

## Q348

### max_subarray_kadane.py

```python
def max_subarray(nums):
    max_ending = max_so_far = nums[0]
    for x in nums[1:]:
        max_ending = max(x, max_ending + x)
        max_so_far = max(max_so_far, max_ending)
    return max_so_far

if __name__ == "__main__":
    print(max_subarray([-2,1,-3,4,-1,2,1,-5,4]))
```

### Questions

1. What maximum subarray sum is returned and which subarray yields it?
2. Explain intuition behind Kadane’s algorithm.
3. Modify to return start and end indices of the maximum-sum subarray.

---

## Q349

### find_peak_element.py

```python
def find_peak(nums):
    """
    Find a peak index (element greater than neighbors) in O(log n) time.
    """
    lo, hi = 0, len(nums) - 1
    while lo < hi:
        mid = (lo + hi) // 2
        if nums[mid] > nums[mid + 1]:
            hi = mid
        else:
            lo = mid + 1
    return lo

if __name__ == "__main__":
    print(find_peak([1,2,3,1]))
```

### Questions

1. What index is returned for the example and why is it a peak?
2. Why does comparing `nums[mid]` and `nums[mid+1]` give O(log n) performance?
3. Modify to return all peak indices in the array (O(n) approach).

---

## Q350

### smallest_missing_positive.py

```python
def first_missing_positive(nums):
    """
    Find the smallest missing positive integer in O(n) time and O(1) extra space.
    Mutates input array.
    """
    n = len(nums)
    for i in range(n):
        while 1 <= nums[i] <= n and nums[nums[i]-1] != nums[i]:
            j = nums[i] - 1
            nums[i], nums[j] = nums[j], nums[i]
    for i in range(n):
        if nums[i] != i + 1:
            return i + 1
    return n + 1

if __name__ == "__main__":
    print(first_missing_positive([3,4,-1,1]))
```

### Questions

1. What value does the example return and why?
2. Explain how cyclic placement yields O(n) time and O(1) space.
3. Modify to avoid mutating the input (describe extra time/space cost).

---


## Q351

### prime_sieve.py

```python
def sieve(n):
    """
    Return list of primes up to n (inclusive).
    """
    if n < 2:
        return []
    is_prime = [True] * (n + 1)
    is_prime[0] = False
    is_prime[1] = False
    p = 2
    while p * p <= n:
        if is_prime[p]:
            for multiple in range(p*p, n+1, p):
                is_prime[multiple] = False
        p += 1
    primes = []
    for i in range(2, n+1):
        if is_prime[i]:
            primes.append(i)
    return primes

if __name__ == "__main__":
    print(sieve(30))
```

### Questions

1. What output does `sieve(30)` produce?
2. Explain why the inner loop starts at `p*p`.
3. Modify to use a boolean array memory optimization (only odd numbers).

---

## Q352

### bubble_sort_verbose.py

```python
def bubble_sort(arr):
    """
    Simple bubble sort that returns a new sorted list.
    """
    n = len(arr)
    out = arr[:]  # copy to avoid mutation
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if out[j] > out[j+1]:
                out[j], out[j+1] = out[j+1], out[j]
                swapped = True
        if not swapped:
            break
    return out

if __name__ == "__main__":
    data = [5,3,8,4,2]
    print("original:", data)
    print("sorted:", bubble_sort(data))
```

### Questions

1. Is `bubble_sort` stable and why?
2. What is the time complexity in worst case?
3. Modify to sort in-place and return `None` (Python convention).

---

## Q353 (buggy)

### find_peak_index.py

```python
def find_peak_index(nums):
    """
    Return index of a peak (element greater than neighbors). Assumes len(nums) >= 1.
    """
    if not nums:
        return -1
    for i in range(1, len(nums)-1):
        if nums[i] > nums[i-1] and nums[i] > nums[i+1]:
            return i
    # fallback: return last index
    return len(nums)
    
if __name__ == "__main__":
    print(find_peak_index([1,3,2,4,1]))
```

### Questions

1. Identify the bug(s) and what happens on edge inputs.
2. Fix the fallback to return a valid index when no strict middle peak exists.
3. Modify to return all peak indices, not just the first.

---

## Q354 (buggy)

### unique_sorted.py

```python
def unique_sorted(seq):
    """
    Return sorted unique items while preserving input order.
    """
    seen = set()
    out = []
    for x in seq:
        if x not in seen:
            out.append(x)
    return out.sort()

if __name__ == "__main__":
    print(unique_sorted([3,1,2,1,3,4]))
```

### Questions

1. Explain why this function fails at runtime.
2. Provide a corrected implementation that returns a list with duplicates removed preserving first occurrence.
3. Also implement a version that returns sorted unique items.

---

## Q355

### binary_search_iterative.py

```python
def binary_search(a, target):
    """
    Return index of target in sorted list a, else -1.
    """
    lo, hi = 0, len(a) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if a[mid] == target:
            return mid
        elif a[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1

if __name__ == "__main__":
    print(binary_search([1,2,4,5,7], 5))
```

### Questions

1. What index does the example print and why?
2. Explain why `(lo+hi)//2` is safe here (or when it's not).
3. Modify to return the insertion point if not found.

---

## Q356 (buggy)

### factorial_recursive.py

```python
def fact(n):
    # recursive factorial
    if n == 0:
        return 1
    return n * fact(n - 1)

if __name__ == "__main__":
    print(fact(-1))
```

### Questions

1. What problem occurs when `fact(-1)` is called?
2. Add input validation to raise `ValueError` for negative inputs.
3. Provide an iterative version that avoids recursion depth limits.

---

## Q357

### flatten_matrix.py

```python
def flatten_matrix(mat):
    """
    Convert 2D matrix to flat list row-major.
    """
    out = []
    for row in mat:
        for val in row:
            out.append(val)
    return out

if __name__ == "__main__":
    m = [[1,2,3],[4,5,6]]
    print(flatten_matrix(m))
```

### Questions

1. How would you flatten in column-major order instead?
2. Write one-line comprehension version of `flatten_matrix`.
3. Modify to handle ragged matrices (rows of different lengths) gracefully.

---

## Q358 (buggy)

### find_missing_number.py

```python
def missing_num(nums):
    """
    Given numbers 0..n with one missing, find missing number.
    """
    n = len(nums)
    total = n * (n + 1) // 2
    return total - sum(nums)

if __name__ == "__main__":
    print(missing_num([0,1,3]))
```

### Questions

1. Explain the off-by-one mistake in this implementation.
2. Correct the function and show output for sample.
3. Provide XOR-based implementation that avoids overflow concerns.

---

## Q359

### readline_tail.py

```python
from collections import deque

def tail(path, n=10):
    with open(path, "r", encoding="utf-8") as f:
        dq = deque(f, maxlen=n)
    return [line.rstrip("\n") for line in dq]

if __name__ == "__main__":
    # Create a sample file and demonstrate
    with open("sample.txt", "w") as f:
        for i in range(1,21):
            f.write(f"line {i}\n")
    print(tail("sample.txt", 5))
```

### Questions

1. Why is `deque` with `maxlen` efficient for tail?
2. What happens if file has fewer than `n` lines?
3. Modify to implement `tail -f` style following (streaming) behavior.

---

## Q360 (buggy)

### parse_csv_simple.py

```python
def parse_csv_line(line):
    """
    Very naive CSV parser splitting on commas.
    """
    return line.split(",")

def parse_csv(path):
    rows = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            rows.append(parse_csv_line(line.strip()))
    return rows

if __name__ == "__main__":
    with open("csv.txt", "w") as f:
        f.write('a,"b,c",d\n')
    print(parse_csv("csv.txt"))
```

### Questions

1. What is wrong with this CSV parser for quoted fields?
2. Replace `parse_csv_line` with one based on Python's `csv` module.
3. Explain cases where using `csv` with different dialects is important.

---

## Q361

### spiral_matrix_coords.py

```python
def spiral_coords(n):
    """
    Yield coordinates (r,c) for an n x n matrix in spiral order.
    """
    top, left = 0, 0
    bottom, right = n - 1, n - 1
    out = []
    while left <= right and top <= bottom:
        # left->right
        for c in range(left, right+1):
            out.append((top, c))
        top += 1
        # top->bottom
        for r in range(top, bottom+1):
            out.append((r, right))
        right -= 1
        if top <= bottom:
            for c in range(right, left-1, -1):
                out.append((bottom, c))
            bottom -= 1
        if left <= right:
            for r in range(bottom, top-1, -1):
                out.append((r, left))
            left += 1
    return out

if __name__ == "__main__":
    print(spiral_coords(3))
```

### Questions

1. Verify that `spiral_coords(3)` produces 9 unique coordinates.
2. Modify to accept rectangular `rows, cols` instead of square `n`.
3. Use the coordinates to produce a filled spiral matrix of numbers 1..n*n.

---

## Q362 (buggy)

### pow_mod.py

```python
def pow_mod(x, y, mod):
    """
    Compute (x ** y) % mod with fast exponentiation.
    """
    res = 1
    x = x % mod
    while y > 0:
        if y % 2 == 0:
            res = (res * x) % mod
        x = (x * x) % mod
        y //= 2
    return res

if __name__ == "__main__":
    print(pow_mod(2,10,1000))
```

### Questions

1. Identify the logic bug in the fast exponentiation loop.
2. Fix the algorithm and explain why the fix works.
3. Add handling for negative exponents (if mod is prime and inverse exists).

---

## Q363

### lru_cache_simple.py

```python
from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key):
        if key not in self.cache:
            return None
        val = self.cache.pop(key)
        self.cache[key] = val
        return val

    def put(self, key, value):
        if key in self.cache:
            self.cache.pop(key)
        elif len(self.cache) >= self.capacity:
            self.cache.popitem(last=False)
        self.cache[key] = value

if __name__ == "__main__":
    c = LRUCache(2)
    c.put(1, 1); c.put(2,2)
    print(c.get(1))
    c.put(3,3)
    print(c.get(2))
```

### Questions

1. What values are printed by the example?
2. Why does `get` re-insert the key at the end?
3. Implement `delete(key)` and `clear()` methods.

---

## Q364 (buggy)

### json_safe_load.py

```python
import json

def safe_load(s):
    try:
        return json.loads(s)
    except json.JSONDecodeError:
        return {}

if __name__ == "__main__":
    print(safe_load("null"))
```

### Questions

1. Why returning `{}` on decode error can be misleading?
2. Improve `safe_load` to optionally raise on invalid input and support a default value parameter.
3. Show what `json.loads("null")` actually returns and explain.

---

## Q365

### fibonacci_iter.py

```python
def fib(n):
    """
    Return nth Fibonacci number (0-indexed) using iteration.
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

if __name__ == "__main__":
    print([fib(i) for i in range(10)])
```

### Questions

1. What sequence is printed for first 10 Fibonacci numbers?
2. Modify to memoize results for repeated calls.
3. Provide a generator yielding infinite Fibonacci sequence.

---

## Q366 (buggy)

### swap_pairs_linkedlist.py

```python
class Node:
    def __init__(self, v, nxt=None):
        self.val = v; self.next = nxt

def swap_pairs(head):
    """
    Swap every two adjacent nodes in a singly linked list (returns new head).
    """
    dummy = Node(0, head)
    prev = dummy
    while prev.next and prev.next.next:
        a = prev.next; b = a.next
        prev.next = b
        a.next = b.next
        b.next = a
        prev = a
    return dummy.next

if __name__ == "__main__":
    # build sample 1->2->3
    h = Node(1, Node(2, Node(3)))
    res = swap_pairs(h)
    p = res
    while p:
        print(p.val)
        p = p.next
```

### Questions

1. Does this correctly handle odd-length lists? Test with 3 nodes.
2. Explain why it uses a dummy node.
3. Modify to swap values instead of nodes (in-place values only).

---

## Q367

### is_palindrome_permutation.py

```python
from collections import Counter

def can_form_palindrome(s):
    """
    Return True if any permutation of s is a palindrome (ignoring spaces).
    """
    s = s.replace(" ", "").lower()
    cnt = Counter(s)
    odd = sum(1 for v in cnt.values() if v % 2)
    return odd <= 1

if __name__ == "__main__":
    print(can_form_palindrome("Tact Coa"))  # "taco cat"
```

### Questions

1. Why does `Tact Coa` return True?
2. Modify to ignore punctuation and non-alphanumeric characters.
3. Write function to actually produce one palindrome permutation when possible.

---

## Q368 (buggy)

### median_running.py

```python
import heapq

class RunningMedian:
    def __init__(self):
        self.lo = []  # max-heap via negation
        self.hi = []  # min-heap

    def add(self, x):
        if not self.lo or x <= -self.lo[0]:
            heapq.heappush(self.lo, x)
        else:
            heapq.heappush(self.hi, x)
        # rebalance
        if len(self.lo) > len(self.hi) + 1:
            heapq.heappush(self.hi, heapq.heappop(self.lo))
        elif len(self.hi) > len(self.lo):
            heapq.heappush(self.lo, -heapq.heappop(self.hi))

    def median(self):
        if not self.lo:
            return None
        if len(self.lo) > len(self.hi):
            return -self.lo[0]
        return (-self.lo[0] + self.hi[0]) / 2.0

if __name__ == "__main__":
    rm = RunningMedian()
    for x in [5,2,3,4,1,6]:
        rm.add(x)
        print("median now:", rm.median())
```

### Questions

1. Identify the bug when pushing/popping between heaps.
2. Fix the push/pop negation errors.
3. Explain invariants of both heaps in correct implementation.

---

## Q369

### graph_dfs_recursive.py

```python
def has_path_dfs(graph, src, dst, visited=None):
    if visited is None:
        visited = set()
    if src == dst:
        return True
    visited.add(src)
    for nb in graph.get(src, []):
        if nb not in visited:
            if has_path_dfs(graph, nb, dst, visited):
                return True
    return False

if __name__ == "__main__":
    g = {"A":["B","C"], "B":["D"], "C":[], "D":[]}
    print(has_path_dfs(g, "A", "D"))
```

### Questions

1. What does the example return?
2. Convert this to an iterative DFS using an explicit stack.
3. Explain why `visited` default should be `None` rather than `set()`.

---

## Q370 (buggy)

### url_join_simple.py

```python
from urllib.parse import urljoin

def join_paths(base, *parts):
    url = base
    for p in parts:
        url = urljoin(url + "/", p)
    return url

if __name__ == "__main__":
    print(join_paths("https://example.com/api", "/v1/users"))
```

### Questions

1. Show a case where this `join_paths` produces an incorrect URL (loses path when part begins with slash).
2. Fix `join_paths` to correctly handle leading/trailing slashes.
3. Add support to preserve query strings in the final part.

---

## Q371

### is_rotation_by_k.py

```python
def is_rotation(s, t):
    """
    Check if t is rotation of s.
    """
    if len(s) != len(t):
        return False
    return t in (s + s)

if __name__ == "__main__":
    print(is_rotation("waterbottle", "erbottlewat"))
```

### Questions

1. Why does `s+s` trick correctly identify rotations?
2. Find rotation offset k when rotation exists.
3. Modify to run in O(n) time without creating `s+s` (KMP-based).

---

## Q372 (buggy)

### balanced_parentheses.py

```python
def is_balanced(s):
    stack = []
    pairs = {')':'(', ']':'[', '}':'{'}
    for ch in s:
        if ch in pairs.values():
            stack.append(ch)
        elif ch in pairs:
            if not stack and stack.pop() != pairs[ch]:
                return False
        # ignore other chars
    return not stack

if __name__ == "__main__":
    print(is_balanced("{[()]}"))
```

### Questions

1. Identify the bug in the `elif` branch and how it misbehaves.
2. Fix the logic for checking matching parentheses.
3. Extend to ignore characters inside string literals (single/double quotes).

---

## Q373

### topological_sort_dag.py

```python
from collections import defaultdict, deque

def topo_sort(edges):
    g = defaultdict(list)
    indeg = defaultdict(int)
    nodes = set()
    for u, v in edges:
        g[u].append(v)
        indeg[v] += 1
        nodes.add(u); nodes.add(v)
    q = deque([n for n in nodes if indeg.get(n,0) == 0])
    res = []
    while q:
        n = q.popleft()
        res.append(n)
        for nb in g[n]:
            indeg[nb] -= 1
            if indeg[nb] == 0:
                q.append(nb)
    if len(res) != len(nodes):
        raise ValueError("cycle detected")
    return res

if __name__ == "__main__":
    print(topo_sort([("a","b"),("b","c")]))
```

### Questions

1. What order does `topo_sort` return for simple DAG?
2. Modify to return multiple valid topological orders (outline approach).
3. Update to detect and return one cycle path instead of raising.

---

## Q374 (buggy)

### split_on_delim.py

```python
def split_once(s, delim):
    idx = s.find(delim)
    if idx == -1:
        return s, ""
    return s[:idx], s[idx+len(delim):]

if __name__ == "__main__":
    print(split_once("a=b=c", "="))
```

### Questions

1. Is there any bug here? Test with delim at start or end.
2. Implement `rsplit_once` that splits from the right (last occurrence).
3. Modify to trim both returned parts.

---

## Q375

### group_adjacent.py

```python
def group_adjacent(seq, keyfunc=lambda x: x):
    out = []
    cur_key = None
    cur_list = []
    for x in seq:
        k = keyfunc(x)
        if cur_list and k != cur_key:
            out.append(cur_list)
            cur_list = []
        cur_list.append(x)
        cur_key = k
    if cur_list:
        out.append(cur_list)
    return out

if __name__ == "__main__":
    print(group_adjacent([1,1,2,2,2,3,1,1]))
```

### Questions

1. What grouping does the example produce?
2. How is this different from grouping ignoring adjacency?
3. Modify to return `(key, group)` pairs instead of just groups.

---

## Q376 (buggy)

### parse_key_value_file.py

```python
def parse_kv(path):
    d = {}
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            if not line.strip() or line.strip().startswith("#"):
                continue
            if "=" in line:
                k, v = line.split("=", 1)
                d[k.strip()] = v.strip()
    return d

if __name__ == "__main__":
    with open("cfg.txt", "w") as f:
        f.write('key = "value=with=equals"\n')
    print(parse_kv("cfg.txt"))
```

### Questions

1. Does this correctly parse values that include `=`? Explain.
2. How to support quoted values and whitespace robustly?
3. Provide an improved parser that handles quoted values (outline or implement).

---

## Q377

### running_sum_generator.py

```python
def running_sum(seq):
    total = 0
    for x in seq:
        total += x
        yield total

if __name__ == "__main__":
    print(list(running_sum([1,2,3,4])))
```

### Questions

1. What list is printed for the example?
2. Modify to accept an initial value offset.
3. Implement a class that supports `.add(x)` and `.current()` returning running sum.

---

## Q378

### replace_nth_occurrence.py

```python
def replace_nth(s, old, new, n):
    idx = -1
    for _ in range(n):
        idx = s.find(old, idx+1)
        if idx == -1:
            return s
    return s[:idx] + new + s[idx+len(old):]

if __name__ == "__main__":
    print(replace_nth("a b a b a", "a", "X", 2))
```

### Questions

1. What string is produced by the example?
2. Modify to replace the nth occurrence from the end.
3. Ensure function handles overlapping `old` substrings correctly (discuss trade-offs).

---

## Q379 (buggy)

### cache_decorator.py

```python
def memoize(fn):
    cache = {}
    def wrapper(*args):
        if args in cache:
            return cache[args]
        res = fn(*args)
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

1. Is this `memoize` safe across functions with mutable args? Explain.
2. Modify `memoize` to support keyword arguments as well.
3. Add a simple `maxsize` eviction strategy (LRU) to the decorator.

---

## Q380

### find_pairs_sum_k.py

```python
def find_pairs(nums, k):
    seen = set()
    res = set()
    for x in nums:
        if k - x in seen:
            res.add(tuple(sorted((x, k-x))))
        seen.add(x)
    return [list(p) for p in res]

if __name__ == "__main__":
    print(find_pairs([1,2,3,2,4], 4))
```

### Questions

1. What pairs are returned for the example?
2. Modify to return indices instead of values.
3. handle case with duplicates and count distinct pairs including positions.

---

## Q381

### ensure_dir.py

```python
import os

def ensure_dir(path):
    if not os.path.exists(path):
        os.makedirs(path, exist_ok=True)
    elif not os.path.isdir(path):
        raise ValueError(f"{path} exists and is not a directory")

if __name__ == "__main__":
    ensure_dir("tmp/example")
    print("done")
```

### Questions

1. What happens if `path` exists as a file?
2. Explain `exist_ok=True` usefulness.
3. Modify to set directory permissions after creation.

---

## Q382 (buggy)

### read_utf8_safe.py

```python
def read_utf8(path):
    with open(path, "rb") as f:
        data = f.read()
    return data.decode("utf-8")

if __name__ == "__main__":
    with open("bin.txt", "wb") as f:
        f.write(b'\xff\xfe')
    print(read_utf8("bin.txt"))
```

### Questions

1. What happens when decoding invalid UTF-8 bytes?
2. Change `read_utf8` to use `errors="replace"` to avoid exceptions.
3. Discuss when `errors="strict"` is preferable.

---

## Q383

### longest_common_prefix.py

```python
def longest_common_prefix(strs):
    if not strs:
        return ""
    prefix = strs[0]
    for s in strs[1:]:
        while not s.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix

if __name__ == "__main__":
    print(longest_common_prefix(["flower","flow","flight"]))
```

### Questions

1. What result does the example print?
2. Explain worst-case complexity and how to improve it.
3. Modify to use binary search on prefix length.

---

## Q384

### sparse_dot.py

```python
def sparse_dot(A, B):
    """
    Multiply sparse matrices represented as dict (i,j) -> value.
    """
    res = {}
    B_by_row = {}
    for (k, j), v in B.items():
        B_by_row.setdefault(k, []).append((j, v))
    for (i, k), va in A.items():
        for j, vb in B_by_row.get(k, []):
            res[(i, j)] = res.get((i, j), 0) + va * vb
    return res

if __name__ == "__main__":
    A = {(0,0):1, (1,0):2}
    B = {(0,1):3}
    print(sparse_dot(A,B))
```

### Questions

1. Explain how grouping B by row improves performance.
2. Modify to accept and return CSR-like compressed sparse row format.
3. Add support for sparse vector (1D) times dense matrix multiplication.

---

## Q385 (buggy)

### tail_file.py

```python
def tail(path, n=10):
    with open(path, "r", encoding="utf-8") as f:
        f.seek(0, 2)
        size = f.tell()
        block = 1024
        data = ""
        while len(data.splitlines()) <= n and size > 0:
            size -= block
            if size < 0:
                block += size
                size = 0
            f.seek(size)
            data = f.read() + data
        return data.splitlines()[-n:]

if __name__ == "__main__":
    with open("t.txt", "w") as f:
        for i in range(1,21):
            f.write(f"{i}\n")
    print(tail("t.txt", 5))
```

### Questions

1. Identify boundary bugs when `size - block` becomes negative.
2. Fix the logic to correctly adjust seek and block lengths.
3. Explain why reading from file end in blocks is efficient for large files.

---

## Q386

### clamp_values.py

```python
def clamp_list(nums, low, high):
    return [low if x < low else high if x > high else x for x in nums]

if __name__ == "__main__":
    print(clamp_list([1, -2, 5, 10], 0, 6))
```

### Questions

1. What output does the example produce?
2. Implement in-place modification version.
3. Modify to accept per-element min/max functions instead of scalars.

---

## Q387 (buggy)

### normalize_whitespace.py

```python
import re

def normalize_ws(s):
    return re.sub(r'\s+', ' ', s)

if __name__ == "__main__":
    print(f"'{normalize_ws('  hello \n\t world  ')}'")
```

### Questions

1. Why might the result include leading/trailing space unexpectedly?
2. Fix to also `strip()` leading/trailing whitespace after normalization.
3. Modify to preserve single newlines while collapsing other whitespace.

---

## Q388

### find_local_extrema.py

```python
def local_extrema(nums):
    out = []
    n = len(nums)
    for i in range(1, n-1):
        if nums[i] > nums[i-1] and nums[i] > nums[i+1]:
            out.append((i, nums[i], 'max'))
        if nums[i] < nums[i-1] and nums[i] < nums[i+1]:
            out.append((i, nums[i], 'min'))
    return out

if __name__ == "__main__":
    print(local_extrema([1,3,2,4,3,5]))
```

### Questions

1. What extrema are identified in the example?
2. How would you treat plateaus (equal neighbors)?
3. Modify to optionally include endpoints as extrema.

---

## Q389

### group_by_key.py

```python
from collections import defaultdict

def group_by(items, keyfunc):
    out = defaultdict(list)
    for it in items:
        out[keyfunc(it)].append(it)
    return dict(out)

if __name__ == "__main__":
    people = [{"name":"A","age":20},{"name":"B","age":30},{"name":"C","age":20}]
    print(group_by(people, lambda p: p["age"]))
```

### Questions

1. What grouping is produced for the sample?
2. Modify to accept an optional `valuefunc` to store transformed values.
3. Implement a streaming version that yields groups as they become full (given a max group size).

---

## Q390 (buggy)

### file_tail_deque.py

```python
from collections import deque

def tail(path, n=10):
    dq = deque()
    with open(path, "r", encoding="utf-8") as f:
        for i, line in enumerate(f):
            if i > n:
                dq.append(line)
            else:
                dq.append(line)
    return [l.rstrip("\n") for l in dq[-n:]]

if __name__ == "__main__":
    with open("tt.txt", "w") as f:
        for i in range(10):
            f.write(f"{i}\n")
    print(tail("tt.txt", 3))
```

### Questions

1. What is wrong/inefficient with this implementation?
2. Provide corrected efficient version using `deque(f, maxlen=n)`.
3. Explain memory trade-offs compared to reading entire file.

---

## Q391

### sliding_window_average.py

```python
from collections import deque

def windowed_average(seq, k):
    if k <= 0:
        raise ValueError("k must be positive")
    dq = deque()
    s = 0
    for i, x in enumerate(seq):
        dq.append(x); s += x
        if i >= k:
            s -= dq.popleft()
        if i >= k-1:
            yield s / k

if __name__ == "__main__":
    print(list(windowed_average([1,2,3,4,5], 3)))
```

### Questions

1. What averages are produced for the example?
2. How does deque maintain O(1) per-step time?
3. Modify to handle variable window size per position.

---

## Q392 (buggy)

### multiply_strings_simple.py

```python
def multiply(num1, num2):
    if num1=="0" or num2=="0": return 0
    m, n = len(num1), len(num2)
    res = [0]*(m+n)
    for i in range(m-1,-1,-1):
        for j in range(n-1,-1,-1):
            res[i+j+1] += int(num1[i])*int(num2[j])
    for k in range(len(res)-1,0,-1):
        res[k-1] += res[k]//10
        res[k] %= 10
    start = 0
    while start < len(res) and res[start]==0:
        start += 1
    return ''.join(map(str,res[start:]))

if __name__ == "__main__":
    print(multiply("123","456"))
```

### Questions

1. Identify the mistake when one multiplicand is "0".
2. Fix to return string "0" in that case and discuss other edge cases.
3. Modify to support negative numbers.

---

## Q393

### find_duplicates_in_file.py

```python
def find_duplicates(path):
    seen = set()
    dups = set()
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.rstrip("\n")
            if line in seen:
                dups.add(line)
            else:
                seen.add(line)
    return sorted(dups)

if __name__ == "__main__":
    with open("dups.txt", "w") as f:
        f.write("a\nb\na\nc\nb\n")
    print(find_duplicates("dups.txt"))
```

### Questions

1. What does the function return for the sample file?
2. How does memory scale with unique lines?
3. Modify to stream duplicates to an output file instead of returning them.

---

## Q394

### find_subsequence_indices.py

```python
def is_subsequence_indices(s, t):
    """
    Return list of indices in t where characters of s are matched in order, or None.
    """
    it = iter(enumerate(t))
    indices = []
    for ch in s:
        for i, c in it:
            if c == ch:
                indices.append(i)
                break
        else:
            return None
    return indices

if __name__ == "__main__":
    print(is_subsequence_indices("ace", "abcde"))
```

### Questions

1. What list is returned in the example?
2. Explain why using a single iterator `it` works for ordering.
3. Modify to return all possible index sequences (combinatorial).

---

## Q395 (buggy)

### luhn_check.py

```python
def luhn_checksum(card_number):
    digits = [int(d) for d in str(card_number)][::-1]
    total = 0
    for i, d in enumerate(digits):
        if i % 2 == 1:
            d *= 2
            if d > 9:
                d -= 9
        total += d
    return total % 10 == 0

if __name__ == "__main__":
    print(luhn_checksum("4532015112830366"))
```

### Questions

1. Identify potential issue when card_number contains spaces or dashes.
2. Add validation to strip non-digit characters and raise on non-digit presence.
3. Provide function to compute check digit for a partial number.

---

## Q396

### parse_ini.py

```python
def parse_ini(path):
    cfg = {}
    section = None
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith(";") or line.startswith("#"):
                continue
            if line.startswith("[") and line.endswith("]"):
                section = line[1:-1].strip()
                cfg[section] = {}
            elif "=" in line and section is not None:
                k, v = line.split("=", 1)
                cfg[section][k.strip()] = v.strip()
    return cfg

if __name__ == "__main__":
    with open("sample.ini", "w") as f:
        f.write("[main]\nkey = value\n")
    print(parse_ini("sample.ini"))
```

### Questions

1. What does this parser return for the sample ini?
2. How does it behave with `key=value` before any section?
3. Modify to support a global (no-section) area and type conversion (int/float/bool).

---

## Q397

### find_pairs_two_sum_indices.py

```python
def two_sum(nums, target):
    seen = {}
    for i, x in enumerate(nums):
        need = target - x
        if need in seen:
            return (seen[need], i)
        seen[x] = i
    return None

if __name__ == "__main__":
    print(two_sum([2,7,11,15], 9))
```

### Questions

1. What pair of indices is returned by the example?
2. Modify to return all index pairs (i < j) that sum to target.
3. Explain how this approach achieves O(n) time.

---

## Q398 (buggy)

### json_key_remap.py

```python
def remap_keys(d, mapping):
    out = {}
    for k, v in d.items():
        new_k = mapping.get(k, k)
        if isinstance(v, dict):
            out[new_k] = remap_keys(v, mapping)
        else:
            out[new_k] = v
    return out

if __name__ == "__main__":
    print(remap_keys({"a":1,"b":{"a":2}}, {"a":"alpha"}))
```

### Questions

1. Does this function mutate nested dict references? Explain.
2. Modify to support mapping values that are callables to transform keys or values.
3. Ensure function preserves lists containing dicts (apply remap recursively).

---

## Q399

### rotate_matrix_copy.py

```python
def rotate_matrix_copy(mat):
    rows = len(mat)
    cols = len(mat[0]) if mat else 0
    res = [[None]*rows for _ in range(cols)]
    for i in range(rows):
        for j in range(cols):
            res[j][rows-1-i] = mat[i][j]
    return res

if __name__ == "__main__":
    print(rotate_matrix_copy([[1,2,3],[4,5,6]]))
```

### Questions

1. What is the rotated result for the rectangular example?
2. Explain why this approach works for non-square matrices.
3. Modify to rotate 90° counter-clockwise.

---

## Q400

### sliding_window_max_gen.py

```python
from collections import deque

def sliding_max_gen(seq, k):
    dq = deque()
    for i, x in enumerate(seq):
        while dq and dq[0] <= i - k:
            dq.popleft()
        while dq and seq[dq[-1]] < x:
            dq.pop()
        dq.append(i)
        if i >= k - 1:
            yield seq[dq[0]]

if __name__ == "__main__":
    print(list(sliding_max_gen([1,3,-1,-3,5,3,6,7], 3)))
```

### Questions

1. What sliding maxima are yielded for the sample?
2. Why does the deque store indices instead of values?
3. Modify to return `(start_index, max_value)` for each window.

---







Here are **50 more** Python coding questions numbered **Q401–Q450**. Each item contains a self-contained code file (kept to ≥15 lines when appropriate) followed by **three learner questions**. Most follow the same style as your earlier sets; roughly ~70% intentionally contain a subtle bug or edge-case to find and fix. No hints in titles and no emojis.

---

## Q401

### prime_test_trial_division.py

```python
def is_prime(n):
    """Trial-division primality test."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

if __name__ == "__main__":
    print([p for p in range(1,51) if is_prime(p)])
```

Questions:

1. What primes are printed for 1..50 and why is 1 not prime?
2. Explain why incrementing `i` by 2 is correct after checking evenness.
3. Modify to handle very large `n` more efficiently (outline Miller–Rabin).

---

## Q402 (buggy)

### sum_digits_recursive.py

```python
def sum_digits(n):
    """Return sum of decimal digits of n (handles negative)."""
    if n < 0:
        n = -n
    if n == 0:
        return 0
    return n % 10 + sum_digits(n // 10)

if __name__ == "__main__":
    print(sum_digits(0))
```

Questions:

1. Is recursion safe for very large numbers? What happens for `0`?
2. Fix potential recursion performance/stack concerns.
3. Provide iterative version and one that returns digit list as well.

---

## Q403

### uniq_preserve_order.py

```python
def unique_preserve(seq):
    seen = set()
    out = []
    for x in seq:
        if x not in seen:
            seen.add(x)
            out.append(x)
    return out

if __name__ == "__main__":
    print(unique_preserve([3,1,2,1,3,4]))
```

Questions:

1. What list is returned and why does it preserve first occurrences?
2. How to adapt for unhashable items (e.g., lists)?
3. Implement a version that returns stable unique based on a key function.

---

## Q404 (buggy)

### factorial_memo.py

```python
_cache = {}

def fact(n):
    if n in _cache:
        return _cache[n]
    if n == 0:
        return 1
    res = n * fact(n-1)
    _cache[n] = res
    return res

if __name__ == "__main__":
    print(fact(5))
```

Questions:

1. Identify bug/edge-case (negative input) and caching concern.
2. Add input validation and make cache local to a memoized wrapper function.
3. Compare recursion vs iterative factorial for large `n` (space/time).

---

## Q405

### transpose_matrix.py

```python
def transpose(mat):
    rows = len(mat)
    cols = len(mat[0]) if mat else 0
    res = [[None]*rows for _ in range(cols)]
    for i in range(rows):
        for j in range(cols):
            res[j][i] = mat[i][j]
    return res

if __name__ == "__main__":
    print(transpose([[1,2,3],[4,5,6]]))
```

Questions:

1. What is the transposed result of the example?
2. Modify to handle ragged (non-rectangular) matrices gracefully.
3. Provide an in-place transpose for square matrices.

---

## Q406 (buggy)

### parse_ints_from_text.py

```python
import re

def extract_ints(text):
    return [int(x) for x in re.findall(r"-?\d+", text)]

if __name__ == "__main__":
    print(extract_ints("Values: 1, 2, three, -4"))
```

Questions:

1. What integers are extracted for the sample and what about overflow/leading zeros?
2. Explain why parsing floats would require different regex/logic.
3. Modify to return numbers as ints only if within a safe range, else raise.

---

## Q407

### words_frequency_topk.py

```python
from collections import Counter

def top_k_words(text, k):
    words = [w.lower() for w in text.split()]
    cnt = Counter(words)
    return [w for w, _ in cnt.most_common(k)]

if __name__ == "__main__":
    print(top_k_words("a a b c a b", 2))
```

Questions:

1. What top-2 words are returned for sample?
2. Why might simple `.split()` be insufficient for punctuation?
3. Modify to ignore stopwords and use stemming (outline or code).

---

## Q408 (buggy)

### binary_gap_offby.py

```python
def binary_gap(n):
    b = bin(n)[2:]
    gaps = b.strip('0').split('1')
    return max((len(x) for x in gaps), default=0)

if __name__ == "__main__":
    print(binary_gap(20))  # 10100 -> expected gap 1
```

Questions:

1. Find and fix logic mistake for some inputs (e.g., trailing zeros).
2. Provide corrected implementation and test cases.
3. Modify to return positions (start,end) of the largest gap.

---

## Q409

### merge_two_sorted_lists.py

```python
def merge(a, b):
    i = j = 0
    res = []
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            res.append(a[i]); i += 1
        else:
            res.append(b[j]); j += 1
    res.extend(a[i:]); res.extend(b[j:])
    return res

if __name__ == "__main__":
    print(merge([1,3,5], [2,4,6]))
```

Questions:

1. What's the merged result and is stability preserved?
2. Modify to merge generators (iterators) instead of lists.
3. Implement in-place merge for arrays with buffer at end (outline).

---

## Q410 (buggy)

### sliding_window_sum.py

```python
def window_sum(nums, k):
    if len(nums) < k:
        return []
    s = sum(nums[:k])
    res = [s]
    for i in range(1, len(nums) - k + 1):
        s += nums[i+k-1] - nums[i-1]
        res.append(s)
    return res

if __name__ == "__main__":
    print(window_sum([1,2,3,4], 3))
```

Questions:

1. Is the loop range correct? Find off-by-one errors.
2. Fix and explain sliding update indices.
3. Modify to yield averages instead of sums.

---

## Q411

### flatten_nested_list.py

```python
def flatten(nested):
    out = []
    for item in nested:
        if isinstance(item, (list, tuple)):
            out.extend(flatten(item))
        else:
            out.append(item)
    return out

if __name__ == "__main__":
    print(flatten([1, [2, [3, 4], 5], 6]))
```

Questions:

1. What flattened list is returned for the example?
2. Modify to support a `max_depth` parameter.
3. Convert to an iterative generator that flattens arbitrarily nested lists.

---

## Q412 (buggy)

### dict_key_error_demo.py

```python
def get_nested(d, keys):
    cur = d
    for k in keys:
        cur = cur[k]
    return cur

if __name__ == "__main__":
    data = {"a":{"b":2}}
    print(get_nested(data, ["a","c"]))
```

Questions:

1. What exception is raised and why?
2. Modify to return a default value when any key is missing.
3. Provide a version that can create missing nested dicts on demand.

---

## Q413

### gcd_euclid.py

```python
def gcd(a, b):
    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a

if __name__ == "__main__":
    print(gcd(48, 18))
```

Questions:

1. What GCD is printed and why use `abs`?
2. Modify to compute LCM using GCD safely (avoid overflow).
3. Extend to compute gcd of a list of integers.

---

## Q414 (buggy)

### safe_divide.py

```python
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return 0

if __name__ == "__main__":
    print(safe_divide(1, 0))
```

Questions:

1. Why returning `0` on division-by-zero can be dangerous/misleading?
2. Propose better error handling/return semantics (raise or return `None`).
3. Modify to support element-wise division on lists with `None` for invalid entries.

---

## Q415

### chunked_reader.py

```python
def read_chunks(path, chunk_size=1024):
    with open(path, "rb") as f:
        while True:
            b = f.read(chunk_size)
            if not b:
                break
            yield b

if __name__ == "__main__":
    with open("big.bin", "wb") as f:
        f.write(b"\x00" * 5000)
    print(sum(len(c) for c in read_chunks("big.bin", 1024)))
```

Questions:

1. How many bytes are printed for the sample file?
2. Modify to yield overlapping windows of bytes of given `window_size`.
3. Explain when binary mode is essential vs text mode.

---

## Q416 (buggy)

### find_max_subarray_bug.py

```python
def max_subarray(nums):
    best = 0
    cur = 0
    for x in nums:
        cur = max(x, cur + x)
        best = max(best, cur)
    return best

if __name__ == "__main__":
    print(max_subarray([-2,-3,-1]))
```

Questions:

1. Why does this implementation fail on all-negative arrays?
2. Fix so it works for any integer array (including all-negative).
3. Modify to also return start/end indices.

---

## Q417

### file_extension_counts.py

```python
import os
from collections import Counter

def count_extensions(root):
    cnt = Counter()
    for dirpath, _, files in os.walk(root):
        for f in files:
            ext = os.path.splitext(f)[1].lower()
            cnt[ext] += 1
    return cnt

if __name__ == "__main__":
    print(count_extensions("."))
```

Questions:

1. How are files without extensions counted?
2. Modify to also compute total sizes per extension.
3. Add option to follow or ignore symlinks.

---

## Q418 (buggy)

### parse_query_string.py

```python
from urllib.parse import parse_qs

def parse_q(url):
    # naive: assume url is only query string
    return parse_qs(url)

if __name__ == "__main__":
    print(parse_q("a=1&b=2&a=3"))
```

Questions:

1. What's wrong if user passes full URL including `?` and path?
2. Improve to accept full URL and extract query part robustly.
3. Modify to return single values (first) instead of lists for single-valued params.

---

## Q419

### kth_element_stream.py

```python
import heapq

class KthLargestStream:
    def __init__(self, k):
        self.k = k
        self.heap = []

    def add(self, x):
        heapq.heappush(self.heap, x)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0] if len(self.heap) == self.k else None

if __name__ == "__main__":
    s = KthLargestStream(3)
    for x in [4,5,8,2]:
        print(s.add(x))
```

Questions:

1. What outputs occur while adding values and what is returned before k elements seen?
2. Modify to support removals of arbitrary elements (hint: lazy deletion or counter).
3. Discuss memory/time trade-offs for very large streams.

---

## Q420 (buggy)

### unique_prefixes_naive.py

```python
def shortest_unique_prefixes(words):
    prefixes = {}
    for w in words:
        for L in range(1, len(w)+1):
            p = w[:L]
            if sum(1 for x in words if x.startswith(p)) == 1:
                prefixes[w] = p
                break
        else:
            prefixes[w] = w
    return prefixes

if __name__ == "__main__":
    # bug: inefficient for many words
    print(shortest_unique_prefixes(["dog","cat","car","cart"]))
```

Questions:

1. Identify performance problem and propose trie-based solution.
2. Implement a trie approach to compute shortest unique prefixes in O(total_chars).
3. Discuss memory usage trade-offs.

---

## Q421

### stable_sort_by_key.py

```python
def stable_sort(items, keyfunc):
    return sorted(items, key=keyfunc)  # Python sort is stable

if __name__ == "__main__":
    data = [("a",2),("b",1),("c",2)]
    print(stable_sort(data, lambda x: x[1]))
```

Questions:

1. What sorted order is produced and why is stability important?
2. Modify to sort by multiple keys (primary then secondary) succinctly.
3. Implement in-place stable sort using `list.sort`.

---

## Q422 (buggy)

### read_json_lines.py

```python
import json

def read_jsonlines(path):
    with open(path, "r", encoding="utf-8") as f:
        return [json.loads(line) for line in f]

if __name__ == "__main__":
    with open("jl.txt", "w") as f:
        f.write('{"a":1}\n{"b":2}\n')
    print(read_jsonlines("jl.txt"))
```

Questions:

1. What happens if file has blank lines or trailing commas?
2. Improve to skip blank lines and handle decode errors gracefully.
3. Modify to stream results yielding parsed objects instead of loading all in memory.

---

## Q423

### group_consecutive_equal.py

```python
def group_by_adjacent(seq):
    out = []
    if not seq:
        return out
    cur = [seq[0]]
    for x in seq[1:]:
        if x == cur[-1]:
            cur.append(x)
        else:
            out.append(cur)
            cur = [x]
    out.append(cur)
    return out

if __name__ == "__main__":
    print(group_by_adjacent([1,1,2,2,2,3,1,1]))
```

Questions:

1. What groups are produced for the example?
2. Modify to return `(value, length)` pairs for runs.
3. Implement a generator version that yields groups lazily.

---

## Q424 (buggy)

### ensure_unique_filename.py

```python
import os

def ensure_unique(path):
    base, ext = os.path.splitext(path)
    i = 1
    while os.path.exists(path):
        path = f"{base}({i}){ext}"
        i += 1
    return path

if __name__ == "__main__":
    open("file.txt", "w").close()
    print(ensure_unique("file.txt"))
```

Questions:

1. Identify bug: what happens if `ensure_unique` is called multiple times?
2. Fix to not mutate `path` variable incorrectly and to be thread-safe (outline).
3. Modify to limit attempts and raise if exhausted.

---

## Q425

### partition_even_odd_inplace.py

```python
def partition_pred(nums, pred):
    i = 0
    for j in range(len(nums)):
        if pred(nums[j]):
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
    return nums

if __name__ == "__main__":
    print(partition_pred([3,2,4,1,6], lambda x: x%2==0))
```

Questions:

1. What final ordering is produced and is relative order preserved?
2. Modify to partition by predicate but preserve relative order (stable partition).
3. Adapt to return partition index (first index of false predicate).

---

## Q426 (buggy)

### find_cycle_in_directed.py

```python
def has_cycle(edges):
    g = {}
    for u, v in edges:
        g.setdefault(u, []).append(v)
    visited = set()
    onstack = set()
    def dfs(u):
        visited.add(u)
        onstack.add(u)
        for v in g.get(u, []):
            if v not in visited and dfs(v):
                return True
            elif v in onstack:
                return True
        onstack.remove(u)
        return False
    for n in g:
        if n not in visited:
            if dfs(n):
                return True
    return False

if __name__ == "__main__":
    print(has_cycle([("a","b"),("b","c"),("c","a")]))
```

Questions:

1. Does this detect cycles correctly for nodes with no outgoing edges?
2. Fix to include nodes mentioned only as targets but not sources.
3. Modify to return one detected cycle path.

---

## Q427

### sliding_window_max_indices.py

```python
from collections import deque

def sliding_max_indices(seq, k):
    dq = deque()
    res = []
    for i, x in enumerate(seq):
        while dq and dq[0] <= i - k:
            dq.popleft()
        while dq and seq[dq[-1]] < x:
            dq.pop()
        dq.append(i)
        if i >= k - 1:
            res.append(dq[0])
    return res

if __name__ == "__main__":
    print(sliding_max_indices([1,3,2,5,4], 3))
```

Questions:

1. What indices are returned for the example?
2. Explain how to extract max values using these indices efficiently.
3. Modify to return all indices equal to the window max when ties exist.

---

## Q428 (buggy)

### safe_json_dump.py

```python
import json

def atomic_write_json(path, obj):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(obj, f)
    return True

if __name__ == "__main__":
    print(atomic_write_json("out.json", {"a":1}))
```

Questions:

1. Why is this not atomic and how can partial writes corrupt file?
2. Implement atomic write via temporary file and `os.replace`.
3. Discuss permission and fsync considerations for durability.

---

## Q429

### zip_longest_custom.py

```python
def zip_longest(*iters, fillvalue=None):
    iters = [iter(it) for it in iters]
    finished = [False]*len(iters)
    while True:
        vals = []
        all_done = True
        for i, it in enumerate(iters):
            if finished[i]:
                vals.append(fillvalue)
            else:
                try:
                    vals.append(next(it))
                    all_done = False
                except StopIteration:
                    finished[i] = True
                    vals.append(fillvalue)
        if all_done:
            break
        yield tuple(vals)

if __name__ == "__main__":
    print(list(zip_longest([1,2],[3], fillvalue=0)))
```

Questions:

1. What tuples are yielded in the example?
2. Compare with `itertools.zip_longest` behavior and complexity.
3. Modify to accept `maxlen` to stop after fixed rounds.

---

## Q430 (buggy)

### atoi_simple.py

```python
def atoi(s):
    s = s.strip()
    sign = 1
    if s and s[0] == '-':
        sign = -1
    if s[0] in '+-':
        s = s[1:]
    num = 0
    for ch in s:
        if not ch.isdigit():
            break
        num = num*10 + (ord(ch) - ord('0'))
    return sign * num

if __name__ == "__main__":
    print(atoi("  -42abc"))
```

Questions:

1. Identify potential `IndexError` on empty string inputs.
2. Fix edge cases and implement 32-bit clamping behavior.
3. Add support for leading `+` sign and test.

---

## Q431

### kth_smallest_quickselect.py

```python
import random

def quickselect(nums, k):
    """
    Return k-th smallest (1-indexed) element.
    """
    if not 1 <= k <= len(nums):
        return None
    pivot = random.choice(nums)
    lows = [x for x in nums if x < pivot]
    highs = [x for x in nums if x > pivot]
    pivots = [x for x in nums if x == pivot]
    if k <= len(lows):
        return quickselect(lows, k)
    elif k <= len(lows) + len(pivots):
        return pivot
    else:
        return quickselect(highs, k - len(lows) - len(pivots))

if __name__ == "__main__":
    print(quickselect([7,10,4,3,20,15], 3))
```

Questions:

1. What element is returned for sample and what is expected?
2. Explain average-case complexity and worst-case issues.
3. Modify to be iterative to reduce recursion depth.

---

## Q432 (buggy)

### regex_split_bug.py

```python
import re

def split_sentences(text):
    parts = re.split(r'([.!?])\s+(?=[A-Z])', text)
    out = []
    for i in range(0, len(parts)-1, 2):
        out.append(parts[i] + parts[i+1])
    if len(parts) % 2 == 1:
        out.append(parts[-1])
    return [s.strip() for s in out if s.strip()]

if __name__ == "__main__":
    print(split_sentences("Mr. Smith went. He left."))
```

Questions:

1. Explain failure modes with abbreviations like "Mr." and how regex brittle.
2. Suggest robust solution using `nltk.sent_tokenize` or rule-based heuristics.
3. Modify to keep abbreviations list to avoid splitting incorrectly (outline).

---

## Q433

### topological_group_levels.py

```python
from collections import defaultdict, deque

def group_tasks(edges):
    g = defaultdict(list)
    indeg = defaultdict(int)
    nodes = set()
    for u, v in edges:
        g[u].append(v)
        indeg[v] += 1
        nodes.add(u); nodes.add(v)
    q = deque([n for n in nodes if indeg.get(n,0) == 0])
    groups = []
    while q:
        level_size = len(q)
        level = []
        for _ in range(level_size):
            x = q.popleft()
            level.append(x)
            for nb in g[x]:
                indeg[nb] -= 1
                if indeg[nb] == 0:
                    q.append(nb)
        groups.append(level)
    if sum(len(g) for g in groups) != len(nodes):
        raise ValueError("cycle")
    return groups

if __name__ == "__main__":
    print(group_tasks([("a","b"),("a","c"),("b","d"),("c","d")]))
```

Questions:

1. What groups (levels) are produced for the example?
2. Explain how indegree and queue produce parallelizable batches.
3. Modify to include isolated nodes supplied via optional `nodes` param.

---

## Q434 (buggy)

### ratio_calculator.py

```python
def ratio(a, b):
    return a / b

if __name__ == "__main__":
    print(ratio(1, 0))
```

Questions:

1. What exception occurs and why is it unhandled?
2. Enhance to return `math.inf` or `None` on division by zero (explain choice).
3. Add input validation for numeric types and handle `Decimal` gracefully.

---

## Q435

### json_pretty_diff.py

```python
import json

def pretty_json(obj):
    return json.dumps(obj, indent=2, sort_keys=True)

if __name__ == "__main__":
    a = {"b":1, "a":2}
    print(pretty_json(a))
```

Questions:

1. How does sorting keys help in diffs?
2. Modify to colorize diffs in terminal (outline or code).
3. Add option to limit depth of pretty printing.

---

## Q436 (buggy)

### get_env_bool.py

```python
import os

def get_env_bool(name, default=False):
    val = os.environ.get(name, default)
    return val.lower() in ("1","true","yes")

if __name__ == "__main__":
    print(get_env_bool("NOT_SET", True))
```

Questions:

1. Identify bug when environment variable not set and `default` boolean provided.
2. Fix to coerce default to string when `get` returns default.
3. Extend accepted true values list and add inverse `get_env_flag` with negative form.

---

## Q437

### reservoir_sample.py

```python
import random

def reservoir_sample(iterable, k):
    it = iter(iterable)
    res = []
    for i, x in enumerate(it):
        if i < k:
            res.append(x)
        else:
            j = random.randrange(i+1)
            if j < k:
                res[j] = x
    return res

if __name__ == "__main__":
    print(reservoir_sample(range(1000), 5))
```

Questions:

1. Explain why this returns uniform sample without knowing total size.
2. Modify to return samples as they arrive (generator) rather than at end.
3. Discuss memory/time for large `k` relative to stream.

---

## Q438 (buggy)

### atomic_counter.py

```python
class Counter:
    def __init__(self):
        self.v = 0

    def inc(self):
        self.v += 1
        return self.v

if __name__ == "__main__":
    c = Counter()
    for _ in range(1000):
        c.inc()
    print(c.v)
```

Questions:

1. Why is this not thread-safe? Provide an example failure using threads.
2. Modify to be thread-safe using `threading.Lock`.
3. Discuss atomic primitives (e.g., `multiprocessing.Value`) for process-shared counters.

---

## Q439

### find_missing_ranges.py

```python
def missing_ranges(nums, lo, hi):
    out = []
    prev = lo - 1
    nums = [n for n in nums if lo <= n <= hi]
    for n in nums:
        if n - prev > 1:
            out.append((prev+1, n-1))
        prev = n
    if hi - prev >= 1:
        out.append((prev+1, hi))
    return out

if __name__ == "__main__":
    print(missing_ranges([0,1,3,50,75], 0, 99))
```

Questions:

1. What ranges are missing for example?
2. Modify to format single-number ranges as `"x"` and multi-number as `"x->y"`.
3. Handle case where `nums` unsorted or contains duplicates.

---

## Q440 (buggy)

### validate_email_simple.py

```python
import re

def is_valid_email(s):
    return re.match(r"[^@]+@[^@]+\.[^@]+", s)

if __name__ == "__main__":
    print(bool(is_valid_email("user@example.com")))
```

Questions:

1. Explain why this regex is too permissive and can accept invalid addresses.
2. Suggest a safer validation strategy (libraries or stricter regex).
3. Modify to return the normalized (lowercased) email when valid.

---

## Q441

### topological_order_all_roots.py

```python
from collections import defaultdict, deque

def topo_all_nodes(edges, nodes=None):
    g = defaultdict(list)
    indeg = defaultdict(int)
    all_nodes = set(nodes or [])
    for u, v in edges:
        g[u].append(v)
        indeg[v] += 1
        all_nodes.add(u); all_nodes.add(v)
    q = deque([n for n in all_nodes if indeg.get(n,0) == 0])
    res = []
    while q:
        n = q.popleft()
        res.append(n)
        for nb in g[n]:
            indeg[nb] -= 1
            if indeg[nb] == 0:
                q.append(nb)
    if len(res) != len(all_nodes):
        raise ValueError("cycle")
    return res

if __name__ == "__main__":
    print(topo_all_nodes([("a","b")], nodes=["c"]))
```

Questions:

1. Why include `nodes` parameter and how does it affect output?
2. Modify to return nodes not in edges (isolated nodes) first.
3. Detect and return cycles when present.

---

## Q442 (buggy)

### factorial_largeint.py

```python
def fact_iter(n):
    res = 1
    for i in range(1, n):
        res *= i
    return res

if __name__ == "__main__":
    print(fact_iter(5))  # expected 120
```

Questions:

1. Why does this return wrong result (off-by-one)?
2. Fix and add optional `mod` parameter to compute factorial modulo `m`.
3. Discuss using `math.factorial` vs custom for speed/accuracy.

---

## Q443

### longest_increasing_subsequence_len.py

```python
import bisect

def lis_length(seq):
    tails = []
    for x in seq:
        i = bisect.bisect_left(tails, x)
        if i == len(tails):
            tails.append(x)
        else:
            tails[i] = x
    return len(tails)

if __name__ == "__main__":
    print(lis_length([10,9,2,5,3,7,101,18]))
```

Questions:

1. What length does this return for example?
2. Explain why `tails` doesn't store actual subsequence but supports length computation.
3. Modify to reconstruct an actual increasing subsequence.

---

## Q444 (buggy)

### url_normalize_strip.py

```python
from urllib.parse import urlparse, urlunparse

def normalize(url):
    p = urlparse(url)
    scheme = p.scheme.lower() or "http"
    netloc = p.netloc.lower()
    path = p.path.rstrip("/")
    return urlunparse((scheme, netloc, path, "", "", ""))

if __name__ == "__main__":
    print(normalize("HTTP://Example.COM/Path/"))
```

Questions:

1. What problem arises when stripping trailing `/` from root path `/`?
2. Fix to ensure root path remains `/` when appropriate.
3. Add preservation/sorting of query parameters.

---

## Q445

### substring_search_kmp.py

```python
def kmp_search(text, pattern):
    if not pattern:
        return 0
    # build lps
    lps = [0]*len(pattern)
    length = 0
    i = 1
    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1; lps[i] = length; i += 1
        else:
            if length:
                length = lps[length-1]
            else:
                lps[i] = 0; i += 1
    # search
    i = j = 0
    while i < len(text):
        if text[i] == pattern[j]:
            i += 1; j += 1
            if j == len(pattern):
                return i - j
        else:
            if j:
                j = lps[j-1]
            else:
                i += 1
    return -1

if __name__ == "__main__":
    print(kmp_search("abxabcabcaby", "abcaby"))
```

Questions:

1. What index does this return and why is KMP efficient?
2. Explain how the LPS array reduces backtracking.
3. Modify to return all match starting indices, not just first.

---

## Q446 (buggy)

### safe_open_write.py

```python
def write_text_atomic(path, text):
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    return True

if __name__ == "__main__":
    write_text_atomic("/root/protected.txt", "data")
```

Questions:

1. Why can this fail due to permissions and leave partial writes?
2. Improve with exception handling and writing to temp then replace atomically.
3. Add optional mode to create parent dirs.

---

## Q447

### arithmetic_progression_sum.py

```python
def ap_sum(a1, n, d=1):
    """Sum of arithmetic progression: a1 + (a1+d) + ... n terms"""
    if n <= 0:
        return 0
    return n * (2*a1 + (n-1)*d) // 2

if __name__ == "__main__":
    print(ap_sum(1, 100, 1))
```

Questions:

1. What sum is printed for 1..100 and why formula uses integer division?
2. Modify to return float when inputs are floats.
3. Use formula to compute sum of even numbers between 2 and 100 inclusive.

---

## Q448 (buggy)

### map_values_bug.py

```python
def map_values(d, fn):
    for k in d:
        d[k] = fn(d[k])
    return d

if __name__ == "__main__":
    dd = {1: [1,2], 2: [3]}
    print(map_values(dd, lambda v: v.append(0)))
```

Questions:

1. Identify mistake: what does `append` return vs expected?
2. Fix to return transformed values and avoid mutating original lists unintentionally.
3. Provide pure functional variant returning new dict.

---

## Q449

### random_subset_probability.py

```python
import random

def random_subset(seq, p):
    out = []
    for x in seq:
        if random.random() < p:
            out.append(x)
    return out

if __name__ == "__main__":
    print(random_subset(list(range(10)), 0.3))
```

Questions:

1. What is expected size of subset in expectation?
2. How to make sampling reproducible?
3. Modify to sample without replacement for large sequences using `reservoir_sample` when `p` small.

---

## Q450 (buggy)

### merge_sorted_iters_bug.py

```python
import heapq

def merge_sorted_iters(iters):
    heap = []
    for idx, it in enumerate(iters):
        try:
            val = next(it)
            heapq.heappush(heap, (val, idx, it))
        except StopIteration:
            pass
    res = []
    while heap:
        val, idx, it = heapq.heappop(heap)
        res.append(val)
        try:
            nxt = next(it)
            heapq.heappush(heap, (nxt, idx, it))
        except StopIteration:
            pass
    return res

if __name__ == "__main__":
    a = iter([1,4,7])
    b = iter([2,3,8])
    print(merge_sorted_iters([a,b]))
```

Questions:

1. What is returned and is there a subtle bug when iterators yield equal values?
2. Explain why `(val, idx, it)` tuple ordering is safe; what if `val` types are incomparable?
3. Modify to accept key function for ordering and support infinite iterators (streaming).

---

