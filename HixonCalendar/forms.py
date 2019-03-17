from django import forms

class BookingForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})

    name = forms.CharField(label="Name", max_length=100)
    email = forms.EmailField(label="Email")
    phone = forms.CharField(label="Phone Number", max_length=100)
    date = forms.DateField(label="Date Requested")
    info = forms.CharField(label="Additional Information", widget=forms.Textarea(attrs={"rows": 3}))