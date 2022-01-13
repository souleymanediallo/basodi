from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from articles.models import Article
from .models import Favorite


# Create your views here.
@login_required
def add_favorite(request, product_id):
    try:
        Favorite.objects.get(username_id=request.user.id, product_id=(product_id))
        messages.warning(request, 'Ce produit est déjà dans vos favoris.')
        return redirect(request.META.get('HTTP_REFERER'))

    except ObjectDoesNotExist:
        Favorite.objects.create(username_id=request.user.id, product_id=(product_id))
        messages.success(request, 'Ce produit a été enregistré.')
        return redirect(request.META.get('HTTP_REFERER'))


@login_required
def my_favorite(request):
    favorites = Favorite.objects.filter(username=request.user)
    context = {"favorites": favorites}
    return render(request, "favorite/favorite_list.html", context)


@login_required
def delete_favorite(request, product_id):
    favorite = get_object_or_404(Favorite, pk=product_id)
    if request.method == "POST":
        favorite.delete()
        messages.success(request, 'Ce produit a été supprimé')
        return redirect("my-favorite")
    return render(request, "favorite/favorite_delete.html")