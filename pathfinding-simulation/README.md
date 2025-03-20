# pathfinding-simulation/README.md

# Pathfinding Simulation

This project visualizes the shortest path algorithms in a grid-based maze. It implements four algorithms: Breadth-First Search (BFS), Depth-First Search (DFS), A*, and Dijkstra's algorithm. Users can input two points in the maze, and the application will display the results side by side.

## Project Structure

```
pathfinding-simulation
├── src
│   ├── algorithms
│   │   ├── astar.py       # A* algorithm implementation
│   │   ├── bfs.py        # BFS algorithm implementation
│   │   ├── dfs.py        # DFS algorithm implementation
│   │   └── dijkstra.py    # Dijkstra's algorithm implementation
│   ├── ui
│   │   ├── grid.py        # Grid management and visualization
│   │   └── window.py      # Main application window and user input
│   └── main.py            # Entry point of the application
├── tests
│   └── test_algorithms.py  # Unit tests for algorithms
├── requirements.txt        # Project dependencies
└── README.md               # Project documentation
```

## Requirements

To run this project, you need to have Python installed along with the required libraries. You can install the dependencies using:

```
pip install -r requirements.txt
```

## Usage

1. Run the application:

   ```
   python src/main.py
   ```

2. Input the start and end points in the grid.
3. Choose the algorithm you want to visualize.
4. Observe the pathfinding process as the algorithm finds the shortest path.

## Contributing

Feel free to submit issues or pull requests if you have suggestions or improvements for the project.