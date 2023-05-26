import os

from flask import Flask, render_template, request
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

from bfs import bfs
from dfs import dfs
from prim import Prim


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('index.html')


@app.route('/display-graph', methods=['GET', 'POST'])
def weightGraph():
    if request.method == 'POST':
        num_nodes = int(request.form['num_nodes'])
        adj_matrix = np.zeros((num_nodes, num_nodes), dtype=int)
        for i in range(num_nodes):
            for j in range(num_nodes):
                adj_matrix[i][j] = int(request.form[f'adj_matrix_{i}_{j}'])

        graph = nx.DiGraph(adj_matrix)
        img_folder = "C:\\Users\\lenovo\\Desktop\\TG GUI Flask\\static\\img"
        # delete existing images in folder
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
        plt.ion()
        plt.show()
        plt.savefig(os.path.join(img_folder, 'graph.png'), format='png')
        return render_template('DisplayGraph.html')
    else:
        return render_template('DisplayGraph.html')


@app.route('/graph', methods=['GET', 'POST'])
def graph():
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

        print("prim", prim_result)

        dfs_result = list(map(str, dfs(graph, start_node))
                          ) if dfs(graph, start_node) else None
        bfs_result = list(map(str, bfs(graph, start_node))
                          ) if bfs(graph, start_node) else None

        img_folder = "C:\\Users\\lenovo\\Desktop\\TG GUI Flask\\static\\img"
        # delete existing images in folder
        for filename in os.listdir(img_folder):
            file_path = os.path.join(img_folder, filename)
            os.unlink(file_path)

        fig = plt.figure(1)
        fig.clf()
        plt.title('Graph')

        # Draw the graph with edge labels
        pos = nx.spring_layout(graph)
        edge_labels = nx.get_edge_attributes(graph, 'weight')
        nx.draw(graph, pos, with_labels=True, node_color='lightblue',
                node_size=500, font_size=10, font_weight='bold')
        nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels)

        plt.ion()
        plt.show()

        plt.savefig(os.path.join(img_folder, 'graph.png'), format='png')

        fig = plt.figure(2)
        fig.clf()
        plt.title('Prim\'s Graph')
        prim_graph = nx.DiGraph()
        prim_graph.add_edges_from(prim_result.keys())
        pos = nx.spring_layout(prim_graph)
        labels = nx.get_edge_attributes(prim_graph, 'weight')
        nx.draw(prim_graph, pos, with_labels=True)
        nx.draw_networkx_edge_labels(prim_graph, pos, edge_labels=labels)
        plt.savefig(os.path.join(img_folder, 'prim_graph.png'), format='png')

        # fig = plt.figure(1)
        # fig.clf()
        # plt.title('Graph')
        # nx.draw(graph, with_labels=True)
        # plt.savefig(os.path.join(img_folder, 'graph.png'), format='png')

        return render_template('result.html', bfs_result=bfs_result, dfs_result=dfs_result, prim_result=prim_result)
    else:
        return render_template('graph.html')


if __name__ == '__main__':
    app.run(debug=True)
