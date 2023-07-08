import pandas as pd
import sqlite3
import subprocess

subprocess.run(['scp', 'fyq@172.105.203.41:~/Diagnosis-of-pneumoconiosis/flaskblog/site.db', './site.db'])
conn = sqlite3.connect('site.db')


df = pd.read_sql('SELECT * FROM user', conn)
df.to_csv('user.csv')
print(df)

df = pd.read_sql('SELECT * FROM xray', conn)

df.to_csv('xray.csv')
print(df)

