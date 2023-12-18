# combinator-in-python

Function combinators in Python.
Includes compose, pipe, tap, alternation, sequence and fork.

## import

```python
import combinator as comb
```

## compose and pipe

```python
def add1(x):
    return x + 1

def times10(x):
    return x * 10

# compose
times10_add1 = comb.compose(add1, times10)
result = times10_add1(5)
print(result)

# > 51

# pipe
add1_times10 = comb.pipe(add1, times10)
result = add1_times10(5)
print(result)

# > 60
```


## tap

```python
result = comb.tap(print, 10)
# > 10
print(result)
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

