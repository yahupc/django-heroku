from principal.models import Receta, Comentario
from principal.forms import ContactoForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.core.mail import EmailMessage
# from principal.models import Bebida

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
	# html = "<html><body>Proyecto de ejemplo </body></html>"
	# return HttpResponse(html)
	return render_to_response('sobre.html',context_instance=RequestContext(request))

def inicio(request):
	recetas = Receta.objects.all()
	return render_to_response('inicio.html',{'recetas':recetas},context_instance=RequestContext(request))

def usuarios(request):
	usuarios = User.objects.all()
	recetas = Receta.objects.all()
	return render_to_response('usuarios.html',{'usuarios':usuarios,'recetas':recetas},context_instance=RequestContext(request))

def lista_recetas(request):
	recetas = Receta.objects.all()
	return render_to_response('recetas.html',{'datos':recetas},context_instance=RequestContext(request))

def detalle_receta(request, id_receta):
	dato = get_object_or_404(Receta, pk=id_receta)
	comentarios = Comentario.objects.filter(receta=dato)
	return render_to_response('receta.html',{'receta':dato,'comentarios':comentarios},context_instance=RequestContext(request))

def contacto(request):
	if request.method=='POST':
		formulario = ContactoForm(request.POST)
		if formulario.is_valid():
			titulo = 'Mensaje desde el recetario de Maestros del Web'
			contenido = formulario.cleaned_data['mensaje'] + "\n"
			contenido += 'Comunicarse a:' + formulario.cleaned_data['correo']
			correo = EmailMessage(titulo, contenido, to=['yahu39pc@gmail.com'])
			correo.send()
			return HttpResponseRedirect('/')
	else:
		formuario = ContactoForm()
	return render_to_response('contactoform.html',{'formulario':formulario}, context_instance=RequestContext(request))