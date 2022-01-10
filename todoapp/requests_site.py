import requests

# response_post = requests.post('http://127.0.0.1:8000/api-token-auth/', data={'username': 'alexl', 'password': '123'})
#
# print(response_post.status_code)
# print(response_post.json())
#
# dct = response_post.json()
# token = dct['token']
#
# response_get = requests.get('http://127.0.0.1:8000/api/', data={'token': token})
# print(response_get.status_code)
# print(response_get.json())

response = requests.get('http://127.0.0.1:8000/api/users',
                        headers={'Accept': 'application/json; version=v2'})

# {'count': 4, 'next': None, 'previous': None, 'results': [{'is_superuser': True, 'is_staff': True},
# {'is_superuser': False, 'is_staff': False}, {'is_superuser': False, 'is_staff': False},
# {'is_superuser': False, 'is_staff': False}]}
print(response.json())
