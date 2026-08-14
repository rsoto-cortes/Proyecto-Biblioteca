from Estructuras.lista_enlazada import LinkedList

LIBROS_FILE = 'libros.txt'
RENTAS_FILE = 'renta_libros.txt'

class Book:
    def __init__(self, codigo, titulo, autor, genero):
        self.codigo = codigo
        self.titulo = titulo
        self.autor = autor
        self.genero = genero

    def __str__(self):
        return self.codigo + ',' + self.titulo + ',' + self.autor + ',' + self.genero

    def display(self):
        return '[' + self.codigo + '] ' + self.titulo + ' - ' + self.autor + ' (' + self.genero + ')'


def _parse_linea(linea):
    partes = [p.strip() for p in linea.split(',')]
    if len(partes) >= 4:
        codigo = partes[0]
        titulo = partes[1]
        autor = partes[2]
        genero = partes[3]
        estado = partes[4] if len(partes) >= 5 else None
        return codigo, titulo, autor, genero, estado
    return None, None, None, None, None


def _leer_linea_por_codigo(codigo, filename):
    with open(filename, 'r', encoding='utf-8') as f:
        for linea in f:
            linea = linea.strip()
            if not linea:
                continue
            partes = [p.strip() for p in linea.split(',')]
            if partes and partes[0].upper() == codigo.upper():
                return linea
    return None


def _eliminar_linea_por_codigo(codigo, filename):
    lineas = []
    encontrado = False
    with open(filename, 'r', encoding='utf-8') as f:
        for linea in f:
            partes = [p.strip() for p in linea.strip().split(',')]
            if partes and partes[0].upper() == codigo.upper():
                encontrado = True
                continue
            lineas.append(linea)

    if encontrado:
        with open(filename, 'w', encoding='utf-8') as f:
            f.writelines(lineas)
    return encontrado


def _agregar_linea(linea, filename):
    with open(filename, 'a', encoding='utf-8') as f:
        f.write(linea + '\n')


class registro:
    @staticmethod
    def guardar_en_archivo(book, filename=LIBROS_FILE):
        with open(filename, 'a', encoding='utf-8') as f:
            f.write('\n' + str(book) + ',DISPONIBLE\n')

    @staticmethod
    def buscar_libro(codigo, filename=LIBROS_FILE):
        linea = _leer_linea_por_codigo(codigo, filename)
        return linea

    @staticmethod
    def eliminar_libro_por_codigo(codigo, filename=LIBROS_FILE):
        return _eliminar_linea_por_codigo(codigo, filename)

    @staticmethod
    def agregar_libro_en_archivo(linea, filename=LIBROS_FILE):
        _agregar_linea(linea, filename)

    @staticmethod
    def _linea_con_estado(linea, estado):
        codigo, titulo, autor, genero, _ = _parse_linea(linea)
        if not codigo:
            return None
        return f"{codigo},{titulo},{autor},{genero},{estado}"

    @staticmethod
    def mover_libro_entre_archivos(codigo, origen=LIBROS_FILE, destino=RENTAS_FILE):
        linea = _leer_linea_por_codigo(codigo, origen)
        if not linea:
            return False
        codigo, titulo, autor, genero, _ = _parse_linea(linea)
        if not codigo:
            return False
        estado = 'RENTADO' if destino == RENTAS_FILE else 'DISPONIBLE'
        nueva_linea = f"{codigo},{titulo},{autor},{genero},{estado}"
        eliminado = _eliminar_linea_por_codigo(codigo, origen)
        if not eliminado:
            return False
        _agregar_linea(nueva_linea, destino)
        return True

    @staticmethod
    def registrar_libro(codigo, titulo, autor, genero):
        lista = LinkedList()
        libro = Book(codigo, titulo, autor, genero)
        lista.insert_at_end(libro)
        registro.guardar_en_archivo(libro)
        return libro

    @staticmethod
    def rentar_libro(codigo):
        return registro.mover_libro_entre_archivos(codigo, LIBROS_FILE, RENTAS_FILE)

    @staticmethod
    def devolver_libro(codigo):
        return registro.mover_libro_entre_archivos(codigo, RENTAS_FILE, LIBROS_FILE)


if __name__ == '__main__':
    print('Registro de libros simple')
    codigo = input('Código: ')
    titulo = input('Título: ')
    autor = input('Autor: ')
    genero = input('Género: ')
    libro = registro.registrar_libro(codigo, titulo, autor, genero)
    print('\nLibro registrado:')
    print(libro.display())
    print('\nGuardado')
