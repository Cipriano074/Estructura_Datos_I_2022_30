class Node_Curso:
    def __init__(self, nombre_curso: str = None, \
        num_max_matriculados: int = 30, \
        next_node = None, prev_node = None):
        self.nombre_curso = nombre_curso
        self.num_max_matriculados = num_max_matriculados
        self.next = next_node
        self.prev = prev_node
        self.Lista_matriculados = Lista_matriculados()
        self.Lista_espera = Lista_espera()

    def __str__(self):
        return str("nombre es "+self.nombre_curso+" tiene capacidad de  "\
            +str(self.num_max_matriculados))

class Node_Estudiante:
    def __init__(self, nombre_estudiante: str = None, \
        id: str = 30, \
        next_estudiante = None, prev_estudiante = None):
        self.nombre_estudiante = nombre_estudiante
        self.id = id
        self.next_estudiante = next_estudiante
        self.prev_estudiante = prev_estudiante

    def __str__(self):
        return str("nombre es "+self.nombre_curso+" tiene capacidad de  "\
            +str(self.num_max_matriculados))


class Lista_matriculados:
    pass
class Lista_espera:
    pass

class Lista_estudiantes:
    def __init__(self, values=None):
        self.head_estudiante = None
        self.tail_estudiante = None
        if values is not None:
            self.add_multiple_nodes(values)
            
    def __str__(self):
        return ' -> '.join([str(node) for node in self])
    
    def __len__(self):
        count = 0
        node = self.head_estudiante
        while node:
            count += 1
            node = node.next_estudiante
        return count
    
    def __iter__(self):
        current = self.head_estudiante
        while current:
            yield current
            current = current.next_estudiante
            
    @property
    def values(self):
        return [node.value for node in self]
    
    def add_node(self, value):
        if self.head_estudiante is None:
            self.tail_estudiante = self.head_estudiante = Node_Curso(value)
        else:
            self.tail_estudiante.next_estudiante = Node_Curso(value)
            self.tail = self.tail_estudiante.next_estudiante
        return self.tail_estudiante
    
    def add_multiple_nodes(self, values):
        for value in values:
            self.add_node(value)
            
    def add_node_as_head(self, value):
        if self.head_estudiante is None:
            self.tail_estudiante = self.head_estudiante = Node_Curso(value)
        else:
            self.head_estudiante = Node_Curso(value, self.head_estudiante)
        return self.head_estudiante

class LinkedList:
    def __init__(self, values=None):
        self.head = None
        self.tail = None
        if values is not None:
            self.add_multiple_nodes(values)
            
    def __str__(self):
        return ' -> '.join([str(node) for node in self])
    
    def __len__(self):
        count = 0
        node = self.head
        while node:
            count += 1
            node = node.next
        return count
    
    def __iter__(self):
        current = self.head
        while current:
            yield current
            current = current.next
            
    @property
    def values(self):
        return [node.value for node in self]
    
    def add_node(self, value):
        if self.head is None:
            self.tail = self.head = Node_Curso(value)
        else:
            self.tail.next = Node_Curso(value)
            self.tail = self.tail.next
        return self.tail
    
    def add_multiple_nodes(self, values):
        for value in values:
            self.add_node(value)
            
    def add_node_as_head(self, value):
        if self.head is None:
            self.tail = self.head = Node_Curso(value)
        else:
            self.head = Node_Curso(value, self.head)
        return self.head


class DoublyLinkedList(LinkedList):
    def add_node(self, value):
        if self.head is None:
            self.tail = self.head = Node_Curso(value)
        else:
            self.tail.next = Node_Curso(value, None, self.tail)
            self.tail = self.tail.next
        return self
    
    def add_node_as_head(self, value):
        if self.head is None:
            self.tail = self.head = Node_Curso(value)
        else:
            current_head = self.head
            self.head = Node_Curso(value, current_head)
            current_head.prev = self.head
        return self.head