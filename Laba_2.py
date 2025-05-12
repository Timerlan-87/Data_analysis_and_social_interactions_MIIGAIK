import networkx as nx
import matplotlib.pyplot as plt

# Создаем граф вручную
G = nx.Graph()

# Добавим 3 группы:
# 1-15: слабосвязанные (левая сторона — "яма")
# 16-35: сильно связанные (центр — "горбик")
# 36-50: снова слабосвязанные (правая "яма")

# Левая группа (1-15)
for i in range(1, 16):
    G.add_node(i)
    if i > 1:
        G.add_edge(i, i - 1)

# Центральная группа (16-35)
for i in range(16, 36):
    G.add_node(i)
    for j in range(16, i):
        G.add_edge(i, j)

# Свяжем левую и центральную группы
G.add_edge(15, 16)

# Правая группа (36-50)
for i in range(36, 51):
    G.add_node(i)
    if i > 36:
        G.add_edge(i, i - 1)

# Связь центра и правой группы
G.add_edge(35, 36)

# Вычисляем меру центральности в собственных векторах
centrality = nx.eigenvector_centrality_numpy(G)

# Сортируем по узлам
centrality_sorted = [centrality[i] for i in range(1, 51)]

# Печать значений
for i, val in enumerate(centrality_sorted, 1):
    print(f"Узел {i:2d}: {val:.5f}")

# Визуализация центральности
plt.figure(figsize=(10, 4))
plt.plot(range(1, 51), centrality_sorted, marker='o')
plt.title("Центральность собственного вектора для 50 узлов")
plt.xlabel("Индекс узла")
plt.ylabel("Центральность")
plt.grid(True)
plt.show()
