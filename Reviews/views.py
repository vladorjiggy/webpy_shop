from django.shortcuts import render, redirect
from Dices.models import Dice
from Reviews.forms import ReviewForm
from Reviews.models import Review
from Useradmin.models import get_myuser_from_user
import logging


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
        form.instance.user = get_myuser_from_user(request.user)
        form.instance.product_reviewed = Dice.objects.get(id=product_id)
        logging.basicConfig(level=logging.DEBUG)
        logging.debug('is valid', form.is_valid())
        logging.debug(form.errors)
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
    product_reviewed = Dice.objects.get(id=that_one_review.product_reviewed.id)
    product_reviewed_id = product_reviewed.id
    context = {'that_one_Review': that_one_review,
               'product_reviewed_id': product_reviewed_id,
               'helpful_votes': that_one_review.get_helpful_count(),
               'not_helpful_votes': that_one_review.get_not_helpful_count()}
    return render(request, 'review-detail.html', context)


def vote(request, pk, helpful_or_not: str):
    logging.basicConfig(level=logging.DEBUG)
    logging.debug('helpful or not', helpful_or_not)
    review = Review.objects.get(id=int(pk))
    user = request.user
    review.vote(user, helpful_or_not)
    return redirect('review_detail', pk=pk)


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
