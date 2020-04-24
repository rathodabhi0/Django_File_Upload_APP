from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.core.files.storage import FileSystemStorage
from .models import ls_20
from .forms import DocumentForm

# Create your views here
import pandas as pd
import json

def base(request):
    return render(request, 'base.html')
def upload(request):
    return render(request,'upload.html')

def apidata(request):
    context = {}
    df = pd.read_csv('election/LS_20.csv')
    df2 = df[['PARTY', 'TOTAL VOTES']].groupby(['PARTY'], as_index=False).sum()
    df3 = df[['TOTAL VOTES'][0]].sum()
    df2['Vote_share'] = ((df2['TOTAL VOTES'] / df3) * 100)
    df4 = df2.sort_values(by=['Vote_share'], ascending=False)
    df19 = df4[['PARTY', 'Vote_share']]
    data1 = pd.Series(df19.Vote_share.values, index=df19.PARTY).to_dict()
    context['data'] = data1
    return JsonResponse(data1)
    # elif request.method == 'GET':
    #     data_try = request.GET.get('document')
    #     print(data_try)
    #     return render(request, 'upload.html')

def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('upload')
    else:
        form = DocumentForm()
    return render(request, 'model_form_upload.html', {
        'form': form
    })


def get_data(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        df = pd.read_csv(uploaded_file)
#        list1 = df.columns
#        print(list(list1))
        df2 = df[['PARTY', 'TOTAL VOTES']].groupby(['PARTY'], as_index=False).sum()
        df3 = df[['TOTAL VOTES'][0]].sum()
        df2['Vote share'] = ((df2['TOTAL VOTES'] / df3) * 100)
        df4 = df2.sort_values(by=['Vote share'], ascending=False)
        data = df4.to_dict()
        data1= json.dump(data)
        context = data1
        return render(request, 'data.html')
