class Nodo:
    def __init__(self, codigo, nombre, autor, genero):
        self.codigo = codigo
        self.nombre = nombre
        self.autor = autor
        self.genero = genero
        self.estado = "DISPONIBLE"
        self.izquierda = None
        self.derecha = None

class Arbol:
    def __init__(self):
        self.raiz = None

    def insertar(self, codigo, nombre, autor, genero):
        if self.buscar(codigo) is not None:
    
            return False
        
        nuevo = Nodo(codigo, nombre, autor, genero)
        
        if self.raiz is None:
            self.raiz = nuevo
        else:
            self._insertar(self.raiz, nuevo)
        
        return True

    def _insertar(self, actual, nuevo):
        if nuevo.codigo < actual.codigo:
            if actual.izquierda is None:
                actual.izquierda = nuevo
            else:
                self._insertar(actual.izquierda, nuevo)
        else:
            if actual.derecha is None:
                actual.derecha = nuevo
            else:
                self._insertar(actual.derecha, nuevo)

    def buscar(self, codigo):
        return self._buscar(self.raiz, codigo)

    def _buscar(self, actual, codigo):
        if actual is None:
            return None
        if codigo == actual.codigo:
            return actual
        if codigo < actual.codigo:
            return self._buscar(actual.izquierda, codigo)
        return self._buscar(actual.derecha, codigo)

    def actualizar(self, codigo, nombre=None, autor=None, genero=None):
        libro = self.buscar(codigo)
        if libro is None:
            print("Libro no encontrado")
            return False
        
        if nombre is not None:
            libro.nombre = nombre
        if autor is not None:
            libro.autor = autor
        if genero is not None:
            libro.genero = genero
        
        print("Libro actualizado")
        return True

    def rentar(self, codigo):
        libro = self.buscar(codigo)
        if libro is None:
            print("Libro no encontrado")
            return False
        if libro.estado == "RENTADO":
            print("Ya esta rentado")
            return False
        
        libro.estado = "RENTADO"
        print("Libro rentado")
        return True

    def devolver(self, codigo):
        libro = self.buscar(codigo)
        if libro is None:
            print("Libro no encontrado")
            return False
        if libro.estado == "DISPONIBLE":
            print("Ya esta disponible")
            return False
        
        libro.estado = "DISPONIBLE"
        print("Libro devuelto")
        return True

    def eliminar(self, codigo):
        if self.buscar(codigo) is None:
            print("Libro no encontrado")
            return False
        
        self.raiz = self._eliminar(self.raiz, codigo)
        print("Libro eliminado")
        return True

    def _eliminar(self, actual, codigo):
        if actual is None:
            return None
        
        if codigo < actual.codigo:
            actual.izquierda = self._eliminar(actual.izquierda, codigo)
        elif codigo > actual.codigo:
            actual.derecha = self._eliminar(actual.derecha, codigo)
        else:
            if actual.izquierda is None and actual.derecha is None:
                return None
            if actual.izquierda is None:
                return actual.derecha
            if actual.derecha is None:
                return actual.izquierda
            
            temp = self._minimo(actual.derecha)
            actual.codigo = temp.codigo
            actual.nombre = temp.nombre
            actual.autor = temp.autor
            actual.genero = temp.genero
            actual.estado = temp.estado
            actual.derecha = self._eliminar(actual.derecha, temp.codigo)
        
        return actual

    def _minimo(self, actual):
        while actual.izquierda is not None:
            actual = actual.izquierda
        return actual

    def mostrar(self):
        libros = []
        self._recorrer(self.raiz, libros)
        
        if not libros:
            print("No hay libros")
            return
        
        print("-" * 50)
        print("Catalogo de libros")
        print("-" * 50)
        for l in libros:
            print("Codigo:", l.codigo)
            print("Nombre:", l.nombre)
            print("Autor:", l.autor)
            print("Genero:", l.genero)
            print("Estado:", l.estado)
            print("-" * 50)
        print("Total:", len(libros))

    def _recorrer(self, actual, libros):
        if actual is not None:
            self._recorrer(actual.izquierda, libros)
            libros.append(actual)
            self._recorrer(actual.derecha, libros)

    def guardar(self, archivo="libros.txt"):
        libros = []
        self._recorrer(self.raiz, libros)
        
        with open(archivo, 'w', encoding='utf-8') as f:
            for l in libros:
                f.write(l.codigo + "," + l.nombre + "," + l.autor + "," + l.genero + "," + l.estado + "\n")
        
        print("Datos guardados en", archivo)

    def cargar(self, archivo="libros.txt"):
        try:
            with open(archivo, 'r', encoding='utf-8') as f:
                for linea in f:
                    datos = linea.strip().split(',')
                    if len(datos) == 4:
                        codigo, nombre, autor, genero = datos
                        self.insertar(codigo, nombre, autor, genero)
                    elif len(datos) == 5:
                        codigo, nombre, autor, genero, estado = datos
                        self.insertar(codigo, nombre, autor, genero)
                        libro = self.buscar(codigo)
                        if libro is not None:
                            libro.estado = estado
            
        except FileNotFoundError:
            print("No hay datos guardados")
            return False