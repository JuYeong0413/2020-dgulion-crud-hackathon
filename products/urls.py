from django.urls import path
from .views import *

app_name="products"
# 앱 이름은 모델(Product)의 복수형(products)으로 지정해 주는 것이 좋다.
# (python manage.py startapp에서부터 복수형을 사용하는 것을 권장함)

# shoppingmall/urls.py에서 products의 urls.py를 products/를 붙여서 include하고 있기 때문에 아래의 path에 실제로는 products/가 붙는다는 점을 염두할 것
urlpatterns = [
    path('', main, name="main"), # url에 아무것도 입력하지 않은 경로의 이름(name)은 main, products의 views에 있는 main 함수를 실행한다.
    path('new/', create, name="create"), # url에 new/ 가 붙은 경로의 이름(name)은 create, products의 views에 있는 create 함수를 실행한다.
    path('<int:product_id>/', show, name="show"),
    # url에 상품 id가 붙은 경로의 이름(name)은 show, products의 views에 있는 show 함수를 실행한다.
    # product_id의 값으로 상품 id값을 가지고 넘어간다.
    path('<int:product_id>/edit/', update, name="update"),
    # url에 상품 id/edit이 붙은 경로의 이름(name)은 update, products의 views에 있는 update 함수를 실행한다.
    # product_id의 값으로 상품 id값을 가지고 넘어간다.
    path('<int:product_id>/delete/', delete, name="delete"),
    # url에 상품 id/delete가 붙은 경로의 이름(name)은 delete, products의 views에 있는 delete 함수를 실행한다.
    # product_id의 값으로 상품 id값을 가지고 넘어간다.
    path('<int:product_id>/create_review', create_review, name="create_review"),
    # url에 상품 id/create_review가 붙은 경로의 이름(name)은 create_review, products의 views에 있는 create_review 함수를 실행한다.
    # product_id의 값으로 상품 id값을 가지고 넘어간다.
    path('<int:review_id>/edit_review', update_review, name="update_review"),
    # url에 리뷰 id/edit_review가 붙은 경로의 이름(name)은 update_review, products의 views에 있는 update_review 함수를 실행한다.
    # review_id의 값으로 리뷰 id값을 가지고 넘어간다.
    path('<int:review_id>/delete_review', delete_review, name="delete_review"),
    # url에 리뷰 id/delete_review가 붙은 경로의 이름(name)은 delete_review, products의 views에 있는 delete_review 함수를 실행한다.
    # review_id의 값으로 리뷰 id값을 가지고 넘어간다.
    path('<int:product_id>/like', like_product, name="like_product"),
    # url에 상품 id/like가 붙은 경로의 이름(name)은 like_product, products의 views에 있는 like_product 함수를 실행한다.
    # product_id의 값으로 상품 id값을 가지고 넘어간다.
    path('likes/', like_list, name="like_list"), # url에 likes/ 가 붙은 경로의 이름(name)은 like-list, products의 views에 있는 like-list 함수를 실행한다.
]
# Django 템플릿 태그(template tag)로 url을 작성할 때 {% url '앱이름:path이름' %} 의 형태로 작성한다.
# {% url 'products:show' product.id %}
# => products라는 이름의 앱에 show라는 이름을 가진 path로 가는데 product.id값을 가지고 간다.
# 이 때 product.id는 name="show"인 path의 <int:product_id> 자리에 담기게 된다.
# name="show"인 path는 views의 show 함수로 연결된다. product_id 자리에 product.id값을 가지고 함수로 넘어간다.
# def show(request, product_id):
# 여기서 product_id가 url에 전달된 id값(<int:product_id>)와 동일함