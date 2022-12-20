from django import forms
from .models import Exprecord

class ExprecordCreateForm(forms.ModelForm):

	class Meta:
		model = Exprecord
		fields = ['item', 'project', 'date', 'cost', 'proof']


class SearchForm(forms.Form):
	query = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'some text'}))