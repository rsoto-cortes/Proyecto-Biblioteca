# Sistema de Gestión de Biblioteca

Este proyecto es una aplicación de escritorio para gestionar un catálogo de libros, registrar préstamos y devoluciones, buscar libros por código y mostrar recomendaciones por autor o género. Está desarrollado en Python con la interfaz gráfica de PyQt5 y utiliza estructuras de datos personalizadas para organizar la información.

## Objetivo

El sistema permite:

- Registrar libros nuevos
- Buscar libros por código
- Mostrar el catálogo completo
- Rentar y devolver libros
- Consultar libros disponibles y prestados
- Obtener recomendaciones según autor o género
- Persistir los datos en archivos de texto

## Funcionalidades principales

### 1. Registro de libros
Se pueden ingresar datos como:
- Código
- Título
- Autor
- Género

Los libros se guardan en el archivo `libros.txt` con su estado actual.

### 2. Búsqueda de libros
El sistema permite buscar un libro por su código y mostrar información como:
- Título
- Autor
- Género
- Estado (disponible o rentado)

### 3. Préstamos y devoluciones
Los libros pueden ser movidos entre los archivos:
- `libros.txt` para libros disponibles
- `renta_libros.txt` para libros rentados

Esto permite llevar un control del estado de cada volumen.

### 4. Recomendaciones
El proyecto cuenta con un gestor de recomendaciones basado en un grafo:
- Conexiones entre libros con el mismo autor
- Conexiones entre libros del mismo género
- Visualización de recomendaciones por código, autor o género

### 5. Estructuras de datos
El proyecto integra distintas estructuras personalizadas:
- Lista enlazada
- Árbol binario de búsqueda
- Grafo

Estas estructuras permiten organizar, buscar y navegar la información del catálogo.

## Estructura del proyecto

```text
proyectoFinal/
├── main.py
├── README.md
├── Requirements.txt
├── libros.txt
├── renta_libros.txt
├── Estructuras/
│   ├── grafo.py
│   ├── lista_enlazada.py
│   └── nodo.py
├── Funciones_libreria/
│   ├── busqueda_libros.py
│   ├── gestor_recomendaciones.py
│   └── registro_libros.py
├── load/
│   └── load_proyecto.py
├── ui/
│   └── Biblioteca.ui
└── env/
    └── ...
```

## Archivos principales

### `main.py`
Archivo principal que inicia la aplicación.

### `load/load_proyecto.py`
Contiene la clase principal de la interfaz correspondiente a la biblioteca y conecta la lógica con la UI.

### `Funciones_libreria/registro_libros.py`
Encargado del registro, búsqueda, eliminación y movimiento entre archivos de libros.

### `Funciones_libreria/busqueda_libros.py`
Implementa la gestión del catálogo mediante un árbol binario de búsqueda.

### `Funciones_libreria/gestor_recomendaciones.py`
Controla la lógica de recomendaciones y el grafo de relaciones entre libros.

### `Estructuras/`
Carpeta con las estructuras de datos base del proyecto.

### `ui/Biblioteca.ui`
Diseño visual de la interfaz de usuario.

## Requisitos

- Python 3.8 o superior
- PyQt5

La dependencias del proyecto están listadas en `Requirements.txt`.

## Instalación

1. Clona o descarga el proyecto.
2. Ve al directorio raíz.
3. Crea un entorno virtual (opcional, pero recomendado):

```bash
python -m venv env
```

4. Activa el entorno virtual:

- En Windows:

```bash
env\Scripts\activate
```

- En Linux/macOS:

```bash
source env/bin/activate
```

5. Instala las dependencias:

```bash
pip install -r Requirements.txt
```

## Ejecución

Desde la raíz del proyecto, ejecuta:

```bash
python main.py
```

Esto abrirá la interfaz principal del sistema de biblioteca.

## Datos del proyecto

Los datos se guardan en archivos de texto:

- `libros.txt`: catálogo general de libros
- `renta_libros.txt`: libros actualmente rentados

El formato típico de cada registro es:

```text
codigo,titulo,autor,genero,estado
```

Ejemplo:

```text
B001,El Principito,Antoine de Saint-Exupéry,Ficción,DISPONIBLE
```

## Nota del proyecto

Este es un proyecto académico de estructura de datos y lógica de programación, por lo que combina una interfaz gráfica con implementaciones manuales de algoritmos y estructuras para simular una biblioteca digital.

## Autor

Proyecto desarrollado como trabajo de programación y estructuras de datos.
