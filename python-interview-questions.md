/ [Home](index.md)

## Python Interview Questions

**Note:** 1000 py questions

---

## 🧠 Core Python Concepts

1. What are the different data types in Python?
2. How does Python implement dynamic typing?
3. What is casting in Python?
4. What is slicing in Python?
5. How are strings immutable in Python, and what does that mean?
6. How to check if a string contains only digits?
7. What are mutable and immutable data types in Python?
8. What is the difference between `is` and `==` in Python?
9. How does Python handle memory management?
10. What is the difference between shallow copy and deep copy?

---

## 🧩 Strings and Collections

11. What are the main differences between lists and tuples?
12. How do you remove duplicates from a list?
13. How can you reverse a list in Python?
14. What are list comprehensions and when to use them?
15. What is the difference between `append()` and `extend()` methods?
16. How do you sort a list of dictionaries by a specific key?
17. How can you merge two dictionaries in Python 3.9+?
18. How do you access dictionary keys safely without raising an error?
19. What is a `set` in Python and when would you use it?
20. How do you find the intersection and union of two sets?

---

## ⚙️ Functions and Scope

21. What are `*args` and `**kwargs` used for?
22. What is the difference between global and local variables?
23. What is the purpose of the `return` statement?
24. What is recursion, and how is it implemented in Python?
25. What are lambda functions, and how are they different from normal functions?
26. What is a closure in Python?
27. How do default parameter values work in Python functions?
28. What happens if you use a mutable object as a default argument?
29. How can you pass a function as an argument to another function?
30. What are decorators in Python?

---

## 🧮 Object-Oriented Programming (OOP)

31. What is a class in Python?
32. What is the difference between a class variable and an instance variable?
33. What is inheritance, and how is it implemented in Python?
34. What is polymorphism in Python?
35. What is method overriding?
36. What are `@staticmethod` and `@classmethod`?
37. What is encapsulation, and how does Python implement it?
38. What does the `super()` function do?
39. How can you make an object callable like a function?
40. What are magic (dunder) methods in Python?

---

## 🔁 Iterators, Generators, and Comprehensions

41. What is the difference between an iterator and an iterable?
42. What are generators in Python?
43. What is the `yield` keyword used for?
44. What is the difference between a generator expression and a list comprehension?
45. How can you create an infinite iterator in Python?

---

## 🧱 Error Handling and Files

46. What is exception handling in Python?
47. What is the difference between `except Exception` and `except BaseException`?
48. How do you handle multiple exceptions in a single block?
49. How can you read and write files in Python?
50. What does the `with` statement do when opening files?

---

# 🐍 Python Interview Questions (Intermediate → Advanced)

## 📦 Modules & Imports

51. What is the difference between absolute and relative imports in Python?
52. How do `__name__ == "__main__"` guards work and why use them?
53. What is the purpose of `__all__` in a module’s `__init__.py`?
54. How does Python find modules on the import path (`sys.path`)?
55. What are namespace packages and how do they differ from regular packages?
56. How do import cycles occur and how can you break them?
57. What does import time vs runtime cost mean, and how do you optimize imports?
58. What is the difference between `import module`, `from module import name`, and `import module as alias`?

## 🎀 Decorators & Descriptors

59. How do function decorators work under the hood?
60. What problems are decorators good at solving?
61. How do you write a decorator that accepts arguments?
62. What is `functools.wraps` and why is it important?
63. What is a descriptor in Python?
64. How do the descriptor methods `__get__`, `__set__`, and `__delete__` work?
65. When would you use a descriptor instead of `@property`?
66. How do method descriptors (bound vs unbound methods) actually bind `self`?

## 🔁 Advanced Iteration & Generators

67. How does the iterator protocol (`__iter__`, `__next__`) work?
68. What are the trade-offs between generators and lists for large data?
69. How do you send values into a generator (`generator.send`) and why?
70. What does `yield from` do and when should you use it?
71. How do you handle exceptions inside generators?
72. What are common `itertools` utilities you should know (e.g., `groupby`, `chain`, `tee`)?
73. How can you implement a custom iterable with internal state?
74. What’s the difference between generator expressions and comprehensions performance-wise?

## 📚 Context Managers & `with`

75. How does the context manager protocol (`__enter__`, `__exit__`) work?
76. How do you write a context manager with `contextlib.contextmanager`?
77. How do you handle exceptions in a context manager cleanly?
78. When should you use `ExitStack`?
79. What are real-world use cases for custom context managers beyond files?

## ⚡ Async & Concurrency

