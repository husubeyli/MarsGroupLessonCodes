import threading
import multiprocessing
import time

import random
len_list = 1000000

big_list = [i for i in range(len_list)]
# print(big_list)

def find_element_in_list(array, part_count, _i, searched_elem):
    # if searched_elem in array:
    for i in array:
        if searched_elem == i:
            print('Index of element: ', array.index(searched_elem) + _i*part_count )
            return searched_elem
    '''
    try:
        print('Index of element: ', array.index(searched_elem) + i*part_count )
    except:
        pass
    '''
    # else:
        # print('Not found')

searched_element = int(input('Axtardiginiz elementi daxil edin: '))
start = time.perf_counter()
print('search without threading', big_list.index(searched_element))
stop = time.perf_counter()

print(f'Stopped  {round(stop-start, 2)}s')
part_count = 1
# big_list[0:2] = 
# big_list[2:4] = 
# big_list[4:6] = 
# big_list[6:8] = 
# big_list[8:] =
start = time.perf_counter()

threads = [] 
for i in range(part_count):
    # print(i*len_list//part_count, (i+1)*len_list/part_count)
    slice_list = big_list[i*len_list//part_count: (i+1)*len_list//part_count]
    thread = multiprocessing.Process(target=find_element_in_list, args=(slice_list, len_list//part_count, i, searched_element))
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

stop = time.perf_counter()

print(f'Stopped  {round(stop-start, 2)}s')