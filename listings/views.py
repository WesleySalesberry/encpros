from django.shortcuts import render
from .models import Listing, ListingPhoto
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator


def index(request):
    listings = Listing.objects.filter(is_published=True).order_by('-list_date')

    paginator = Paginator(listings, 6)
    page = request.GET.get('page')
    paged_listing = paginator.get_page(page)

    context = {
        'listings': paged_listing,
    }
    return render(request, 'listings/listings.html', context)


def listing(request, listing_id):

    return render(request, 'listings/listing.html')


def search(request):
    return render(request, 'listings/search.html')
