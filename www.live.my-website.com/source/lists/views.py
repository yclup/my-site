from django.shortcuts import render, redirect
from django.http import HttpResponse
from lists.models import Item, List
from django.template import loader
from django.http import Http404
# Create your views here.


def home_page(request):
    return render(request, 'home.html')


def view_list(request, list_id):
    try:
        list_ = List.objects.get(id=list_id)
        template = loader.get_template('list.html')
        context = {'list': list_}
        return HttpResponse(template.render(context, request))
    except List.DoesNotExist:
        raise Http404("List does not exist")


def new_list(request):
    if request.method == 'POST':
        list_ = List.objects.create()
        Item.objects.create(text=request.POST['item_text'], list=list_)
        return redirect(f'/lists/{list_.id}')


def add_item(request, list_id):
    list_ = List.objects.get(id=list_id)
    Item.objects.create(text=request.POST['item_text'], list=list_)
    return redirect(f'/lists/{list_.id}')
