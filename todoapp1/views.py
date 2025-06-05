from django.shortcuts import render, HttpResponse, redirect
from .models import task, status,CustomUser
from .froms import TaskForm, RegisterForm, LoginForm
from django.contrib.auth import authenticate, login, get_user_model
from django.contrib import messages
from django.contrib.auth.decorators import login_required

User = get_user_model()


# Create your views here.
@login_required
def task_list(request):
    # tasks = task.objects.all()
    tasks=task.objects.filter(user=request.user)
    print("Logged-in user:", request.user, "ID:", request.user.id)
    return render(request,'index.html', {'tasks': tasks})
@login_required
def task_list1(request):
    tasks = task.objects.filter(required_user=request.user)
    return render(request, 'tasks.html', {'tasks': tasks})
@login_required
def add_task(request,id):
    if request.method == 'POST':
         # Get the user by ID
        form = TaskForm(request.POST)
        if form.is_valid():
            user_de= CustomUser.objects.get(id=id) 
            task_instance = form.save(commit=False)  # Don't save yet
            task_instance.required_user = request.user  
            task_instance.user= user_de   # Set the user
            print("User:", request.user, "ID:", request.user.id)  # Debugging line
            task_instance.save()                     # Now save with user
            return redirect('task_list')
            
    else:
        form = TaskForm()
    return render(request, 'addtask.html', {'form': form})
@login_required
def change_post(request, id):
    task_obj = task.objects.get(id=id)
    statu= status.objects.all()
    if request.method == 'POST':
        # form = TaskForm(request.POST, instance=task_obj)
        status_id = request.POST.get('status')
        status_instance = status.objects.get(id=status_id)  
        task_obj.status = status_instance
        # form = TaskForm(request.POST, instance=task_obj)    
        # task_obj.status = status_instance
        task_obj.save()
        return redirect('index1')
    else:
        form = TaskForm(instance=task_obj)
    return render(request, 'change.html', {'form': form,"status":statu})
@login_required
def delete_task(request,id):
    post = task.objects.get(id=id)
    post.delete()
    return redirect('task_list')
def register(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            confirm_password = form.cleaned_data['confirm_password']
            if password == confirm_password:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                messages.success(request, "User Created Successfully")
                return redirect('login')
            else:
                messages.error(request, "Passwords do not match.")
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':    
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                request,
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )
            if user is not None:
                login(request, user)
                if user.user_type == '1':
                    return redirect('user_profile')
                else:
                    return redirect('index1')
                # Change to your homepage route
            else  :
                messages.error(request, 'Invalid username or password.')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})
@login_required
def user_profile(request):
    form = CustomUser.objects.exclude(id=request.user.id)
    
    return render(request, 'user.html', {'users': form})