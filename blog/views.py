from django.shortcuts import render, redirect
from blog.models import Post, Restaurant
from django.views.generic import CreateView
from blog.forms import PostForm


# Create your views here.
def index(request):
    # 전체 포스팅을 가지고 올 준비 아직 안 가지고옴
    post_qs = Post.objects.all().order_by('-id')
    return render(request, 'blog/index.html', {
        'post_list' : post_qs, } )

def single_post_page(request, pk):
    post = Post.objects.get(pk=pk) # 값 그자체 keyword??
    return render(request, 'blog/single_post_page.html',{ 'post' : post ,})


def res_index(request):
    # 전체 포스팅을 가지고 올 준비 아직 안 가지고옴
    rest_qs = Restaurant.objects.all().order_by('-id')
    return render(request, 'blog/restaurants.html', {
        'res_list' : rest_qs, } )


def single_rest_page(request, pk):
    post = Restaurant.objects.get(pk=pk) # 값 그자체 keyword??
    return render(request, 'blog/single_rest_page.html',{ 'post' : post ,})





# post_new = CreateView.as_view(
#     form_class=PostForm,
#     model=Post,
#     success_url="/blog/",
# )

def post_new(request):
    # print("request.method = " , request.method)
    # print("request.post = " , request.POST)
    if request.method == "GET":
        form = PostForm()
    else:
        form = PostForm(request.POST)
        if form.is_valid():  # 유효성 검사?? 통과한 값들이 저장된 dict
            # form.cleaned_data
            post = form.save() # ModelForm  에서 지원
            # return redirect('/blog/')
            # return redirect(f"/blog/{ post.pk }/")
            # return redirect(post.get_absolute_url())
            return redirect(post)

    return render(request, "blog/post_form.html", {'form' :form, })


def res_new(request):
    # print("request.method = " , request.method)
    # print("request.post = " , request.POST)
    if request.method == "GET":
        form = PostForm()
    else:
        form = PostForm(request.POST)
        if form.is_valid():  # 유효성 검사?? 통과한 값들이 저장된 dict
            # form.cleaned_data
            post = form.save() # ModelForm  에서 지원
            # return redirect('/blog/')
            # return redirect(f"/blog/{ post.pk }/")
            # return redirect(post.get_absolute_url())
            return redirect(post)

    return render(request, "blog/rest_form.html", {'form' :form, })