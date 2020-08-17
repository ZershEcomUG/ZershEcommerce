from django import forms

class CheckoutForm(forms.Form):
    phone = forms.IntegerField()
    location = forms.CharField()
    address = forms.CharField()
    building_apartment_name = forms.CharField(required=False)
    order_notes = forms.CharField( required=False , widget=forms.Textarea)

class ReviewForm(forms.Form):
    review = forms.IntegerField()
    review_text = forms.CharField( required=False , widget=forms.Textarea)