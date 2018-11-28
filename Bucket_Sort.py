import math
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Link_List:
    def __init__(self):
        self.head = None
        self.size = 0

    def insert_node(self,bucket_nodes,index,value):
        current_node = bucket_nodes[index]
        previous_node = Node(None)
        new_node = Node(value)
        
        if current_node.next == None:
            current_node.next = new_node
        else:
            previous_node = current_node
            current_node = current_node.next
            while current_node.next != None and current_node.data < value:
                previous_node = current_node
                current_node = current_node.next
            new_node.next = previous_node.next
            previous_node.next = new_node
            
        
    def print_all(self,bucket_nodes):
        for nodes in bucket_nodes:
            while nodes.next !=None:
                nodes = nodes.next
                print(nodes.data)

    

class Bucket_Sort:
    def __init__(self):
        self.given_list = None;

    def bucketSort(self,given_list):
        self.given_list = given_list;
        bucket_nodes = [Node(i) for i in range(0,10)]
        '''for nodes in bucket_nodes:
            nodes = Link_List()'''

        link_list = Link_List()
        for i in range(0, len(self.given_list)):
            index = math.floor(given_list[i]*10)
            link_list.insert_node(bucket_nodes,index,given_list[i])
            
        link_list.print_all(bucket_nodes)
        

b_sort = Bucket_Sort()
given_list = [.78,.17,.39,.26,.72,.94,.21,.12,.23,.71,.10,.01,.68]
b_sort.bucketSort(given_list)

