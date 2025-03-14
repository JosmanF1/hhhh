"""
Juego de Ruleta Simulado

Este programa permite a un usuario apostar en una ruleta virtual. 
El jugador puede elegir entre diferentes tipos de apuestas y ver su historial.

Características:
- Apostar por número específico.
- Apostar por sección.
- Apostar por color.
- Ver historial de apuestas.

El juego finaliza cuando el saldo del jugador es 0 o cuando elige salir.
"""

import random  # Importamos el módulo random para generar números aleatorios

def ruleta():
    """
    Función principal del juego de ruleta.
    Inicializa el saldo del jugador y permite realizar diferentes tipos de apuestas.
    """
    saldo = 100  # Saldo inicial del jugador
    historial = []  # Lista para registrar las apuestas realizadas
    ruleta = list(range(1, 37))  # Números disponibles en la ruleta (1-36)
    
    # Diccionario que asigna un color a cada número (pares = rojo, impares = negro)
    colores = {n: 'rojo' if n % 2 == 0 else 'negro' for n in ruleta}  
    
    ganadas = 0  # Contador de apuestas ganadas
    perdidas = 0  # Contador de apuestas perdidas
    
    while saldo > 0:  # El juego continúa mientras el jugador tenga saldo
         # Muestra el menú de opciones disponibles
        print(f"Saldo: {saldo} coins")
        print("1. Apostar por número")
        print("2. Apostar por sección")
        print("3. Apostar por color")
        print("4. Ver historial")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")# Solicita al usuario que ingrese una opción y la almacena en la variable 'opcion
        
        if opcion == "5":
            break  # Termina el juego
        elif opcion == "4":
            # Muestra el historial de apuestas
            print("Historial de apuestas:")
            for h in historial:  # Recorre la lista de historial y muestra cada apuesta realizad
                print(f"Apostado: {h[0]}, Ganancia: {h[1]}")
            if perdidas == 0:
                print("Promedio de éxito: No hay apuestas perdidas aún.")
            else:
                print(f"Promedio de éxito: {ganadas / perdidas:.2f}")
        elif opcion == "1":  
            # Apuesta por número específico
            monto = int(input("Monto a apostar: "))  # Solicita el monto de la apuesta y lo convierte a entero
            if monto > saldo:  # Verifica si el usuario tiene suficiente saldo
                print("No tienes suficiente saldo para esta apuesta.")
                continue
            num = int(input("Número (1-36): "))
            resultado = random.choice(ruleta)  # Se genera un número aleatorio
            color = colores[resultado]  # Se obtiene el color del número generado
            print(f"Resultado: {resultado} ({color})")
            ganancia = 0
            if num == resultado:
                ganancia = monto * 20  # Gana 20 veces la apuesta si acierta
                ganadas += 1
            else:
                perdidas += 1
            saldo += ganancia - monto  # Se actualiza el saldo
            historial.append((monto, ganancia))  # Se guarda en el historial
            print("Ganaste!" if ganancia else "Perdiste.")
        elif opcion == "2":  
            # Apuesta por sección
            monto = int(input("Monto a apostar: "))
            if monto > saldo: # Verifica si el usuario tiene suficiente saldo
                print("No tienes suficiente saldo para esta apuesta.")
                continue # Vuelve al inicio del bucle
                # Muestra las secciones disponibles para aposta
            print("1. Sección A (1-12)")
            print("2. Sección B (13-24)")
            print("3. Sección C (25-36)")
             #Solicita la sección elegida y la convierte a minúsculas para evitar errores por mayúsculas/minúsculas  
            sec = input("Selecciona una sección (A/B/C): ").lower()
            
            if sec == "a":
                rango = range(1, 13)  # Define el rango de la sección A
                nombre_seccion = "A"
            elif sec == "b":
                rango = range(13, 25)  # Define el rango de la sección B
                nombre_seccion = "B"
            elif sec == "c":
                rango = range(25, 37)  # Define el rango de la sección C
                nombre_seccion = "C"
            else:
                print("Sección no válida.")
                continue
            
            resultado = random.choice(ruleta)  # Se genera un número aleatorio
            color = colores[resultado]  # Se obtiene el color del número generado
            print(f"Resultado: {resultado} ({color})")
            ganancia = 0
            if resultado in rango:
                ganancia = monto * 5  # Gana 5 veces la apuesta si acierta
                ganadas += 1
            else:
                perdidas += 1
            saldo += ganancia - monto  # Se actualiza el saldo
            historial.append((monto, ganancia))  # Se guarda en el historial
            print(f"Ganaste! (Sección {nombre_seccion})" if ganancia else "Perdiste.")
        elif opcion == "3":  
            # Apuesta por color
            monto = int(input("Monto a apostar: "))  # Solicita el monto de la apuesta
            if monto > saldo:
                print("No tienes suficiente saldo para esta apuesta.")
                continue
            col = input("Color (rojo/negro): ").lower()  # Solicita el color a apostar
            resultado = random.choice(ruleta)  # Se genera un número aleatorio
            color = colores[resultado]  # Se obtiene el color del número generado
            print(f"Resultado: {resultado} ({color})")  # Se muestra el resultado
            ganancia = 0  # Inicializa la ganancia en 0
            if col == color:
                ganancia = monto * 2  # Si acierta, gana el doble de la apuesta
                ganadas += 1  # Aumenta el contador de apuestas ganadas
            else:
                perdidas += 1  # Aumenta el contador de apuestas perdidas
            saldo += ganancia - monto  # Se actualiza el saldo restando la apuesta y sumando la ganancia
            historial.append((monto, ganancia))  # Se registra la apuesta en el historial
            print("Ganaste!" if ganancia else "Perdiste.")  # Se muestra el resultado
    
    print(f"Saldo final: {saldo} coins")  # Se muestra el saldo final al terminar el juego

# Punto de entrada principal del programa
if __name__ == "__main__":
    ruleta()  # Se ejecuta el juego
