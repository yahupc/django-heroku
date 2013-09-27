from django.http import HttpResponse

def index_view(request):
	html = "Probando DJANGO en Heroku!!!"
	return HttpResponse(html)