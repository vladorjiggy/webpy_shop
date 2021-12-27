from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, DeleteView

from Customerservice.forms import ProductEditForm
from .forms import DiceForm
from .models import Dice
from Useradmin.models import get_myuser_from_user


class ProductListView(ListView):
    model = Dice
    context_object_name = 'all_products'  # Default: object_list
    template_name = 'product-list.html'  # Default: book_list.html

    def get_context_data(self, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        myuser = get_myuser_from_user(self.request.user)
        user_is_authorized = myuser.is_authorized()
        context['user_is_authorized'] = user_is_authorized
        return context


class ProductDetailView(DetailView):
    model = Dice
    context_object_name = 'that_one_product'  # Default: book
    template_name = 'product-detail.html'  # Default: book_detail.html

    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        myuser = get_myuser_from_user(self.request.user)
        user_is_authorized = myuser.is_authorized()
        context['user_is_authorized'] = user_is_authorized
        return context


class ProductCreateView(CreateView):
    model = Dice
    form_class = DiceForm
    template_name = 'product-create.html'  # Default: book_form.html
    success_url = reverse_lazy('product-list')

    def get_context_data(self, **kwargs):
        context = super(ProductCreateView, self).get_context_data(**kwargs)
        myuser = get_myuser_from_user(self.request.user)
        user_is_authorized = myuser.is_authorized()
        context['user_is_authorized'] = user_is_authorized
        return context

    '''def upload_file(self, request, pk):
        if request.method == 'POST':
            form = DiceForm(request.POST, request.FILES)
            if form.is_valid():
                instance = Dice(product_info=request.FILES['file'])
                instance.save()
                return HttpResponseRedirect('product-detail')
            else:
                pass
            
        else:
            form = DiceForm()
        return render(request, 'product-detail.html', {'form': form})'''

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


def product_edit(request, pk: str):
    product_id = pk
    product = Dice.objects.get(id=product_id)
    if request.method == 'POST':
        form = ProductEditForm(request.POST)
        if form.is_valid():
            product.name = form.cleaned_data['name']
            product.description = form.cleaned_data['description']
            product.colour = form.cleaned_data['colour']
            product.sides = form.cleaned_data['sides']
            product.prize = form.cleaned_data['prize']
            product.image = form.cleaned_data['image']
            product.save()
            return redirect('product-list')

    else:
        form = ProductEditForm(request.POST or None, instance=product)
        user = request.user
        context = {'form': form,
                   'product': product,
                   'user': user}
        return render(request, 'product-edit.html', context)
