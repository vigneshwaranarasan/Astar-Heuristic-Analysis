#  Advanced Implementation of the A* Pathfinding Algorithm with Heuristic Analysis

This project implements the **A\*** (A-star) search algorithm **from scratch** in Python, using a custom **weighted grid-based graph structure**.  
The main objective is to compare the performance of **two admissible heuristics**:

- **Manhattan Distance**
- **Euclidean Distance**

The project includes a fully functional A* implementation, random grid generation with obstacles, a testing harness that runs **10 predefined experiments**, and a raw log output used for heuristic performance comparison.

---

##  **Project Directory Structure**

```
vigneshwaranarasan-astar-heuristic-analysis/
│
├── README.md
├── LICENSE
│
├── data/
│   └── astar_raw_log.txt        # Raw log data from 10 test cases
│
└── src/
    ├── astar.py                 # Core A* search algorithm
    ├── graph.py                 # Weighted grid / graph implementation
    ├── heuristics.py            # Manhattan & Euclidean heuristic functions
    ├── main.py                  # Main entry point to run experiments
    ├── priority_queue.py        # Min-heap priority queue for A*
    └── tester.py                # Testing harness for 10 randomized grids
```

---

##  **Project Overview**

This project fulfills the requirements of the “Advanced Implementation of the A* Pathfinding Algorithm with Heuristic Analysis” assignment.  
The implementation focuses on:

- Designing a **generic grid/graph representation** with weighted edges  
- Implementing the **A\*** search algorithm from scratch  
- Using a **Priority Queue** for the open set  
- Comparing **two admissible heuristics**  
- Generating **10 randomized test scenarios**  
- Logging performance metrics including:
  - Path existence  
  - Path length  
  - Total path cost  
  - Nodes expanded  
  - Execution time (ms)

All experiments are captured in **data/astar_raw_log.txt** and can be used for report writing, plotting, and performance discussion.

---

##  **Tasks Completed**

### **1. Grid/Graph Data Structure**
A fully customizable grid with:
- Weighted cells  
- Obstacles  
- Boundary & neighbor validation  
- Random generation with obstacle probability  

Implemented in:  
📄 `src/graph.py`

---

### **2. Core A\* Search Algorithm**
The A\* algorithm is implemented from scratch with:
- Priority Queue (min-heap)  
- `g(n)` cost tracking  
- Heuristic integration  
- Path reconstruction  
- Node expansion counting  
- Execution time measurement  

Implemented in:  
📄 `src/astar.py`  
📄 `src/priority_queue.py`

---

### **3. Two Admissible Heuristics**
Both heuristics satisfy the admissibility requirement on a 4-connected grid:

- **Manhattan Distance**  
- **Euclidean Distance**

Implemented in:  
📄 `src/heuristics.py`

---

### **4. Testing Harness — 10 Experiments**
A complete experimental runner generates:
- 10 grid configurations (sizes 20×20 to 40×40)  
- Two heuristic runs per grid  
- Auto-generated raw logs  

Implemented in:  
📄 `src/tester.py`

Run through:  
📄 `src/main.py`

---

### **5. Performance Comparison Log**
All 20 runs (10 test cases × 2 heuristics) are saved in:

 `data/astar_raw_log.txt`

Format:

```
test_id,heuristic,found,path_length,total_cost,
nodes_expanded,execution_time_ms,width,height,obstacle_prob
```

Example entry:

```
1,manhattan,True,39,92.8565,301,0.7659,20,20,0.2
```

---

##  **Summary of Results**

### **Manhattan Heuristic**
- Expands fewer nodes in most cases  
- Slightly faster on dense obstacle grids  
- Very consistent for grid-based movement  

### **Euclidean Heuristic**
- Produces the **same optimal path cost**  
- Sometimes expands more nodes  
- Slightly faster in open, larger grids  

Both heuristics always produce **optimal paths**.

---

##  **How to Run the Project**

### **1. Clone the repository**

```bash
git clone https://github.com/vigneshwaranarasan/Astar-Heuristic-Analysis.git
cd Astar-Heuristic-Analysis
```

### **2. Run experiments**

```bash
python src/main.py
```

### **3. Check the output log**

```
data/astar_raw_log.txt
```

---

##  **Expected Deliverables (Completed)**

### ✔ Full runnable A* source code  
### ✔ Testing harness with 10 cases  
### ✔ Raw log output for comparative analysis  
### ✔ Heuristic performance comparison  

---

##  **License**

This project is licensed under the **MIT License**.

---

##  **Author**

**Vigneshwaranarasan**  
GitHub: https://github.com/vigneshwaranarasan
