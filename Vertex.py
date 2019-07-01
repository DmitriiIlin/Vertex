class Vertex:

    def __init__(self, val):
        self.Value = val
  
class SimpleGraph:
	
    def __init__(self, size):
        self.max_vertex = size
        self.m_adjacency = [[0] * size for _ in range(size)]
        self.vertex = [None] * size
        
    def AddVertex(self, v):
        # ваш код добавления новой вершины 
        # с значением value 
        # в свободное место массива vertex
        for every_vertex in range(0,len(self.vertex)):
            if self.vertex[every_vertex]==None:
                new_vertex=Vertex(v)
                self.vertex[every_vertex]=new_vertex
                break
        else:
            pass
        return every_vertex
	
    # здесь и далее, параметры v -- индекс вершины
    # в списке  vertex
    def RemoveVertex(self, v):
        # ваш код удаления вершины со всеми её рёбрами
        if self.vertex[v]==None or v>len(self.vertex)-1:
            pass
        else:
            for evere_edge in range(0,len(self.vertex)):
                self.m_adjacency[v][evere_edge]=0
                self.m_adjacency[evere_edge][v]=0
            self.vertex[v]=None
	
    def IsEdge(self, v1, v2):
        # True если есть ребро между вершинами v1 и v2
        if self.vertex[v1]==None or self.vertex[v2]==None or v1>len(self.vertex)-1 or v2>len(self.vertex)-1:
            pass
        else:     
            if self.m_adjacency[v1][v2]==1 and self.m_adjacency[v2][v1]==1:
                return True
            else:
                return False
    

    def AddEdge(self, v1, v2):
        # добавление ребра между вершинами v1 и v2
        if self.vertex[v1]==None or self.vertex[v2]==None or v1>len(self.vertex)-1 or v2>len(self.vertex)-1:
            pass
        else:   
            self.m_adjacency[v1][v2],self.m_adjacency[v2][v1]=1,1

	
    def RemoveEdge(self, v1, v2):
        # удаление ребра между вершинами v1 и v2
        Edge=self.IsEdge(v1,v2)
        if Edge!=True:
            pass
        else:
            self.m_adjacency[v1][v2],self.m_adjacency[v2][v1]=0,0


        
"""
m=SimpleGraph(5)
vertex_0=m.AddVertex(20)
vertex_1=m.AddVertex(25)
vertex_2=m.AddVertex(35)
vertex_3=m.AddVertex(45)
vertex_4=m.AddVertex(55)
print(m.vertex)
print(m.m_adjacency)
m.AddEdge(0,1)
print(m.m_adjacency)
print(m.IsEdge(0,1))
m.RemoveEdge(0,1)
print(m.IsEdge(0,1))
m.AddEdge(0,1)
print(m.m_adjacency)
print(m.vertex)
m.RemoveVertex(0)
print(m.m_adjacency)
print(m.vertex)
"""