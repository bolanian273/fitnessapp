import uuid
import base64
from io import BytesIO
import matplotlib.pyplot as plt
import seaborn as sns

def generate_code():
    code = str(uuid.uuid4()).replace('-', '').upper()[:12]
    return code


def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph

def get_chart(chart_type, data, data21, **kwargs):
    plt.switch_backend('AGG')
    fig = plt.figure(figsize=(10, 5))
    key = "PT_Test_Date"
    data = data.drop(['id','cn_id','average'], axis=1)  
    data21 = data21.drop(['id','cn_id','average'], axis=1)
    if chart_type == '#1':
        # plt.bar(data['transaction_id'], data['price'])
        # sns.barplot(x=key, y="average", data=data)
        plt.style.use('seaborn')
        data.set_index(key).plot.bar()
        
        plt.legend(loc=2, prop={'size': 6})
        plt.xticks(rotation = 45)
        # sns.barplot(x = key, y = "push_ups", data = data)
        # sns.countplot(x=key, hue = 'push_ups', data = data)
    elif chart_type == '#2':
        # plt.plot(data21[key], data21['average'], color = 'green', marker='o', linestyle='dashed')
        plt.style.use('seaborn')
        # sns.set_style('dark')
        sns.lineplot(data=data21, x=key,y=data21['sit_ups'], lw=2.5,  marker='o', markersize= 9, label="SitUps" ).set(ylabel="Count")
        sns.lineplot(data=data21, x=key,y=data21['push_ups'], lw=2.5,  marker='o', markersize= 9, label="PushUps" )
        sns.lineplot(data=data21, x=key,y=data21['chin_ups'], lw=2.5,  marker='o', markersize= 9, label="ChinUps")
        sns.lineplot(data=data21, x=key,y=data21['One_Mile'], lw=2.5,  marker='o', markersize= 9, label="One Mile")
        sns.lineplot(data=data21, x=key,y=data21['Two_Miles'], lw=2.5, marker='o', markersize= 9, label="Two Miles")
        plt.legend(fontsize=7)
        plt.xticks(rotation = 45)


        # data21 = data21.pivot(key,"sit_ups","One_Mile","Two_Miles")
        # data21.head()
        # sns.lineplot(data=data21)
        # sns.lineplot(x=key, y=data21 ,data=data21)

        
    elif chart_type == '#3':
        plt.style.use('seaborn')
        data.set_index(key).plot.bar()
        plt.legend(loc=2, prop={'size': 6})
        plt.xticks(rotation = 45) 
        plt.style.use('fivethirtyeight')
        sns.lineplot(data=data21, x=key,y=data21[key], lw=4, color='green',  marker='X', markersize= 14, linestyle='dashed', alpha  = 0.5)   

              
        
    else:
        print('Error')
    plt.tight_layout()
    chart = get_graph()
    return chart