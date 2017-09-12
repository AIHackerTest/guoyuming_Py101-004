# export FLASK_APP=webapp_mvp.py  export FLASK_DEBUG=1／n flask run
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
##changelog：
1 历史记录去重、分行显示

bug处理：
返回异常值也写入history，想明白为什么，如何捕捉并排除它们

迭代优化：
输入城市为空、点击查询返回友好提示
无历史记录时，点击历史，友好反馈
"""

from flask import Flask, request, render_template, url_for
from search_weather import weather_query


app = Flask(__name__)
history_list = []

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
                weather_result = weather_query(city)
                history_list.append(weather_result)
                return render_template('result.html', weather_result=weather_result)
            except KeyError:
                return render_template('404.html')

        elif request.args.get('history') == "历史":
            entry = set(history_list)
            return render_template('history.html',entry=entry)






# adding this statement, appears making no difference
if __name__ == "__main__":
    app.run()
