import json
import os
# 1. Averiguamos la ruta absoluta de la carpeta donde está guardado este main.py
CARPETA_ACTUAL = os.path.dirname(os.path.abspath(__file__))
# 2. Unimos esa carpeta con el nombre del archivo JSON
ARCHIVO_INVENTARIO = os.path.join(CARPETA_ACTUAL, 'inventario.json')

def cargar_datos():
    try:
        with open(ARCHIVO_INVENTARIO, 'r', encoding='utf-8') as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("⚠️ Advertencia: El archivo de inventario está corrupto. Iniciando en blanco.")
        return []

def guardar_datos(inventario):
    with open(ARCHIVO_INVENTARIO, 'w', encoding='utf-8') as archivo:
        json.dump(inventario, archivo, indent=4, ensure_ascii=False)

# --- NUEVAS FUNCIONES DE LA INTERFAZ ---

def mostrar_menu():
    print("\n" + "="*45)
    print("📦 SISTEMA DE CONTROL DE INVENTARIO")
    print("="*45)
    print("1. Agregar nuevo bien (Alta)")
    print("2. Listar todo el inventario")
    print("3. Buscar bien por Código Patrimonial")
    print("4. Salir")
    print("="*45)

def agregar_bien(inventario):
    print("\n--- REGISTRAR NUEVO BIEN ---")
    codigo = input("Ingrese el Código Patrimonial (Ej. 7408950001): ")
    
    # Validar que el código no exista ya (Evitar duplicados)
    for item in inventario:
        if item["codigo_patrimonial"] == codigo:
            print("❌ Error: Ya existe un bien registrado con ese código.")
            return # Termina la función aquí para no duplicar

    descripcion = input("Descripción del equipo (Ej. Monitor 24\"): ")
    estado = input("Estado (Bueno/Regular/Malo): ")
    
    try:
        stock = int(input("Cantidad (Stock): "))
    except ValueError:
        print("❌ Error: El stock debe ser un número entero. Se asignará 1 por defecto.")
        stock = 1

    nuevo_bien = {
        "codigo_patrimonial": codigo,
        "descripcion": descripcion,
        "estado": estado,
        "stock": stock
    }
    
    # Actualizamos la memoria
    inventario.append(nuevo_bien)
    # ¡Guardamos en el disco de inmediato!
    guardar_datos(inventario) 
    print(f"✅ Bien '{descripcion}' agregado con éxito y guardado en disco.")

def listar_inventario(inventario):
    print("\n--- INVENTARIO ACTUAL ---")
    if not inventario: # Forma "Pythonica" de preguntar si una lista está vacía
        print("📭 El inventario está vacío.")
        return
    
    # Creamos un encabezado tipo tabla para que se vea profesional
    print(f"{'CÓDIGO':<15} | {'DESCRIPCIÓN':<25} | {'ESTADO':<10} | {'STOCK'}")
    print("-" * 65)
    
    for item in inventario:
        # El :<15 asegura que el texto ocupe exactamente 15 espacios alineados a la izquierda
        print(f"{item['codigo_patrimonial']:<15} | {item['descripcion']:<25} | {item['estado']:<10} | {item['stock']}")

def buscar_bien(inventario):
    print("\n--- BUSCAR BIEN ---")
    codigo = input("Ingrese el Código Patrimonial a buscar: ")
    
    for item in inventario:
        if item["codigo_patrimonial"] == codigo:
            print("\n✅ ¡Bien encontrado!")
            print(f"Código: {item['codigo_patrimonial']}")
            print(f"Descripción: {item['descripcion']}")
            print(f"Estado: {item['estado']}")
            print(f"Stock: {item['stock']}")
            return # Encontramos el ítem, salimos de la función
            
    print("❌ No se encontró ningún bien con ese código.")

def main():
    # 1. Al iniciar el programa, cargamos los datos del archivo a la variable en memoria
    inventario = cargar_datos()
    
    while True:
        mostrar_menu()
        opcion = input("Elige una opción (1-4): ")
        
        if opcion == '1':
            agregar_bien(inventario)
        elif opcion == '2':
            listar_inventario(inventario)
        elif opcion == '3':
            buscar_bien(inventario)
        elif opcion == '4':
            print("¡Hasta luego! Saliendo del sistema...")
            break
        else:
            print("❌ Opción no válida.")

if __name__ == "__main__":
    main()