/ [Home](index.md)

## Expert Coding Assignments


1. Gateway Adapter

https://github.com/kactlabs/Tovexity/tree/aws-integration

This has AWS dependency, Remvoe the AWS dependency and keep vanialla Gateway adapter



2. Get Above 5
```
import random

loop_count = 0

def get_random_numbers():

    numbers = []

    for _ in range(5):
        numbers.append(random.randint(1, 10))

    return numbers

def get_above_5(results):

    global loop_count

    loop_count += 1

    print(f'loop_count: {loop_count}: results: {results}')

    if len(results) > 5:
        return results

    random_numbers = get_random_numbers()

    for number in random_numbers:
        if number > 5:
            results.append(number)

    return get_above_5(results)

print(get_above_5([]))
```


3. I need to collect Medium articles by using Brave (BraveArticleCollector). If 10 articles not collected, recurse it.
https://github.com/kactlabs/genainewsagent/blob/main/brave_article_collector.py
