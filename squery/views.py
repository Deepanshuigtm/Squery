from django.shortcuts import render
from datetime import date



def startingpage(request):
    return render (request,"squery/index.html")

def querys(request):
    return render (request,"squery/query.html")
