# HANDS ON — Sistema Inteligente de Atendimento com Filas

## Perguntas e Respostas

### 1. Por que a ordem de atendimento da fila de prioridade pode ser diferente da ordem da fila clássica?

Na fila clássica (FIFO — First In, First Out), o único critério de atendimento é a ordem de chegada. Na fila de prioridade, a estrutura reorganiza os elementos com base no grau de importância ou urgência definido (no caso do exercício, de 1 a 3). A ordem de chegada só é levada em consideração como critério de desempate quando dois elementos possuem o mesmo nível de prioridade — no nosso `heapq`, isso é garantido pelo campo `contador` na tupla `(prioridade, contador, cliente)`, que preserva a sequência original entre elementos de mesma prioridade.

### 2. Em quais situações reais uma fila de prioridade seria mais adequada?

Ela é essencial em sistemas onde o atraso no processamento de certos eventos pode causar impactos críticos. Exemplos incluem:

- **Saúde:** triagem em prontos-socorros, onde pacientes com risco de morte são atendidos antes de casos leves.
- **Computação:** escalonamento de processos no sistema operacional, garantindo que tarefas críticas do kernel não travem por causa de aplicativos de usuário.
- **Redes:** roteadores priorizando pacotes de chamadas de voz e vídeo (VoIP) em relação a downloads de arquivos, evitando latência e falhas na comunicação.
- **Atendimento ao público:** caixas preferenciais em bancos para idosos ou pessoas com deficiência.

### 3. Quais são as vantagens e limitações de uma fila circular?

**Vantagens:** otimização do uso de memória em arrays de tamanho fixo. Ao remover elementos do início da fila, as posições ficam vazias, e a fila circular consegue reaproveitar esses espaços fazendo o índice final (`rear`) "dar a volta" no array, sem precisar deslocar todos os outros elementos uma posição para frente.

**Limitações:** o tamanho máximo é estático e predefinido — uma vez atingida a capacidade total, a estrutura não cresce dinamicamente como uma lista encadeada. Além disso, o controle lógico dos ponteiros usando aritmética modular é mais suscetível a erros de implementação.

### 4. O que acontece ao tentar inserir um elemento em uma fila circular cheia?

Ocorre uma condição de overflow (transbordamento). A estrutura identifica que a próxima posição a ser preenchida pelo `rear` colidiria com o `front`, indicando que todos os espaços estão ocupados com elementos ainda não processados. A operação de inserção é bloqueada/rejeitada para não sobrescrever dados pendentes.