from principal.models import Receta, Comentario
from django.contrib.auth.models import User
from django.http import HttpResponse
from principal.models import Bebida
from django.shortcuts import render_to_response, get_object_or_404

def index_view(request):

	html = "<h1>Probando DJANGO en Heroku!!!</h1>"
	return HttpResponse(html)

def post(request, id):
	id1 = int(id)
	html = id1
	return HttpResponse(html)

def lista_bebidas(request):
	bebidas = Bebida.objects.all()
	return render_to_response('lista_bebidas.html',{'lista':bebidas})

def sobre(reques):
	html = "<html><body>Proyecto de ejemplo </body></html>"
	return HttpResponse(html)