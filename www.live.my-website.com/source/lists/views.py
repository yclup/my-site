from django.shortcuts import render, redirect
from django.http import HttpResponse
from lists.models import Item, List
from django.template import loader
from django.http import Http404
from django.core.exceptions import ValidationError
from django.utils.html import escape
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
        item = Item.objects.create(text=request.POST['item_text'], list=list_)
        try:
            item.full_clean()
            item.save()
        except ValidationError:
            list_.delete()
            error = "You can't have an empty list item"
            return render(request, 'home.html', {'error': error})
        return redirect(f'/lists/{list_.id}')


def add_item(request, list_id):
    list_ = List.objects.get(id=list_id)
    Item.objects.create(text=request.POST['item_text'], list=list_)
    return redirect(f'/lists/{list_.id}')