80. What is the difference between concurrency and parallelism?
81. How does `asyncio`’s event loop work conceptually?
82. What are `async def`, `await`, and `async with` / `async for`?
83. How do tasks differ from coroutines in `asyncio`?
84. When should you use `asyncio.to_thread` or thread pools with async code?
85. How do you handle timeouts and cancellations in `asyncio`?
86. What are the differences between threads, processes, and async IO in Python?
87. How do you avoid blocking the event loop in async applications?
88. What are common pitfalls mixing `asyncio` with blocking libraries?

## ✍️ Typing & Dataclasses

89. What benefits does static typing bring to Python projects?
90. How do `TypedDict`, `Protocol`, and `NewType` differ?
91. What is variance (covariant/contravariant) in type hints and where does it matter?
92. How do `@dataclass` features like `field(default_factory=...)` work?
93. What’s the difference between `slots=True` dataclasses and normal dataclasses?
94. How do you type hint callables, generators, and async functions?
95. What tools (e.g., mypy, pyright) catch which classes of errors?

## 🧠 Memory, GC, and Performance

96. How does Python’s reference counting and garbage collector work together?
97. What is a memory leak in Python and how can it happen?
98. How do `__slots__` reduce memory usage and when should you use them?
99. What are common performance bottlenecks in Python and how do you profile them?
100. When should you use C extensions, Cython, or `numpy` for performance-critical code?

Excellent 🔥 — here’s the **final batch of 50 advanced-to-expert level Python interview questions (101–150)**, covering topics such as design patterns, metaprogramming, async internals, data structures, testing, optimization, and practical coding scenarios — all in **Markdown** format.

---

# 🧠 Python Interview Questions (Advanced → Expert)

---

## 🏗️ Design Patterns & Architecture

101. What is the Singleton pattern, and how do you implement it in Python?
102. How does the Factory Method pattern work in Python?
103. How can you implement the Observer pattern using Python’s features?
104. How do you implement the Strategy pattern using functions or classes?
105. What is the difference between composition and inheritance, and when to prefer each?
106. What are mixins, and how do you use them properly?
107. What is dependency injection, and how can it be applied in Python?
108. How do you implement a simple plugin architecture in Python?
109. What is the Adapter pattern, and how do you use it with existing Python classes?
110. What’s the role of the `abc` module in enforcing design patterns?

---

## 🧬 Metaprogramming & Reflection

111. What are metaclasses in Python, and why are they powerful?
112. How can you create a custom metaclass?
113. How do `__new__` and `__init__` differ in object creation?
114. What does the `type()` function do when used with three arguments?
115. How do you dynamically add attributes or methods to a class?
116. What is monkey patching, and why should you use it carefully?
117. What are annotations (`__annotations__`) and how are they stored?
118. How does Python’s `inspect` module help in metaprogramming?
119. What is introspection, and what built-in functions support it?
120. What are the trade-offs between using metaclasses and decorators?

---

## ⚙️ Advanced OOP Mechanics

121. What is method resolution order (MRO) and how does it work?
122. How can you inspect a class’s MRO in Python?
123. What is the diamond problem, and how does Python resolve it?
124. How can you use `super()` in multiple inheritance scenarios?
125. What happens when you override `__getattribute__` vs `__getattr__`?
126. What are `__call__`, `__len__`, and other magic methods used for?
127. How does operator overloading work in Python?
128. How can you make a custom class hashable?
129. How can you prevent class inheritance in Python?
130. What does object identity (`id()`) tell you about memory usage?

---

## ⚡ Async Internals & Parallel Execution

131. What is the Global Interpreter Lock (GIL), and why does it exist?
132. How does the GIL affect multi-threaded performance in Python?
133. How can you achieve parallelism despite the GIL?
134. What are the differences between `threading`, `multiprocessing`, and `asyncio`?
135. How does Python’s `concurrent.futures` module simplify concurrency?
136. How do you safely share state between threads or processes?
137. What is event-driven programming, and how does it relate to asyncio?
138. How do async generators differ from regular generators?
139. How does cooperative multitasking work in async programs?
140. What are common debugging techniques for async code?

---

## 🧩 Data Structures & Algorithms in Python

141. How is a Python list implemented internally?
142. How does Python’s dictionary maintain insertion order?
143. What’s the time complexity of lookups in a set or dict?
144. How are tuples more memory-efficient than lists?
145. How do you implement a stack or queue efficiently in Python?
146. What is the difference between `deque` and list for queue operations?
147. How would you implement a linked list in Python?
148. What are Python’s built-in heap and priority queue utilities?
149. What’s the difference between shallow and deep copying for nested data?
150. How do you store large numeric arrays efficiently in Python (e.g., using `array` or `numpy`)?

---
