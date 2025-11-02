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


## 🧺 Lists

151. What is a list in Python?
152. How do you create a list?
153. How do you access elements from a list using indexes?
154. How do you change the value of an element in a list?
155. How do you add an item to a list?
156. What is the difference between `append()` and `insert()`?
157. How do you remove elements from a list?
158. What is the difference between `remove()`, `pop()`, and `del`?
159. How can you get the length of a list?
160. How do you check if an element exists in a list?
161. How do you iterate through a list?
162. How can you copy a list properly?
163. What happens if you use `list1 = list2`?
164. What is list slicing?
165. How do you reverse a list?
166. How do you sort a list in ascending or descending order?
167. What is the difference between `sort()` and `sorted()`?
168. How can you concatenate two lists?
169. How do you find the maximum and minimum values in a list?
170. How can you remove duplicates from a list?

---

## 🧱 Tuples

171. What is a tuple in Python?
172. How is a tuple different from a list?
173. How do you create a tuple with a single element?
174. How do you access elements in a tuple?
175. Are tuples mutable or immutable?
176. How do you convert a list to a tuple and vice versa?
177. How can you find the index of an element in a tuple?
178. How can you count how many times an element appears in a tuple?
179. When should you prefer using a tuple over a list?
180. Can a tuple contain mutable objects?

---

## 🧮 Sets

181. What is a set in Python?
182. How do you create a set?
183. What are the main characteristics of sets?
184. How do you add an element to a set?
185. How do you remove an element from a set?
186. What is the difference between `discard()` and `remove()` in sets?
187. How do you find the union of two sets?
188. How do you find the intersection of two sets?
189. How do you find the difference between two sets?
190. How do you check if a set is a subset or superset of another?
191. Can a set contain duplicate elements?
192. What happens if you try to add a duplicate element to a set?
193. How can you check if two sets are disjoint?
194. What is a frozen set?
195. When would you use a frozen set instead of a normal set?

---

## 🗂️ Dictionaries

196. What is a dictionary in Python?
197. How do you create a dictionary?
198. How do you access values using keys in a dictionary?
199. How do you add or update an entry in a dictionary?
200. How do you remove a key-value pair from a dictionary?

---


## 🧩 Functions (Core Concepts)

201. What is a function in Python?
202. How do you define a function in Python?
203. How do you call a function?
204. What is the purpose of the `return` statement?
205. What happens if a function doesn’t have a `return` statement?
206. What is the difference between a function that returns a value and one that doesn’t?
207. What are positional arguments in a function?
208. What are keyword arguments?
209. What are default arguments in Python functions?
210. What are variable-length arguments (`*args` and `**kwargs`)?
211. What is the difference between `*args` and `**kwargs`?
212. What happens when you call a function with missing arguments?
213. How can you specify both positional and keyword-only arguments?
214. What is scope in Python?
215. What are local and global variables?
216. How do you modify a global variable inside a function?
217. What is the `nonlocal` keyword used for?
218. What are anonymous (lambda) functions?
219. How do lambda functions differ from normal functions?
220. When should you use a lambda function?

---

## 🔁 Loops and Iteration

221. What is the difference between `for` and `while` loops?
222. How does the `range()` function work?
223. How can you loop through both index and value in a list?
224. What is the difference between `break` and `continue`?
225. What happens when you use `else` with a `for` or `while` loop?
226. How can you iterate over a dictionary’s keys and values?
227. How can you iterate over a string character by character?
228. How can you iterate through a list in reverse order?
229. What is the purpose of the `enumerate()` function?
230. How do nested loops work in Python?

---

## 🧮 Conditional Statements

231. What are conditional statements in Python?
232. How does the `if` statement work?
233. What is the purpose of `elif`?
234. What is the difference between `if` and `elif`?
235. What happens when no condition in an `if-elif` chain is true?
236. How do you write a one-line conditional (ternary) expression?
237. Can you nest `if` statements?
238. How do you combine multiple conditions using logical operators?
239. What is the difference between `and` and `or` in conditions?
240. What is the difference between `is`, `in`, and `==` in condition checks?

---

## 📥 Input / Output (I/O)

241. How do you get user input from the keyboard?
242. What data type does `input()` return?
243. How do you convert user input into integers or floats?
244. How do you print output in Python?
245. How do you print multiple variables in one line?
246. What does the `end` parameter in `print()` do?
247. How do you format output strings using f-strings?
248. How do you read from a file in Python?
249. How do you write data to a file in Python?
250. What happens if you try to read a file that doesn’t exist?

---


## ⚠️ Exception Handling

251. What is an exception in Python?
252. How does Python handle runtime errors?
253. What is the purpose of the `try` and `except` blocks?
254. What happens if an exception is not handled?
255. How do you catch multiple exceptions in a single block?
256. How can you execute code after an exception, no matter what happens?
257. What is the `finally` block used for?
258. What is the `else` block in exception handling used for?
259. How can you raise an exception manually?
260. How do you create custom exception classes in Python?
261. What is the difference between `raise` and `assert`?
262. What are common built-in exceptions in Python?
263. How do you handle file-related exceptions?
264. What is the purpose of `try...finally` without an `except`?
265. What is exception chaining?
266. How do you log exceptions using the `logging` module?
267. Can you catch exceptions inside a `lambda` function?
268. How does Python propagate exceptions through the call stack?
269. What is the difference between syntax errors and runtime errors?
270. How can you suppress specific exceptions using `contextlib.suppress()`?

---

## 📦 Modules and Imports

271. What is a module in Python?
272. How do you import a module in Python?
273. What is the difference between `import module` and `from module import name`?
274. How do you import multiple names from a module?
275. How do you rename an imported module or function?
276. What is the purpose of the `as` keyword in imports?
277. How do you import everything from a module?
278. Why is using `from module import *` not recommended?
279. What is the `__name__` variable used for in a Python file?
280. What happens when you run a module directly versus importing it?
281. What are built-in Python modules?
282. How can you see all available modules in your Python installation?
283. How do you install an external Python package?
284. What is `pip`, and how does it work?
285. How do you uninstall a package using pip?
286. What is the purpose of a virtual environment in Python?
287. How do you create and activate a virtual environment?
288. What is the difference between `requirements.txt` and `pyproject.toml`?
289. How do you reload a module in Python without restarting the interpreter?
290. How can you check the version of an installed module?

---

## 🧮 Basic Coding Logic & Practice

291. How do you check if a number is even or odd in Python?
292. How do you find the largest of three numbers?
293. How do you swap two variables without using a temporary variable?
294. How do you find the factorial of a number?
295. How do you check if a number is prime?
296. How do you find all prime numbers in a given range?
297. How do you find the sum of all digits of a number?
298. How do you reverse an integer number in Python?
299. How do you count the number of vowels in a string?
300. How do you check if a string is a palindrome?

---
