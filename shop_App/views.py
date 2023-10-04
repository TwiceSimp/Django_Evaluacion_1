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
            {"titulo": "Playstation 5", "foto": "ps5.png", "precio": "$560.990", "descripcion": "Frecuencia variable de GPU hasta 2.23 GHz (10.3 TFLOPS). Memoria GDDR6 16 GB con ancho de banda de 448 GB/s. Unidad de almacenamiento SSD 825 GB. Ancho de banda de lectura 5.5 GB/s (datos puros) y 9 GB/s (datos comprimidos)."},
            {"titulo": "Nintendo Switch", "foto": "switch.png", "precio": "$320.990", "descripcion": " ofrece colores brillantes y contrastes definidos, la consola Nintendo Switch incluye 64 GB de almacenamiento interno, una base con un puerto LAN para conexión por cable para jugar en el televisor, un soporte ajustable y amplio y audio mejorado."},
            {"titulo": "Xbox Series X", "foto": "xbox.png", "precio": "$360.990", "descripcion": "CPU: CPU Zen 2 personaliza de 8 núcleos a 3,8 GHz (3,66 GHz con SMT)Tarjeta gráfica: GPU de 12 TERAFLOPS, 52 CU a 1,825 GHz con RDNA 2 personalizada.Memoria: GDDR6 de 16 GB.Almacenamiento interno: SSD NVME personalizado de 1 TB (ampliable),Resolución: 4K.Alto rango dinámico: HDR 8K."}                                                                                  
        ]
    elif categoria == 'computacion':
        productos = [
            {"titulo": "Macbook", "foto": "mac.png", "precio": "$870.990", "descripcion": "El MacBook Air M1 cuenta con un procesador Apple M1, GPU integrada, almacenamiento SSD y una pantalla Retina de alta resolución."},
            {"titulo": "Notebook Asus", "foto": "notebook.png", "precio": "$520.990", "descripcion": "Los notebooks gamers Asus suelen tener potentes tarjetas gráficas NVIDIA/AMD, procesadores Intel/AMD de alto rendimiento, amplia RAM y almacenamiento SSD para un rendimiento gaming óptimo."},
            {"titulo": "HP Pavillion", "foto": "hp.png", "precio": "$760.990", "descripcion": "La HP Pavilion generalmente cuenta con procesadores Intel o AMD, opciones de RAM y almacenamiento variadas, gráficos integrados o dedicados, y una pantalla de calidad."}
        ]
    elif categoria == 'telefonos':
        productos = [
            {"titulo": "Iphone", "foto": "iphone.png", "precio": "$1.230.990", "descripcion": "Smartphone con pantalla de 6.7, Apple A16 Bionic, 6GB RAM, opciones de almacenamiento de 128GB a 1TB, sin microSD, cámara triple de 48MP+12MP+12MP."},
            {"titulo": "Samsung", "foto": "samsung.png", "precio": "$870.990", "descripcion": "Smartphone con cámaras traseras de 200 MP + 10 MP (telefoto) + 12 MP (ultra gran angular) + 10 MP (telefoto doble), cámara frontal de 12 MP. Ofrece 45 horas de conversación y 13.75 días en espera. Pantalla Dynamic AMOLED WQHD+ (New Edge) de 6.8 con resolución 2x3080 x 1400 píxeles."},
            {"titulo": "Xiaomi", "foto": "xiaomi.png", "precio": "$680.990", "descripcion": "Dispositivo con sistema operativo Android 13 y MIUI 14, alimentado por un chipset MediaTek Dimensity 8200-Ultra. Equipado con un procesador Octa-core (1x Cortex-A78 3.1 GHz + 3x Cortex-A78 3.0 GHz + 4x Cortex-A55 2.0 GHz) fabricado en TSMC de 4nm, y una GPU Arm Mali-G610."}
        ]


    producto = next((p for p in productos if p["titulo"].replace(" ", "-").lower() == producto_titulo), None)

    if not producto:
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







