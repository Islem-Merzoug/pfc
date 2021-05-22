from django.shortcuts import render

import requests
import sys
import subprocess

from subprocess import run, PIPE

def button(request):
    return render(request, 'home.html')

def output(request):
    data = requests.get("https://reactnative.dev/movies.json")
    print(data.text)
    data = data.text
    return render(request, 'home.html', {'data': data})

def external(request):
    inp = request.POST.get('param')

    out = run([sys.executable, '//home//islem//Documents//full_projects//PFEenv//src//test.py', inp], shell=False, stdout=PIPE)
    # out = run([sys.executable, 'src/Skin_Segmentation/Script/unet2d_model_prediction2.py', inp], shell=False, stdout=PIPE)

    print(out)
    return render(request, 'home.html', {'data1': out.stdout} )