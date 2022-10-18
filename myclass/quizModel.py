import json
import requests

url= 'https://opentdb.com/api.php?amount=20&category=21&difficulty=medium&type=multiple'

response=requests.get(url)
result =response.json()['results']
file = open('quiz.txt', 'w')

print(result, file=file)
