import pandas as pd
import json
import re
from flask import Flask, render_template
import sys
sys.stdout.encoding  # 'UTF-8'

data = pd.read_excel('1.xlsx')
data = data.where(pd.notnull(data), None)

data_top = data.head(15) 
#data_dd = data.loc[:4] #выводит 2 строчки
data_dd = data.iloc[:,:4]#предметы data.iloc[:,3] кабинеты

def norm(aa):
    for i in range(len(aa)):
        if aa[i] != None:
            aa[i] = re.sub(" +", " ", str(aa[i]))
    return aa 


#print(data_dd)


aa = norm(data_dd['1 КУРС'].tolist())
aud = norm(data_dd['Unnamed: 3'].tolist())



dic = {"monday":[["value", 'i','hate','niggers'],['damn','yra','is','gay']],"tuesday":["value", 'i','hate','niggers'] }
group = aa[0]
group = re.sub(" ", "", group)
#print(group)
#print('______________________')
aa = aa[1:]
aud = aud[1:]
dic ={
    "week":"0",#0 - четная, 1 - нечетная
    group: [
        { "monday":aa[:4],'auditory':aud[:4]},
        { "tuesday":aa[6:10],'auditory':aud[6:10]},
        { "wednesday":aa[12:16],'auditory':aud[12:16]},
        { "thursday":aa[18:22],'auditory':aud[18:22]},
        { "friday":aa[24:28],'auditory':aud[24:28]}
     ]
 } 
# Вариант 1
import json

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False

@app.route('/')
def index():
    return render_template('a.html', variable=json.dumps(dic, indent=4, sort_keys=True,ensure_ascii=False))

if __name__ == '__main__':
    app.run()
