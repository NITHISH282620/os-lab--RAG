import networkx as nx
import matplotlib.pyplot as plt

# Load processes from file
def load_processes():
    with open("processes.txt", "r") as file:
        return [line.strip() for line in file.readlines()]

# Load resources from file
def load_resources():
    with open("resources.txt", "r") as file:
        return [line.strip() for line in file.readlines()]

# Dictionary to store the resource allocation graph
graph = {}

# Allocate resource
def allocate_resource(process, resource):
    if resource in graph:
        print(f"❌ {resource} is already allocated!")
    else:
        graph[resource] = process
        print(f"✅ {resource} allocated to {process}")

# Request resource
def request_resource(process, resource):
    if process in graph and graph[process] == resource:
        print(f"❌ {process} already has {resource}!")
    else:
        graph[process] = resource
        print(f"🔄 {process} is requesting {resource}")

# Detect deadlock using cycle detection
def detect_deadlock():
    visited = set()
    stack = set()

    def dfs(node):
        if node in stack:  # Cycle detected
            return True
        if node in visited:
            return False
        visited.add(node)
        stack.add(node)
        for neighbor in graph.get(node, []):
            if dfs(neighbor):
                return True
        stack.remove(node)
        return False

    for node in graph:
        if dfs(node):
            print("\n❌ Deadlock Detected! ❌")
            return True
    print("\n✅ No Deadlock Detected ✅")
    return False

# Draw the graph
def draw_graph():
    G = nx.DiGraph()
    for key, value in graph.items():
        G.add_edge(key, value)

    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color="lightblue", edge_color="red", node_size=2000, font_size=10)
    plt.show()

# User Interface
def main():
    print("📌 Loading Processes & Resources...")
    processes = load_processes()
    resources = load_resources()
    
    print(f"✅ Processes: {processes}")
    print(f"✅ Resources: {resources}")

    while True:
        print("\n🔹 Menu:")
        print("1️⃣ Allocate Resource")
        print("2️⃣ Request Resource")
        print("3️⃣ Check Deadlock")
        print("4️⃣ Show Graph")
        print("5️⃣ Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            p = input("Enter Process (e.g., P1): ")
            r = input("Enter Resource (e.g., R1): ")
            allocate_resource(p, r)

        elif choice == "2":
            p = input("Enter Process (e.g., P1): ")
            r = input("Enter Resource (e.g., R1): ")
            request_resource(p, r)

        elif choice == "3":
            detect_deadlock()

        elif choice == "4":
            draw_graph()

        elif choice == "5":
            print("🚀 Exiting...")
            break

        else:
            print("❌ Invalid Choice!")

if __name__ == "__main__":
    main()
