from django.shortcuts import render
from store.popo.items import Item


# Create your views here.
def get_all_items():
    items = [
        Item(image="images/item1.jpg", type="Kendaraan" ,name="Harley-Davidson", desc="Harley-Davidson Pan America", price=230.99),
        Item(image="images/item2.jpg", type="Komponen PC" ,name="NVIDIA", desc="Nvidia GTX 1660 Ti", price=89.99),
        Item(image="images/item3.jpg", type="Item Game" ,name="VALORANT", desc="VALORANT Prime 2.0 Phantom", price=75.99),
        Item(image="images/item4.png", type="Alat Sex", name="Fiesta" ,desc="Kondom Fiesta Dotted", price=20.99),
        Item(image="images/item5.png", type="Pakaian", name="New Balance", desc="New Balance 530 BKT Edition", price=50.99),
        Item(image="images/item6.jpg", type="Musik", name="Vinyl Record" ,desc="Vinyl Laufey Bewitched", price=20.99),
    ]
    return items
def store(request):
    items = get_all_items()
    return render(request, 'store/store.html', {'items': items})


def cart(request):
    all_items = get_all_items()
    items = []
    for i in range(3):
        items.append(all_items[i])

    total = sum(item.price for item in items)
    context = {
        'items': items,
        'total': total,
    }
    return render(request, 'store/cart.html', context)


def checkout(request):
    context = {}
    return render(request, 'store/checkout.html', context)
