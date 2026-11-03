def mostrar_menu():
    print("\n" + "="*30)
    print("📋 GESTOR DE TAREAS CLI")
    print("="*30)
    print("1. Agregar una tarea")
    print("2. Ver todas las tareas")
    print("3. Marcar tarea como completada")
    print("4. Eliminar una tarea")
    print("5. Salir")
    print("="*30)

def agregar_tarea(lista_tareas):
    """Solicita el título de la tarea y la añade a la lista."""
    titulo = input("✍️ Escribe la descripción de la tarea: ")
    
    # Lógica para autoincrementar el ID (como un PRIMARY KEY IDENTITY)
    if len(lista_tareas) == 0:
        nuevo_id = 1
    else:
        # Buscamos el ID del último elemento y le sumamos 1
        nuevo_id = lista_tareas[-1]['id'] + 1 
        
    nueva_tarea = {
        'id': nuevo_id,
        'titulo': titulo,
        'completada': False # Por defecto, una tarea nueva no está completada
    }
    
    lista_tareas.append(nueva_tarea)
    print(f"✅ Tarea '{titulo}' agregada con éxito (ID: {nuevo_id}).")

def ver_tareas(lista_tareas):
    """Muestra todas las tareas formateadas. Si no hay, avisa al usuario."""
    print("\n--- TUS TAREAS ---")
    if len(lista_tareas) == 0:
        print("📭 No hay tareas pendientes. ¡Todo al día!")
        return # Termina la función aquí mismo si no hay tareas
        
    for tarea in lista_tareas:
        # Usamos un operador ternario para mostrar un check o un reloj de arena
        estado = "✅" if tarea['completada'] else "⏳"
        print(f"[{tarea['id']}] {estado} {tarea['titulo']}")
        
def completar_tarea(lista_tareas):
    # Primero mostramos las tareas para que el usuario vea los IDs
    ver_tareas(lista_tareas)
    if len(lista_tareas) == 0:
        return # Si no hay tareas, salimos de la función
    
    # Manejo de errores (try/except) por si el usuario escribe letras en vez de números
    try:
        id_ingresado = int(input("\nIngresa el ID de la tarea que terminaste: "))
        
        # Buscamos la tarea recorriendo la lista
        tarea_encontrada = False
        for tarea in lista_tareas:
            if tarea['id'] == id_ingresado:
                tarea['completada'] = True # ¡Hacemos el "UPDATE"!
                tarea_encontrada = True
                print(f"🎉 ¡Genial! Marcaste '{tarea['titulo']}' como completada.")
                break # Rompemos el bucle for porque ya encontramos la tarea
                
        if not tarea_encontrada:
            print("❌ No se encontró ninguna tarea con ese ID.")
            
    except ValueError:
        print("❌ Error: Debes ingresar un número, no letras.")

def eliminar_tarea(lista_tareas):
    ver_tareas(lista_tareas)
    if len(lista_tareas) == 0:
        return
    
    try:
        id_ingresado = int(input("\nIngresa el ID de la tarea a eliminar: "))
        
        # Enumerate nos da el índice (posición 0, 1, 2...) y la tarea misma
        tarea_encontrada = False
        for indice, tarea in enumerate(lista_tareas):
            if tarea['id'] == id_ingresado:
                # El método pop() elimina un elemento de la lista usando su índice
                tarea_eliminada = lista_tareas.pop(indice) 
                tarea_encontrada = True
                print(f"🗑️ La tarea '{tarea_eliminada['titulo']}' ha sido eliminada.")
                break
                
        if not tarea_encontrada:
            print("❌ No se encontró ninguna tarea con ese ID.")
            
    except ValueError:
        print("❌ Error: Debes ingresar un número, no letras.")

def main():
    tareas = [] 
    
    while True:
        mostrar_menu()
        opcion = input("Elige una opción (1-5): ")
        
        if opcion == '1':
            agregar_tarea(tareas)
        elif opcion == '2':
            ver_tareas(tareas)
        elif opcion == '3':
            completar_tarea(tareas)
        elif opcion == '4':
            eliminar_tarea(tareas)
        elif opcion == '5':
            print("¡Hasta luego! Saliendo del programa...")
            break 
        else:
            print("❌ Opción no válida. Por favor, intenta de nuevo.")

if __name__ == "__main__":
    main()