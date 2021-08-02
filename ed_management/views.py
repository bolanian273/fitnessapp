from django.shortcuts import render,get_object_or_404,redirect
from django.http import JsonResponse
from fitness_analyser.models import Fitness, Cadet_Bio
from .models import ED
from threshold_managment.models import Threshold
from authorized_user.models import CustomUser
from .forms import Increment
import pandas as pd
import json

# Create your views here.


def ED_View(request):  # sourcery no-metrics

	for e in Cadet_Bio.objects.all():
			for f in ED.objects.all():
				if f.cn.C_N != e.C_N:
					c = Cadet_Bio.objects.get(C_N=e.C_N)
					ff = ED.objects.get_or_create(cn=c)
					f.ED_count = 0

	for _ in range(2):

		form = Increment(request.POST or None)
		df1 = None
		df2 = None
		cadet_df_merged = None
		
		# print(ed.values())			

		qs = Fitness.objects.all()
		qs1 = Cadet_Bio.objects.all()
		qs_df = pd.DataFrame(qs1.values())

		ed = ED.objects.all()
		ed = pd.DataFrame(ed.values())
		# print(ed)
		if len(qs) > 0:
			df1 = pd.DataFrame(qs.values())
			# # print(df1)
			# print('####################')
			df2 = df1.groupby(['cn_id'], as_index=False).agg({'average':['mean']})
			df2.columns = list(map(''.join,df2.columns.values))
			# df2 = df1.groupby(['cn_id']).agg({'average': 'mean'})
			df2.rename({'cn_id': 'C_No'}, axis=1, inplace=True)
			ed.rename({'cn_id': 'C_No'}, axis=1 , inplace=True)
			df2.rename({'averagemean': 'Avg'}, axis=1, inplace=True)
			df2['Avg']=df2['Avg'].apply(lambda x:round(x,2))
			qs_df.rename({'C_N': 'C_No'}, axis=1,inplace=True)
			qs_df.rename({'date_joined': 'JoinedOn'}, axis=1,inplace=True)
			# qs_df.drop(['id','JoinedOn'], axis=1, inplace=True)
			ed.drop(['id'], axis=1, inplace=True)
			cadet_df_merged = pd.merge(qs_df, df2 ,on='C_No')
			cadet_df_merged = pd.merge(cadet_df_merged,ed,on='C_No')

			# cadet_df_merged.insert(4, 'NewCol1', 'Bre')
			cadet_df_merged.drop(['JoinedOn'], axis=1, inplace=True)
			# print(cadet_df_merged)
			# print(cadet_df_merged['Avg'])
			# print(cadet_df_merged['ED_count'])

			for th in Threshold.objects.all():

				data_q = cadet_df_merged.loc[(cadet_df_merged['Avg'] < th.Fitness_Standard_per) & (cadet_df_merged['ED_count'] <= 0)] 
				dicti = data_q.to_dict('records')
				# print(data_q)
				for dic in dicti:
					for val,cal in dic.items():
						if val == 'C_No':
							ed1 = ED.objects.get(cn_id=cal)
							ed1.ED_count += 2
							ed1.save()


				data_q1 = cadet_df_merged.loc[(cadet_df_merged['Avg'] >= th.Fitness_Standard_per) & (cadet_df_merged['ED_count'] > 0)]
				# print(data_q1)
				dicti1 = data_q1.to_dict('records')
				for dic in dicti1:
					for val,cal in dic.items():
						if val == 'C_No':
							ed1 = ED.objects.get(cn_id=cal)
							ed1.ED_count *= 0
							ed1.save() 

			cadet_df_merged.drop(['ED_count'], axis=1, inplace=True)
			# print(cadet_df_merged)
			ed1 = ED.objects.all()
			ed1 = pd.DataFrame(ed1.values())
			# print(ed1)
			ed1.rename({'cn_id': 'C_No'}, axis=1 , inplace=True)
			ed1.drop(['id'], axis=1, inplace=True)
			cadet_df_merged2 = pd.merge(cadet_df_merged,ed,on='C_No')
			# print(cadet_df_merged2)

			cadet_df_merged1=cadet_df_merged.to_html()
			#DF to json converter
			json_records = cadet_df_merged2.reset_index().to_json(orient='records')
			data = []
			data = json.loads(json_records)
	context = {

		'form':form,
		'df':cadet_df_merged1,
		'd':data,
	}

	return render(request, 'ed_management/ed.html', context)



def Update_ED(request,id):
	ed = ED.objects.get(cn_id=id)
	form = Increment()
	if request.method == 'POST':
		# print(request.POST)
		data = (request.POST.get('ED_count'))
		data = int(data)
		# print(type(data))
		form = Increment(request.POST)
		if form.is_valid():
			# print("Pass")
			if ed.ED_count == 0 and data < 0:
				print("Very Funny")
			else:
				ed.ED_count += data
				ed.save()
	
	return redirect('ed_management:ED')