from django.shortcuts import render, redirect
from .models import Flor,Ticket
from django.contrib.auth.models import User
from .forms import CustomUserForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,logout,login as login_autent
# agregar un "decorator" para impedir ingresar a las paginas si no esta logeado
from django.contrib.auth.decorators import login_required
from .clases import elemento
import datetime

# Creación de las VIEWS

def home(request): #Render del Home
    return render(request, 'core/home.html')

def contacto(request):
    return render(request, 'core/contacto.html')

def login(request):
    if request.POST:
        usuario=request.POST.get("txtUsuario")
        password=request.POST.get("txtPass")
        us=authenticate(request,username=usuario,password=password)
        msg=''
        request.session["carrito"] = []        
        request.session["carritox"] = []        
        print('realizado')
        if us is not None and us.is_active:
            login_autent(request,us)#autentificacion de login            
            return render(request,'core/home.html')
        else:
            return render(request,'core/login.html')

    return render(request,'registration/login.html')

@login_required(login_url='/login/')
def tienda(request):
    flores = Flor.objects.all()
    return render(request, 'core/tienda.html', {'flores':flores})

def registro_usuario(request):
    data = {
        'form':CustomUserForm()
    }
    if request.method == 'POST':
        formulario = CustomUserForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            #Autenticar al usuario y redirigir al inicio
            username = formulario.cleaned_data['username'] #Toma al campo user
            password = formulario.cleaned_data['password1'] #Toma la contraseña
            user = authenticate(username=username, password=password) #Autentica con el user y pass recien tomados
            login(request, user)
            return redirect(to='home') #Redirige al Login
    return render(request, 'registration/registro.html', data)


@login_required(login_url='/login/')
def grabar_carro(request):
    x=request.session["carritox"]    
    usuario=request.user.username
    suma=0
    try:
        for item in x:        
            nombre=item["nombre"]
            precio=int(item["precio"])
            cantidad=int(item["cantidad"])
            total=int(item["total"])        
            ticket=Ticket(
                usuario=usuario,
                nombre=nombre,
                precio=precio,
                cantidad=cantidad,
                total=total,
                fecha=datetime.date.today()
            )
            ticket.save()
            suma=suma+int(total)  
            print("reg grabado")                 
        mensaje="Grabado"
        request.session["carritox"] = []
    except:
        mensaje="error al grabar"            
    return render(request,'core/carrito.html',{'x':x,'total':suma,'mensaje':mensaje})

@login_required(login_url='/login/')
def carro_compras(request,id):
    f=Flor.objects.get(nombre=id)
    x=request.session["carritox"]
    el=elemento(1,f.nombre,f.precio,1)
    sw=0
    suma=0
    clon=[]
    for item in x:        
        cantidad=item["cantidad"]
        if item["nombre"]==f.nombre:
            sw=1
            cantidad=int(cantidad)+1
        ne=elemento(1,item["nombre"],item["precio"],cantidad)
        suma=suma+int(ne.total())
        clon.append(ne.toString())
    if sw==0:
        clon.append(el.toString())
    x=clon    
    request.session["carritox"]=x
    flores=Flor.objects.all()    
    return render(request,'core/tienda.html',{'flores':flores,'total':suma})
    
@login_required(login_url='/login/')
def carros(request):
    x=request.session["carritox"]
    suma=0
    for item in x:
        suma=suma+int(item["total"])           
    return render(request,'core/carrito.html',{'x':x,'total':suma})

@login_required(login_url='/login/')
def carro_compras_mas(request,id):
    f=Flor.objects.get(nombre=id)
    x=request.session["carritox"]
    suma=0
    clon=[]
    for item in x:        
        cantidad=item["cantidad"]
        if item["nombre"]==f.nombre:
            cantidad=int(cantidad)+1
        ne=elemento(1,item["nombre"],item["precio"],cantidad)
        suma=suma+int(ne.total())
        clon.append(ne.toString())
    x=clon    
    request.session["carritox"]=x
    x=request.session["carritox"]        
    return render(request,'core/carrito.html',{'x':x,'total':suma})

@login_required(login_url='/login/')
def carro_compras_menos(request,id):
    f=Flor.objects.get(nombre=id)
    x=request.session["carritox"]
    clon=[]
    suma=0
    for item in x:        
        cantidad=item["cantidad"]
        if item["nombre"]==f.nombre:
            cantidad=int(cantidad)-1
        ne=elemento(1,item["nombre"],item["precio"],cantidad)
        suma=suma+int(ne.total)
        clon.append(ne.toString())
    x=clon    
    request.session["carritox"]=x
    x=request.session["carritox"]    
    return render(request,'core/carrito.html',{'x':x,'total':total})

def agregar_carrito(request, id):
    #recuperar los valores de una session
    #"carrito"
    lista=request.session.get("carrito","")
    #agrega en una sesion el carrito el titulo

    #un arreglo de flores (gracioso?)
    arr=lista.split(";")
    cant=1
    for f in arr:
        flor=f.split(":")
        if flor[0]==id:
            cant=flor[1]+1

    #sesion "carrito"que muestra el 
    #titulo de nuestra flor
    lista=lista+";"+str(id)+str(":")+str(cant)

    request.session["carrito"]=lista
    flores = Flor.objects.all()
    return render(request,"core/tienda.html",{'msg':'agrego','flores':flores})

def carrito(request):
    lista=request.session.get("carrito","")
    #transformar el listado de peliculas en un arreglin
    arreglo=lista.split(";")
    return render(request, 'core/carrito.html',{'contenido':arreglo})

def vaciar_carrito(request):
    request.session["carrito"]=""
    lista=request.session.get("carrrito","")
    return render(request,'core/carrito.html',{'contenido':lista})

######################################################################
def isset(variable):
	return variable in locals() or variable in globals()