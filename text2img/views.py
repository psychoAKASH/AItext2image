from django.shortcuts import render, HttpResponse, redirect
from text2img.generator import gene


# Create your views here.
def index(request):
    return render(request, 'index.html')


def about(request):
    return HttpResponse("this is the about page.")


def contact(request):
    return HttpResponse("this is the contact page.")


def genimg(request):
    img1 = {}
    img2 = {}
    img3 = {}
    if request.method == "POST":
        text = request.POST.get('prompt')
        result = gene(text)
        img1 = result[0]
        img2 = result[1]
        img3 = result[2]

    return render(request, 'genimg.html', {'response1': img1, 'response2': img2, 'response3': img3})


