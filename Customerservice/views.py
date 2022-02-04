from django.shortcuts import render, redirect
from django.contrib.admin.views.decorators import staff_member_required
from Reviews.models import Review
from Customerservice.forms import ProductEditForm
from Dices.models import Dice

'''
def review_delete(request, pk: str):
    review_id = pk
    review = Review.objects.get(id=review_id)
    if request.method == 'POST':
        if 'edit' in request.POST:
            form = ReviewEditForm(request.POST)
            if form.is_valid():
                new = form.cleaned_data['text']
                review.text = new
                review.save()
        elif 'delete' in request.POST:
            Review.objects.get(id=review_id).delete()

        return redirect('review-delete')

    else:
        form = ReviewEditForm(request.POST or None, instance=review)
        user = request.user
        context = {'form': form,
                   'review': review,
                   'user': user}
        return render(request, 'review-edit-delete.html', context)
'''


