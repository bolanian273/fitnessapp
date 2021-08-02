from django.shortcuts import render
from fitness_analyser.models import Cadet_Bio
from authorized_user.models import CustomUser
from django.http import JsonResponse
from .utils import get_report_image
from .models import Reports
from datetime import date

from django.conf import settings
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa


# Create your views here.

def create_report_view(request):
    if request.method == 'POST':
        today = date.today()
        print("Today's date:", today)
        cn = request.POST.get('cn')
        cadet_obj = Cadet_Bio.objects.get(C_N=cn)
        subj = request.POST.get('name')
        remarks = request.POST.get('remarks')
        image = request.POST.get('image')

        img = get_report_image(image)

        # obj = Reports.objects.create(cn=cadet_obj, name=name, image=image, remarks=remarks)

        # print(cadet_obj.C_N, cadet_obj.name, cadet_obj.entry, cadet_obj.house, name, remarks, image)
        print(img)
        print("####")
        print(type(img))
        # print(type(cn), type(name), type(remarks), type(today))

        context = {
            'date': today,
            'cn': cadet_obj.C_N,
            'name': cadet_obj.name,
            'entry': cadet_obj.entry,
            'house': cadet_obj.house,
            'remarks': remarks,
            'subj':subj,
            'img': image,
        }
        # render_pdf_view(context)
    return render_pdf_view(context)


def render_pdf_view(context):
    template_path = 'report/pdf.html'
    # obj = Report.objects.get(pk=pk)
    # obj = get_object_or_404(Report, pk=pk)
    context = context

    print("%%%%%%%%%%%%%")
    # print(context)
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    # if download
    # response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    # if display
    response['Content-Disposition'] = 'filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response
