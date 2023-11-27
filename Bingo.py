import random

class Bingo:
    def __init__(self):
        self.inicio()
        self.verificarBingo()


    def inicio(self): # Menu principal
        while True:
            print("1. Configurar juego. \n"
                  "2. Jugar. \n"
                  "0. Salir. \n")
            opcion = input("Digite opcion: ")
            if opcion == "1":
                self.configurador()
            elif opcion == "2":
                self.jugar()
            elif opcion == "0":
                self.salir()
            else:
                print("Opcion invalida")


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
            carton = [] # lista del carton para el jugador actual
            for f in range(5): # se generan los numeros de cada carton
                fila = random.sample(range(f * 15 + 1, (f + 1) * 15 + 1), 5) # se generan los numeros de cada fila
                if f == 2: 
                    fila[2] = " * "
                carton.append(fila) # se agregan los numeros al carton del jugador actual
            self.bingo.append(carton) # se agrega el carton a la lista de cartones
            self.mostrarCartones(i) # se llama a la funcion mostrarCartones

    def mostrarCartones(self, i): 
        print(f"\nCartón de {self.nombres[i]}:")
        print(" B   I   N   G   O ")
        for f in range(5): 
            for c in range(5): 
                print(f"{self.bingo[i][c][f]:2}", end="  ") # se imprimen los numeros de cada carton
            print(" ", end="\n") # se imprime un espacio para separar cada fila
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
            self.verificarBingo(forma, self.default) # se llama a la funcion verificarBingo
            
    def verificarBingo(self): # Verificar si alguien hizo Bingo en alguna forma
        self.verificarTodo()
        self.verificarCuadrado()
        self.verificarLetraL()
        self.verificarLetraB()
        self.verificarLetraI()
        self.verificarLetraN()
        self.verificarLetraG()
        self.verificarLetraO()

    def marcarNumero(self, num):
        for i in range(self.numJugadores): 
            for f in range(5): 
                for c in range(5): 
                    if self.bingo[i][f][c] == num: 
                        self.bingo[i][f][c] = "\033[91m\033[4m{}\033[0m".format(num)  # Change the number to a colored string

    def todo(self):
        
        letra = random.choice("BINGO") # se genera una letra aleatoria
    
        if (letra=="B"):
            num=random.randint(1,15)
        elif(letra=="I"):
            num=random.randint(16,30)
        elif(letra=="N"):
            num=random.randint(31,45)
        elif(letra=="G"):
            num=random.randint(46,60)
        elif(letra=="O"):
            num=random.randint(61,75)

        print(f"Balota: {letra}-{num}")
        self.marcarNumero(num) # se llama a la funcion marcarNumero
        
        for i in range(self.numJugadores): # se recorre la lista de cartones
            for f in range(5): 
                fila=[]
                for c in range(5): 
                    if(self.bingo[i][f][c]==num): 
                        fila.append("X")
                    else:
                        fila.append(self.bingo[i][f][c])
                self.bingo[i][f] = fila
            self.mostrarCartones(i)

    def verificarTodo(self): # Verificar si alguien hizo Bingo en esta forma
        for i in range(self.numJugadores): 
            for f in range(5):
                # Si todos los números están marcados (marcarNumero) en el cartón se hace bingo
                if all(isinstance(self.bingo[i][f][c], str) and self.bingo[i][f][c].startswith("\033[91m\033[4m") for c in range(5)):
                    print(f"Bingo de {self.nombres[i]}")
                    self.inicio()
                
    def cuadrado(self):
        
        # Se genera un número aleatorio para marcar en el cuadrado
        num = random.randint(1, 75)
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
        self.marcarNumero(num) # se llama a la funcion marcarNumero

        # Marcar el cuadrado en cada cartón
        for i in range(self.numJugadores): 
            for f in range(5): 
                fila = [] 
                for c in range(5): 
                    if self.bingo[i][f][c] == num: 
                        fila.append("X")
                    elif (f == 1 or f == 3) and (c == 1 or c == 3) and self.bingo[i][f][c] == num: # Marcar el cuadrado
                        fila.append("X") 
                    else:
                        fila.append(self.bingo[i][f][c])
                self.bingo[i][f] = fila
            self.mostrarCartones(i)

        # Verificar si alguien hizo Bingo en esta forma
        self.verificarBingo()
    
    def verificarCuadrado(self):
        for i in range(self.numJugadores):
            cuadrado = [self.bingo[i][f][c] for f in [0, 4] for c in range(5)] + [self.bingo[i][f][c] for f in range(1, 4) for c in [0, 4]]  # Get the outer square
            if all(isinstance(x, str) and x.startswith("\033[91m\033[4m") for x in cuadrado):  # Si todos los elementos son números subrayados y con color
                print(f"Bingo de {self.nombres[i]} en el cuadrado")
                self.inicio()  # Retorna al menu principal

    def letraL(self):

        # Se genera un número aleatorio para marcar en el cuadrado
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
        self.marcarNumero(num) # se llama a la funcion marcarNumero



        for i in range(self.numJugadores):
            for f in range(5):
                fila = []
                for c in range(5):
                    if (f == 0 or f == 1 or f == 2 or f == 3) and c == 0:  # Marcar la letra L
                        if self.bingo[i][f][c] == num:
                            fila.append("X")
                        else:
                            fila.append(self.bingo[i][f][c])
                    elif f == 4:  # Marcar la base de la L
                        if self.bingo[i][f][c] == num:
                            fila.append("X")
                        else:
                            fila.append(self.bingo[i][f][c])
                    else:
                        fila.append(self.bingo[i][f][c])
                self.bingo[i][f] = fila
            self.mostrarCartones(i)  
        
        # Verificar si alguien hizo Bingo en esta forma
        self.verificarBingo()

    def verificarLetraL(self):
        for i in range(self.numJugadores):
            letraL = [self.bingo[i][f][0] for f in range(5)] + self.bingo[i][4]  # Tomar la columna B y la fila inferior
            if all(isinstance(x, str) and x.startswith("\033[91m\033[4m") for x in letraL):  # Si todos los elementos son números subrayados y con color
                print(f"Bingo de {self.nombres[i]} en la letra L")
                self.inicio()  # Retorna al menu principal

    def letraB(self):
        # Se genera un número aleatorio para marcar en la cuadrado
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

        print(f"Balota: {letra}-{num}")
        self.marcarNumero(num) # se llama a la funcion marcarNumero

        # Marcar la letra B en cada cartón
        for i in range(self.numJugadores):
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
            self.mostrarCartones(i)

        # Verificar si alguien hizo Bingo en esta forma
        self.verificarBingo()

    def verificarLetraB(self):
        for i in range(self.numJugadores):
            columnaB = [self.bingo[i][f][0] for f in range(5)]  # Tomar la columna B
            if all(isinstance(x, str) and x.startswith("\033[91m\033[4m") for x in columnaB):  # Si todos los elementos son números subrayados y con color
                print(f"Bingo de {self.nombres[i]} en la letra B")
                self.inicio()  # Retorna al menu principal

    def letraI(self): 
        # Se genera un número aleatorio para marcar en la cuadrado
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

        print(f"Balota: {letra}-{num}")
        self.marcarNumero(num) # se llama a la funcion marcarNumero

        # Marcar la letra I en cada cartón
        for i in range(self.numJugadores):
            for f in range(5):
                fila = []
                for c in range(5):
                    if c == 2 or f == 0 or f == 4:  # Marcar la letra I
                        if self.bingo[i][f][c] == num:
                            # en vez de X, el numero cambia de color
                            fila.append("X")
                        else:
                            fila.append(self.bingo[i][f][c])
                    else:
                        fila.append(self.bingo[i][f][c])
                self.bingo[i][f] = fila
            self.mostrarCartones(i)

        # Verificar si alguien hizo Bingo en esta forma
        self.verificarBingo()
    
    def verificarLetraI(self):
        for i in range(self.numJugadores):
            if all(isinstance(self.bingo[i][f][2], str) and self.bingo[i][f][2].startswith("\033[91m\033[4m") for f in range(5)):  # Si todos los elementos de la columna del medio son números subrayados y con color
                print(f"Bingo de {self.nombres[i]}")
                self.inicio() 

    def letraN(self):
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

        print(f"Balota: {letra}-{num}")
        self.marcarNumero(num) # se llama a la funcion marcarNumero

        # Marcar la letra N en cada cartón
        for i in range(self.numJugadores):
            for f in range(5):
                fila = []
                for c in range(5):
                    if c == 2: # Marcar la letra N
                        if f == 2: # Marcar la diagonal de la letra N
                            fila.append(" * ")
                        elif self.bingo[i][f][c] == num:
                            fila.append("X")
                        else:
                            fila.append(self.bingo[i][f][c])
                    else:
                        fila.append(self.bingo[i][f][c])
                self.bingo[i][f] = fila
            self.mostrarCartones(i)

        # Verificar si alguien hizo Bingo en esta forma
        self.verificarBingo()
    
    def verificarLetraN(self):
        for i in range(self.numJugadores):
            letraN = [self.bingo[i][f][2] for f in [0, 1, 3, 4]]  # Tomar la columna I
            if all(isinstance(x, str) and x.startswith("\033[91m\033[4m") for x in letraN):  # Si todos los elementos son números subrayados y con color
                print(f"Bingo de {self.nombres[i]} en la letra N")
                self.inicio()  # Retorna al menu principal

    def letraG(self):
        # Se genera un número aleatorio para marcar en la cuadrado
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

        print(f"Balota: {letra}-{num}")
        self.marcarNumero(num) # se llama a la funcion marcarNumero

        # Marcar la letra G en cada cartón
        for i in range(self.numJugadores):
            for f in range(5):
                fila = []
                for c in range(5):
                    if (f == 0 or f == 1 or f == 2 or f == 3) and c == 4:
                        # Marcar la letra G
                        fila.append("X")
                    else:
                        fila.append(self.bingo[i][f][c])
                self.bingo[i][f] = fila
            self.mostrarCartones(i)

        # Verificar si alguien hizo Bingo en esta forma
        self.verificarBingo()

    def verificarLetraG(self):
        for i in range(self.numJugadores):
            if all(isinstance(self.bingo[i][f][4], str) and self.bingo[i][f][4].startswith("\033[91m\033[4m") for f in range(5)):  # Si todos los elementos de la columna G son números subrayados y con color
                print(f"Bingo de {self.nombres[i]}")
                self.inicio()  # Retorna al menu principal

    def letraO(self):
        # Se genera un número aleatorio para marcar en la cuadrado
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

        print(f"Balota: {letra}-{num}")
        self.marcarNumero(num) # se llama a la funcion marcarNumero

        for i in range(self.numJugadores):
            for f in range(5):
                fila = []
                for c in range(5): 
                    if (f == 0 or f == 4) and (c == 0 or c == 4): # Marcar la letra O
                        if self.bingo[i][f][c] == num:
                            fila.append("X")
                        else:
                            fila.append(self.bingo[i][f][c])
                    else:
                        fila.append(self.bingo[i][f][c])
                self.bingo[i][f] = fila
            self.mostrarCartones(i)

        # Verificar si alguien hizo Bingo en esta forma
        self.verificarBingo()

    def verificarLetraO(self):
        for i in range(self.numJugadores):
            letraO = [self.bingo[i][f][c] for f in [0, 4] for c in range(5)] + [self.bingo[i][f][c] for f in range(1, 4) for c in [0, 4]]  # Get the "O" pattern
            if all(isinstance(x, str) and x.startswith("\033[91m\033[4m") for x in letraO):  # Si todos los elementos son números subrayados y con color
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
