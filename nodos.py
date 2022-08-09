# Lo primero que hacemos es, definir nuestra clase Nodo. 
# Definimos nuestro método __init__, que es el constructor de nuestra clase Nodo .
# En el constructor, le pasamos los parámetros de Self (para apuntar al objeto actual que estamos instanciando), valor (el valor que asignaremos al nodo) 
# y link (por defecto, asignamos que este es None considerando que puede ser el último elemento.)
class Nodo:
    def __init__(self, valor, link=None):
        self.valor = valor
        self.link = link
# Definimos métodos para acceder a los datos del nodo y a sus links.
    def ver_valor(self):
        return self.valor
    
    def ver_link(self):
        return self.link
# Para este ejemplo, vamos a crear método para modificar o setear el valor del link del nodo. No implementaremos método para cambiar el valor.
    def set_link(self, link):
        self.link = link
# Con esto ya tenemos construida nuestra clase Nodo y nuestros métodos. Ahora podemos instanciarlos.
# Para este ejemplo, vamos a crear 3 nodos los cuales vamos a linkear de la siguiente manera.
# nodo_a(valor: "hola mundo") >>> nodo_b(valor: 1986) >>> nodo_c(valor: [3, 4, 5, 6])

# Instanciamos los nodos asignandolos a las variables correspondientes.
nodo_a = Nodo("hola mundo")
nodo_b = Nodo(1986)
nodo_c = Nodo([3, 4, 5, 6])

# Ahora procedemos a establecer el enlace entre los nodos, utilizando el método de set_link que definimos en nuestra clase Nodo.
# Recuerda que debemos linkear el nodo_a > nodo_b, y luego el nodo_b > nodo_c.
nodo_a.set_link(nodo_b)
nodo_b.set_link(nodo_c)

# A modo de prueba, vamos a crear 3 variables, almacenar los valores de 3 nodos e imprimir los mismos. 
# Si todo está bien, debemos tener impresos los valores en consola. Utilizamos el metodo ver_valor().
valor_nodo_a = nodo_a.ver_valor()
valor_nodo_b_directo = nodo_b.ver_valor()
valor_nodo_b = nodo_a.ver_link().ver_valor()
valor_nodo_c_directo = nodo_c.ver_valor()
valor_nodo_c = nodo_b.ver_link().ver_valor()


# imprimimos nuestras variales.
print("El valor del nodo a, es: ", valor_nodo_a)
print("El valor del nodo b, accediendo de forma directa es: ", valor_nodo_b_directo)
print("El valor del nodo b, accdediendo desde el nodo_a usando link es: ", valor_nodo_b)
print("El valor del nodo b, accediendo de forma directa es: ", valor_nodo_c_directo)
print("El valor del nodo b accdediendo desde el nodo_b usando link es: ", valor_nodo_c)