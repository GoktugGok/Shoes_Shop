from shoes.models import Category

def category_context(request):
    return {
        'all_categories': Category.objects.filter(level=0)
    }
