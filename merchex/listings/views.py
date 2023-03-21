from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from listings.models import Band, Listing

from listings.forms import ContactUsForm, BandForm, ListingForm
from django.core.mail import send_mail


def band_list(request):  # rename from hello -> <model_type.html>
    bands = Band.objects.all()
    return render(request, 'listings/band_list.html', context={'bands': bands})

    # return HttpResponse(
    #     f"""
    # <h1>Hello Django!</h1>
    # <p>This is my favorite bands:</p>
    # <ul>
    #  <li>{bands[0].name}</li>
    #  <li>{bands[1].name}</li>
    #  <li>{bands[2].name}</li>
    #  <li>{bands[3].name}</li>
    # </ul>
    #     """)

# How can we get any id you type into the URL address bar
# gets passed to the view and then to the template?

# We need to somehow convert that id into its respective
# Band  object in the database.

# answer: we insert this line to get the Band with that id:
# band = Band.objects.get(id=id)

# .get(id=id) -> which is to say “get me the object that has this id.”

# Then we pass that  band  to the template

# Let’s update the template now


def band_detail(request, id):
    band = get_object_or_404(Band, id=id)
    # band = Band.objects.get(id=id)

    # https://docs.djangoproject.com/en/4.1/topics/http/shortcuts/#get-object-or-404
    # Use get() to return an object, or raise a Http404 exception if the object does not exist.
    # klass may be a Model, Manager, or QuerySet object. All other passed arguments and keyword
    # arguments are used in the get() query.

    return render(request, 'listings/band_detail.html', context={'band': band})

# def band_detail(request, id):
#     return render(request, 'listings/band_detail.html', context={'id': id})


def about(request):
    return HttpResponse("<h1>About Us</h1> <p>We love Merch!</p>")


def listing_list(request):
    listings = Listing.objects.all()
    return render(request, 'listings/listing_list.html', context={'listings': listings})


def contact(request):

    # add these print statements so we can take a look at `request.method & request.POST`
    print('The request method is:', request.method)
    print('The POST data is:', request.POST)

    # Before submit button the console output is:

    # The request method is: GET
    # The POST data is: <QueryDict: {}>
    # [20/Mar/2023 20:08:51] "GET /contact-us/ HTTP/1.1" 200 589

    # You can see that request.POST  is an empty
    # QueryDict during a GET request (which is a special type of Python  dict)

    # After entering some data, the console output is:

    # The request method is: POST
    # The POST data is: <QueryDict: {'csrfmiddlewaretoken': ['MAk6JmXaoscsRZ72q2MdsBtqYhpHXFziEAOIflKhgKzln39oOnVBdYXAZNW2gc3p'], 'name': ['jaythree'], 'email': ['admin@admin.com'], 'message': ['Hi you there']}>
    # [20/Mar/2023 20:09:02] "POST /contact-us/ HTTP/1.1" 200 589

    # we need to somehow handle both request scenarios in our view:

    # If this is a GET request, we should display an empty form to the user.

    # If this is a POST request, we should take a look at the data and see if it is valid. (We’ll get to the actual sending of the email soon enough.)

    # the old method:

    # form = ContactUsForm()
    # return render(request, 'listings/contact.html', context={'form': form})

    # So we need an  if  statement:

    # form = ContactUsForm()

    if request.method == 'POST':
        # create an instance of our form, and fill it with the POST data
        form = ContactUsForm(request.POST)
        if form.is_valid():
            send_mail(
                subject=f'Message from {form.cleaned_data["name"] or "anonymous"} via MerchEx Contact Us form',
                message=form.cleaned_data['message'],
                from_email=form.cleaned_data['email'],
                recipient_list=['admin@merchex.xyz'],
            )
            return redirect('email-sent')
    else:
        # this must be a GET request, so create an empty form
        form = ContactUsForm()

    return render(request, 'listings/contact.html', context={'form': form})


def email_sent(request):
    return render(request, 'listings/email_sent.html')


def band_create(request):
    if request.method == 'POST':
        form = BandForm(request.POST)
        if form.is_valid():
            band = form.save()
            return redirect('band-detail', band.id)
    else:
        form = BandForm()
    return render(request, 'listings/band_create.html', context={'form': form})


def band_update(request, id):
    band = Band.objects.get(id=id)

    if request.method == 'POST':
        form = BandForm(request.POST, instance=band)
        if form.is_valid():
            form.save()
            return redirect('band-detail', band.id)
    else:
        form = BandForm(instance=band)
    return render(request, 'listings/band_update.html', context={'form': form})


def band_delete(request, id):
    band = Band.objects.get(id=id)
    if request.method == 'POST':
        band.delete()
        return redirect('band-list')

    return render(request, 'listings/band_delete.html', context={'band': band})


def listing_create(request):
    if request.method == 'POST':
        form = ListingForm(request.POST)
        if form.is_valid():
            listing = form.save()
            return redirect('listing-detail', listing.id)
    else:
        form = ListingForm()
    return render(request, 'listings/listing_create.html', context={'form': form})


def listing_delete(request, id):
    listing = Listing.objects.get(id=id)
    if request.method == 'POST':
        listing.delete()
        return redirect('listing-list')
    return render(request, 'listings/listing_delete.html', context={'listing': listing})


def listing_update(request, id):
    listing = Listing.objects.get(id=id)

    if request.method == 'POST':
        form = ListingForm(request.POST, instance=listing)
        if form.is_valid():
            form.save()
            return redirect('listing-detail', listing.id)
    else:
        form = ListingForm(instance=listing)
    return render(request, 'listings/listing_update.html', context={'form': form})


def listing_detail(request, id):
    listing = get_object_or_404(Listing, id=id)
    return render(request, 'listings/listing_detail.html', context={'listing': listing})
