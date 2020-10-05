
def logger(func):
    def wrapper(*args, **kwargs):
        print('args: ', args, 'kwargs: ', kwargs)
        # try:
        result = func(*args, **kwargs)
        # except Exception as e:
        #     print(e)
        #     result = e
        with open('text.txt', 'a') as file:
            file.write(f'{args} \n')
            file.write(f'{kwargs} \n')
            file.write(f'result: {result} \n')
        return result
    return wrapper
        

@logger
def sum(a, b, c):
    return a + b +c 

@logger
def divide(c, d):
    return c / d

print('ededlerin cemi: ', sum(1, 2, c=4))

print('ededlerin qistemi: ', divide(c=15,d=0))

print('ededlerin qistemi: ', divide(1,2))


