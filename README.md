# combinator-in-python

Function combinator in Python.

## import

```python
import combinator as comb
```

## tap

```python
def printAddFive(num):
    print(num + 5)

result = comb.tap(printAddFive, 10)
print(result)
# > 15
# > 10
```


## alternation

```python
def isBiggerThan10(num):
    if num > 10:
        return 'Bigger than 10'
    return False

def isOdd(num):
    if num % 2 == 0:
        return False
    return 'Odd number'

alt = comb.alternation(isBiggerThan10, isOdd)
print(alt(5))
#> Odd number
```

## sequence

```python
def wakeup(name):
    print(name, 'wake up.')

def enjoy(name):
    print(name, 'enjoy.')

def sleep(name):
    print(name, 'sleep.')

oneDay = comb.sequence(wakeup, enjoy, sleep)
oneDay('I')
#> I wake up.
#> I enjoy.
#> I sleep.
```

## fork

```python
def join(a, b):
    return '{} and {} joined.'.format(a, b)

def left(value):
    return 'left ' + value

def right(value):
    return 'right ' + value

fork = comb.fork(join, left, right)
result = fork('side')
print(result)
# result -> left side and right side joined.
```

