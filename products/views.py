from django.shortcuts import render, redirect, get_object_or_404
from .models import *

# 새로운 상품 생성
def create(request):
    if request.method == "POST": # POST 방식으로 요청이 들어오면
        name = request.POST.get('name') # <form>에서 name="name"인 <input>의 값을 가져와서 name이라는 변수에 담는다.
        description = request.POST.get('description') # <form>에서 name="description"인 <input>의 값을 가져와서 description이라는 변수에 담는다.
        price = request.POST.get('price') # <form>에서 name="price"인 <input>의 값을 가져와서 price라는 변수에 담는다.
        stock = request.POST.get('stock') # <form>에서 name="stock"인 <input>의 값을 가져와서 stock이라는 변수에 담는다.
        seller = request.user # 요청을 보낸 사용자(request.user)를 seller라는 변수에 담는다.
        image = request.FILES.get('image') # 이미지 파일을 image라는 변수에 담는다.
        Product.objects.create(name=name, description=description, price=price, stock=stock, seller=seller, image=image) # 상품 생성
        return redirect('products:main') # 상품을 생성하고 나서 메인 페이지로 이동한다.
    return render(request, 'products/new.html') # POST 방식의 요청이 아니라면 new.html을 띄워준다.


# 메인 페이지
def main(request):
    all_products = Product.objects.all().order_by('-created_at') # 모든 상품을 all_products라는 변수에 담는다.
    return render(request, 'products/main.html', {'products': all_products}) # main.html을 띄워주는데 products라는 이름으로 all_products를 가지고 간다.


# 상세보기 페이지
def show(request, product_id): # 상세보기는 특정 상품에 대한 페이지이기 때문에 어떤 상품의 상세보기인지 id값을 알아야 한다.
    show_product = get_object_or_404(Product, pk=product_id) # primary key가 전달받은 product_id와 일치하는 상품을 가져와서 product라는 변수에 담는다. 없으면 404 에러
    all_reviews = show_product.reviews.all().order_by('-created_at') # 해당 상품의 모든 리뷰를 all_reviews라는 변수에 담는다.
    return render(request, 'products/show.html', {'product': show_product, 'reviews': all_reviews}) # show.html을 띄워주는데 product라는 이름으로 show_product를, reviews라는 이름으로 all_reviews를 가지고 간다.


# 상품 수정
def update(request, product_id): # 상품 수정은 특정 상품에 대한 페이지/기능이기 때문에 어떤 상품을 수정하는지 id값을 알아야 한다.
    product = get_object_or_404(Product, pk=product_id) # primary key가 전달받은 product_id와 일치하는 상품을 가져와서 product라는 변수에 담는다. 없으면 404 에러
    if request.method == "POST": # POST 방식으로 요청이 들어오면
        product.name = request.POST['name'] # <form>에서 name="name"인 <input>의 값을 가져와서 name이라는 변수에 담는다.
        product.description = request.POST['description'] # <form>에서 name="description"인 <input>의 값을 가져와서 description이라는 변수에 담는다.
        product.price = request.POST['price'] # <form>에서 name="price"인 <input>의 값을 가져와서 price라는 변수에 담는다.
        product.stock = request.POST['stock'] # <form>에서 name="stock"인 <input>의 값을 가져와서 stock이라는 변수에 담는다.
        if request.FILES.get('image') != None: # 이미지가 있으면(None이 아니면)
            product.image = request.FILES.get('image') # 이미지 파일을 image라는 변수에 담는다.
        product.save() # 상품을 저장(값 업데이트)한다.
        return redirect('products:show', product.id) # 상세보기 페이지로 이동한다. 상세보기에서는 상품 id값을 알아야 하기 때문에 id값을 함께 보낸다.
    return render(request, 'products/edit.html', {"product": product}) # POST 방식의 요청이 아니라면 edit.html을 띄워준다.
    # 그런데 edit.html에서는 기존에 저장되어 있는 속성값을 보여줄 것이기 때문에 product라는 이름으로 product(변수에 담은 상품)를 가지고 간다.


# 상품 삭제
def delete(request, product_id): # 상품 삭제는 특정 상품에 대한 기능이기 때문에 어떤 상품을 삭제하는지 id값을 알아야 한다.
    product = get_object_or_404(Product, pk=product_id) # primary key가 전달받은 product_id와 일치하는 상품을 가져와서 product라는 변수에 담는다. 없으면 404 에러
    product.delete() # product라는 변수에 담긴 상품을 삭제(delete)한다.
    return redirect('products:main') # 메인 페이지로 이동한다.


# 리뷰 생성
def create_review(request, product_id):
    if request.method == "POST":
        product = get_object_or_404(Product, pk=product_id)
        current_user = request.user
        review_rating = request.POST.get('rating')
        review_content = request.POST.get('content')
        Review.objects.create(writer=current_user, rating=review_rating, content=review_content, product=product)
    return redirect('products:show', product_id)