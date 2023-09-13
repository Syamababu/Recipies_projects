from django.shortcuts import render,redirect
from django.contrib.auth.models import User
# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from htmlapp.models import Recipe


def home(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def furniture(request):
    return render(request,'furniture.html')

@csrf_exempt
def login_page(request):
    if request.method=='POST':
        user_name = request.POST.get('user_name')
        password = request.POST.get('password')
        user = authenticate(username=user_name, password=password)
        # print('=====User.objects.filter(username=username)=====',User.objects.filter(username=user_name))
        # print('======username=====,',user_name)
        # # if username!=User.objects.filter(username=username).values:
        # #     messages.info(request, "username not register yet.")
        # #     return redirect('/login/')
        # print('=====user=======',user)
        if user is None:
            messages.info(request, "Invalid credential.")
            return redirect('/login/')
        else:
            login(request, user)
            return render(request, 'index.html', {'name' : user_name })
    return render(request, 'login.html')

@csrf_exempt
def register(request):
    if request.method=='POST':
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        username=request.POST.get('user_name')
        password=request.POST.get('password')

        user = User.objects.create_user(
            first_name=first_name,last_name=last_name,username=username,password=password
        )      
        user.set_password(password)
        user.save()
        messages.info(request, "Account created successfully.")
        return redirect('/register/')
    return render(request, 'register.html')

def logout_view(request):
    logout(request)
    return redirect('/home/')


def addrecipe(request):
    if request.method=='POST' :
        title=request.POST.get('title')
        description=request.POST.get('description')
        photo = request.FILES.get('photo')
        print('======================',photo)
        Recipe.objects.create(title=title,description=description,photo=photo)

    return render(request , 'add.html')


# def recipelist(request):
#         recipes=Recipe.objects.all().order_by('-created_at')
#         if request.GET.get('serach'):
#             recipes=Recipe.objects.filter(title__icontains = request.GET.get('serach'))
#         print('=====================',request.GET.get('serach'))

#         context={'recipes':recipes}


#         return render(request , 'recipe.html',context)

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def recipelist(request):
        recipes=Recipe.objects.all().order_by('-created_at')
        
        if request.GET.get('serach'):
            recipes=Recipe.objects.filter(title__icontains = request.GET.get('serach'))
        # context={'recipes':recipes}

        page = request.GET.get('page', 1)
        paginator = Paginator(recipes, 3)
        try:
            recipes = paginator.page(page)
        except PageNotAnInteger:
            recipes = paginator.page(1)
        except EmptyPage:
            recipes = paginator.page(paginator.num_pages)

        return render(request , 'recipe.html',{ 'recipes': recipes })

# def index(request):
#     user_list = User.objects.all()
#     page = request.GET.get('page', 1)

#     paginator = Paginator(user_list, 10)
#     try:
#         users = paginator.page(page)
#     except PageNotAnInteger:
#         users = paginator.page(1)
#     except EmptyPage:
#         users = paginator.page(paginator.num_pages)

#     return render(request, 'core/user_list.html', { 'users': users })

def updaterecipe(request,pk):
    recipes=Recipe.objects.get(id=pk)
    # context={'recipes':recipes}
    # print(recipes.title)
    # print(recipes.description)
    if request.method=='POST':
        title=request.POST.get('title')
        description=request.POST.get('description')
        photo = request.FILES.get('photo')
        recipes.title=title
        recipes.description=description
        recipes.photo=photo
        recipes.save()
        return redirect('/recipe/')
    return render(request , 'update.html',{'recipes':recipes})

def recipedelete(request,pk):
    obj=Recipe.objects.get(id=pk)
    obj.delete()
    return redirect('/recipe/')


