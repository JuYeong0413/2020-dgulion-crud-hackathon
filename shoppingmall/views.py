from django.shortcuts import render

# 메인 페이지
def main(request):
    return render(request, 'main.html') # main.html을 띄워준다.
