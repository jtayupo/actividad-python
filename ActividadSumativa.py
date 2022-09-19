class Notas: #Se crea la clase Notas
  
  def __init__(self):#Con este método se nicializan los Atributos
    self.nota1=(input("Ingrese la nota 1: "))#Se solicita al usuario ingresar valor numérico de la nota 1
    self.nota2=(input("Ingrese la nota 2: "))#Se solicita al usuario ingresar valor numérico de la nota 2
    self.nota3=(input("Ingrese la nota 3: "))#Se solicita al usuario ingresar valor numérico de la nota 3
    
    try:
      self.nota1=float(self.nota1)#Validación de lo ingresado por teclado
      self.nota2=float(self.nota2)
      self.nota3=float(self.nota3)
    
    except ValueError:
      print("ERROR los valores deben ser númericos entre 1 y 7\n""Fin del programa") #Error de validación si el valor no es numérico
      exit()
      
    while (self.nota1<1 or self.nota1>7) or (self.nota2<1 or self.nota2>7) or (self.nota3<1 or self.nota3>7): #Se establece rango del 1 al 7 para las notas
      print("ERROR los valores deben ser númericos entre 1 y 7\n""Fin del programa" ) #Error de validación si el valor es menor a 1 o mayor a 7
      exit()
      
  def nota_promedio(self): #Método para calcular el promedio de notas
    promedio = float((self.nota1 + self.nota2+ self.nota3) / 3)
    print("El premedio es: ", format(promedio,'.2f'))
    """ print("El promedio es: ",promedio) """
  
  def menor_nota(self):#Método para calcular la nota menor
      if(self.nota1 < self.nota2 and self.nota1 < self.nota3):
        print("La nota más baja es: ", self.nota1)
      else:
        if(self.nota2 < self.nota1 and self.nota2 < self.nota3):
          print("La nota más baja es: ", self.nota2)
        else:
          print("La nota más baja es: ", self.nota3)
    
  def mayor_nota(self):#Método para calcular la nota mayor
    if(self.nota1 > self.nota2 and self.nota1 > self.nota3):
      print("La nota más alta es: ", self.nota1)
    else:
      if(self.nota2 > self.nota1 and self.nota2 > self.nota3):
        print("La nota más alta es: ", self.nota2)
      else:
        print("La nota más alta es: ", self.nota3)
  
    
Nota = Notas() #Creación del objeto Nota
Nota.nota_promedio() #Llamar a método para calcular el promedio
Nota.menor_nota() #Llamar a método para calcular la nota menor
Nota.mayor_nota()#Llamar a método para calcular la nota mayor

#Fin








    
