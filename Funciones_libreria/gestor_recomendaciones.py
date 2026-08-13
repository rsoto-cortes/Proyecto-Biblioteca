from Estructuras.grafo import Grafo


class GestorRecomendaciones:

    def __init__(self):
        # Grafo del proyecto
        self.grafo = Grafo()

        # Lista donde se almacenan los libros
        self.libros = []

    def cargar_libros(self, archivo="libros.txt"):
        self.libros.clear()

        try:
            with open(archivo, "r", encoding="utf-8") as f:
                for linea in f:
                    linea = linea.strip()

                    if linea == "":
                        continue

                    datos = linea.split(",")

                    if len(datos) < 4:
                        continue

                    libro = {
                        "codigo": datos[0].strip(),
                        "nombre": datos[1].strip(),
                        "autor": datos[2].strip(),
                        "genero": datos[3].strip(),
                        "estado": datos[4].strip() if len(datos) >= 5 else "DISPONIBLE"
                    }

                    self.libros.append(libro)

        except FileNotFoundError:
            print("No existe el archivo libros.txt")

    def mostrar_libros(self):
        if len(self.libros) == 0:
            print("\nNo existen libros registrados.\n")
            return

        print("\nCATALOGO DE LIBROS\n")

        for libro in self.libros:
            print("----------------------------")
            print("Codigo :", libro["codigo"])
            print("Nombre :", libro["nombre"])
            print("Autor  :", libro["autor"])
            print("Genero :", libro["genero"])
            print("Estado :", libro["estado"])

        print("----------------------------")

    def buscar_codigo(self, codigo):
        codigo = codigo.upper()

        for libro in self.libros:
            if libro["codigo"] == codigo:
                return libro

        return None

    def buscar_autor(self, autor):
        encontrados = []

        for libro in self.libros:
            if libro["autor"].lower() == autor.lower():
                encontrados.append(libro)

        return encontrados

    def buscar_genero(self, genero):
        encontrados = []

        for libro in self.libros:
            if libro["genero"].lower() == genero.lower():
                encontrados.append(libro)

        return encontrados

    def obtener_autores(self):
        autores = []

        for libro in self.libros:
            if libro["autor"] not in autores:
                autores.append(libro["autor"])

        autores.sort()
        return autores

    def obtener_generos(self):
        generos = []

        for libro in self.libros:
            if libro["genero"] not in generos:
                generos.append(libro["genero"])

        generos.sort()
        return generos

    def mostrar_autores(self):
        print("\nAUTORES\n")

        for autor in self.obtener_autores():
            print(autor)

    def mostrar_generos(self):
        print("\nGENEROS\n")

        for genero in self.obtener_generos():
            print(genero)

    def construir_grafo(self):
        # Elimina todo el contenido anterior
        self.grafo.clear()

        # Agregar todos los libros como vértices
        for libro in self.libros:
            self.grafo.add_vertex(libro["codigo"])

        # Crear conexiones entre libros
        for i in range(len(self.libros)):
            for j in range(i + 1, len(self.libros)):
                libro1 = self.libros[i]
                libro2 = self.libros[j]

                # Si tienen el mismo autor
                if libro1["autor"] == libro2["autor"]:
                    self.grafo.add_edge(
                        libro1["codigo"],
                        libro2["codigo"]
                    )

                # Si tienen el mismo género
                elif libro1["genero"] == libro2["genero"]:
                    self.grafo.add_edge(
                        libro1["codigo"],
                        libro2["codigo"]
                    )

    def mostrar_lista_adyacencia(self):
        print("\nLISTA DE ADYACENCIA\n")

        lista = self.grafo.get_adjacency_list()

        for vertice in lista:
            print(f"{vertice} -> {lista[vertice]}")

    def mostrar_matriz(self):
        vertices, matriz = self.grafo.get_adjacency_matrix()

        print("\nMATRIZ DE ADYACENCIA\n")

        print("     ", end="")

        for vertice in vertices:
            print(f"{vertice:8}", end="")

        print()

        for i in range(len(vertices)):
            print(f"{vertices[i]:5}", end="")

            for valor in matriz[i]:
                print(f"{valor:^8}", end="")

            print()

    def mostrar_aristas(self):
        print("\nARISTAS DEL GRAFO\n")

        aristas = self.grafo.get_edges()

        for arista in aristas:
            print(arista[0], "<---->", arista[1])

    def vecinos(self, codigo):
        codigo = codigo.upper()

        if not self.grafo.contains_vertex(codigo):
            print("Ese libro no existe.")
            return

        vecinos = self.grafo.get_adjacent_vertices(codigo)

        print()
        print("Libros relacionados con", codigo)
        print(vecinos)

    def total_libros(self):
        return self.grafo.vertex_count()

    def total_relaciones(self):
        return self.grafo.edge_count()

    def recomendar_por_codigo(self, codigo):
        codigo = codigo.upper()

        if not self.grafo.contains_vertex(codigo):
            print("\nEse libro no existe.")
            return

        vecinos = self.grafo.get_adjacent_vertices(codigo)

        if len(vecinos) == 0:
            print("\nNo existen recomendaciones para ese libro.")
            return

        libro = self.buscar_codigo(codigo)

        print("\n===================================")
        print("LIBRO SELECCIONADO")
        print("===================================")
        print("Codigo :", libro["codigo"])
        print("Nombre :", libro["nombre"])
        print("Autor  :", libro["autor"])
        print("Genero :", libro["genero"])

        print("\nLIBROS RECOMENDADOS\n")

        for vecino in vecinos:
            recomendado = self.buscar_codigo(vecino)
            print("------------------------------")
            print("Codigo :", recomendado["codigo"])
            print("Nombre :", recomendado["nombre"])
            print("Autor  :", recomendado["autor"])
            print("Genero :", recomendado["genero"])

    def recomendar_por_autor(self, autor):
        encontrados = self.buscar_autor(autor)

        if len(encontrados) == 0:
            print("\nNo existen libros de ese autor.")
            return

        print("\nLIBROS DEL AUTOR\n")

        for libro in encontrados:
            print(libro["codigo"], "-", libro["nombre"])

    def recomendar_por_genero(self, genero):
        encontrados = self.buscar_genero(genero)

        if len(encontrados) == 0:
            print("\nNo existen libros de ese genero.")
            return

        print("\nLIBROS DEL GENERO\n")

        for libro in encontrados:
            print(libro["codigo"], "-", libro["nombre"])

    def informacion_libro(self, codigo):
        libro = self.buscar_codigo(codigo)

        if libro is None:
            print("Libro no encontrado.")
            return

        print("\nINFORMACION DEL LIBRO\n")
        print("Codigo :", libro["codigo"])
        print("Nombre :", libro["nombre"])
        print("Autor  :", libro["autor"])
        print("Genero :", libro["genero"])
        print("Estado :", libro["estado"])

    def relacionados(self, codigo1, codigo2):
        if self.grafo.contains_edge(codigo1, codigo2):
            print("\nLos libros SI estan relacionados.")
        else:
            print("\nLos libros NO estan relacionados.")

    def mostrar_todas_recomendaciones(self):
        print("\n=========== RECOMENDACIONES ==========")

        for libro in self.libros:
            vecinos = self.grafo.get_adjacent_vertices(libro["codigo"])

            print(libro["codigo"], "-", libro["nombre"])

            if len(vecinos) == 0:
                print("   Sin recomendaciones.")
            else:
                for vecino in vecinos:
                    recomendado = self.buscar_codigo(vecino)
                    print("   ->", recomendado["nombre"])

            print()