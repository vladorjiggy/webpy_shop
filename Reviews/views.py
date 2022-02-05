from django.shortcuts import render, redirect
from Dices.models import Dice
from Reviews.forms import ReviewForm, ReviewEditForm
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
        user = request.user
        form.instance.user = user
        form.instance.product_reviewed = Dice.objects.get(id=product_id)

        review = Review.objects.filter(
            product_reviewed=product_id).filter(user=user)
        if len(review) > 0:
            pass
        else:
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
    delete_review_allowed = False
    voting_allowed = False

    if request.user.is_anonymous:
        voting_allowed = False
    else:
        voting_allowed = True

    if that_one_review.user == request.user or request.user.is_staff == 1:
        delete_review_allowed = True
    else:
        delete_review_allowed = False

    product_reviewed_id = product_reviewed.id
    context = {'that_one_Review': that_one_review,
               'product_reviewed_id': product_reviewed_id,
               'helpful_votes': that_one_review.get_helpful_count(),
               'not_helpful_votes': that_one_review.get_not_helpful_count(),
               'delete_review_allowed': delete_review_allowed,
               'voting_allowed': voting_allowed
               }
    if request.method == 'DELETE':
        if delete_review_allowed:
            Review.objects.filter(id=review_id).delete()

    return render(request, 'review-detail.html', context)


def vote(request, pk, helpful_or_not: str):

    logging.basicConfig(level=logging.DEBUG)
    logging.debug('helpful or not', helpful_or_not)
    review = Review.objects.get(id=int(pk))
    allVotes = review.get_all_votes()
    voted = False
    for votes in allVotes:
        if(votes.user == request.user):
            print(votes.helpful_or_not, helpful_or_not)
            voted = True
    if(voted == False):
        user = request.user
        review.vote(user, helpful_or_not)
    return redirect('review_detail', pk=pk)


def review_delete(request, **kwargs):
    if request.method == 'POST':
        review_id = kwargs['pk']
        Review.objects.filter(id=review_id).delete()
        return redirect('reviews_product', pk=review_id)
    else:
        review_id = kwargs['pk']
        that_one_review = Review.objects.get(id=review_id)
        context = {'that_one_review': that_one_review}
        return render(request, 'review-delete.html', context)

def review_edit(request, pk: str):
    review_id = pk
    review = Review.objects.get(id=review_id)
    if request.method == 'POST':
        form = ReviewEditForm(request.POST)
        
        review.rating = form.data['rating']
        review.title = form.data['title']
        review.text = form.data['text']
        
        review.save()
        return redirect('review_detail', pk=pk)

    else:
        form = ReviewEditForm(request.POST or None, instance=review)
        user = request.user
        edit_allowed = True
        if user == review.user:
            edit_allowed = True
        else: 
            edit_allowed = False
        
        context = {'form': form,
                   'review': review,
                   'user': user,
                   'edit_allowed': edit_allowed
                   }
        return render(request, 'review-edit.html', context)
