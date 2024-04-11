import json

data = {'name': 'John', 'age': 30, 'city': 'New York'}

# Convert Python dictionary to JSON string
json_string = json.dumps(data)

print(json_string)
