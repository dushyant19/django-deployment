from django.shortcuts import render

# Create your views here.
def index(request):
    dict = {'text':"i love you",'number':2000}
    return render(request,'template_url_app/index.html',dict)

def other(request):
    return render(request,'template_url_app/other.html')

def relative_url_template(request):
    return render(request,'template_url_app/relative_url_template.html')

