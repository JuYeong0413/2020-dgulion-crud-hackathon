from django.shortcuts import render, redirect, get_object_or_404
from .models import Product

# Create your views here.
def create(request):
    if request.method == "POST":
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        stock = request.POST.get('stock')
        seller = request.user
        image = request.FILES.get('image')
        Product.objects.create(name=name, description=description, price=price, stock=stock, seller=seller, image=image)
        return redirect('products:main')
    return render(request, 'products/new.html')


def main(request):
    all_products = Product.objects.all()
    return render(request, 'products/main.html', {'products': all_products})


def show(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'products/show.html', {'product': product})


def update(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.method == "POST":
        product.name = request.POST['name']
        product.description = request.POST['description']
        product.price = request.POST['price']
        product.stock = request.POST['stock']
        product.image = request.FILES.get('image')
        product.save()
        return redirect('products:show', product.id)
    return render(request, 'products/edit.html', {"product": product})


def delete(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    return redirect('products:main')
