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



def product_list(request, **kwargs):
    all_products = Dice.objects.filter()
    for product in all_products:
        ave = Review.reviews_average(product)
        product.average_rating = ave[0]
        product.count_ratings = ave[1]
    context = {
        'all_products': all_products,
        'max_stars': [1,2,3,4,5]
    }

    return render(request, 'product-list.html', context)

def single_product(request, **kwargs):
    dice_id = kwargs['pk']
    that_one_product = Dice.objects.get(id=dice_id)
    ave = Review.reviews_average(that_one_product)
    that_one_product.average_rating = ave[0]
    that_one_product.count_ratings = ave[1]
    context = {
        'that_one_product': that_one_product,
        'max_stars': [1,2,3,4,5]
        }
    review_allowed = False
    
    if not request.user.is_anonymous:
        user_is_authorized = request.user.is_authorized()
        review = Review.objects.filter(product_reviewed=kwargs['pk']).filter(user=request.user)
        if len(review) > 0:
            review_allowed = False
        else: 
            review_allowed = True
    
    context['review_allowed'] = review_allowed
    context['user_is_authorized'] = user_is_authorized
    

    if request.method == 'POST':
        product = Dice.objects.get(id=kwargs['pk'])
        ShoppingCart.add_item(request.user, product)

    if request.method == 'DELETE':
        if request.user.is_staff == 1:
            Dice.objects.filter(id=dice_id).delete()

    return render(request, 'product-detail.html', context)

class ProductCreateView(CreateView):
    model = Dice
    form_class = DiceForm
    template_name = 'product-create.html'  # Default: book_form.html
    success_url = reverse_lazy('product-list')

    def get_context_data(self, **kwargs):
        context = super(ProductCreateView, self).get_context_data(**kwargs)
        hasFunction = getattr(self, "is_authorized", None)
        if callable(hasFunction):
            user_is_authorized = self.request.user.is_authorized()
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
        search_rating = request.POST['rating']
        if search_string_title:
            products_found = products_found.filter(name__contains=search_string_title)
        if search_rating:
            products_found = Review.all_products_by_rating(search_rating)
        form_in_function_based_view = SearchForm()

        
        for product in products_found:
            ave = Review.reviews_average(product)
            product.average_rating = ave[0]
            product.count_ratings = ave[1]
        
        context = {'form': form_in_function_based_view,
                   'all_products': products_found,
                   'show_results': True,
                   'max_stars': [1,2,3,4,5]}
        return render(request, 'product-list.html', context)

    else:
        form_in_function_based_view = SearchForm()
        context = {'form': form_in_function_based_view,
                   'show_results': False}
        return render(request, 'product-search.html', context)

def product_edit(request, pk: str):
    product = Dice.objects.get(id=pk)
    if request.method == 'POST':
        form = ProductEditForm(request.POST)
        product.name = form.data['name']
        product.description = form.data['description']
        product.colour = form.data['colour']
        product.sides = form.data['sides']
        product.prize = form.data['prize']
        if request.FILES.get('image', False):
            product.image = request.FILES['image']
        if request.FILES.get('product_info', False):
            product.product_info = request.FILES['product_info']
        product.save()
        return redirect('product-list')

    else:
        form = ProductEditForm(request.POST or None, instance=product)
        context = {'form': form,
                   'product': product,
                   'user': request.user
                }
        return render(request, 'product-edit.html', context)