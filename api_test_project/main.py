import requests
url = 'https://mars.se-pro.site'


class Blogger:
    url = 'https://mars.se-pro.site'

    def __init__(self, full_name):
        blogger_data = {
            'full_name': full_name
        }
        response = requests.post(f'{self.url}/bloggers/', data=blogger_data)
        # print(response.status_code)
        blogger = response.json()
        # print('response ', blogger)
        self.id = blogger['id']
        self.full_name = blogger['full_name']
    
    def delete(self, id=None):
        if id:
            response = requests.delete(f'{self.url}/bloggers/{id}/')
        else:
            response = requests.delete(f'{self.url}/bloggers/{self.id}/')
        # print(response.status_code)

    def update(self, full_name):
        blogger_data = {
            'full_name': full_name
        }
        response = requests.put(f'{self.url}/bloggers/{self.id}/', data=blogger_data)
        # print(response.status_code)
        blogger = response.json()
        self.id = blogger['id']
        self.full_name = blogger['full_name']
        # print(blogger)

    @classmethod
    def all(cls):
        response = requests.get(f'{cls.url}/bloggers/')
        # print(response.status_code)
        bloggers = response.json()
        print(bloggers)
        for blogger in bloggers:
            print('blogger = ', blogger['full_name'])

    def __str__(self):
        return f"Id: {self.id} Name: {self.full_name} "


# Blogger.all()

eyyub = Blogger('Eyyub Amiraslanov')

print(eyyub)

eyyub.update('Kenan Semenderli')

print(eyyub)

# Blogger.all()


# eyyub = Blogger('Eyyub Amiraslanov')

# print(eyyub)

# eyyub.delete(20)



# def get_all_bloggers():
#     response = requests.get(f'{url}/blogger/')
#     print(response.status_code)
#     bloggers = response.json()
#     for blogger in bloggers:
#         print('blogger = ', blogger['full_name'])

# def create_blogger(full_name):
#     blogger_data = {
#         'full_name': full_name
#     }
#     response = requests.post(f'{url}/bloggers/', data=blogger_data)
#     print(response.status_code)
#     blogger = response.json()
#     print(blogger)


# def change_blogger(blogger_id, full_name):
#     blogger_data = {
#         'full_name': full_name
#     }
#     response = requests.put(f'{url}/bloggers/{blogger_id}/', data=blogger_data)
#     print(response.status_code)
#     blogger = response.json()
#     print(blogger)

# def partial_change_blogger(blogger_id, full_name):
#     blogger_data = {
#         'full_name': full_name
#     }
#     response = requests.patch(f'{url}/bloggers/{blogger_id}/', data=blogger_data)
#     print(response.status_code)
#     blogger = response.json()
#     print(blogger)

# def get_blogger(blogger_id):
#     response = requests.get(f'{url}/bloggers/{blogger_id}/')
#     print(response.status_code)
#     blogger = response.json()
#     print(blogger)


# def delete_blogger(blogger_id):
#     response = requests.delete(f'{url}/bloggers/{blogger_id}/')
#     print(response.status_code)


# delete_blogger(2)

# get_blogger(2)