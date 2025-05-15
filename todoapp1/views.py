from pyexpat.errors import messages
from django.shortcuts import render,HttpResponse,redirect
from .models import task,status
from .froms import TaskForm

# Create your views here.
def task_list(request):
    tasks = task.objects.all()
    
    # if request.method == 'POST':
    #     form = TaskForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('index1')
    # else:
    #     form = TaskForm()
    # return HttpResponse("Task List: " + ", ".join([str(task) for task in tasks]))\
    return render(request,'index.html', {'tasks': tasks})
def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index1')
    else:
        form = TaskForm()
    return render(request, 'addtask.html', {'form': form})
def change_post(request, id):
    task_obj = task.objects.get(id=id)
    status= status.objects.all()
    if request.method == 'POST':
        # form = TaskForm(request.POST, instance=task_obj)
        status_id = request.POST.get('status')
        status_instance = status.objects.get(id=status_id)  # ✅ Correct
        task_obj.status = status_instance
        form = TaskForm(request.POST, instance=task_obj)
        if form.is_valid():
            task_obj.status = status_instance
            form.save()
            return redirect('index1')
    else:
        form = TaskForm(instance=task_obj)
    return render(request, 'change.html', {'form': form,"status":s})
def delete_task(request,id):
    
    post = task.objects.get(id=id)
    post.delete()
    return redirect('index1')