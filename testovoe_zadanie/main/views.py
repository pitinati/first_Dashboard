from django.shortcuts import render
from .models import Testovoe, Comments
from .forms import TestovoeForm
# Create your views here.
def index(request):
    table = Testovoe.objects.all()
    return render(request, 'main/index.html', {'table': table})

def about(request, number ):
   
    if request.method == 'POST':
        new_comm = Comments(request.POST['item_id'],request.POST['comment'] )
        new_comm.save()
        
    table = Testovoe.objects.get(id=number)
    comments = Comments.objects.all().filter(item_id=number)
    return render(request,'main/about.html',{'table': table, 'comments': comments})