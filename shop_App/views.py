from django.http import HttpResponseNotFound
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


def descripcion_producto(request, categoria, producto_titulo):
    if categoria == 'consolas':
        productos = [
            {"titulo": "Playstation 5", "foto": "ps5.png", "precio": "$560.990", "descripcion": "Consola Playstation 5"},
            {"titulo": "Nintendo Switch", "foto": "switch.png", "precio": "$320.990", "descripcion": "Consola Nintendo switch"},
            {"titulo": "Xbox Series X", "foto": "xbox.png", "precio": "$360.990", "descripcion": "Consola Xbox Series X"}
        ]
    elif categoria == 'computacion':
        productos = [
            {"titulo": "Macbook", "foto": "mac.png", "precio": "$870.990", "descripcion": "Notebook MacBook Air M1"},
            {"titulo": "Notebook Asus", "foto": "notebook.png", "precio": "$520.990", "descripcion": "Notebook Gamer Asus"},
            {"titulo": "HP Pavillion", "foto": "hp.png", "precio": "$760.990", "descripcion": "Notebook Gamer HP Pavillion"}
        ]
    elif categoria == 'telefonos':
        productos = [
            {"titulo": "Iphone", "foto": "iphone.png", "precio": "$1.230.990", "descripcion": "Telefono Iphone 14 Pro Max"},
            {"titulo": "Samsung", "foto": "samsung.png", "precio": "$870.990", "descripcion": "Telefono Samsung S23 Ultra"},
            {"titulo": "Xiaomi", "foto": "xiaomi.png", "precio": "$680.990", "descripcion": "Telefono Xiaomi 13T"}
        ]

    # Buscamos el producto según el título
    producto = next((p for p in productos if p["titulo"].replace(" ", "-").lower() == producto_titulo), None)

    if not producto:
        # Manejar el caso en que el producto no se encuentra
        return HttpResponseNotFound("Producto no encontrado")

    data = {"categoria": categoria, "producto": producto}
    return render(request, "shop_App/descripcionProducto.html", data)

def consolas(request):
    productos_consolas = [
        {"titulo": "Playstation 5", "foto": "ps5.png", "producto1": "Playstation 5"},
        {"titulo": "Nintendo Switch", "foto": "switch.png", "producto2": "Nintendo Switch"},
        {"titulo": "Xbox Series X", "foto": "xbox.png", "producto3": "Xbox Series X"}
    ]

    data = {"titulo": "Consolas", "productos": productos_consolas, "categoria": "consolas"}
    return render(request, "shop_App/producto.html", data)

def telefonos(request):
    productos_telefonos = [
        {"titulo": "Iphone", "foto": "iphone.png", "producto1": "Iphone"},
        {"titulo": "Samsung", "foto": "samsung.png", "producto2": "Samsung"},
        {"titulo": "Xiaomi", "foto": "xiaomi.png", "producto3": "Xiaomi"}
    ]

    data = {"titulo": "Telefonos", "productos": productos_telefonos, "categoria": "telefonos"}
    return render(request, "shop_App/producto.html", data)

def computacion(request):
    productos_computacion = [
        {"titulo": "Macbook", "foto": "mac.png", "producto1": "Macbook"},
        {"titulo": "Notebook Asus", "foto": "notebook.png", "producto2": "Notebook Asus"},
        {"titulo": "HP Pavillion", "foto": "hp.png", "producto3": "HP Pavillion"}
    ]

    data = {"titulo": "Computación", "productos": productos_computacion, "categoria": "computacion"}
    return render(request, "shop_App/producto.html", data)







