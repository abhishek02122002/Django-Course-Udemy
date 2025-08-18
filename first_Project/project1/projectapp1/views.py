from django.shortcuts import render
from django.http import HttpResponse;

def show_data(request):
    data = {
        'name': 'Abhishek',
        'age': 20,
        'country': 'India',
    }
    return render(request, 'myapp/show_data.html', {'my_dict': data})

def getData(request):
    name= request.GET.get("myname")
    a =request.GET.get('a')
    b =request.GET.get('b')
    sum = int(a)+int(b);
    return HttpResponse(f"The name is{name} and the sum is {sum}");

def calculate(request):
     val1 = request.GET.get('v1');
     val2 = request.GET.get('v2');
     try: 
         val1 = int(val1) ;
         val2 = int(val2);
         return HttpResponse(f"Sum is {int(val1)+ int(val2)}")
     except ValueError:
         return HttpResponse("invalid one ")