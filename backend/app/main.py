from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import networkx as nx

app = FastAPI()

class Node(BaseModel):
    id: str

class Edge(BaseModel):
    source: str
    target: str

class Pipeline(BaseModel):
    nodes: List[Node]
    edges: List[Edge]

@app.post("/pipelines/parse")
async def parse_pipeline(pipeline: Pipeline):
    G = nx.DiGraph()
    
    for node in pipeline.nodes:
        G.add_node(node.id)
    
    for edge in pipeline.edges:
        G.add_edge(edge.source, edge.target)
    
    return {
        "num_nodes": G.number_of_nodes(),
        "num_edges": G.number_of_edges(),
        "is_dag": nx.is_directed_acyclic_graph(G)
    }