# I'm a stub for the neo4j connection
from src import memory_node
from src import memory_interface


class Neo4j(object):
    def create_node(self, node: memory_node.MemoryNodeModel):
        print(node.__str__())
        return None

    def get_node_by_id(self, id_, memory: memory_interface.MemoryInterface):
        pass

    def update_node(self,node: memory_node.MemoryNodeModel):
        pass

    def delete(self, node: memory_node.MemoryNodeModel):
        pass
