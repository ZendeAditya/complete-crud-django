from django.shortcuts import render,HttpResponseRedirect
from .forms import StudentForm
from django.contrib import messages
from .models import Addstudent
from django.db.models import Q
# Create your views here.
def home(request):
    return render(request,'crud/home.html')

def add_student(request):
    if request.method =='POST':
        form = StudentForm(request.POST or None)
        if form.is_valid():
            name = form.cleaned_data['name']
            roll_number = form.cleaned_data['roll_number']
            address = form.cleaned_data['address']
            instagram_link = form.cleaned_data['instagram_link']
            stu = Addstudent(name=name,roll_number=roll_number,address=address,instagram_link=instagram_link)
            stu.save()
            messages.success(request,"Student Added Successfully!!")
            return HttpResponseRedirect('/all_student/')
    else:
        form = StudentForm()
    context = {'form':form}
    return render(request,'crud/add_student.html', context)

def all_student(request):
    data = Addstudent.objects.all()
    context = {'data':data}
    return render(request,'crud/all_student.html',context)

def edit_student(request,name=None):
    edit_student = Addstudent.objects.get(name=name)
    form = StudentForm(request.POST or None,instance=edit_student)
    if form.is_valid():
        form.save()
        messages.success(request,'Student updated succussfully!!')
        return HttpResponseRedirect('/all_student/')
    context = {'form':form}
    return render(request,'crud/edit_student.html',context)

def delete_student(request,name = None):
    delete_student = Addstudent.objects.filter(name=name).first()
    delete_student.delete()
    messages.success(request,"Student deleted Successfully!!")
    return render(request,'crud/all_student.html')

def search(request):
    searchs =  request.POST['search']
    student = Addstudent.objects.filter( Q(name__icontains=search))
    print(search,student)
    context = {'student':student}
    return render(request,'crud/search.html',context)