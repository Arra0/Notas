while True:
 print("\nMi Calculadora")
 print("1-Suma")
 print("2-Resta")
 print("3-Multiplicación")
 print("4-División")
 print("5-Salir")
 opcion = input("Elige una opción: ")
 if opcion == '5':
  print("Hasta luego")
  break
 elif opcion < "1" or opcion > '5':
  print ( 'Opcion no Valida')
 else:
  num1 = float(input("Ingresa el primer número: "))
  num2 = float(input("Ingresa el segundo número: "))
 if opcion == '1':
  print("Resultado:", num1 + num2)
 elif opcion == '2':
  print("Resultado:", num1 - num2)
 elif opcion == '3':
  print("Resultado:", num1 * num2)
 elif opcion == '4':
  if num2 != 0:
   print("Resultado: ", num1 / num2)
  else:
   print("No se puede dividir entre cero")
 else:
  print("Finalizado")