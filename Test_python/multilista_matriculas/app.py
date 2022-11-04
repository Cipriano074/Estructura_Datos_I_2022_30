#from app.Classess import LinkedList
from Classess import LinkedList

lista_simple = LinkedList([ "ED1","FISICA","MEC. SOLIDOS","POB"])

print(lista_simple)
print(len(lista_simple))
print(lista_simple.head.Lista_espera)
print(lista_simple.head.Lista_matriculados)

estudiante = [["Juan","01"], ["Maria","02"],["Carlos","03"]]

"""
for i, obj in enumerate(lista_simple):
    print(estudiante[i], obj)
"""
P=lista_simple.head

for i in range(len(lista_simple)):
    print(P.Lista_matriculados.add_node(estudiante[i]))
    P = P.next
"""
P=lista_simple.head
for i in range(len(lista_simple)):
    print(P.Lista_matriculados)
    P = P.next
    """
print(lista_simple)
