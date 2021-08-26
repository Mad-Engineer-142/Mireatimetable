from flask import Flask, render_template
import pandas as pd
import json
import re

data = pd.read_excel('1.xlsx')
data = data.where(pd.notnull(data), None)

data_top = data.head(15) 
data_dd = data.loc[:4] #выводит 2 строчки
data_dd = data_dd.iloc[:,:4]#предметы data.iloc[:,3] кабинеты

def norm(aa):
    for i in range(len(aa)):
        if aa[i] != None:
            aa[i] = re.sub(" +", " ", str(aa[i]))
    return aa 


#print(data_dd)

time = norm(data_dd['Unnamed: 1'].tolist())

aa = norm(data_dd['1 КУРС'].tolist())
aud = norm(data_dd['Unnamed: 3'].tolist())

print('___________')
print(aud)
print('___________')
#json_dump = json.dumps(aa[0]:{[data_dd['Unnamed: 0'].tolist()[1], {'bar': ('baz', None, 1.0, 2)}]})
json_dump = json.dumps([aa[0], {data_dd['Unnamed: 0'].tolist()[1]: [[time[1],aa[1],aud[1]], [time[2],aa[2],aud[2]], [time[3],aa[3],aud[3]], [time[4],aa[4],aud[4]]]}], ensure_ascii=False).encode('utf8')
#'group':


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('a.html', variable=json_dump.decode())

if __name__ == '__main__':
    app.run()