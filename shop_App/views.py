from django.shortcuts import render

def inicio(request):
    return render(request,'shop_App/index.html')

def consolas(request):
    data = {"titulo": "Consolas", "foto1": "ps5.png","foto2":"switch.png","foto3":"xbox.png","producto1":"Playstation 5",
            "producto2":"Nintendo Switch ", "producto3": "Xbox series x"}
    return render(request, "shop_App/producto.html", data)

def computacion(request):
    data = {"titulo": "Computación", "foto1": "mac.png","foto2":"notebook.png","foto3":"hp.png","producto1":"Macbook",
            "producto2":"Notebook Asus", "producto3": "HP Pavillion"}
    return render(request,"shop_App/producto.html", data )

def telefonos(request):
    data = {"titulo": "Telefonos", "foto1": "iphone.png","foto2":"samsung.png","foto3":"xiaomi.png","producto1":"Iphone",
            "producto2":"Samsung ", "producto3": "Xiaomi"}
    return render(request,"shop_App/producto.html", data )

def usuario(request):
    data = {"titulo": "Usuario","foto":"usuario.jpg","nombre": "Edinson Aravena", "edad": 20, "carrera": "Ingeniería en informática", "correo":"edinson.aravena@inacapmail.cl"}
    return render(request,"shop_App/usuario.html", data)


def productoUno(request):
    data = {"categoria": "consolas",
            "titulo1":"Playstation 5", "titulo2": "Nintendo Switch", "titulo3":"Xbox Series X",
            "foto1":"ps5.png","foto2": "switch.png", "foto3": "xbox.png",
            "precio1":"$560.990", "precio2":"$320.990","precio3": "$360.990",
            "descripcion1":"Consola Playstation 5", "descripcion2":"Consola Nintendo switch","descripcion3":"Consola Xbox Series X"}
    return render(request,"shop_app/descripcionProducto.html", data )
    
def productoDos(request):
    data = {"categoria": "Computación",
            "titulo1":" Macbook", "titulo2": "Notebook Asus", "titulo3":"HP Pavillion",
            "foto1":"mac.png","foto2":"notebook.png","foto3":"hp.png",
            "precio1":"$870.990", "precio2":"$520.990","precio3": "$760.990",
            "descripcion1":"Notebook MacBook Air M1", "descripcion2":"Notebook Gamer Asus","descripcion3":"Notebook Gamer HP Pavillion"}
    return render(request,"shop_app/descripcionProducto.html", data )

def productoTres(request):
    data = {"categoria": "Celulares",
            "titulo1":" Iphone", "titulo2": "Samsung", "titulo3":"Xiaomi",
            "foto1":"iphone.png","foto2":"samsung.png","foto3":"xiaomi.png",
            "precio1":"$1.230.990", "precio2":"$870.990","precio3": "$680.990",
            "descripcion1":"Telefono Iphone 14 Pro Max", "descripcion2":"Telefono Samsumg S23 Ultra","descripcion3":"Telefono Xiomi 13T"}
    return render(request,"shop_app/descripcionProducto.html", data )







