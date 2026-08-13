1. Introducción

Esta aplicación permite gestionar un catálogo de libros de una biblioteca. Puedes registrar nuevos libros, buscarlos, rentarlos, devolverlos y ver recomendaciones según el autor o el género.

-2. Requisitos

Antes de usar la aplicación asegúrate de tener instalado:

- Python 3.8 o superior
- PyQt5

Si no tienes las dependencias, puedes instalarlas desde la carpeta del proyecto con:


pip install -r Requirements.txt


-3. Ejecutar la aplicación

Desde la carpeta principal del proyecto, usa el siguiente comando:


python main.py


Se abrirá la interfaz principal de la biblioteca.

-4. Registrar un libro

1. En el campo de texto principal, escribe los datos del libro en este formato:


codigo,titulo,autor,genero


Ejemplo:


B001,El principito,Antoine de Saint-Exupéry,Ficción


2. Haz clic en el botón de registrar.
3. Si la información es correcta, el libro quedará guardado en el catálogo.

-5. Buscar un libro

1. Ingresa el código del libro en el campo de búsqueda.
2. Haz clic en buscar.
3. La aplicación mostrará:
   - código
   - nombre
   - autor
   - género
   - estado del libro

-6. Rentar un libro

1. Escribe el código del libro en el campo de renta.
2. Haz clic en el botón de rentar.
3. El libro se moverá a la lista de libros rentados.

-7. Devolver un libro

1. Escribe el código del libro en el campo de devolución.
2. Haz clic en el botón de devolver.
3. El libro volverá a quedar disponible en el catálogo.

-8. Ver catálogo

La interfaz muestra el listado de libros registrados y su estado actual. También puedes consultar los libros rentados en la sección correspondiente.

-9. Recomendaciones

La aplicación puede mostrar recomendaciones según:

- autor
- género

Selecciona una opción en los menús disponibles para ver libros relacionados.

-10. Archivos de datos

La aplicación guarda la información en archivos de texto:

- `libros.txt`: libros disponibles o registrados en el catálogo
- `renta_libros.txt`: libros actualmente rentados

-11. Solución rápida de errores

La aplicación no abre
- Verifica que hayas instalado las dependencias.
- Revisa que estés ejecutando el programa desde la carpeta correcta.

No se guarda el libro
- Asegúrate de escribir los datos con el formato correcto: `codigo,titulo,autor,genero`.
- No dejes espacios extra o campos incompletos.

El libro no aparece al buscarlo
- Confirma que el código sea correcto.
- Verifica que el libro esté registrado en el archivo correspondiente.

-12. Resumen

Con esta aplicación puedes administrar una biblioteca de manera simple y práctica: registrar libros, buscar información, controlar préstamos, devolver materiales y obtener recomendaciones útiles para los usuarios.
