import requests



word = input('Oxsar menasini bilmek istediyiniz sozu daxil edin: ')

url = 'https://api.datamuse.com/words?'

response = requests.get(f'{url}ml={word}')

print('status_code == ', response.status_code)

word_objs = response.json()

for word_obj in word_objs:
    print('word = ', word_obj['word'], word_obj['score'])
