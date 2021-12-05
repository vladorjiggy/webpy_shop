from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, DeleteView
from .forms import DiceForm
from .models import Dice


class ProductListView(ListView):
    model = Dice
    context_object_name = 'all_products'  # Default: object_list
    template_name = 'product-list.html'  # Default: book_list.html


class ProductDetailView(DetailView):
    model = Dice
    context_object_name = 'that_one_product'  # Default: book
    template_name = 'product-detail.html'  # Default: book_detail.html


class ProductCreateView(CreateView):
    model = Dice
    form_class = DiceForm
    template_name = 'product-create.html'  # Default: book_form.html
    success_url = reverse_lazy('product-list')
'''
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
'''

class ProductDeleteView(DeleteView):
    model = Dice
    success_url = reverse_lazy('product-list')
    context_object_name = 'that_one_product'
    template_name = 'product-confirm_delete.html'