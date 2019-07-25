from django.shortcuts import render

# Create your views here.



def index(request):
    return render(request, 'index.html')

#def create(request):
#def update(request, blog_id):
#def delete(request, blog_id):
#def detail(request, blog_id):


#def comment(request, post_id):
#def co_update(request, post_id):
#def co_delete(request,post_id):