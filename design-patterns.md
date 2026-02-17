# Design Patterns Catalog

Source: [Refactoring Guru - Design Patterns](https://refactoring.guru/design-patterns/catalog)

## Index

### Creational Patterns (5)
1. [Factory Method](#1-factory-method)
2. [Abstract Factory](#2-abstract-factory)
3. [Builder](#3-builder)
4. [Prototype](#4-prototype)
5. [Singleton](#5-singleton)

### Structural Patterns (7)
6. [Adapter](#6-adapter)
7. [Bridge](#7-bridge)
8. [Composite](#8-composite)
9. [Decorator](#9-decorator)
10. [Facade](#10-facade)
11. [Flyweight](#11-flyweight)
12. [Proxy](#12-proxy)

### Behavioral Patterns (10)
13. [Chain of Responsibility](#13-chain-of-responsibility)
14. [Command](#14-command)
15. [Iterator](#15-iterator)
16. [Mediator](#16-mediator)
17. [Memento](#17-memento)
18. [Observer](#18-observer)
19. [State](#19-state)
20. [Strategy](#20-strategy)
21. [Template Method](#21-template-method)
22. [Visitor](#22-visitor)

---

## Creational Patterns

These patterns provide various object creation mechanisms, which increase flexibility and reuse of existing code.

### 1. Factory Method
Provides an interface for creating objects in a superclass, but allows subclasses to alter the type of objects that will be created.

### 2. Abstract Factory
Lets you produce families of related objects without specifying their concrete classes.

### 3. Builder
Lets you construct complex objects step by step. The pattern allows you to produce different types and representations of an object using the same construction code.

### 4. Prototype
Lets you copy existing objects without making your code dependent on their classes.

### 5. Singleton
Lets you ensure that a class has only one instance, while providing a global access point to this instance.

---

## Structural Patterns

These patterns explain how to assemble objects and classes into larger structures while keeping these structures flexible and efficient.

### 6. Adapter
Allows objects with incompatible interfaces to collaborate.

### 7. Bridge
Lets you split a large class or a set of closely related classes into two separate hierarchies—abstraction and implementation—which can be developed independently of each other.

### 8. Composite
Lets you compose objects into tree structures and then work with these structures as if they were individual objects.

### 9. Decorator
Lets you attach new behaviors to objects by placing these objects inside special wrapper objects that contain the behaviors.

### 10. Facade
Provides a simplified interface to a library, a framework, or any other complex set of classes.

### 11. Flyweight
Lets you fit more objects into the available amount of RAM by sharing common parts of state between multiple objects instead of keeping all of the data in each object.

### 12. Proxy
Lets you provide a substitute or placeholder for another object. A proxy controls access to the original object, allowing you to perform something either before or after the request gets through to the original object.

---

## Behavioral Patterns

These patterns are concerned with algorithms and the assignment of responsibilities between objects.

### 13. Chain of Responsibility
Lets you pass requests along a chain of handlers. Upon receiving a request, each handler decides either to process the request or to pass it to the next handler in the chain.

### 14. Command
Turns a request into a stand-alone object that contains all information about the request. This transformation lets you pass requests as method arguments, delay or queue a request's execution, and support undoable operations.

### 15. Iterator
Lets you traverse elements of a collection without exposing its underlying representation (list, stack, tree, etc.).

### 16. Mediator
Lets you reduce chaotic dependencies between objects. The pattern restricts direct communications between the objects and forces them to collaborate only via a mediator object.

### 17. Memento
Lets you save and restore the previous state of an object without revealing the details of its implementation.

### 18. Observer
Lets you define a subscription mechanism to notify multiple objects about any events that happen to the object they're observing.

### 19. State
Lets an object alter its behavior when its internal state changes. It appears as if the object changed its class.

### 20. Strategy
Lets you define a family of algorithms, put each of them into a separate class, and make their objects interchangeable.

### 21. Template Method
Defines the skeleton of an algorithm in the superclass but lets subclasses override specific steps of the algorithm without changing its structure.

### 22. Visitor
Lets you separate algorithms from the objects on which they operate.

---

## Summary

Total: 22 Design Patterns
- Creational: 5 patterns
- Structural: 7 patterns
- Behavioral: 10 patterns

Content was rephrased for compliance with licensing restrictions.
