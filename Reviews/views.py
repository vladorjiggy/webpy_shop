from django.shortcuts import render, redirect
from Reviews.forms import ReviewForm
from Reviews.models import Review
# Create your views here.


def review_list_1(request, **kwargs):
    dice_id = kwargs['pk']
    all_the_reviews = Review.objects.filter(product_reviewed=dice_id)
    context = {'all_the_Reviews': all_the_reviews}
    return render(request, 'review-list.html', context)


def review_list_2(request, **kwargs):
    user_id = kwargs['pk']
    all_the_reviews = Review.objects.filter(user=user_id)
    context = {'all_the_Reviews': all_the_reviews}
    return render(request, 'review-list.html', context)


def review_create(request, **kwargs):
    if request.method == 'POST':
        product_id = kwargs['pk']
        form = ReviewForm(request.POST)
        form.instance.user = request.user
        form.instance.product_reviewed = product_id
        if form.is_valid():
            form.save()
        else:
            pass
        return redirect('product-detail', product_id)
    else:
        form = ReviewForm()
        context = {'form': form}
        return render(request, 'review-create.html', context)


def review_detail(request, **kwargs):
    review_id = kwargs['pk']
    that_one_review = Review.objects.get(id=review_id)
    context = {'that_one_Review': that_one_review}
    return render(request, 'review-detail.html', context)


<<<<<<< HEAD
=======
def vote(request, pk, helpful_or_not):
    review = Review.objects.get(id=int(pk))
    user = request.user
    review.vote(user, helpful_or_not)
    redirect('review-detail', pk=pk)


>>>>>>> maren-development
def review_delete(request, **kwargs):
    if request.method == 'POST':
        review_id = kwargs['pk']
        Review.objects.filter(id=review_id).delete()
        return redirect('review-list_2')
    else:
        review_id = kwargs['pk']
        that_one_review = Review.objects.get(id=review_id)
        context = {'that_one_review': that_one_review}
        return render(request, 'review-delete.html', context)
