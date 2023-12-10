
def identity(arg):
    return arg

def tap(f, arg):
    f(arg)
    return arg

def alternation(fn1, fn2):
    def newFunction(val):
        return fn1(val) or fn2(val)
    return newFunction

def sequence(*funcs):
    def newFunction(val):
        for f in funcs:
            f(val)
    return newFunction

def fork(join, fn1, fn2):
    def newFunction(val):
        return join(fn1(val), fn2(val))
    return newFunction

