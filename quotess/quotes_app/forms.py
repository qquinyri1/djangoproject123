from django.forms import ModelForm, CharField, DateField, TextInput, DateInput, Textarea
from .models import Author, Tag, Quote


class TagForm(ModelForm):
    name = CharField(min_length=3, max_length=25, required=True)

    class Meta:
        model = Tag
        fields = ['name']


class AuthorForm(ModelForm):
    fullname = CharField(min_length=5, max_length=100, widget=TextInput())
    born_date = DateField(widget=DateInput(), help_text="Valid date format 'mm/dd/yyyy'")
    born_location = CharField(min_length=5, max_length=150, widget=TextInput())
    description = CharField(min_length=10, max_length=255, widget=Textarea())

    class Meta:
        model = Author
        fields = ['fullname', 'born_date', 'born_location', 'description']


class QuoteForm(ModelForm):
    quote = CharField(min_length=10, max_length=255, widget=Textarea())

    class Meta:
        model = Quote
        fields = ['quote']


