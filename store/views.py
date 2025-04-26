from django.shortcuts import render
from store.popo.items import Item


# Create your views here.

def store(request):
    items = [
        Item(image="images/item1.jpg", desc="Harley-Davidson Pan America"),
        Item(image="images/item2.jpg", desc="Nvidia GTX 1660 Ti"),
        Item(image="images/item3.jpg", desc="VALORANT Prime 2.0 Phantom"),
        Item(image="images/item4.png", desc="Kondom Fiesta Dotted"),
        Item(image="images/item5.png", desc="New Balance 530 BKT Edition"),
        Item(image="images/item6.jpg", desc="Vinyl Laufey Bewitched"),
    ]
    return render(request, 'store/store.html', {'items': items})


def cart(request):
    context = {}
    return render(request, 'store/cart.html', context)


def checkout(request):
    context = {}
    return render(request, 'store/checkout.html', context)
