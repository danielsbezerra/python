#!/bin/python3

# pipenv run python3 main.py

import json, requests
# HTTP (requests or urllib2)
# Decode (json, simplejson or any XML lib)


# Obtain all objects
response = requests.get("http://jsonplaceholder.typicode.com/comments")
print(response.status_code)
print(response.content)
comments = json.loads(response.content)
# # print(comments[0]["body"])
for comment in comments[0:5]:
        print(comment["name"])


# Obtain a specifc object
response = requests.get("http://jsonplaceholder.typicode.com/comments/5")
# post = requests.get("http://jsonplaceholder.typicode.com/posts/%d" % comment["postId"])
print(response.status_code)
print(response.content)
comment = json.loads(response.content)
print(comment["name"])


# Insert data
user_post = {"postId": 1, "name": "John Doe The Second", "email": "john@doe2.com", "body": "This is my simple post!"}
response = requests.post("http://jsonplaceholder.typicode.com/comments/", data=user_post)
print(response.status_code)
print(response.content)


# Replace data
query = {"email": "john@doe2.com"}
response = requests.put("http://jsonplaceholder.typicode.com/comments/10", data=query)
print(response.status_code)
print(response.content)


# Delete data
response = requests.delete("http://jsonplaceholder.typicode.com/comments/10")
print(response.status_code)
print(response.content)