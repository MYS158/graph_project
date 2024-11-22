# Proyecto Graph

El Proyecto Graph es una biblioteca de Python para crear y gestionar grafos. Soporta grafos dirigidos y no dirigidos, ponderados y no ponderados, e incluye algoritmos como BFS, DFS, el algoritmo de caminos más cortos de Dijkstra, Hierholzer, Kruskal y Prim. Además, el proyecto ofrece herramientas de visualización con propiedades personalizables para nodos y aristas, permitiendo representar estructuras de red de manera efectiva.

## Tabla de Contenidos
- [Características](#características)
- [Instalación](#instalación)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Uso](#uso)
- [Ejemplos](#ejemplos)
- [Pruebas](#pruebas)

## Características

- **Creación de Grafos**: Soporta grafos dirigidos y no dirigidos, con pesos opcionales en las aristas.
- **Algoritmos de Grafos**: Implementa varios algoritmos, incluyendo:
  - Búsqueda en Amplitud (BFS)
  - Búsqueda en Profundidad (DFS)
  - Algoritmo de Caminos Más Cortos de Dijkstra
  - Algoritmo de Hierholzer para circuitos eulerianos
  - Árbol de Expansión Mínima de Kruskal
  - Árbol de Expansión Mínima de Prim
- **Visualización**: Proporciona herramientas para la visualización de grafos con opciones de colores personalizados, grosor de aristas, tamaño de nodos y más.

## Instalación

1. **Instala Python y Visual Studio Code**:
   - Descarga e instala la versión más reciente de Python desde el sitio oficial: [python.org](https://www.python.org/)
   - Asegúrate de marcar la opción para agregar Python al PATH durante la instalación.
   - Descarga e instala la versión más reciente de Visual Studio Code desde el sitio oficial: [visualstudio.com](https://code.visualstudio.com/)

2. **Clona el repositorio**:  
   Usa Git para clonar el repositorio o descárgalo directamente. Si usas Git, ejecuta el siguiente comando en tu terminal:  
   ```bash
   git clone https://github.com/MYS158/graph_project.git
   ```

3. **Navega al directorio del proyecto**:  
   Abre tu terminal o consola y ejecuta:  
   ```bash
   cd graph_project
   ```

4. **Instala las dependencias necesarias**:  
   Asegúrate de tener instalado `pip`. Si instalaste Python correctamente, `pip` ya debería estar disponible. Ejecuta el siguiente comando:  
   ```bash
   pip install -r requirements.txt
   ```

5. **Ejecuta un ejemplo**:  
   Una vez instaladas las dependencias, puedes ejecutar uno de los ejemplos proporcionados en la carpeta `examples` usando `main.py`:  
   ```bash
   python main.py
   ```
   Asegúrate de reemplazar `<your_example>` con el nombre del script que desees ejecutar.

6. **Verifica la instalación**:  
   Para confirmar que todo funciona correctamente, ejecuta las pruebas unitarias incluidas en el proyecto. Usa este comando:  
   ```bash
   python -m unittest discover -s tests
   ```

## Estructura del Proyecto

El proyecto está organizado de la siguiente manera:

```
graph_project/  
│  
├── .venv/                   # Entorno virtual  
│   ├── Include/             # Encabezados C para paquetes de Python  
│   ├── Lib/                 # Librerías de Python instaladas  
│   ├── Scripts/             # Ejecutables, incluyendo Python y pip  
│   ├── share/               # Archivos compartidos y datos para algunos paquetes  
│   ├── .gitignore           # Asegura que el entorno virtual no se suba a Git  
│   └── pyvenv.cfg           # Archivo de configuración del entorno virtual  
│  
├── .vscode/                 # Configuraciones de Visual Studio Code  
│   ├── launch.json          # Configuración del depurador  
│   └── settings.json        # Configuración personalizada del editor  
│  
├── algorithms/              # Algoritmos de grafos  
│   ├── bfs.py               # Búsqueda en amplitud (Breadth-First Search)  
│   ├── dfs.py               # Búsqueda en profundidad (Depth-First Search)  
│   ├── dijkstra.py          # Algoritmo de Dijkstra  
│   ├── hierholzer.py        # Algoritmo de Hierholzer  
│   ├── kruskal.py           # Algoritmo de Kruskal  
│   ├── prim.py              # Algoritmo de Prim  
│   └── __init__.py          # Marca esta carpeta como un paquete de Python  
│  
├── data/                    # Archivos de datos para cargar grafos  
│  
├── docs/                    # Documentación  
│   ├── LEAME.md             # Documentación en español  
│   └── README.md            # Documentación principal del proyecto en inglés  
│  
├── examples/                # Ejemplos de uso  
│   ├── algorithm_example.py # Ejemplo de uso de algoritmos  
│   ├── neural_network.py    # Visualización de una red neuronal como un grafo  
│   ├── pentagram.py         # Ejemplo gráfico con un pentagrama  
│   └── __init__.py  
│  
├── tests/                   # Pruebas unitarias  
│   ├── test_algorithms.py   # Pruebas para los algoritmos de grafos  
│   ├── test_graph.py        # Pruebas para los métodos de grafos  
│   └── __init__.py  
│  
├── utils/                   # Funciones utilitarias  
│   ├── errors.py            # Clases de errores personalizados  
│   ├── helpers.py           # Funciones auxiliares  
│   ├── visualization.py     # Utilidades de visualización  
│   └── __init__.py  
│  
├── config.py                # Archivo de configuración para ajustes globales  
├── graph.py                 # Clase principal de Grafos  
├── main.py                  # Punto de entrada del proyecto  
└── requirements.txt         # Paquetes de Python requeridos  
```

## Uso

### Crear un Grafo

Para crear un grafo básico, importa la clase `Graph` y agrega nodos y aristas:

```python
from graph import Graph
graph = Graph(directed=True, weighted=True)
graph.add_node("A")
graph.add_node("B")
graph.add_edge("A", "B", weight=3)
graph.draw(title="Ejemplo de Grafo")
```

### Algoritmos

GraphProject incluye varios algoritmos. Aquí hay un ejemplo usando BFS y el algoritmo de Dijkstra:

```python
from graph import Graph
from algorithms.bfs import bfs
from algorithms.dijkstra import dijkstra

# Crear un grafo no dirigido
graph = Graph(directed=False, weighted=True)
graph.add_node("A")
graph.add_node("B")
graph.add_node("C")
graph.add_edge("A", "B", weight=2)
graph.add_edge("B", "C", weight=3)

# Ejecutar BFS
print("Recorrido BFS desde el nodo 'A':")
bfs_result = bfs(graph, "A")
print(bfs_result)

# Ejecutar el algoritmo de Dijkstra
print("Algoritmo de Dijkstra desde el nodo 'A':")
dijkstra_result = dijkstra(graph, "A")
print(dijkstra_result)
```

### Visualización

Personaliza propiedades visuales como colores de nodos, tamaño, grosor de aristas y más:

```python
node_colors = {"A": "red", "B": "green", "C": "blue"}
graph.draw(
    title="Grafo Personalizado",
    node_colors=node_colors,
    node_size=700,
    edge_thickness=2,
    font="Times New Roman",
    font_size=12
)
```

## Ejemplos

El directorio `examples/` contiene scripts de ejemplo que demuestran diferentes casos de uso:

- `algorithm_example.py`: Ejemplo básico de creación y visualización de un grafo.
- `neural_network.py`: Ejemplo de visualización de una red neuronal como grafo.
- `pentagram.py`: Visualización de un grafo en forma de pentagrama.

## Pruebas

Para ejecutar las pruebas unitarias, usa el siguiente comando:

```bash
python -m unittest discover tests/
```

Esto ejecutará las pruebas en `tests/test_graph.py` y `tests/test_algorithms.py` para asegurar que todo funcione correctamente.

Creado por Miguel Muñoz, 2024  
UAEH - Licenciatura en Ciencias Computacionales
