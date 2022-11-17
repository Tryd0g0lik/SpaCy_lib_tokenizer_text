from django.shortcuts import render

from apps.myprogram import tokenizingText
from forms import FormName


def TokenizertextFile(request):

	context = {}
	if  request.method == 'POST':
		f = 'new_prodject/apps/files/' + request.POST['path_file']

		dataOfFile = tokenizingText(f)

		template = 'apps/paths.html'
		context = {'data_token': dataOfFile}
		return render(request, template, context)

	else:
		template = 'apps/output.html'
		form = FormName()
		context = {'form' : form}

		return render(request, template, context)

