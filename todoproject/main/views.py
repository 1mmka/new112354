from typing import Any, Dict
from django.db.models.query import QuerySet
from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import ListView
from main.models import ToDoList,TakeImage
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core.paginator import Paginator

# Create your views here.
class FullList(ListView):
    model = ToDoList
    template_name = 'list.html'
    context_object_name = 'full_list'
    
    def post(self,request):
        if self.request.POST['title']:
            newTask = self.request.POST
        else:
            newTask = None
        temp = ToDoList.objects.create(title = newTask.get('title'))
        temp.save()
        
        return redirect('full_list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['delete'] = TakeImage.objects.get(image = 'uploads/5598.jpg')
        
        tasks = ToDoList.objects.all()
        paginator = Paginator(tasks,4) # 4 записи/1 страницу
        page_number = self.request.GET.get('page') # взять номер страницы
        page = paginator.get_page(page_number)  # взять записи по странице
        
        context['page'] = page
        
        return context

def DeleteTask(request,pk):
    task = get_object_or_404(ToDoList,id=pk)
    task.delete()
    return HttpResponseRedirect(reverse('full_list'),status=302)