import networkx as nx
import matplotlib.pyplot as plt

if __name__ =="__main__":
    MyGraph= nx.Graph()
    x = input("Inserire nomi degli edges? Y/N ")
    if x in "Nn":
        while True:
            instr=input("Inserire nomi nodes separati da una virgola o stop: ")
            if instr in "stopSTOP":
                break
            ListNodes= list(instr.split(","))
            if len(ListNodes) != 2:
                print("Errore nei nomi")
                continue
            for i in ListNodes:
                if i not in MyGraph.nodes():
                    MyGraph.add_node(i)
            MyGraph.add_edge(ListNodes[1], ListNodes[0])
        pos = nx.spring_layout(MyGraph)
        nx.draw(MyGraph, pos, edge_color='black', width=1, linewidths=1,
                node_size=500, node_color='pink', alpha=0.9,labels={node: node for node in MyGraph.nodes()})
        plt.axis('off')
        plt.show()
    elif x in "Yy":
        LabelEdgeDict=dict()
        while True:
            instr = input("Inserire nomi nodes separati da una virgola o stop: ")
            if instr in "stopSTOP":
                break
            ListNodes = list(instr.split(","))
            if len(ListNodes) != 3:
                print("Errore nei nomi")
                continue
            for i in ListNodes:
                if i not in MyGraph.nodes() and ListNodes.index(i) != 1:
                    MyGraph.add_node(i)
            MyGraph.add_edge(ListNodes[0], ListNodes[2])
            LabelEdgeDict[ListNodes[0], ListNodes[2]] = ListNodes[1]
        pos = nx.spring_layout(MyGraph)
        nx.draw(MyGraph, pos, edge_color='black', width=1, linewidths=1,
                node_size=500, node_color='pink', alpha=0.9, labels={node: node for node in MyGraph.nodes()})
        nx.draw_networkx_edge_labels(MyGraph, pos, edge_labels=LabelEdgeDict, font_color='red')

        plt.axis('off')
        plt.show()
    else:
        print("Errore.")


