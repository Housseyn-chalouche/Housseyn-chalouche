import sqlite3


conn = sqlite3.connect('todo.db')
print('database opend succesfuly')

cur = conn.execute('select * from users join tasks on users.user_id=tasks.user_id where users.user_name like('hocine%')
for curser in cur:
    print(cur,'\n')

                   # "select sqlite_version()" sqlite version
                   # second line on the branch1
conn.close()
