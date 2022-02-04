from diagrams import Cluster, Diagram
from diagrams.aws.compute import ECS
from diagrams.aws.database import RDS
from diagrams.aws.network import Route53
from diagrams.k8s.infra import Node, Master

with Diagram("Minikube local setup diagram", show=False):
    
    with Cluster("Local minicube enviroment"):
        master_node = Master("MasterNode")
        slave_node = Node("SlaveNode")

    master_node >> slave_node