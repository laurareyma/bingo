import random

class Bingo:
    def _init_(self):
        self.inicio()

    def inicio(self): # Menu principal 

        opcion=-1 # para que entre al while
        while(opcion!=0): # mientras opcion sea diferente de 0, se ejecuta el menu
            opciones={1: self.configurador, 2: self.jugar, 0: self.salir} # diccionario de opciones
            print("1. Configurar juego. \n"
                  "2. Jugar. \n"
                  "0. Salir. \n")
            opcion=(int(input("Digite opcion: "))) 
            opciones.get(opcion, self.default)() # si la opcion no esta en el diccionario, se ejecuta default

    def configurador(self): # Configurador de juego
        self.numJugadores=(int(input("Digite numero de jugadores: "))) # se pide el numero de jugadores
        self.nombres=[] # lista de nombres de jugadores
        for i in range(self.numJugadores): # se pide el nombre de cada jugador
            nombre=(input(f"Ingrese el nombre del jugador {i+1}: ")) 
            self.nombres.append(nombre) 
        self.cartones() # se llama a la funcion cartones

    def cartones(self): # Generador de cartones
        for i in range(self.numJugadores): # se generan los cartones de cada jugador
            print(" "+self.nombres[i]) # se imprime el nombre del jugador
            print(" B   I   N   G   O ") # se imprime el titulo del carton
            self.bingo = [] # lista de cartones
            for f in range(5): # se generan los numeros de cada carton
                fila = random.sample(range(f * 15 + 1, (f + 1) * 15 + 1), 5) # se generan los numeros de cada fila
                self.bingo.append(fila) # se agregan los numeros a la lista de cartones
            self.mostrarCartones() # se llama a la funcion mostrarCartones

    def mostrarCartones(self): 
        for f in range(5): 
            for c in range(5): 
                print(f"{self.bingo[c][f]:2}", end="  ") # se imprimen los numeros de cada carton
            print()
            

    def jugar(self): 
        forma=-1 # para que entre al while
        while(forma!=0): # mientras opcion sea diferente de 0, se ejecuta el menu

            formas={1: self.todo, 2: self.cuadrado, 3: self.letraL, 4: self.letraB, 5: self.letraI, 6: self.letraN, 7: self.letraG, 8: self.letraO, 0: self.regresar}
            print("=======OPCIONES=========\n"
                "1: Todo.\n"
                "2: Cuadrado.\n"
                "3: Letra L.\n"
                "4: Letra B.\n"
                "5: Letra I.\n"
                "6: Letra N.\n"
                "7: Letra G.\n"
                "8: Letra O.\n"
                "0: Regresar.\n")
            forma=(int(input("Digite la opcion: "))) 
            formas.get(forma, self.default)() # si la opcion no esta en el diccionario, se ejecuta default

    def todo(self):
        # llenar todo el carton, no importa el orden, si el número está en el cartón se marca (cambia de color)
        # se genera un numero aleatorio
        # se busca el numero en el carton
        # si se encuentra, se marca
        # si no se encuentra, se genera otro numero aleatorio
        # se repite hasta que se encuentren todos los numeros del carton
        # se repite para todos los cartones
        # se repite para todos los jugadores
        # se repite hasta que alguien cante bingo
        letra = random.choice("BINGO")
        
        if (letra=="B"):
            num=random.randint(1,15)
        if(letra=="I"):
            num=random.randint(16,30)
        if(letra=="N"):
            num=random.randint(31,45)
        if(letra=="G"):
            num=random.randint(46,60)
        if(letra=="O"):
            num=random.randint(61,75)
            
        print(f"Balota: {letra}-{num}")
        
        for f in range(5):
            fila=[]
            for c in range(5):
                if(self.bingo[c][f]==num):
                    fila.append("X")
                else:
                    fila.append(self.bingo[c][f])
            print(fila)

    def verificarBingo(self):
        # Verificar si alguien hizo Bingo en esta forma
        for i in range(self.numJugadores):
            for f in range(5):
                fila = []
                for c in range(5):
                    if (f == 1 or f == 3) and (c == 1 or c == 3): # si es una posición del cuadrado
                        # Marcar el cuadrado
                        fila.append("X")

    def cuadrado(self):
        # Se genera un número aleatorio para marcar en el cuadrado
        num = random.randint(1, 75) 
        print(f"Balota: {num}") 

        # Marcar el cuadrado en cada cartón
        for i in range(self.numJugadores): 
            print(f"\nCartón de {self.nombres[i]}:") 
            for f in range(5): 
                fila = [] 
                for c in range(5): 
                    if (f == 1 or f == 3) and (c == 1 or c == 3): # si es una posición del cuadrado
                        # Marcar el cuadrado
                        fila.append("X") 
                    else:
                        fila.append(self.bingo[i][c][f])
                print(fila)

        # Verificar si alguien hizo Bingo en esta forma
        self.verificarBingo()

    def letraL(self):
        # Se genera un número aleatorio para marcar en el cuadrado
        num = random.randint(1, 75)
        print(f"Balota: {num}")

        # Marcar la letra L en cada cartón
        for i in range(self.numJugadores):
            print(f"\nCartón de {self.nombres[i]}:")
            for f in range(5):
                fila = []
                for c in range(5):
                    if (f == 1 or f == 2 or f == 3) and c == 1:
                        # Marcar la letra L
                        fila.append("X")
                    else:
                        fila.append(self.bingo[i][c][f])
                print(fila)

    def letraB(self):
        
        # Se genera un número aleatorio para marcar en el cuadrado
        num = random.randint(1, 75)
        print(f"Balota: {num}")

        # Marcar la letra B en cada cartón
        for i in range(self.numJugadores):
            print(f"\nCartón de {self.nombres[i]}:")
            for f in range(5):
                fila = []
                for c in range(5):
                    if (f == 0 or f == 1 or f == 2 or f == 3) and c == 1:
                        # Marcar la letra B
                        fila.append("X")
                    else:
                        fila.append(self.bingo[i][c][f])
                print(fila)

    def letraI(self):
        # Se genera un número aleatorio para marcar en el cuadrado
        num = random.randint(1, 75)
        print(f"Balota: {num}")

        # Marcar la letra I en cada cartón
        for i in range(self.numJugadores):
            print(f"\nCartón de {self.nombres[i]}:")
            for f in range(5):
                fila = []
                for c in range(5):
                    if (f == 0 or f == 1 or f == 2 or f == 3) and c == 2:
                        # Marcar la letra I
                        fila.append("X")
                    else:
                        fila.append(self.bingo[i][c][f])
                print(fila)


    def letraN(self):
        # Se genera un número aleatorio para marcar en el cuadrado
        num = random.randint(1, 75)
        print(f"Balota: {num}")

        # Marcar la letra N en cada cartón
        for i in range(self.numJugadores):
            print(f"\nCartón de {self.nombres[i]}:")
            for f in range(5):
                fila = []
                for c in range(5):
                    if (f == 0 or f == 1 or f == 2 or f == 3) and c == 3:
                        # Marcar la letra N
                        fila.append("X")
                    else:
                        fila.append(self.bingo[i][c][f])
                print(fila)

    def letraG(self):
        # Se genera un número aleatorio para marcar en el cuadrado
        num = random.randint(1, 75)
        print(f"Balota: {num}")

        # Marcar la letra G en cada cartón
        for i in range(self.numJugadores):
            print(f"\nCartón de {self.nombres[i]}:")
            for f in range(5):
                fila = []
                for c in range(5):
                    if (f == 0 or f == 1 or f == 2 or f == 3) and c == 4:
                        # Marcar la letra G
                        fila.append("X")
                    else:
                        fila.append(self.bingo[i][c][f])
                print(fila)

    def letraO(self):
        # Se genera un número aleatorio para marcar en el cuadrado
        num = random.randint(1, 75)
        print(f"Balota: {num}")

        # Marcar la letra O en cada cartón
        for i in range(self.numJugadores):
            print(f"\nCartón de {self.nombres[i]}:")
            for f in range(5):
                fila = []
                for c in range(5):
                    if (f == 0 or f == 1 or f == 2 or f == 3) and c == 5:
                        # Marcar la letra O
                        fila.append("X")
                    else:
                        fila.append(self.bingo[i][c][f])
                print(fila)
    
    def regresar(self):
        self.inicio()
        
    def salir(self):
        # se sale del programa
        print("Gracias por jugar")
        exit()

    def default(self):
        # si la opcion no esta en el diccionario, se ejecuta default
        print("Opcion invalida")
        self.inicio()
Bingo()
