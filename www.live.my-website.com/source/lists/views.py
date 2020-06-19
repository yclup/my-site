from django.shortcuts import render, redirect
from django.http import HttpResponse
from lists.models import Item, List
from django.template import loader
from django.http import Http404
from django.core.exceptions import ValidationError
from django.utils.html import escape
from lists.forms import ItemForm
# Create your views here.


def home_page(request):
    return render(request, 'home.html', {'form': ItemForm()})


def view_list(request, list_id):
    try:
        form = ItemForm()
        list_ = List.objects.get(id=list_id)
        error = ""
        if request.method == 'POST':
            form = ItemForm(request.POST)
            if form.is_valid():
                Item.objects.create(text=form.cleaned_data['text'], list=list_)
                return redirect(list_)

        return render(request, 'list.html', {'list': list_, 'error': error, 'form': form})
    except List.DoesNotExist:
        raise Http404("List does not exist")


def new_list(request):
    form = ItemForm(request.POST)
    if form.is_valid():
        list_ = List.objects.create()
        Item.objects.create(text=request.POST['text'], list=list_)
        return redirect(list_)
    else:
        return render(request, 'home.html', {'form': form})
