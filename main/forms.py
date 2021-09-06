from django import forms
from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator


GENDER_CHOICES = [
    ('3', 'Select gender'),
    ('1', 'Male'),
    ('0', 'Female')
]


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)


class PerformanceForm(forms.Form):
    jamb_score = forms.IntegerField(label="Candidate Jamb Score",
                                    validators=[MinValueValidator(1, message="Input is invalid!"),
                                                MaxValueValidator(400, message="Please provide a valid input")],)

    post_ume_score = forms.IntegerField(label="Candidate post UME AGG Score",
                                    validators=[MinValueValidator(1, message="Input is invalid!"),
                                                MaxValueValidator(100, message="Please provide a valid input")],)



    overal_aggregate_score = forms.FloatField(label="Candidate aggregate score",
                                         validators=[MinValueValidator(1, message="Year is invalid!"),
                                                     MaxValueValidator(100, message="Please provide a valid input")],)

    gender = forms.IntegerField(
        label="Gender", widget=forms.Select(choices=GENDER_CHOICES))
