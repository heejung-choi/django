from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostForm
from .models import Post
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

# Create your views here.
def index(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'posts/index.html', context)


@login_required
def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES) #사진도 같이 저장
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('posts:index')
    else:
        form = PostForm()
    context = {
        'form': form
    }
    return render(request, 'posts/form.html', context)
    # 랜더링을 해서 보내준다. -> 완전한 html 문서를 만들어준다. 사용자에게 리턴

@login_required
def like(request, pk):
    user = request.user
    post = get_object_or_404(Post, pk=pk)
    # user.like_posts => user가 좋아요 버튼을 누른 게시물들
    # post.like_users => post에 좋아요 버튼을 누른 유저들
    if post in user.like_posts.all():
        # 이미 누른경우
        user.like_posts.remove(post)
        liked = False
    else:
        # 아직 안누른경우
        user.like_posts.add(post)
        liked = True
    # return redirect('posts:index')
    context = {
        'msg': '좋아요 기능이 동작 했습니다.',
        'liked': liked
    }
    return JsonResponse(context)
    # key value , -> json
    # json을 파이썬 코드로 바꿔 준다.
    #{data: {…}, status: 200, statusText: "OK", headers: {…}, config: {…}, …}
    #config: {url: "/posts/5/like/", method: "get", headers: {…}, transformRequest: Array(1), transformResponse: Array(1), …}
    #data: {msg: "좋아요 기능이 동작 했습니다."}
    #headers: {content-length: "87", content-type: "application/json", date: "Fri, 26 Jun 2020 06:36:11 GMT", server: "WSGIServer/0.2 CPython/3.7.6", vary: "Cookie", …}
    #request: XMLHttpRequest {readyState: 4, timeout: 0, withCredentials: false, upload: XMLHttpRequestUpload, onreadystatechange: ƒ, …}
    #status: 200
    #statusText: "OK"
    #__proto__: Object
    # 클릭시 해당 요청이 나타나게 된다.