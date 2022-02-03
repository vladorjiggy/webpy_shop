from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, DeleteView

from Customerservice.forms import ProductEditForm
from .forms import DiceForm, SearchForm
from .models import Dice
from Useradmin.models import get_myuser_from_user
from Shoppingcart.models import ShoppingCart
from Reviews.models import Review


class ProductListView(ListView):
    model = Dice
    context_object_name = 'all_products'
    template_name = 'product-list.html'

    
    def get_context_data(self, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        print('h')
        # Add to shopping cart
        if self.request.method == 'POST':
            myuser = self.request.user
            #product = Dice.objects.filter(id=self.kwargs['pk'])
            #ShoppingCart.add_item(myuser, product)


def single_product(request, **kwargs):
    dice_id = kwargs['pk']
    that_one_product = Dice.objects.get(id=dice_id)
    context = {'that_one_product': that_one_product}

    myuser = request.user
    user_is_authorized = myuser.is_authorized()
    review_allowed = True
    review = Review.objects.filter(product_reviewed=kwargs['pk']).filter(user=myuser)
    print(review)
    if len(review) > 0:
        review_allowed = False
    else: 
        review_allowed = True
    context['review_allowed'] = review_allowed
    context['user_is_authorized'] = user_is_authorized
    

    if request.method == 'POST':
        myuser = request.user
        product = Dice.objects.get(id=kwargs['pk'])
        ShoppingCart.add_item(myuser, product)

    if request.method == 'DELETE':
        print('DELETE')
        user = request.user
        if user.is_staff == 1:
            Dice.objects.filter(id=dice_id).delete()

    return render(request, 'product-detail.html', context)

'''
class ProductDetailView(DetailView):
    model = Dice
    context_object_name = 'that_one_product' 
    template_name = 'product-detail.html'
    
    def get_queryset(self, *args, **kwargs):
        return Dice.objects.filter(id=self.kwargs['pk']) # evtl self

    
    
    def form_valid(self, form):
        # Add to shopping cart
        if self.request.method == 'POST':
            myuser = self.request.user
            product = Dice.objects.filter(id=self.kwargs['pk'])
            ShoppingCart.add_item(myuser, product)

    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        myuser = self.request.user
        user_is_authorized = myuser.is_authorized()
        review_allowed = 'True'
        review = Review.objects.filter(product_reviewed=self.kwargs['pk']).filter(user=myuser)
        print(review)
        if len(review) > 0 | review:
            review_allowed = 'False'
        else: 
            review_allowed = 'True'
        context['review_allowed'] = review_allowed
        context['reviews'] = review
        context['user_is_authorized'] = user_is_authorized
        return context
'''

class ProductCreateView(CreateView):
    model = Dice
    form_class = DiceForm
    template_name = 'product-create.html'  # Default: book_form.html
    success_url = reverse_lazy('product-list')

    def get_context_data(self, **kwargs):
        context = super(ProductCreateView, self).get_context_data(**kwargs)
        myuser = self.request.user
        invert_op = getattr(self, "is_authorized", None)
        if callable(invert_op):
            user_is_authorized = myuser.is_authorized()
        else:
            user_is_authorized = False
        context['user_is_authorized'] = user_is_authorized
        return context

    def upload_file(self, request, pk):
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
        return render(request, 'product-detail.html', {'form': form})


    def form_valid(self, form):
        form.instance.superuser = self.request.user
        return super().form_valid(form)



class ProductDeleteView(DeleteView):
    model = Dice
    success_url = reverse_lazy('product-list')
    context_object_name = 'that_one_product'
    template_name = 'product-confirm_delete.html'

def product_delete(request, **kwargs):
    if request.method == 'DELETE':
        user = request.user
        product_id = kwargs['pk']
        if user.is_staff == 1:
            Dice.objects.filter(id=product_id).delete()

def product_search(request):
    if request.method == 'POST':
        search_string_sides = request.POST['sides']
        products_found = Dice.objects.filter(sides__contains=search_string_sides)
        search_string_title = request.POST['name']
        if search_string_title:
            products_found = products_found.filter(name__contains=search_string_title)

        form_in_function_based_view = SearchForm()
        context = {'form': form_in_function_based_view,
                   'all_products': products_found,
                   'show_results': True}
        return render(request, 'product-list.html', context)

    else:
        form_in_function_based_view = SearchForm()
        context = {'form': form_in_function_based_view,
                   'show_results': False}
        return render(request, 'product-search.html', context)

def product_edit(request, pk: str):
    product_id = pk
    product = Dice.objects.get(id=product_id)
    if request.method == 'POST':
        form = ProductEditForm(request.POST)
        #print(form.data['image'])
        
        product.name = form.data['name']
        product.description = form.data['description']
        product.colour = form.data['colour']
        product.sides = form.data['sides']
        product.prize = form.data['prize']
        product.image = request.FILES['image']
        product.product_info = request.FILES['product_info']
        
        product.save()
        return redirect('product-list')

    else:
        form = ProductEditForm(request.POST or None, instance=product)
        user = request.user
        context = {'form': form,
                   'product': product,
                   'user': user}
        return render(request, 'product-edit.html', context)


def product_detail(request, **kwargs):
    # print(kwargs)
    product_id = kwargs['pk']
    that_one_computer_in_my_function_based_view = Dice.objects.get(id=product_id)
    # print(str(computer_id), " :: ", that_one_computer_in_my_function_based_view)

    # Add to shopping cart
    if request.method == 'POST':
        myuser = request.user
        ShoppingCart.add_item(myuser, that_one_computer_in_my_function_based_view)

    context = {'that_one_product': that_one_computer_in_my_function_based_view}
    return render(request, 'product-detail.html', context)