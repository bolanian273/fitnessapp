from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, TemplateView
from .models import Fitness, Cadet_Bio, Threshold, CSV
from report.forms import ReportForm
from .forms import FitnessGraphForm
from .utils import get_chart
import pandas as pd
import json
import csv
from django.utils.dateparse import parse_date
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse


# Create your views here.

class UploadTemplateView(TemplateView):
    template_name = 'fitness_analyser/upload.html'


def csv_upload_view(request):
    print("CSV Success")

    if request.method == 'POST':
        csv_file_name = request.FILES.get('file').name
        csv_file = request.FILES.get('file')
        obj, created = CSV.objects.get_or_create(file_name=csv_file_name)
        if created:
            obj.csv_file = csv_file
            obj.save()
            with open(obj.csv_file.path, 'r') as f:
                reader = csv.reader(f)
                reader.__next__()
                reader.__next__()
                for row in reader:
                    print(row)
                    data = row
                    c_n = int(data[0])
                    push_up = int(data[1])
                    chin_up = int(data[2])
                    sit_up = int(data[3])
                    onemile = int(data[4])
                    twomiles = int(data[5])
                    PTdate = parse_date(data[6])

                    try:
                        cadet_obj = Cadet_Bio.objects.get(C_N=c_n)

                    except Cadet_Bio.DoesNotExist:
                        cadet_obj = None

                    if cadet_obj is not None:
                        fitness_obj = Fitness.objects.create(push_ups=push_up, chin_ups=chin_up, sit_ups=sit_up,
                                                             One_Mile=onemile, Two_Miles=twomiles, cn=cadet_obj,
                                                             PT_Test_Date=PTdate)

                        fitness_obj.save()
                        # return JsonResponse({'ex': False})
        else:
            return JsonResponse({'ex': True})

    return HttpResponse()


@login_required
def home_view(request):
    hello = 'Hello world from the view'
    return render(request, 'fitness_analyser/home.html', {
        'hello': hello
    })


@login_required
def fitness_list_view(request):
    df1 = None
    df2 = None
    cadet_df_merged = None
    qs = Fitness.objects.all()
    qs1 = Cadet_Bio.objects.all()
    qs77 = Threshold.objects.all().values()
    qs_df = pd.DataFrame(qs1.values())
    if len(qs) > 0:
        df1 = pd.DataFrame(qs.values())
        # print(df1)
        print('####################')
        df2 = df1.groupby(['cn_id'], as_index=False).agg({'average': ['mean']})
        df2.columns = list(map(''.join, df2.columns.values))
        # df2 = df1.groupby(['cn_id']).agg({'average': 'mean'})
        df2.rename({'cn_id': 'C_No'}, axis=1, inplace=True)
        df2.rename({'averagemean': 'Avg'}, axis=1, inplace=True)
        df2['Avg'] = df2['Avg'].apply(lambda x: round(x, 2))
        qs_df.rename({'C_N': 'C_No'}, axis=1, inplace=True)
        qs_df.rename({'date_joined': 'JoinedOn'}, axis=1, inplace=True)
        # qs_df.drop(['id','JoinedOn'], axis=1, inplace=True)
        cadet_df_merged = pd.merge(qs_df, df2, on='C_No')
        df2 = df2.to_html()
        qs_df = qs_df.to_html()
        cadet_df_merged1 = cadet_df_merged.to_html()

        # DF to json converter
        json_records = cadet_df_merged.reset_index().to_json(orient='records')
        data = []
        data = json.loads(json_records)

    else:
        print('no data')

    context = {
        'df2': df2,
        'qs_df': qs_df,
        'cadet_df_merged': cadet_df_merged1,
        'd': data,
        'qs77': qs77,
    }

    return render(request, 'fitness_analyser/main.html', context)


@login_required
def fitness_detail_view(request, id):
    no_data = None
    date_from = None
    date_to = None
    chart_type = None
    obj1 = None
    df1 = None
    chart = None
    chart1 = None
    chart2 = None
    f_id = id
    form = FitnessGraphForm(request.POST or None)
    report_form = ReportForm()
    obj = get_object_or_404(Cadet_Bio, pk=id)
    if request.method == 'POST':
        date_from = request.POST.get('date_from')
        date_to = request.POST.get('date_to')
        chart_type = request.POST.get('chart_type')
        obj1 = Fitness.objects.filter(cn_id=id).filter(PT_Test_Date__gte=date_from).filter(PT_Test_Date__lte=date_to)
        if len(obj1) > 0:
            df1 = pd.DataFrame(obj1.values())
            df1['PT_Test_Date'] = df1['PT_Test_Date'].apply(lambda x: x.strftime('%B-%Y'))
            df21 = df1
            # if chart_type == '#3':
            #     chart1, chart2 = get_chart(chart_type, df1, df21)
            # else:
            chart = get_chart(chart_type, df1, df21)

            df1 = df1.to_html()

        else:
            no_data = "No data is available in this Date Range"

    context = {
        'fid': f_id,
        'object': obj,
        'qrf': obj1,
        'form': form,
        'df1': df1,
        'chart': chart,
        'chart1': chart1,
        'chart2': chart2,
        'report_form': report_form,
        'no_data': no_data,
    }
    return render(request, 'fitness_analyser/detail.html', context)
