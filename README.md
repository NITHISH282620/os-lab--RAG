Resource Allocation Graph (RAG)

 Overview
This project implements a Resource Allocation Graph (RAG) to simulate resource allocation and request management in an operating system. It also includes a **deadlock detection** mechanism and graphical visualization of the graph.

Features
- Allocate Resources: Assign resources to processes.
- Request Resources: Simulate a process requesting a resource.
- Deadlock Detection: Check for cycles in the resource allocation graph.
- Graph Visualization: View the graph using NetworkX and Matplotlib.
- File-Based Input: Load processes and resources from text files.

 Installation
 Prerequisites
Ensure you have Python 3.x installed along with the required libraries:
     >pip install networkx matplotlib


 Project Structure

Resource_Allocation_Graph/
│-- processes.txt        # List of processes
│-- resources.txt        # List of resources
│-- README.md            # Documentation
│-- .gitignore           # Git ignore file


 Usage
1.Prepare Input Files:
   - Create `processes.txt` with a list of processes (e.g., `P1`, `P2`)
   - Create `resources.txt` with a list of resources (e.g., `R1`, `R2`)

2. Run the Program:
```sh
python rag.py
```

3. Interact with the Menu:
   - `1️⃣` Allocate a resource
   - `2️⃣` Request a resource
   - `3️⃣` Check for deadlocks
   - `4️⃣` View the resource allocation graph
   - `5️⃣` Exit

 Example
```
📌 Loading Processes & Resources...
✅ Processes: ['P1', 'P2']
✅ Resources: ['R1', 'R2']

🔹 Menu:
1️⃣ Allocate Resource
2️⃣ Request Resource
3️⃣ Check Deadlock
4️⃣ Show Graph
5️⃣ Exit
```

Deadlock Detection
If a cycle is detected in the graph, the program will notify the user:
```
 Deadlock Detected!
```
If no deadlock is found:
```
 No Deadlock Detected 
```

 Graph Visualization
The program uses NetworkX and Matplotlib to visualize the resource allocation graph. Example:
```
P1 → R1
R1 → P2
P2 → R2
R2 → P1 (Cycle detected!)
```

.gitignore File
To prevent tracking virtual environment files, include the following in `.gitignore`:
```
# Ignore virtual environment
venv/
```


 License
This project is open-source and free to use!

