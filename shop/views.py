from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Contact
from math import ceil
# Create your views here.

def index(request):
    # products = Product.objects.all()
    
    # n = len(products)
    # nSlides = n//4 + ceil((n/4) - (n//4))
    # params={'No_of_slides':nSlides, 'range':range(1,nSlides), 'product': products }
    # allprods = [[products,range(1,nSlides),nSlides],[products,range(1,nSlides),nSlides]]
   
    allprods = []
    catprods = Product.objects.values('category' , 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n//4 + ceil((n/4) - (n//4))
        allprods.append([prod,range(1,nSlides),nSlides])

    params = {'allprods': allprods}
    return render(request,'shop/index.html', params)

def about(request):
    return render(request,'shop/about.html')

def contact(request):
    if request.method=="POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        address = request.POST.get('address', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        query = request.POST.get('query', '')
        pin = request.POST.get('pin', '')
        password = request.POST.get('password', '')
        contact = Contact(name=name, email=email, phone=phone, address=address, city=city, state=state, query=query, pin=pin, password=password)
        contact.save()
      
    return render(request,'shop/contact.html')

def tracker(request):
    return render(request,'shop/tracker.html')

def search(request):
    return render(request,'shop/search.html')

def productView(request, myid):
    # fetch the product using the id
    product = Product.objects.filter(id = myid)
    

    return render(request,'shop/prodview.html', {'product': product[0]})

def checkout(request):
    return render(request,'shop/checkout.html')


def login(request):
    return render(request,'shop/login.html')