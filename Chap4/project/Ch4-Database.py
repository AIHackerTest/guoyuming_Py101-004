# python3 Ch4-Database.py
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sqlite3
conn = sqlite3.connect('weather_result.db')
c = conn.cursor()

for row in c.execute('SELECT * FROM weather_result'):
     print(row)

# delete all records in the table
c.execute('DELETE FROM weather_result')
conn.commit()
conn.close()
# c.execute('''CREATE TABLE weather_result
#                 (city text,  condition text, temperature real)''')

# search_weather.weather_query(city)
# in_database = [(user_input, weather_condition, temperature)]
# c.executemany('INSERT INTO weather_result VALUES(?,?,?)', in_database)



# c.execute("INSERT INTO demo VALUES('2017-9-9', 198)")
#
# conn.commit()
#
# conn.close()
#
# # start to process
# # import sqlite3  # type directly in CLI
# conn = sqlite3.connect('example.db')
# c = conn.cursor()
#
# # three lines to query one mathcing row
# t = (26,)
# c.execute('SELECT * FROM weather_result WHERE temperature=?', t)
# print(c.fetchone())
#
# # insert multiple rows
# purchases = [('2017-9-10', '268'),
#              ('2017-9-11', '88')
#             ]
#
# c.executemany('INSERT INTO demo VALUES(?,?)', purchases)
#
# # query all rows by ascending selected colunm
# for row in c.execute('SELECT * FROM demo ORDER BY price'):
#     print(row)
# # query all rows by original order
# for row in c.execute('SELECT * FROM demo'):
#     print(row)
