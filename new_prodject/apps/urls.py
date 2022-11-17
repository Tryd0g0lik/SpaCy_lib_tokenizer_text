from django.urls import path

from apps.views import TokenizertextFile

urlpatterns = [
	path("", TokenizertextFile),
	path("paths/", TokenizertextFile),

]