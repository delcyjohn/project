from django import forms
from paintermodule.models import Painter

class PainterForm(forms.ModelForm):
	class Meta():
		model=Painter
		exclude=("create_date",)