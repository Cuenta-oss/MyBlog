from django.shortcuts import render
from .models import postTable, categoryTable

# Create your views here.


def blog(request):
    varBlog = postTable.objects.all()
    varCategory = categoryTable.objects.all()
    context = {
        'varBlog': varBlog,
        'varCategory': varCategory
    }
    return render(request, 'appPost/blog.html', context)


def filter_category(request, id):
    varCategory = categoryTable.objects.get(id=id)
    varPost = postTable.objects.filter(categorias= id)
    context = {
        'varCategory': varCategory,
        'varPost': varPost
    }
    return render(request, 'appPost/filterCategory.html', context)


""" def all_categories(request):
    varCategoryAll = categoryTable.objects.all()
    varPostAll = postTable.objects.all()
    context = {
        'varCategoryAll': varCategoryAll,
        'varPostAll': varPostAll,
    }

    return render(request, 'appPost/blog.html', context)
 """