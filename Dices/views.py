from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, DeleteView
from .forms import DiceForm, SearchForm
from .models import Dice
from Shoppingcart.models import ShoppingCart


class ProductListView(ListView):
    model = Dice
    context_object_name = 'all_products'  # Default: object_list
    template_name = 'product-list.html'  # Default: book_list.html


class ProductDetailView(DetailView):
    model = Dice
    context_object_name = 'that_one_product'  # Default: book
    template_name = 'product-detail.html'  # Default: book_detail.html
    def get_queryset(self, *args, **kwargs):
        return Dice.objects.filter(id=self.kwargs['pk']) # evtl self

    def form_valid(self, form):
        # Add to shopping cart
        if self.request.method == 'POST':
            myuser = self.request.user
            ShoppingCart.add_item(myuser, self.get_queryset())


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

def book_search(request):
    if request.method == 'POST':
        search_string_sides = request.POST['sides']
        products_found = Dice.objects.filter(sides__contains=search_string_sides)
        search_string_title = request.POST['name']
        if search_string_title:
            products_found = products_found.filter(name__contains=search_string_title)

        form_in_function_based_view = SearchForm()
        context = {'form': form_in_function_based_view,
                   'products_found': products_found,
                   'show_results': True}
        return render(request, 'product-search.html', context)

    else:
        form_in_function_based_view = SearchForm()
        context = {'form': form_in_function_based_view,
                   'show_results': False}
        return render(request, 'product-search.html', context)
