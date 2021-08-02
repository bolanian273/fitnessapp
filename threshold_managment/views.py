from django.shortcuts import render, get_object_or_404, redirect
from .models import Threshold
from .forms import Fitness_Standard


# Create your views here.
def TM_View(request):
    form = Fitness_Standard()
    th = Threshold.objects.all()
    th = th.values()
    print(th)

    context = {
        'form': form,
        'th': th,

    }

    return render(request, 'threshold_managment/main.html', context)


def update_View(request):
    print(request.method)
    print(request.POST)
    thh = Threshold.objects.get(id=1)

    print(thh)
    form = Fitness_Standard()
    if request.method == 'POST':
        _extracted_from_update_View_9(request, thh)
    return redirect('threshold_managment:TH')


def _extracted_from_update_View_9(request, thh):
    print(request.POST)
    data = (request.POST.get('Fitness_Standard_per'))
    data = int(data)
    print(type(data))
    form = Fitness_Standard(request.POST)
    if form.is_valid():
        print("Pass")
        if data < 50:
            print("Very Funny")
        else:
            thh.Fitness_Standard_per = data
            # self.Threshold.User ='admin'
            thh.save()

# def Update_ED(request,id):
# 	ed = ED.objects.get(cn_id=id)
# 	form = Increment()
# 	if request.method == 'POST':
# 		print(request.POST)
# 		data = (request.POST.get('ED_count'))
# 		data = int(data)
# 		print(type(data))
# 		form = Increment(request.POST)
# 		if form.is_valid():
# 			print("Pass")
# 			ed.ED_count += data
# 			ed.save()

# 	return redirect('ed_management:ED')
