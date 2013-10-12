from principal.models import Receta, Comentario
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.template import RequestContext
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

def sobre(request):
	html = "<html><body>Proyecto de ejemplo </body></html>"
	return HttpResponse(html)

def inicio(request):
	recetas = Receta.objects.all()
	return render_to_response('inicio.html',{'recetas':recetas})

def usuarios(request):
	usuarios = User.objects.all()
	recetas = Receta.objects.all()
	return render_to_response('usuarios.html',{'usuarios':usuarios,'recetas':recetas})

def lista_recetas(request):
	recetas = Receta.objects.all()
	return render_to_response('recetas.html',{'datos':recetas},context_instance=RequestContext(request))

def detalle_receta(request, id_receta):
	dato = get_object_or_404(Receta, pk=id_receta)
	comentario = Comentario.objects.filter(recetario=dato)
	return render_to_response('receta.html','comentarios':comentarios,context_instance=RequestContext(request))
