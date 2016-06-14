from django import forms
from .models import Hotel

class QueryForm(forms.Form):
	class Meta:
		model = Hotel
		fields = ('hotel_id')