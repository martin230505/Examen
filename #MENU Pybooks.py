#Tienda Pybooks

productos = {'8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
                      '2175HD': ['Acer', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
                      'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
                     'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
                     'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
                     '123FHD': ['Acer', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
                     '342FHD': ['Acer', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
                     'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050'],
                           }

stock = {'8475HD': [387990,10], 
        '2175HD': [327990,4],
        'JjfFHD': [424990,1],
        'fgdxFHD': [664990,21],
        '123FHD': [290890,32],
        '342FHD': [444990,7],
        'GF75HD': [749990,2],
        'UWU131HD': [349990,1],
        'FS1230HD': [249990,0],
                 }

def mostrar_todo():
    if productos :
        for modelo, datos in productos.items():
            print(f"{modelo}:{datos}")
    else:
        print('no hay productos en el sistema.')

#funcion q debe entragar el stock de una marca
def stock_marca():
    marca=input('marca a buscar:').lower()
    encontrados = False
    for modelo, datos in productos.items():
        if datos[0].lower() == marca:
            print(f"{modelo}: {datos}")
            encontrados = True
        if not encontrados :
            print('no hay productos de esa marca.')

   
#funcion que busque por RAM y Precio / que reciba la ram minima, y la ram minima , el precio como parametro y no debe retornar nada 


def busqueda_ram_precio(ram_min, ram_max, precio_max):
    encontrados= False
    for modelo, datos in productos.items():
        ram_num=int(datos[2].remplace("GB", ""))
        if ram_min <= ram_num <= ram_max and datos[5] <= precio_max:
            print(f'{modelo}:{datos}')
            encontrados = True
    if not encontrados:
        print('no se encontraron productos')

  
#funcion para eliminar producto

def eliminar_producto():
    while True:
        modelo = input("Codigo del producto a eliminar:").upper()
        if modelo in productos :
            confirmar = input(f"seguro desea eliminar{modelo}? si o no ?").lower()
            if confirmar == 'si':
                del productos[modelo]
                print('producto eliminado.')
            else:
                print('operacion cancelada.')
        else:
            print ('producto no encontrado.')
        otro = input ('¿desea eliminar otro modelo ? si o no?').lower()
        if otro != 'si':
            break
        

#salir 

def salir():
    print("MUCHAS GRACIAS POR USAR PYBOOKS!!!!!.")
    exit()


#funcion principal (menu)
def menu():

    while True :
            print('***Menu Principal***')
            print('1. Stock Marca ')
            print('2.Busqueda por RAM y Precio $')
            print('3. Eliminar Producto')
            print('4. Salir')
            print('5. mostrar todo.')
            
            opc = input ('ingrese una opcion 1- 5:')
            if opc == '1':
                stock_marca()
            elif opc =='2':
                try:
                    ram_min = int(input("RAM minima, ej 4:"))
                    ram_max = int(input("RAM Maxima:"))
                    precio = int(input("precio maximo:"))
                    busqueda_ram_precio(ram_min,ram_max, precio)
                except:
                    print("valores invalidos. intenta otra vez.")

                busqueda_ram_precio()
            elif opc =='3':
                eliminar_producto()
            elif opc == '4':
                salir()
            elif opc == '5':
                mostrar_todo()
            else:
                print ('opcion invalida.')
menu() 
    
