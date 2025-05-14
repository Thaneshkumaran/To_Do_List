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
def change_status(request,task_id):
    task_obj = task.objects.get(id=task_id)
    status=status.objects.all()
    # if task_obj.status == status.TODO:
    #     task_obj.status = status.DONE
    #     task_obj.save()
    #     return redirect('index1')
    # else:
    #     task_obj.status = status.TODO
    
    return render(request, 'index.html', {"statuses": status, "task": task_obj})
def delete_task(request,id):
    
    post = task.objects.get(id=id)
    post.delete()
    return redirect('index1')