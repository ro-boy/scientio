import pytest, os
from src.scientio.session import Session
from src.scientio.ontology.node import Node
from src.scientio.ontology.ontology import Ontology


def test_init():
    """
    Integration test with a default neo4j instance.
    Should be executed by Travis after setting up neo4j in docker.
    """
    # No default values here, because public.
    address = os.environ['NEO4J_ADDRESS']
    user = os.environ['NEO4J_USERNAME']
    passw = os.environ['NEO4J_PASSWORD']
    ontpath = "../../src/scientio/examples/example_ontology.yml"

    o = Ontology(path_to_yaml=ontpath)
    s = Session(ontology=o, neo4j_address=address,
                neo4j_username=user, neo4j_password=passw)

    # TODO add dummy values
    n = Node()
    n_response = s.create(n)

    assert (n_response is not None)
