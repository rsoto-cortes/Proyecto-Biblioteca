from Estructuras.nodo import Node

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_beginning(self, data):
        new_node = Node(data)

        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)

        if self.head:
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.head = new_node
            self.tail = new_node

   

    def search(self, data):
        current_node = self.head
        while current_node is not None:
            if current_node.data == data:
                return True
            current_node = current_node.next
        return False

    def print_list(self):
        temp = self.head
        print("Head -> ", end="")
        while temp is not None:
            data = temp.data
            if isinstance(data):
                print(data.display(), "->", end="")
            else:
                print(data, "->", end="")
            temp = temp.next
        print("<- Tail")


    def delet_at_beginning(self):
        if self.head != self.tail:
            self.head = self.head.next
        else:
            self.head = None
            self.tail = None

    def delet_at_end(self):
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            temp = self.head
            while temp.next != self.tail:
                temp = temp.next
            self.tail = temp
            self.tail.next = None


if __name__ == '__main__':
    biblioteca = LinkedList()
    biblioteca.load_from_file()
    biblioteca.print_books()

    print('\nIngrese un nuevo libro:')
    codigo = input('Código: ')
    titulo = input('Título: ')
    autor = input('Autor: ')
    genero = input('Género: ')

    biblioteca.insert_book(codigo, titulo, autor, genero)
    print('\nLibro agregado. Guardado en libros.txt.')
    biblioteca.print_books()

        