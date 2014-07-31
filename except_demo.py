# Copyright © 2014 Bart Massey
# Demo exception handling

class DemoException1(Exception):
    def __init__(self):
        pass

class DemoException2(Exception):
    def __init__(self, value):
        self.value = value

def raise_except(n):
    if n == 1:
        raise DemoException1()
    if n == 2:
        raise DemoException2("boo")
    if n == 3:
        return int("bogus")
    if n == 4:
        raise ValueException()
    return n

def show_except(n):
    try:
        r = raise_except(n)
    except DemoException1:
        print("demo exception 1")
        return None
    except DemoException2 as e:
        print("demo exception 2: %s" % (e.value,))
        return None
    except:
        print("unknown exception")
        raise
#   else:
#       print("unhandled exception")
#       return None
    finally:
        print("finally...")
    return r

def call_show_except(n):
    try:
        print(show_except(n))
    except:
        print("nope")
