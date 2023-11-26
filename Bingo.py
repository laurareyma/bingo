import random

class Bingo:
    def __init__(self):
        self.inicio()
        self.verificarBingo()

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
        self.numJugadores=(int(input("Digite numero de jugadores: ")))
        self.nombres=[] # lista de nombres de jugadores
        self.bingo = [] # lista de cartones
        for i in range(self.numJugadores): # se pide el nombre de cada jugador
            nombre=(input(f"Ingrese el nombre del jugador {i+1}: ")) 
            self.nombres.append(nombre) 
        self.cartones() # se llama a la funcion cartones

    def cartones(self): # Generador de cartones
        for i in range(self.numJugadores): # se generan los cartones de cada jugador
            print(" "+self.nombres[i]) # se imprime el nombre del jugador
            print(" B   I   N   G   O ") # se imprime el titulo del carton
            carton = [] # lista del carton para el jugador actual
            for f in range(5): # se generan los numeros de cada carton
                fila = random.sample(range(f * 15 + 1, (f + 1) * 15 + 1), 5) # se generan los numeros de cada fila
                carton.append(fila) # se agregan los numeros al carton del jugador actual
            self.bingo.append(carton) # se agrega el carton a la lista de cartones
            self.mostrarCartones(i) # se llama a la funcion mostrarCartones

    def mostrarCartones(self, i): 
        for f in range(5): 
            for c in range(5): 
                print(f"{self.bingo[i][c][f]:2}", end="  ") # se imprimen los numeros de cada carton
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


        
        for i in range(self.numJugadores):
            for f in range(5):
                fila=[]
                for c in range(5):
                    if(self.bingo[i][f][c]==num):
                        fila.append("X")
                    else:
                        fila.append(self.bingo[i][f][c])
                self.bingo[i][f] = fila
                print(fila)

    def verificarTodo(self):
        for i in range(self.numJugadores):
            for f in range(5):
                if all(x == "X" for x in self.bingo[i][f]): # si todos los elementos de la fila son X
                    print(f"Bingo de {self.nombres[i]}")
                    self.inicio() # se vuelve al menu principal
    
    def verificarBingo(self):
        self.verificarTodo()
        self.verificarCuadrado()
        self.verificarLetraL()
        self.verificarLetraB()
        self.verificarLetraI()
        self.verificarLetraN()
        self.verificarLetraG()
        self.verificarLetraO()

        # Verificar si alguien hizo Bingo en esta forma
        for i in range(self.numJugadores):
            for f in range(5):
                fila = []
                for c in range(5):
                    if (f == 1 or f == 3) and (c == 1 or c == 3): # si es una posición del cuadrado
                        # Marcar el cuadrado pero en vez de X, el numero cambia de color 
                        fila.append(self.bingo[i][f][c])
                    if all(x == "X" for x in fila): # si todos los elementos de la fila son X
                        print(f"Bingo de {self.nombres[i]}")
                        self.inicio() # se vuelve al menu principal
        
                        
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
                    if self.bingo[i][f][c] == num: 
                        fila.append("X")
                    elif (f == 1 or f == 3) and (c == 1 or c == 3): # si es una posición del cuadrado
                        # Marcar el cuadrado
                        fila.append("X") 
                    else:
                        fila.append(self.bingo[i][f][c])
            self.bingo[i][f] = fila

        # Verificar si alguien hizo Bingo en esta forma
        self.verificarBingo()

    def verificarCuadrado(self):
        for i in range(self.numJugadores):
            cuadrado = [self.bingo[i][f][c] for f in [0, 4] for c in range(5)] + [self.bingo[i][f][c] for f in range(1, 4) for c in [0, 4]]  # Get the outer square
            if all(x == "X" for x in cuadrado):  # If all elements are "X"
                print(f"Bingo de {self.nombres[i]} en el cuadrado")
                self.inicio()  # Return to the main menu

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
                    if (f == 0 or f == 1 or f == 2 or f == 3) and c == 0: # Marcar la letra L
                        if self.bingo[i][f][c] == num:
                            fila.append("X")
                        else:
                            fila.append(self.bingo[i][f][c])
                    elif f == 4: # Marcar la base de la L
                        if self.bingo[i][f][c] == num:
                            fila.append("X")
                        else:
                            fila.append(self.bingo[i][f][c])
                    else:
                        fila.append(self.bingo[i][f][c])
                self.bingo[i][f] = fila
                print(fila)
        
        # Verificar si alguien hizo Bingo en esta forma
        self.verificarBingo()

    def verificarLetraL(self):
        for i in range(self.numJugadores):
            letraL = [self.bingo[i][f][0] for f in range(5)] + self.bingo[i][4]  # Get the "L" pattern
            if all(x == "X" for x in letraL):  # If all elements are "X"
                print(f"Bingo de {self.nombres[i]} en la letra L")
                self.inicio()  # Return to the main menu

    def letraB(self):
        # Se genera un número aleatorio para marcar en la cuadrado
        num = random.randint(1, 15)
        print(f"Balota: {num}")

        # Marcar la letra B en cada cartón
        for i in range(self.numJugadores):
            print(f"\nCartón de {self.nombres[i]}:")
            for f in range(5):
                fila = []
                for c in range(5):
                    if c == 0: # Marcar la letra B
                        if self.bingo[i][f][c] == num:
                            fila.append("X")
                        else:
                            fila.append(self.bingo[i][f][c])
                    else:
                        fila.append(self.bingo[i][f][c])
                self.bingo[i][f] = fila
                print(fila)

        # Verificar si alguien hizo Bingo en esta forma
        self.verificarBingo()

    def verificarLetraB(self):
        for i in range(self.numJugadores):
            columnaB = [self.bingo[i][f][0] for f in range(5)]  # Get the first column
            if all(x == "X" for x in columnaB):  # If all elements are "X"
                print(f"Bingo de {self.nombres[i]} en la letra B")
                self.inicio()  # Return to the main menu

    

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
                    if c == 2 or f == 0 or f == 4:  # Marcar la letra I
                        if self.bingo[i][f][c] == num:
                            fila.append("X")
                        else:
                            fila.append(self.bingo[i][f][c])
                    else:
                        fila.append(self.bingo[i][f][c])
                self.bingo[i][f] = fila
                print(fila)

        # Verificar si alguien hizo Bingo en esta forma
        self.verificarBingo()
    
    def verificarLetraI(self):
        for i in range(self.numJugadores):
            if all(self.bingo[i][f][2] == "X" for f in range(5)): # if all elements in the middle column are X
                print(f"Bingo de {self.nombres[i]}")
                self.inicio() 

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
                    if c == 2: # Marcar la letra N
                        if f == 2: # Marcar la diagonal de la letra N
                            fila.append(" ")
                        elif self.bingo[i][f][c] == num:
                            fila.append("X")
                        else:
                            fila.append(self.bingo[i][f][c])
                    else:
                        fila.append(self.bingo[i][f][c])
                self.bingo[i][f] = fila
                print(fila)

        # Verificar si alguien hizo Bingo en esta forma
        self.verificarBingo()
    
    def verificarLetraN(self):
        for i in range(self.numJugadores):
            letraN = [self.bingo[i][f][2] for f in [0, 1, 3, 4]]  # Get the "N" pattern
            if all(x == "X" for x in letraN):  # If all elements are "X"
                print(f"Bingo de {self.nombres[i]} en la letra N")
                self.inicio()  # Return to the main menu

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
                        fila.append(self.bingo[i][f][c])
                print(fila)

        # Verificar si alguien hizo Bingo en esta forma
        self.verificarBingo()

    def verificarLetraG(self):
        for i in range(self.numJugadores):
            if all(self.bingo[i][f][4] == "X" for f in range(5)): # if all elements in the rightmost column are "X"
                print(f"Bingo de {self.nombres[i]}")
                self.inicio() # return to the main menu

    def letraO(self):
        num = random.randint(1, 75)
        print(f"Balota: {num}")

        for i in range(self.numJugadores):
            print(f"\nCartón de {self.nombres[i]}:")
            for f in range(5):
                fila = []
                for c in range(5):
                    if (f == 0 or f == 4) and (c == 0 or c == 4):
                        if self.bingo[i][f][c] == num:
                            fila.append("X")
                        else:
                            fila.append(self.bingo[i][f][c])
                    else:
                        fila.append(self.bingo[i][f][c])
                self.bingo[i][f] = fila
                print(fila)

        # Verificar si alguien hizo Bingo en esta forma
        self.verificarBingo()
    
    def verificarLetraO(self):
        for i in range(self.numJugadores):
            letraO = [self.bingo[i][f][c] for f in [0, 4] for c in range(5)] + [self.bingo[i][f][c] for f in range(1, 4) for c in [0, 4]]  # Get the "O" pattern
            if all(x == "X" for x in letraO):  # Si todos los elementos son "X"
                print(f"Bingo de {self.nombres[i]} en la letra O")
                self.inicio()  # Retorna al menu principal
    
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
