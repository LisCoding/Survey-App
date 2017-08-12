from django.shortcuts import render, HttpResponse, redirect

def index(request):
    return render(request,'survey_app/index.html')


def process(request):
    try:
        request.session['count']
    except KeyError:
        request.session['count'] = 0
    request.session['name'] = request.POST['f_name']
    request.session['location'] = request.POST['locations']
    request.session['language'] = request.POST['leng']
    request.session['comment'] = request.POST['comment']
    request.session['count'] += 1
    return redirect('/survey/result')

def result(request):
    return render(request,'survey_app/result.html')

def back(request):
    return redirect('/')
