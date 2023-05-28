from algorithms.prim import Prim
from algorithms.dfs import dfs
from algorithms.bfs import bfs
from algorithms.kosaraju import kosaraju
import os

from flask import Flask, render_template, request
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')


app = Flask(__name__)

#  PLEASE CHANGE THE PATH SO IT SUITS YOUR LOCAL ENV
img_folder = "C:\\Users\\lenovo\\Desktop\\Graph_Theory_Interface\\static\\img"


@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('index.html')


@app.route('/explanation', methods=['GET', 'POST'])
def explanation():
    return render_template('Explanation.html')


@app.route('/display-graph', methods=['GET', 'POST'])
def displayGraph():
    if request.method == 'POST':
        num_nodes = int(request.form['num_nodes'])
        adj_matrix = np.zeros((num_nodes, num_nodes), dtype=int)
        for i in range(num_nodes):
            for j in range(num_nodes):
                adj_matrix[i][j] = int(request.form[f'adj_matrix_{i}_{j}'])

        graph = nx.DiGraph(adj_matrix)

        for filename in os.listdir(img_folder):
            file_path = os.path.join(img_folder, filename)
            os.unlink(file_path)

        fig = plt.figure(1)
        fig.clf()
        plt.title('Graph')

        pos = nx.spring_layout(graph)
        edge_labels = nx.get_edge_attributes(graph, 'weight')
        nx.draw(graph, pos, with_labels=True, node_color='lightblue',
                node_size=500, font_size=10, font_weight='bold')
        nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels)

        plt.savefig(os.path.join(img_folder, 'graph.png'), format='png')
        return render_template('DisplayGraph.html', display_result=True)
    else:
        return render_template('DisplayGraph.html', display_result=False)


@app.route('/graph-algorithms/dfs', methods=['GET', 'POST'])
def dfsAlgo():
    if request.method == 'POST':
        num_nodes = int(request.form['num_nodes'])
        adj_matrix = np.zeros((num_nodes, num_nodes), dtype=int)

        for i in range(num_nodes):
            for j in range(num_nodes):
                adj_matrix[i][j] = int(request.form[f'adj_matrix_{i}_{j}'])

        start_node = int(request.form['start_node'])

        graph = nx.DiGraph(adj_matrix)

        dfs_result = list(map(str, dfs(graph, start_node))
                          ) if dfs(graph, start_node) else None

        for filename in os.listdir(img_folder):
            file_path = os.path.join(img_folder, filename)
            os.unlink(file_path)

        fig = plt.figure(1)
        fig.clf()
        plt.title('Graph')

        pos = nx.spring_layout(graph)
        edge_labels = nx.get_edge_attributes(graph, 'weight')
        nx.draw(graph, pos, with_labels=True, node_color='lightblue',
                node_size=500, font_size=10, font_weight='bold')
        nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels)

        plt.savefig(os.path.join(img_folder, 'dfs_graph.png'), format='png')

        return render_template('Dfs.html', dfs_result=dfs_result, display_result=True)
    else:
        return render_template('Dfs.html', display_result=False)


@app.route('/graph-algorithms/bfs', methods=['GET', 'POST'])
def bfsAlgo():
    if request.method == 'POST':
        num_nodes = int(request.form['num_nodes'])
        adj_matrix = np.zeros((num_nodes, num_nodes), dtype=int)

        for i in range(num_nodes):
            for j in range(num_nodes):
                adj_matrix[i][j] = int(request.form[f'adj_matrix_{i}_{j}'])

        start_node = int(request.form['start_node'])

        graph = nx.DiGraph(adj_matrix)

        bfs_result = list(map(str, bfs(graph, start_node))
                          ) if bfs(graph, start_node) else None

        for filename in os.listdir(img_folder):
            file_path = os.path.join(img_folder, filename)
            os.unlink(file_path)

        fig = plt.figure(1)
        fig.clf()
        plt.title('Graph')

        pos = nx.spring_layout(graph)
        edge_labels = nx.get_edge_attributes(graph, 'weight')
        nx.draw(graph, pos, with_labels=True, node_color='lightblue',
                node_size=500, font_size=10, font_weight='bold')
        nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels)

        plt.savefig(os.path.join(img_folder, 'bfs_graph.png'), format='png')

        return render_template('Bfs.html', bfs_result=bfs_result, display_result=True)
    else:
        return render_template('Bfs.html', display_result=False)


