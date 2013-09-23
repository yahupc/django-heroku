from django.http import HttpResponse

def index_view(request):
	html = "<body style = "background: blue">
	<h1>Probando DJANGO en Heroku!!!</h1>
	</body>"
	return HttpResponse(html)
