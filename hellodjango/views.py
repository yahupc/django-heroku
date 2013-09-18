from django.http import HttpResponse

def index_view(request):
	html = "Probando Django en Heroku!!!"
	return HttpResponse(html)