from django import forms
from buyermodule.models import BuyerModel

class BuyerForm(forms.ModelForm):
	class Meta():
		model=BuyerModel
		exclude=("create_date",)