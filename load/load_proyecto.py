from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic
from Funciones_libreria.registro_libros import registro
from Funciones_libreria.gestor_recomendaciones import GestorRecomendaciones
from Funciones_libreria.busqueda_libros import Arbol


class Biblioteca(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/Biblioteca.ui", self)

        self.gestor = GestorRecomendaciones()
        self.catalogo = Arbol()

        self.btn_registrar.clicked.connect(self.registrar_libro)
        self.btn_actualizar.clicked.connect(self.actualizar_catalogo)
        self.btn_rentar.clicked.connect(self.rentar_libro)
        self.btn_devolucion.clicked.connect(self.devolver_libro)
        self.btn_buscar.clicked.connect(self.buscar_libro)
        self.com_autores.currentIndexChanged.connect(self.recomendar_por_autor)
        self.com_genero.currentIndexChanged.connect(self.recomendar_por_genero)
        self.lista_rentados.setReadOnly(True)
        self.lista_catalogo.setReadOnly(True)
        self.recom.setReadOnly(True)
        self.resultado_bus.setReadOnly(True)

        self.cargar_datos()

    def cargar_datos(self):
        self.gestor.cargar_libros()
        self.catalogo.cargar()
        self.gestor.construir_grafo()
        self.llenar_combos()
        self.actualizar_catalogo()
        self.cargar_rentados()

    def cargar_rentados(self):
        try:
            with open('renta_libros.txt', 'r', encoding='utf-8') as f:
                lineas = [line.strip() for line in f if line.strip()]
        except FileNotFoundError:
            lineas = []

        if not lineas:
            self.lista_rentados.setPlainText('No hay libros rentados.')
            return

        self.lista_rentados.setPlainText('\n'.join(lineas))

    def llenar_combos(self):
        self.com_autores.blockSignals(True)
        self.com_genero.blockSignals(True)

        self.com_autores.clear()
        self.com_genero.clear()

        self.com_autores.addItem("Seleccione un autor")
        self.com_genero.addItem("Seleccione un género")

        for autor in self.gestor.obtener_autores():
            self.com_autores.addItem(autor)

        for genero in self.gestor.obtener_generos():
            self.com_genero.addItem(genero)

        self.com_autores.blockSignals(False)
        self.com_genero.blockSignals(False)

    def actualizar_catalogo(self):
        if len(self.gestor.libros) == 0:
            self.lista_catalogo.setPlainText('No hay libros registrados.')
            return

        lineas = []
        for libro in self.gestor.libros:
            estado = libro.get('estado', 'DISPONIBLE')
            lineas.append(f"{libro['codigo']}, {libro['nombre']}, {libro['autor']}, {libro['genero']}, {estado}")

        self.lista_catalogo.setPlainText('\n'.join(lineas))

    def registrar_libro(self):
        texto = self.ent_libro.text().strip()
        if texto == '':
            self.lbl_mensaje.setText('Ingrese los datos del libro separados por coma')
            return

        partes = [parte.strip() for parte in texto.split(',')]
        if len(partes) != 4:
            self.lbl_mensaje.setText('Formato incorrecto. Use: codigo,titulo,autor,genero')
            return

        codigo, titulo, autor, genero = partes
        try:
            registro.registrar_libro(codigo, titulo, autor, genero)
            self.lbl_mensaje.setText('Libro registrado correctamente.')
            self.ent_libro.clear()
            self.cargar_datos()
        except Exception as e:
            self.lbl_mensaje.setText('Error al guardar el libro: ' + str(e))

    def buscar_libro(self):
        codigo = self.ent_bus_cod.text().strip().upper()
        if codigo == '':
            self.resultado_bus.setPlainText('Ingrese un código para buscar.')
            return

        libro = self.gestor.buscar_codigo(codigo)
        if libro is None:
            linea = registro.buscar_libro(codigo, 'renta_libros.txt')
            if linea:
                partes = [parte.strip() for parte in linea.split(',')]
                if len(partes) >= 4:
                    estado = partes[4] if len(partes) >= 5 else 'RENTADO'
                    libro = {
                        'codigo': partes[0],
                        'nombre': partes[1],
                        'autor': partes[2],
                        'genero': partes[3],
                        'estado': estado
                    }

        if libro is None:
            self.resultado_bus.setPlainText('Libro no encontrado.')
            return

        self.resultado_bus.setPlainText(
            f"Código: {libro['codigo']}\n" \
            f"Nombre: {libro['nombre']}\n" \
            f"Autor: {libro['autor']}\n" \
            f"Género: {libro['genero']}\n" \
            f"Estado: {libro.get('estado', 'DISPONIBLE')}"
        )

    def rentar_libro(self):
        codigo = self.ent_renta.text().strip().upper()
        if codigo == '':
            self.lbl_mensaje_3.setText('Ingrese el código del libro a rentar.')
            return

        if registro.rentar_libro(codigo):
            self.lbl_mensaje_3.setText('Libro rentado correctamente.')
            self.cargar_datos()
        else:
            self.lbl_mensaje_3.setText('No se pudo rentar el libro.')

    def devolver_libro(self):
        codigo = self.ent_devol.text().strip().upper()
        if codigo == '':
            self.lbl_mensaje_2.setText('Ingrese el código del libro a devolver.')
            return

        if registro.devolver_libro(codigo):
            self.lbl_mensaje_2.setText('Libro devuelto correctamente.')
            self.cargar_datos()
        else:
            self.lbl_mensaje_2.setText('No se pudo devolver el libro.')

    
    def recomendar_por_autor(self):
        autor = self.com_autores.currentText()
        if autor == 'Seleccione un autor':
            self.recom.setPlainText('')
            return

        encontrados = self.gestor.buscar_autor(autor)
        if len(encontrados) == 0:
            self.recom.setPlainText('No hay libros para ese autor.')
            return

        texto = [f"{libro['codigo']}: {libro['nombre']}" for libro in encontrados]
        self.recom.setPlainText('Libros del autor:\n' + '\n'.join(texto))

    def recomendar_por_genero(self):
        genero = self.com_genero.currentText()
        if genero == 'Seleccione un género':
            self.recom.setPlainText('')
            return

        encontrados = self.gestor.buscar_genero(genero)
        if len(encontrados) == 0:
            self.recom.setPlainText('No hay libros para ese género.')
            return

        texto = [f"{libro['codigo']}: {libro['nombre']}" for libro in encontrados]
        self.recom.setPlainText('Libros del género:\n' + '\n'.join(texto))
        
        