from django.shortcuts import render
from django.http import HttpResponse
from listings.choices import price_choices, bedroom_choices, state_choices

from listings.models import Listing
from counsellors.models import Counsellor

def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]

    context = {
        'listings': listings,
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices
    }

    return render(request, 'pages/index.html', context)


def about(request):
    # Get all counsellors
    counsellors = Counsellor.objects.order_by('-hire_date')

    # Get MVP
    mvp_counsellors = Counsellor.objects.all().filter(is_mvp=True)

    context = {
        'counsellors': counsellors,
        'mvp_counsellors': mvp_counsellors
    }

    return render(request, 'pages/about.html', context)
