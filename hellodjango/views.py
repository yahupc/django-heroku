from django.http import HttpResponse

def index_view(request):
	html = "Bienvenido al curso"
	return HttpResponse(html)