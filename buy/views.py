from django.shortcuts import render
from item.models import Item

def item(request, pk):
    item_id = pk
    item = Item.objects.get(id=item_id)
    
    return render(request, 'index.html', {'item':item})

