# export FLASK_APP=webapp_mvp.py  export FLASK_DEBUG=1／n flask run
# python3 webapp_mvp.py
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
## 实现功能（0911）：
api返回储存到数据库
两次查询同样城市（同时防止写入一样的数据），不经过api，直接调用数据库行
封装SQlite函数
历史记录从db中取，还是从展示结果字段中打印？从展示结果打印，因为每次查询的城市不同

##优化点：
if语句嵌套太深，如何优化？
如果一个城市两次查询温度会变化，如何历史记录如何去重？
如何不重建表格，改变数据库table中temprature 数据类型，float/real 改成 int/integer
用户可以更新天气
进阶框架
"""

from flask import Flask, request, render_template, url_for
from search_weather import weather_query
import sqlite3


app = Flask(__name__)
history_list = []

def test_entry(city):
    conn = sqlite3.connect('weather_result.db')
    c = conn.cursor()
    t = (city, )
    c.execute('SELECT * FROM weather_result WHERE city=?', t)
    data_entry = c.fetchone()
    return data_entry

    conn.close()

def store_db(in_data):
    in_database = [in_data]
    conn = sqlite3.connect('weather_result.db')
    c = conn.cursor()
    c.executemany('INSERT INTO weather_result VALUES(?,?,?)', in_database)
    conn.commit()
    conn.close()

def fetch_db(city):
    conn = sqlite3.connect('weather_result.db')
    c = conn.cursor()
    new_key = (city, )
    c.execute('SELECT * FROM weather_result WHERE city=?', new_key)
    out_data = list(c.fetchone())
    weather = str(f'{out_data[0]}的天气{out_data[1]}，气温{out_data[2]}摄氏度 ')
    return weather

    conn.close()



@app.route('/') # 当访问网站的 "/" 页面时，将触发我们自定义的函数
def menu_layout():
    return render_template('weather.html')

@app.route('/user_input')
def weather_app():
    while True:
        if request.args.get('help') == "帮助":
            return render_template('user_guide.html')

        elif request.args.get('search') == "查询":
            city = request.args.get('city_name')
            try:
                data_entry = test_entry(city)
                if data_entry is None:
                    in_data = weather_query(city)
                    store_db(in_data)
                    weather = fetch_db(city)

                    history_list.append(weather)

                else:
                    out_data = list(data_entry)
                    weather = str(f'{out_data[0]}的天气{out_data[1]}，气温{out_data[2]}摄氏度 ')

                    history_list.append(weather)

                return render_template('result.html', weather=weather)

            except KeyError:
                return render_template('404.html')

        elif request.args.get('history') == "历史":
            entry = set(history_list)
            return render_template('history.html',entry=entry)



# adding this statement, appears making no difference
if __name__ == "__main__":
    app.run(debug=True)
