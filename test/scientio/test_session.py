import os
import unittest
from session import Session
from ontology.node import Node
from ontology.ontology import Ontology

class Test(unittest.TestCase):
    def test_init(self):
        """
        Integration test with a default neo4j instance.
        Should be executed by Travis after setting up neo4j in docker.
        """

        # Default values are neo4j defaults.
        address = os.environ.get('NEO4J_ADDRESS', 'localhost:7474')
        user = os.environ.get('NEO4J_USERNAME', 'neo4j')
        passw = os.environ.get('NEO4J_PASSWORD', 'neo4j')
        ontpath = "examples/example_ontology.yaml"

        o = Ontology(path_to_yaml=str(ontpath))
        s = Session(ontology=o, neo4j_address=address,
                    neo4j_username=user, neo4j_password=passw)

        # TODO add dummy values
        n = Node(metatype=o.get_type('Person'))
        n.set_name('Test')
        n_response = s.create(n)

        assert (n_response is not None)
