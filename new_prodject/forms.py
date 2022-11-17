from django import forms



class FormName(forms.Form):
	path_file = forms.FileField(label='filName')
