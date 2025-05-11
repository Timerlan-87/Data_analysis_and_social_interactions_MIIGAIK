import networkx as nx
import matplotlib.pyplot as plt # Импортируем для возможной визуализации (опционально)

n = 60  # Количество вершин
p = 0.45 # Вероятность появления ребра между любой парой вершин

print(f"Параметры графа Эрдёша-Реньи:")
print(f"Количество вершин (n): {n}")
print(f"Вероятность ребра (p): {p}")
print("-" * 30)

# Генерация графа в модели Эрдёша-Реньи G(n, p)
G = nx.erdos_renyi_graph(n, p)

print("Граф сгенерирован.")
print(f"Количество вершин в сгенерированном графе: {G.number_of_nodes()}")
print(f"Количество рёбер в сгенерированном графе: {G.number_of_edges()}")
print("-" * 30)

# Вычисление фактической средней степени вершины в сгенерированном графе
num_edges = G.number_of_edges()
num_nodes = G.number_of_nodes() # Это то же самое, что и n

# Вычисляем фактическую среднюю степень
if num_nodes > 0:
    actual_avg_degree = (2 * num_edges) / num_nodes
else:
    actual_avg_degree = 0 # Граф без вершин имеет среднюю степень 0

print(f"Фактическая средняя степень вершины в сгенерированном графе: {actual_avg_degree:.4f}")

# Вычисление теоретической средней степени вершины по формуле
theoretical_avg_degree = (n - 1) * p

print(f"Теоретическая средняя степень вершины по формуле (n-1)*p: {theoretical_avg_degree:.4f}")

# Сравнение результатов
print("-" * 30)
print("Сравнение:")
print(f"Фактическая средняя степень:  {actual_avg_degree:.4f}")
print(f"Теоретическая средняя степень: {theoretical_avg_degree:.4f}")

# Вычисляем разницу для понимания отклонения
difference = abs(actual_avg_degree - theoretical_avg_degree)
print(f"Разница между фактической и теоретической средней степенью: {difference:.4f}")

# Визуализация графа
plt.figure(figsize=(10, 10))
nx.draw(G, with_labels=False, node_size=50, width=0.5, alpha=0.7, edge_color='gray')
plt.title(f"Граф Эрдёша-Реньи G({n}, {p})")
plt.show()