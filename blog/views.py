from django.shortcuts import render, get_object_or_404
from .models import Portfolio, Comment
from django.db.models import Avg

# Create your views here.



#def index(request):
#def create(request):
#def update(request, blog_id):
#def delete(request, blog_id):
def detail(request, blog_id):
    blog_detail = get_object_or_404(Portfolio, pk=blog_id)

    #평균별점 구하는 부분(참고 : 템플릿상에서 {{average}}값이 평균별점값)
    a = Comment.objects.filter(post=blog_id).aggregate(Avg('grade'))
    b = a['grade__avg']
    if b is None:
        average = 0
    else:
        average = round(b,1) 

    return render(request, 'detail.html', {'blog': blog_detail,"average":average})


#def comment(request, post_id):
#def co_update(request, post_id):
#def co_delete(request,post_id):