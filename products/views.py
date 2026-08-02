from django.core.paginator import Paginator
from django.db.models import Prefetch, Q
from django.shortcuts import render

from products.models import Category, Product, ProductImage


def _product_queryset(category_ids):
    return (
        Product.objects.filter(is_active=True, category_id__in=category_ids)
        .select_related('category')
        .prefetch_related(
            Prefetch(
                'images',
                queryset=ProductImage.objects.order_by('-is_primary', 'sort_order', 'id'),
            )
        )
    )


def women(request):
    women_category = (
        Category.objects.filter(is_active=True, parent__isnull=True)
        .filter(Q(slug__iexact='women') | Q(name__iexact='women'))
        .first()
    )

    products = Product.objects.none()

    if women_category:
        category_ids = [
            women_category.id,
            *women_category.children.filter(is_active=True).values_list('id', flat=True),
        ]
        products = _product_queryset(category_ids).order_by('-created_at', 'name')

    paginator = Paginator(products, 8)
    page_obj = paginator.get_page(request.GET.get('page'))

    context = {
        'women_category': women_category,
        'products': page_obj,
        'page_obj': page_obj,
    }
    return render(request, 'women.html', context)


def kids(request):

    kids_category = (
        Category.objects.filter(
            is_active=True
        )
        .filter(
            Q(slug__iexact='kids') |
            Q(name__iexact='kids')
        )
        .first()
    )


    products = Product.objects.none()


    if kids_category:

        category_ids = [
            kids_category.id,
            *kids_category.children.filter(
                is_active=True
            ).values_list('id', flat=True),
        ]

        products = (
            _product_queryset(category_ids)
            .order_by('-created_at', 'name')
        )


    paginator = Paginator(products, 8)

    page_obj = paginator.get_page(
        request.GET.get('page')
    )


    context = {
        'kids_category': kids_category,
        'products': page_obj,
        'page_obj': page_obj,
    }


    return render(
        request,
        'kids.html',
        context
    )