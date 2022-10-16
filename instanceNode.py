from node import Node


node1 = None
node2 = Node("A", None)
# Los nodos al ser secuanciales permiten refrencias a cualquier lugar.
node3 = Node("B", node2)



def show_relations():
    '''
    Este script perfectamente puede ser una función que recibe al nodo como parámetro pythony llamo para mostrar las
    relaciones.

    '''
    print("Esto es la ubicación en memoria de los nodos")
    print(node2) #<node.Node object at 0x0000022017FEAD30>
    print(node3) #<node.Node object at 0x0000022017FEAD90>
    print("Esto es el dato y muestra la relación entre nodos")
    print(node2.data,"-->", node2.next) #A --> None
    print(node3.data,"-->", node3.next) #B --> <node.Node object at 0x0000015356D6AD30>
    print("El siguiente dato del nodo es:")
    # Se refiere al nodo que está conectado y luego al dato que este contiene.
    print(node3.next.data) #'A'
    print("Creando el nodo1 y mostrando datos y relacion con nodo3 obtenemos: ")
    # Asignar una propiedad a un elemento para volverlo nodo.
    # Al intanciar la clase con una relación estamos ligando los nodos.
    node1= Node("C", node3)
    print(node1.data,"-->", node1.next)#C --> <node.Node object at 0x0000022017FEAD90>



def create_nodes():
    print("Creo nodos que se asignan a un solo valor en memoria, en este caso a node2: ")
    for node in range(5): #n --> <node.Node object at 0x000001B2AD991FD0>
        head = Node(node, node2)
        print(head.data,"-->", head.next)


def run():
    show_relations()
    create_nodes()

if __name__ == '__main__':
    run()