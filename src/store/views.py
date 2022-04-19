from django.shortcuts import render

from store.models import Produit

# Create your views here.


def index(request):
    produit = Produit.objects.all()
    return render(request, "store/index.html", context={"produit": produit})
