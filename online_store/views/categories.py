from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect, get_object_or_404

from online_store.models import Category


def category_add_view(request: WSGIRequest):
    if request.method == "GET":
        return render(request, 'category_create.html')
    category_data = {
        'name': request.POST.get('name'),
        'desc': request.POST.get('desc')
    }
    category = Category.objects.create(**category_data)
    return redirect('category_view', pk=category.pk)

def category_view(request, pk):
    category = get_object_or_404(Category, pk=pk)
    return render(request, 'category.html', context={
        'category': category
    })

def category_remove_view(request, pk):
    category = Category.objects.get(pk=pk)
    context = {'category': category}
    category.delete()
    return render(request, 'remove_category.html', context=context)




