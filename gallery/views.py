from django.shortcuts import render

from gallery.models import Gallery


def gallery(request):
    galleries = (
        Gallery.objects.filter(is_active=True)
        .prefetch_related('gallery_images')
        .order_by('sort_order', 'id')
    )

    context = {
        'galleries': galleries,
    }
    return render(request, 'gallery.html', context)
