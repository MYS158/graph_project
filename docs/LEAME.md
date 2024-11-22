# Graph Project

Graph Project es un proyecto en Python diseñado para trabajar con grafos. Permite a los usuarios crear grafos dirigidos o no dirigidos, ponderados o no ponderados, y soporta varios algoritmos de grafos, incluyendo BFS, DFS, el camino más corto de Dijkstra, los algoritmos de Kruskal y Prim. La librería también incluye capacidades de visualización para estructuras de redes, con opciones para personalizar las propiedades de nodos y aristas.

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
    - Búsqueda en Anchura (BFS)
    - Búsqueda en Profundidad (DFS)
    - Camino más corto de Dijkstra
    - Árbol de Expansión Mínima de Kruskal
    - Árbol de Expansión Mínima de Prim
- **Visualización**: Proporciona herramientas para la visualización de grafos con opciones para personalizar colores, grosor de las aristas, tamaño de los nodos y más.

## Instalación
1. **Instalar Python y Visual Studio Code**:
    - Descarga e instala la última versión de Python desde el sitio web oficial: [python.org](https://www.python.org/)
    - Asegúrate de marcar la opción para agregar Python al PATH del sistema durante la instalación.
    - Descarga e instala la última versión de Visual Studio Code desde el sitio web oficial: [visualstudio.com](https://code.visualstudio.com/)
2. **Clonar el repositorio**:
    Usa Git para clonar el repositorio o descárgalo directamente. Si usas Git, ejecuta el siguiente comando en tu terminal:
    ```bash
    git clone https://drive.google.com/drive/folders/1jXMeYYUYiB7u1rKwhD1znut63Tdrv2k2?usp=sharing
    ```
3. **Navegar al directorio del proyecto**:
    Abre tu terminal o línea de comandos y ejecuta:
    ```bash
    cd graph_project
    ```
4. **Instalar los paquetes requeridos**:
    Asegúrate de tener pip instalado. Si tienes Python instalado, pip debería estar incluido. Ejecuta el siguiente comando para instalar los paquetes necesarios:
    ```bash
    pip install -r requirements.txt
    ```
5. **Ejecutar el ejemplo**:
    Después de instalar los paquetes necesarios, puedes ejecutar uno de los códigos de ejemplo proporcionados en la carpeta de ejemplos ejecutando `main.py` 
    (desde `examples.<tu_ejemplo>` importa `run`):
    ```bash
    python main.py
    ```
    Asegúrate de reemplazar `<tu_ejemplo>` con el nombre real del script que desees ejecutar.
6. **Verificar la instalación**:
    Para verificar que todo está funcionando correctamente, puedes ejecutar las pruebas unitarias incluidas en el proyecto. Ejecuta el siguiente comando:
    ```bash
    python -m unittest discover -s tests
    ```

## Estructura del Proyecto

El proyecto está organizado de la siguiente manera:

```
graph_project/
│
├── .venv/                   # Entorno virtual
│   ├── Include/             # Cabeceras C para paquetes de Python
│   ├── Lib/                 # Librerías de Python instaladas
│   ├── Scripts/             # Ejecutables, incluyendo Python y pip
│   ├── share/               # Archivos compartidos y datos para algunos paquetes
│   ├── .gitignore           # Asegura que el entorno virtual no se suba a git
│   └── pyvenv.cfg           # Archivo de configuración del entorno virtual
│
├── .vscode/                 # Configuración de Visual Studio Code
│   ├── launch.json          # Configuración del depurador
│   └── settings.json        # Configuración personalizada del editor
│
├── algorithms/              # Algoritmos de grafos
│   ├── bfs.py               # Búsqueda en Anchura (BFS)
│   ├── dfs.py               # Búsqueda en Profundidad (DFS)
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
│   └── README.md            # Documentación principal en inglés
│
├── examples/                # Ejemplos de uso
│   ├── algorithm_example.py # Ejemplo de uso de los algoritmos
│   ├── neural_network.py    # Visualización de una red neuronal como un grafo
│   ├── pentagram.py         # Ejemplo gráfico con un pentágono
│   └── __init__.py
│
├── tests/                   # Pruebas unitarias
│   ├── test_algorithms.py   # Pruebas de los algoritmos de grafos
│   ├── test_graph.py        # Pruebas de los métodos del grafo
│   └── __init__.py
│
├── utils/                   # Funciones utilitarias
│   ├── errors.py            # Clases de errores personalizados
│   ├── helpers.py           # Funciones auxiliares
│   ├── visualization.py     # Utilidades de visualización
│   └── __init__.py
│
├── config.py                # Archivo de configuración para ajustes globales
├── graph.py                 # Clase principal Graph
├── main.py                  # Punto de entrada del proyecto
└── requirements.txt         # Paquetes de Python requeridos
```

## Uso

### Creando un Grafo

Para crear un grafo básico, importa la clase `Graph` y agrega nodos y aristas:

```python
from graph import Graph
graph = Graph(directed=True, weighted=True)
graph.add_node("A")
graph.add_node("B")
graph.add_edge("A", "B", weight=3)
graph.draw(title="Example Graph")
```

### Algoritmos

GraphProject soporta varios algoritmos. Aquí hay un ejemplo de uso de BFS y el algoritmo de Dijkstra:

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

# Realizar BFS
print("Recorrido BFS comenzando desde el nodo 'A':")
bfs_result = bfs(graph, "A")
print(bfs_result)

# Realizar el algoritmo de Dijkstra
print("Algoritmo de Dijkstra comenzando desde el nodo 'A':")
dijkstra_result = dijkstra(graph, "A")
print(dijkstra_result)
```

### Visualización

Personaliza las propiedades visuales como los colores de los nodos, tamaño, grosor de las aristas, y más:

```python
node_colors = {"A": "red", "B": "green", "C": "blue"}
graph.draw(
    title="Custom Graph",
    node_colors=node_colors,
    node_size=700,
    edge_thickness=2,
    font="Times New Roman",
    font_size=12
)
```

## Ejemplos

El directorio 'examples/' contiene scripts de ejemplo que muestran diferentes casos de uso:

- `algorithm_example.py`: Ejemplo básico de crear y visualizar un grafo.
- `neural_network.py`: Ejemplo de visualización de una estructura de red neuronal.
- `pentagram.py`: Visualización de un grafo con forma de pentágono.

## Pruebas

Para ejecutar las pruebas unitarias, usa el siguiente comando:

```bash
python -m unittest discover tests/
```

Esto ejecutará las pruebas en `tests/test_graph.py` y `tests/test_algorithms.py` para asegurar que todo funciona como se espera.

Hecho por Miguel Muñoz, 2024  
UAEH - Licenciatura en Ciencias Computacionales