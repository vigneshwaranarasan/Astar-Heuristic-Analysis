# ⭐ Advanced Implementation of the A* Pathfinding Algorithm with Heuristic Analysis

This project provides a complete implementation of the **A*** search algorithm on a weighted 2D grid, along with a comparative performance analysis of **Manhattan** and **Euclidean** heuristics.  
The goal is to study how heuristic selection impacts path optimality, nodes expanded, execution time, and search efficiency.

---

## 📁 Project Directory Structure

```
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
```

---

## 📌 Project Overview

This project fulfills all the tasks outlined in the “Advanced Implementation of the A* Pathfinding Algorithm with Heuristic Analysis” assignment.

The implementation compares two admissible heuristics:

- **Manhattan Distance**
- **Euclidean Distance**

Both produce the same optimal path cost but differ in node expansions and execution time.

---

## ✔️ Tasks Completed

### **1. Grid/Graph Data Structure**
Implemented in `src/graph.py`  
Features:
- Weighted grid  
- Obstacles  
- Random map generator  
- Neighbor lookup  

---

### **2. A* Search Algorithm**
Implemented in `src/astar.py`  
Includes:
- Priority Queue  
- g-cost tracking  
- f-cost computation  
- Path reconstruction  
- Node expansion count  
- Execution time  

---

### **3. Two Admissible Heuristics**
Implemented in `src/heuristics.py`:
- Manhattan (L1)
- Euclidean (L2)

---

### **4. Testing Harness — 10 Experiments**
Implemented in `src/tester.py`  
Each test:
- Generates a solvable grid  
- Runs both heuristics  
- Records:
  - path_length  
  - total_cost  
  - nodes_expanded  
  - execution_time_ms  

---

### **5. Raw Log Output**
Saved in:  
```
data/astar_raw_log.txt
```
Contains detailed results for all 20 runs (10 × 2 heuristics).

---

## 📊 Summary of Experimental Results

### **Manhattan Heuristic**
- Fewer nodes expanded in most cases  
- More consistent in dense environments  

### **Euclidean Heuristic**
- Same optimal cost as Manhattan  
- Occasionally faster  
- Slightly higher node expansions  

---

## ▶️ How to Run the Project

### **Clone the repository**
```bash
git clone https://github.com/vigneshwaranarasan/Astar-Heuristic-Analysis.git
cd Astar-Heuristic-Analysis
```

### **Run all experiments**
```bash
python src/main.py
```

### **View results**
Logs:
```
data/astar_raw_log.txt
```

Reports:
```
docs/Astar_Report.docx
docs/Astar_Report.pdf
```

---

## 📄 License
This project is licensed under the **MIT License**.

---

## 👨‍💻 Author
**Vigneshwaranarasan**  
GitHub: https://github.com/vigneshwaranarasan
