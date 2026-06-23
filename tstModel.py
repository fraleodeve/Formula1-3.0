from model.model import Model

m = Model()
m.buildGraph(1991, 1995)
n, a = m.getDetails()
print(n)
print(a)
