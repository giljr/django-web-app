from django import forms

from listings.models import Band, Listing


class BandForm(forms.ModelForm):
    class Meta:
        model = Band
        fields = '__all__'

# Now, you might think that we would start by defining another form class,
# and for each field in our model, defining a corresponding form field, like this:

# class BandForm(forms.Form):
#    name = forms.CharField(max_length=100)
#    biography = forms.CharField(max_length=1000)
#    year_formed = forms.IntegerField(min_value=1900, max_value=2021)
#    official_homepage = forms.URLField(required=False)

# Even though we are building two separate things - a model and a form -
# there seems to be a lot of duplicated information between the two.
# We’ve already defined each field in the model, specifying the data types
# (string, integer), and the rules (e.g.,  max_length  ).

# Why should we have to define them in the form too?

# Wouldn’t it be great if we could let the model define the form?

# That’s exactly what  ModelForm's are for. Look above ☝️

# We just generated a form for our model without defining any
# form fields at all - we let the model do that for us!

# And here’s the best part:
# if we change the fields on the model,
# the form is automatically updated.👌️

# It’s great that Django can generate a form for us,
# but what if the default form doesn’t quite meet our needs?

# Well, you could build a form from scratch,
# like we did with the  ContactUsForm  , and use that.
# But it’s also possible to customize a ModelForm.
# We can  exclude  them from the form, like this:
#   fields = '__all__'  # delete this line
#   exclude = ('active', 'official_homepage')


class ListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = '__all__'


class ContactUsForm(forms.Form):
    # We allow the user to remain anonymous by making the  name  field optional
    name = forms.CharField(required=False)
    email = forms.EmailField()
    message = forms.CharField(max_length=1000)
