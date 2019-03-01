from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from .forms import TeacherForm
from .models import Teacher

# Create your views here.

def index(request):
    allTeachers=Teacher.objects.all()
    context={
        'TeacherList':allTeachers
    }
    return render(request,"schoolApp/index.html",context)

#Form to enter a new teacher
def enterTeacher(request):
    newTeacher=TeacherForm(request.POST or None)
    if newTeacher.is_valid():
        newTeacher.save()
        return redirect('submit')
    return render(request,'schoolApp/createTeacher.html',{'create':newTeacher})

#Lets user know if form was submitted successfully
def submit(request):
    return render(request,'schoolApp/submit.html')

#enables the user to be edited
def editCard(request,ID):
    usedCard = get_object_or_404(Teacher,pk=ID)    #gets id from user
    editCard=TeacherForm(request.POST or None, instance=usedCard)   #uses instance to enable the editing
    if editCard.is_valid():
        editCard.save()
        return redirect('submit')
    return render(request,'schoolApp/createTeacher.html',{'create':editCard})   #renders to create page to enable editing

 #Delete Time card
def deleteCard(request,ID):
    currentCard = get_object_or_404(Teacher,pk=ID)  #obtains id
    if request.method== 'POST': #If they hit the button in the post request, it will delete
        currentCard.delete()    #deletes card
        return redirect('index')

    return render(request,'schoolApp/deleteTeacher.html',{'deleteTeacher':currentCard})

#Gets Teacher Info
def teacherinfo(request,ID):
    teacherID=get_object_or_404(Teacher,pk=ID)
    return render(request,'schoolApp/teacherinfo.html',{'context':teacherID},)

#Gets Hours from all Schools
def allhours(request,ID):
    teacherSchool=get_object_or_404(Teacher,pk=ID)
    schoolOnly=Teacher.objects.filter(school=teacherSchool.school)
    print(teacherSchool.school)

    return render(request,'schoolApp/allhours.html',{'context':schoolOnly})