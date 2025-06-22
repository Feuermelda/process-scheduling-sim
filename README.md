# Process Scheduling Simulator

Welcome to the **Process Scheduling Simulator** - a collection of Python scripts that bring CPU scheduling algorithms to life! This playful project was built to help understand how operating systems manage multiple processes, using fair and unfair techniques alike.

---

## Included Algorithms

- **Round Robin (`round-robin-sim.py`)**  
  A time-slicing CPU party where everyone gets a turn - whether they finish or not.

<!-- Future entries -->
- **First-Come, First-Served (Coming soon)**
- **Shortest Job First (Coming soon)**
- **Priority Scheduling (Coming soon)**
- **Multilevel Feedback Queue (Coming soon)**

---

## How to Run

Make sure you have **Python 3** installed. Then from the terminal:

```bash
python3 round-robin-sim.py
```
The script will prompt you for:
1. A list of process names
2. A list of corresponding step counts
3. A time slice value

It then simulates execution using the Round Robin algorithm and prints each step.