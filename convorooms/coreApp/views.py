from django.shortcuts import render
# Create your views here.

rooms = [
    {"id" : 1 , "name" : "Lets learn Python together!"},
    {"id" : 2 , "name" : "Have some fun with MERN projects.."},
    {"id" : 3 , "name" : "Lets dive into frontend using React!"},
]

def home(request):
    context = {"rooms":rooms}
    return render(request , 'home.html' , context)

def room(request):
    return render(request , 'room.html')