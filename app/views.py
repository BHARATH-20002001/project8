from django.shortcuts import render

# Create your views here.
def forloop(request):
    d={'name':'Bharath','age':22,'contactme':'984390****'}
    return render(request,'forloop.html',context=d)

