import json

# 딕셔너리 정의
my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}

# 딕셔너리를 JSON 문자열로 변환
json_str = json.dumps(my_dict)

print(type(json_str))