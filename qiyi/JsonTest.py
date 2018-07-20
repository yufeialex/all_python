# 1、json.dumps()和json.loads()是json格式处理函数（可以这么理解，json是字符串）
# 2、json.dump()和json.load()主要用来读写json文件函数

import json

# json.dumps()函数的使用，将字典转化为字符串
dict1 = {"age": "12"}
json_info = json.dumps(dict1)
print("dict1的类型：" + str(type(dict1)))
print("通过json.dumps()函数处理：")
print("json_info的类型：" + str(type(json_info)))

# json.loads函数的使用，将字符串转化为字典
json_info = '{"age": "12"}'
dict1 = json.loads(json_info)
print("json_info的类型：" + str(type(json_info)))
print("通过json.dumps()函数处理：")
print("dict1的类型：" + str(type(dict1)))

# json.dump()函数的使用，将json信息写进文件
json_info = "{'age': '12'}"
file = open('1.json', 'w', encoding='utf-8')
json.dump(json_info, file)

# json.load()函数的使用，将读取json信息
file = open('1.json', 'r', encoding='utf-8')
info = json.load(file)
print(info)

res = '{"highlight_score": [[399.52, 408.52, 0.07090245932340622], [408.52, 417.52, 0.06075265631079674]], ' \
      '"qipu_id": "1181511500"}'
res = json.loads(res)
aa = dict()
aa['highlight_score'] = res['highlight_score']
print(aa['highlight_score'])