@app.route('/graph-algorithms/prim', methods=['GET', 'POST'])
def primAlgo():
    if request.method == 'POST':
        num_nodes = int(request.form['num_nodes'])
        adj_matrix = np.zeros((num_nodes, num_nodes), dtype=int)

        for i in range(num_nodes):
            for j in range(num_nodes):
                adj_matrix[i][j] = int(request.form[f'adj_matrix_{i}_{j}'])

        start_node = int(request.form['start_node'])

        graph = nx.DiGraph(adj_matrix)

        prim = Prim(num_nodes)
        prim.graph = adj_matrix
        prim_result = prim.primMST()

        for filename in os.listdir(img_folder):
            file_path = os.path.join(img_folder, filename)
            os.unlink(file_path)

        fig = plt.figure(1)
        fig.clf()
        plt.title('Graph')

        pos = nx.spring_layout(graph)
        edge_labels = nx.get_edge_attributes(graph, 'weight')
        nx.draw(graph, pos, with_labels=True, node_color='lightblue',
                node_size=500, font_size=10, font_weight='bold')
        nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels)

        plt.savefig(os.path.join(
            img_folder, 'prim_graph_before.png'), format='png')

        fig = plt.figure(2)
        fig.clf()
        plt.title('Prim\'s Graph')
        prim_graph = nx.DiGraph()
        prim_graph.add_edges_from(prim_result.keys())
        pos = nx.spring_layout(prim_graph)
        labels = nx.get_edge_attributes(prim_graph, 'weight')
        nx.draw(prim_graph, pos, with_labels=True)
        nx.draw_networkx_edge_labels(prim_graph, pos, edge_labels=labels)
        plt.savefig(os.path.join(
            img_folder, 'prim_graph_after.png'), format='png')

        return render_template('Prim.html', prim_result=prim_result, display_result=True)
    else:
        return render_template('Prim.html', display_result=False, prim_result={})


@app.route('/graph-algorithms/kosaraju', methods=['GET', 'POST'])
def kosarajuAlgo():
    if request.method == 'POST':
        num_nodes = int(request.form['num_nodes'])
        adj_matrix = np.zeros((num_nodes, num_nodes), dtype=int)

        for i in range(num_nodes):
            for j in range(num_nodes):
                adj_matrix[i][j] = int(request.form[f'adj_matrix_{i}_{j}'])

        graph = nx.DiGraph(adj_matrix)
        start_node = int(request.form['start_node'])

        # Step 1: Convert adjacency matrix to adjacency list
        graph_dict = {node: [] for node in range(num_nodes)}
        for i in range(num_nodes):
            for j in range(num_nodes):
                if adj_matrix[i][j] != 0:
                    graph_dict[i].append(j)

        # Step 2: Apply Kosaraju's algorithm
        kosaraju_result = kosaraju(graph_dict, start_node)
        # kosaraju_result = kosaraju(graph_dict)

        # Step 3: Convert the kosaraju_result to a format suitable for visualization
        component_labels = {}
        for i, component in enumerate(kosaraju_result):
            for node in component:
                component_labels[node] = i

        # Step 4: Visualize the graph with component labels
        for filename in os.listdir(img_folder):
            file_path = os.path.join(img_folder, filename)
            os.unlink(file_path)

        fig = plt.figure(1)
        fig.clf()
        plt.title('Graph')

        pos = nx.spring_layout(graph)
        node_colors = [component_labels[node] for node in graph.nodes()]
        nx.draw(graph, pos, with_labels=True, node_color=node_colors,
                cmap='viridis', node_size=500, font_size=10, font_weight='bold')

        plt.savefig(os.path.join(
            img_folder, 'kosaraju_graph.png'), format='png')

        return render_template('Kosaraju.html', kosaraju_result=kosaraju_result, display_result=True)
    else:
        return render_template('Kosaraju.html', display_result=False)


if __name__ == '__main__':
    app.run(debug=True)
