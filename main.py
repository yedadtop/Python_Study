
def log(func):
    def inner(*args,**kw):
        print("ahha")
        return func(*args, **kw)
    return inner


def add(x,y):
    return x+y


print(log(add)(1,2))

