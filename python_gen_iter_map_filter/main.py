def range_dec(f):
    def wrapper(*args, **kwargs):
        if len(args) + len(kwargs.keys()) == 1:
            stop = kwargs.get('stop') or args[0]
            return f(0, stop, 1)
        elif len(args) + len(kwargs.keys()) == 2:
            start = kwargs.get('start') or args[0]
            stop = kwargs.get('stop') or args[1]
            return f(start, stop, 1)
        else:
            start = kwargs.get('start') or args[0]
            stop = kwargs.get('stop') or args[1]
            step = kwargs.get('step') or  args[2]
            return f(start, stop, step)
    return wrapper


@range_dec
def my_range_gen(start, stop, step):
    i = start
    if step > 0:
        while True:
            if i < stop:
                yield i
                i += step
            else:
                break
    else:
        while True:
            if i > stop:
                yield i
                i += step
            else:
                break


# for i in my_range_gen(20):
#     print(i)


for i in range(start=1, stop=20, step=1):
    print(i)