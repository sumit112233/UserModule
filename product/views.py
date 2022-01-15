from django.shortcuts import render
from .forms import ProdForm
from .models import Product

def ProductCreate(request):
    form = ProdForm()
    if request.method == "POST":
        print("----------------------------"*3)
        print('Receiving a post request')
        form = ProdForm(request.POST)
        if form.is_valid():
            print("The form is valid")
            print(form.cleaned_data)
            name = form.cleaned_data['name']
            weight = form.cleaned_data['weight']
            price =form.cleaned_data['price']

            pro = Product.objects.create(
                name = name,
                weight = weight,
                price = price,

            )
            pro.save(using='prodb')

    context = {
        "form":ProdForm()
    }
    return render(request, "product/create_product.html", context)

def all_Product(request):
    queryset = Product.objects.all()
    context = {
        "queryset":queryset
    }
    return render(request, "product/all_product.html",context)