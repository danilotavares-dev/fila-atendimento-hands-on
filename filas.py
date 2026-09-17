from collections import deque
import heapq
import random

class Cliente:
    def __init__(self, nome, senha, prioridade):
        self.nome = nome
        self.senha = senha
        self.prioridade = prioridade
        
        
class FilaClassica:
    def __init__(self):
        self.fila = deque()
        
    def empty(self):
        return len(self.fila) == 0
        
    def size(self):
        return len(self.fila)
        
    def head(self):
        if not self.empty():
            return self.fila[0]
        return None
        
    def enqueue(self, cliente):
        self.fila.append(cliente)
        
    def dequeue(self):
        if not self.empty():
            return self.fila.popleft()
        return None
    
    
class FilaCircular:
    def __init__(self, capacidade=5):
        self.capacidade = capacidade
        self.fila = [None] * capacidade
        self.front = -1
        self.rear = -1
        
    def isEmpty(self):
        return self.front == -1
        
    def isFull(self):
        return (self.rear + 1) % self.capacidade == self.front
        
    def enqueue(self, cliente):
        if self.isFull():
            print("Fila cheia!")
            return
        
        if self.isEmpty():
            self.front = 0
            
        self.rear = (self.rear + 1) % self.capacidade
        self.fila[self.rear] = cliente
        print(f"Inserido: {cliente.nome} | Índices -> front: {self.front}, rear: {self.rear}")
        
    def dequeue(self):
        if self.isEmpty():
            print("Fila vazia!")
            return None
        
        cliente_removido = self.fila[self.front]
        self.fila[self.front] = None
        
        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.capacidade
        
        print(f"Removido: {cliente_removido.nome} | Índices -> front: {self.front}, rear: {self.rear}")
        return cliente_removido
        
        
class FilaPrioridade:
    def __init__(self):
        self.fila = []
        self.contador = 0
        
    def enqueue(self, cliente):
        self.contador += 1
        heapq.heappush(self.fila, (cliente.prioridade, self.contador, cliente))
        
    def dequeue(self):
        if self.fila:
            return heapq.heappop(self.fila)[2]
        return None
        
    def empty(self):
        return len(self.fila) == 0
        
        
def simulacao():
    nomes = ["Alice", "Bruno", "Carla", "Daniel", "Eva", "Fabio", "Gisele", "Hugo", "Igor", "Julia", 
             "Kauan", "Lara", "Marcos", "Nina", "Otavio", "Paula", "Quintino", "Rita", "Samuel", "Tatiana"]
    
    clientes_gerados = []
    
    for i in range(20):
        prioridade = random.randint(1, 3)
        cliente = Cliente(nomes[i], f"S{(i+1):02d}", prioridade)
        clientes_gerados.append(cliente)

    print("--- CLIENTES GERADOS (ORDEM DE CHEGADA) ---")
    
    for c in clientes_gerados:
        print(f"[{c.senha}] {c.nome} - Prioridade: {c.prioridade}")

    print("\n--- TESTE FILA CLÁSSICA ---")
    
    fc = FilaClassica()
    
    for c in clientes_gerados:
        fc.enqueue(c)
        
    while not fc.empty():
        atendido = fc.dequeue()
        print(f"Atendendo: [{atendido.senha}] {atendido.nome} - Prioridade: {atendido.prioridade}")

    print("\n--- TESTE FILA CIRCULAR ---")
    
    fcirc = FilaCircular(5)
    
    for i in range(3):
        fcirc.enqueue(clientes_gerados[i])
    fcirc.dequeue()
    fcirc.dequeue()
    
    for i in range(3, 7):
        fcirc.enqueue(clientes_gerados[i])

    print("\n--- TESTE FILA DE PRIORIDADE ---")
    
    fp = FilaPrioridade()
    
    for c in clientes_gerados:
        fp.enqueue(c)
        
    while not fp.empty():
        atendido = fp.dequeue()
        print(f"Atendendo: [{atendido.senha}] {atendido.nome} - Prioridade: {atendido.prioridade}")

if __name__ == "__main__":
    simulacao()