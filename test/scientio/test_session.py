import pytest, os, pathlib
from src.scientio.session import Session
from src.scientio.ontology.node import Node
from src.scientio.ontology.ontology import Ontology


def test_init():
    """
    Integration test with a default neo4j instance.
    Should be executed by Travis after setting up neo4j in docker.
    """

    # Default values are neo4j defaults.
    address = os.environ.get('NEO4J_ADDRESS', 'localhost:7474')
    user = os.environ.get('NEO4J_USERNAME', 'neo4j')
    passw = os.environ.get('NEO4J_PASSWORD', 'neo4j')
    ontpath = "src/scientio/examples/example_ontology.yaml"

    o = Ontology(path_to_yaml=str(ontpath))
    s = Session(ontology=o, neo4j_address=address,
                neo4j_username=user, neo4j_password=passw)

    # TODO add dummy values
    n = Node()
    n_response = s.create(n)

    assert (n_response is not None)
