from django.shortcuts import render
from django.http import HttpResponse

def Midterm_A(request):
    jobroles = ('reporting executive', 'business analyst', 'data analyst', 'statistician', 'data scientist', 'data engineer/architect', 'machine learning engineer', 'big data engineer') 
   
    return render(request, "midterma.html", {''})


    
      

    