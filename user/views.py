from django.views import generic
from django.shortcuts import render, redirect,reverse
from . models import User, Post
from .forms import UserForm, PostForm

class HomeView(generic.TemplateView):

    template_name = 'Home.html'



def user_create(request):
    form = UserForm()
    if request.method == "POST":
        print("----------------------------"*3)
        print('Receiving a post request')
        form = UserForm(request.POST)
        if form.is_valid():
            print("The form is valid")
            print(form.cleaned_data)
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email =form.cleaned_data['email']
            password = form.cleaned_data['password']
            username = form.cleaned_data['username']
            User.objects.create(
                first_name = first_name,
                last_name = last_name,
                email = email,
                password = password,
                username=username,
            )
            print("Lead has been created")


    context = {
        "form":UserForm()
    }
    return render(request, "user/create_user.html", context)



def Post_create(request):
    form = PostForm()
    if request.method == "POST":
        print("----------------------------"*3)
        print('Receiving a post request')
        form = PostForm(request.POST)
        if form.is_valid():
            print("The form is valid")
            print(form.cleaned_data)
            user = form.cleaned_data['user']
            text = form.cleaned_data['text']
            Post.objects.create(
                user = User.objects.all(),
                text = text,
                           )


    context = {
        "form":PostForm()
    }
    return render(request, "post/create_post.html", context)

def all_post(request):
    queryset = Post.objects.all()
    context = {
        "queryset":queryset
    }
    return render(request, "post/all_post.html",context)