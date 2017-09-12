# python3 Py104_Ch2_realtime_weather2_1.py
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests, json

weather_dict = {'key':'kooevgqw7vj6lcro', 'location':'beijing', 'language':'zh-Hans',
'unit':'c', 'start':'0', 'days':'3'
}


r = requests.get('https://api.seniverse.com/v3/weather/daily.json', params = weather_dict)
weather_response = r.json()
print(r)
print(weather_response)



"""
# 此版本实现了国内城市天气中文查询，更简单的url组装
下一步行动：
1. 中文查询外国城市天气，API是否有权限，编码如何转换？
2. 从json中取出更多的值，比如播报时间、风向
3. 进阶任务

教练建议：
1. API 有提供查询不到结果的返回，可以判断一下再进行赋值
2. 用 try...except... 来捕获 KeyError 是一个办法，但如果可以根据 API 文档对各种情况的返回进行处理，就更好了
"""
