 Advanced Implementation of the A* Pathfinding Algorithm with Heuristic Analysis

This project provides a complete implementation of the A* search algorithm on a weighted 2D grid, along with a comparative performance analysis of Manhattan and Euclidean heuristics.
The goal is to study how heuristic selection impacts:

Path optimality

Nodes expanded

Execution time

Efficiency in dense vs. sparse maps

All experiments, results, logs, and documentation are included.

 Project Directory Structure
vigneshwaranarasan-astar-heuristic-analysis/
│
├── README.md
├── LICENSE
│
├── data/
│   └── astar_raw_log.txt           # Raw performance logs for 10 test cases
│
├── docs/
│   ├── Astar_Report.docx           # Full textual analysis and project report
│   └── Astar_Report.pdf            # PDF version of the project report
│
└── src/
    ├── astar.py                    # Core A* search implementation
    ├── graph.py                    # Weighted grid / node storage
    ├── heuristics.py               # Manhattan & Euclidean heuristics
    ├── main.py                     # Entry point to run experiments
    ├── priority_queue.py           # Min-heap priority queue wrapper
    └── tester.py                   # Experiment runner for 10 grid tests

📌 Project Overview

The A* algorithm finds the lowest-cost path between two nodes by combining:

g(n) → cost from the start

h(n) → heuristic estimate to the goal

This project uses a custom weighted grid graph supporting:

Obstacles

Randomly generated terrain

Variable movement cost

Multiple map sizes and densities

Two admissible heuristics are compared:

Heuristic	Description	Notes
Manhattan Distance	Uses L1 distance	Ideal for 4-direction grids
Euclidean Distance	Straight-line distance	Smooth continuous estimation
✔️ Tasks Completed (as per assignment)
1. Grid/Graph Data Structure

A custom GridMap class was implemented to handle:

Weighted nodes

Obstacles

Neighbor lookup

Grid randomization

📄 File: src/graph.py

2. A* Search Algorithm

Complete A* implementation with:

PriorityQueue for open set

g-cost table

Came-from table for path reconstruction

Node expansion counter

Execution time recording

📄 File: src/astar.py

3. Two Admissible Heuristics

Both heuristics satisfy admissibility and consistency on a 4-connected grid.

📄 File: src/heuristics.py

4. Testing Harness (10 test cases)

The system automatically generates 10 random grid scenarios with varying:

Dimensions

Obstacle densities

Random seeds

Each scenario is solved using:

Manhattan A*

Euclidean A*

📄 File: src/tester.py

5. Comparative Analysis

All experimental results are saved in:

📁 data/astar_raw_log.txt

Format:

test_id,heuristic,found,path_length,total_cost,nodes_expanded,execution_time_ms,width,height,obstacle_prob


These logs were used to produce:

The full report (docs/Astar_Report.docx / .pdf)

Performance comparison conclusions

📊 Summary of Results
Manhattan Heuristic

Expands fewer nodes in most test cases

Slightly more consistent in cluttered environments

Best for strict grid-based movement

Euclidean Heuristic

Produces identical optimal path costs

Sometimes faster in large open grids

Slightly more node expansions overall

Conclusion

Both heuristics guarantee optimal paths, but their efficiency trade-offs differ depending on map density and weight distribution.

▶️ Running the Project
1. Clone the repository
git clone https://github.com/vigneshwaranarasan/Astar-Heuristic-Analysis.git
cd Astar-Heuristic-Analysis

2. Run all 10 experiments
python src/main.py

3. View results

Logs saved to:

data/astar_raw_log.txt


Report available in:

docs/Astar_Report.pdf
docs/Astar_Report.docx

📄 License

This project is licensed under the MIT License.
See the LICENSE file for details.

👨‍💻 Author

Vigneshwaranarasan
GitHub: https://github.com/vigneshwaranarasan
