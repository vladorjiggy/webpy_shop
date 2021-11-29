from django.shortcuts import render, redirect
from Reviews.forms import ReviewForm
from Reviews.models import Review
# Create your views here.


def review_list_1(request, **kwargs):
    dice_id = kwargs['pk']
    all_the_reviews = Review.objects.get(product_reviewed=dice_id)
    context = {'all_the_Reviews': all_the_reviews}
    return render(request, 'review-list.html', context)


def review_list_2(request, **kwargs):
    user_id = kwargs['pk']
    all_the_reviews = Review.objects.get(user=user_id)
    context = {'all_the_Reviews': all_the_reviews}
    return render(request, 'review-list.html', context)


def review_create(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        form.instance.user = request.user
        form.instance.product_reviewed = request.product_reviewed # todo muss ein Diceobject einlesen
        if form.is_valid():
            form.save()
        else:
            pass
        return redirect('review-list')
    else:
        form = ReviewForm()
        context = {'form': form}
        return render(request, 'review-create.html', context)


def review_detail(request, **kwargs):
    review_id = kwargs['pk']
    that_one_review = Review.objects.get(id=review_id)
    context = {'that_one_Review': that_one_review}
    return render(request, 'review-detail.html', context)


def game_delete(request, **kwargs):
    if request.method == 'POST':
        review_id = kwargs['pk']
        Review.objects.filter(id=review_id).delete()
        return redirect('review-list_2')
    else:
        review_id = kwargs['pk']
        that_one_review = Review.objects.get(id=review_id)
        context = {'that_one_review': that_one_review}
        return render(request, 'review-delete.html', context)
