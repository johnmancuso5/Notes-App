from django.shortcuts import render, redirect
from django.http import HttpResponse

# Importing model
from .models import Notes

# Create your views here.
def index(request):
    note = Notes.objects.all()[:10]

    # Object being saved
    context = {
        'notes':note
    }
    return render(request, 'index.html', context)

def details(request, id):
    note = Notes.objects.get(id=id)
    context = {
        'note':note
    }
    return render(request, 'details.html', context)

def add(request):
    if(request.method == 'POST'):
        title = request.POST['title']
        text = request.POST['text']

        if(len(text) <= 255):
            note = Notes(title=title,text=text)
            note.save()
            return redirect('/notes')
        else:
            note = Notes(title=title,text=text)
            note.save()
            return redirect('/notes/add')
            

    else:
        return render(request, 'add.html')

def delete(request, id):
    note_id = request.GET.getlist('DeleteButton')
    note = Notes.objects.get(id=note_id)

    if request.method == 'POST':        
        note.delete()
        return redirect('/')

    context = {
        'note':note
    }
    return render(request, 'index.html', context)
