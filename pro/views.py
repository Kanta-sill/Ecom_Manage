from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .models import Item
from .forms import ItemForm
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.core.paginator import Paginator

# Create your views here.

class IndexClassView(ListView):
    model = Item
    template_name = 'pro/index.html'
    context_object_name = 'item_list'

def item_list(request):
    item_objects=Item.objects.all()

    item_name=request.GET.get('item_name')
    if item_name != '' and item_name is not None:
        item_objects=item_objects.filter(name__icontains=item_name)

    paginator=Paginator(item_objects, 2)
    page=request.GET.get('page')
    item_objects=paginator.get_page(page)
    return render(request, 'pro/item_list.html', {'item_objects':item_objects})

class FoodView(DetailView):
    model = Item
    template_name = 'pro/detail.html'

class CreateItem(CreateView):
    model = Item
    fields = ['user_name','name', 'item_desc', 'item_price', 'item_image']
    template_name = 'pro/item_form.html'
    #
    # def form_valid(self, form):
    #     form.instance.user_name=self.request.user
    #
    #     return super().form_valid(form)

class UpdateItem(UpdateView):
    model = Item
    fields = ['user_name','name', 'item_desc', 'item_price', 'item_image']
    template_name = 'pro/item_form.html'

class DeleteItem(DeleteView):
    model = Item
    template_name = 'pro/item_delete.html'
    success_url = reverse_lazy('pro:index')