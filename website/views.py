from django.db.models import Prefetch
from django.shortcuts import render

from gallery.models import Gallery
from products.models import Product, ProductImage
from testinomial.models import Testimonial 


def home(request):
    # 1. Fetch active gallery items
    home_gallery = (
        Gallery.objects.filter(
            is_active=True,
            show_on_home=True,
        )
        .order_by('sort_order', 'id')
    )

    # 2. Fetch featured products
    home_products = (
        Product.objects.filter(
            is_active=True,
            attribute_values__attribute__slug='show-on-home-page',
            attribute_values__value='1',
        )
        .order_by('-created_at', 'name')
        .prefetch_related(
            Prefetch(
                'images',
                queryset=ProductImage.objects.order_by('-is_primary', 'sort_order', 'id'),
            )
        )
    )

    # 3. Fetch active testimonials
    testimonials = Testimonial.objects.filter(is_active=True)

    # Combine everything in one context dictionary
    context = {
        'home_gallery': home_gallery,
        'home_products': home_products,
        'testimonials': testimonials,
    }
    
    return render(request, 'home.html', context)

def about(request):
    return render(request, 'about.html')

