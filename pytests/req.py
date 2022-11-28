import requests

headers = {'accept':'application/json', 'Content-Type': 'application/json'}
params_get = {'status':'available'}
user = {"id": 0,
  "username": "string",
  "firstName": "string",
  "lastName": "string",
  "email": "string",
  "password": "string",
  "phone": "string",
  "userStatus": 0}
user_change = {"id": 0,
  "username": "user",
  "firstName": "string",
  "lastName": "string",
  "email": "string",
  "password": "string",
  "phone": "string",
  "userStatus": 0}

res_get = requests.get('https://petstore.swagger.io/v2/pet/findByStatus', params=params_get, headers=headers)
res_post = requests.post('https://petstore.swagger.io/v2/user', headers=headers, data=user)
res_put = requests.put('https://petstore.swagger.io/v2/user/string', headers=headers, data=user_change)
res_del = requests.delete('https://petstore.swagger.io/v2/user/string', headers=headers, data=user)

print('----------------')
print('res_get_code: ', res_get.status_code)
print('res_get_text: ', res_get.text)
print('res_get_json: ', res_get.json())
print('res_get_type: ', type(res_get.json()))
print('----------------')
print('res_post_code: ', res_post.status_code)
print('res_post_text: ', res_post.text)
print('res_post_json: ', res_post.json())
print('res_post_type: ', type(res_post.json()))
print('----------------')
print('res_put_code: ', res_put.status_code)
print('res_put_text: ', res_put.text)
print('res_put_json: ', res_put.json())
print('res_put_type: ', type(res_put.json()))
print('----------------')
print('res_del_code: ', res_del.status_code)
print('res_del_text: ', res_del.text)
print('res_del_json: ', res_del.json())
print('res_del_type: ', type(res_del.json()))
