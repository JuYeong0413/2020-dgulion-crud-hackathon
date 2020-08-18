from django.db import models
from django.contrib.auth.models import User

# 상품
class Product(models.Model):
    name = models.CharField(max_length=50) # 상품명
    description = models.TextField() # 설명
    price = models.IntegerField() # 가격
    stock = models.IntegerField() # 재고
    image = models.ImageField(upload_to='images/', null=True) # 이미지
    # upload_to='images/' => MEDIA_ROOT 안의 images/ 폴더 안에 저장한다.
    # null=True => 객체(오브젝트)를 생성할 때 없어도 된다.
    seller = models.ForeignKey(User, on_delete=models.CASCADE) # 판매자
    # ForeignKey(1:N 관계) => 한 명의 사용자(User)는 여러 개의 상품(Product)을 등록할 수 있다.
    # on_delete=models.CASCADE => 1(사용자)인 쪽의 데이터가 삭제되면 N(상품)은? 같이 지운다(CASCADE).
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)


# 후기
class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews') # 상품
    # ForeignKey(1:N 관계) => 한 명의 상품(Product)에는 여러 개의 후기(Review)가 달릴 수 있다.
    # on_delete=models.CASCADE => 1(상품)인 쪽의 데이터가 삭제되면 N(후기)은? 같이 지운다(CASCADE).
    # related_name='reviews' => 역으로 추적할 때 사용할 이름
    # 1:N 관계에서 1쪽에서 N에 접근하기 위해서는 set을 사용한다. related_name을 설정해주면 set 대신 사용할 수 있다. (동일한 기능임)
    # >>> from products.models import *
    # >>> first_product = Product.objects.get(pk=1)
    # >>> first_product.reviews
    writer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True) # 작성자
    # ForeignKey(1:N 관계) => 한 명의 사용자(User)는 여러 개의 후기(Review)를 등록할 수 있다.
    # on_delete=models.SET_NULL => 1(사용자)인 쪽의 데이터가 삭제되면 N(후기)은? null로 값을 대체한다.
    # (사용자가 탈퇴한다고 해서 후기까지 모두 없애는것보다 "탈퇴한 작성자" 등으로 표시하는 게 적절하다고 판단함)
    # SET_NULL 로 지정해주었기 때문에 null=True도 함께 작성해주었다.
    rating = models.IntegerField() # 평점
    content = models.TextField() # 내용
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)