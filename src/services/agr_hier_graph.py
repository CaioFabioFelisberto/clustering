import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.preprocessing import StandardScaler

df_jogadores = pd.read_csv('data/jogadores.csv')

# 2. Separando as features e normalizando (Regra de ouro pra IA não pirar)
X = df_jogadores[['Desarme', 'Passe', 'Velocidade', 'Resistencia']]
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 3. Calculando a Matriz de Linkage (Hierarquia Aglomerativa com método de Ward)
# O método de Ward minimiza a variância dentro dos clusters
linked = linkage(X_scaled, method='ward')

# 4. Plotando o Dendrograma da Massa
plt.figure(figsize=(12, 7))
dendrogram(
    linked,
    labels=df_jogadores['Jogador'].values,
    leaf_rotation=45,
    leaf_font_size=10,
)

plt.title('🌳 Dendrograma de Scout: Achando Clones Táticos para o Verdão  Palmeirense 🐷', fontsize=12, fontweight='bold')
plt.xlabel('Jogadores')
plt.ylabel('Distância Euclidiana (Dificuldade de Fusão)')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()

# Salvando a árvore de scout
plt.savefig('graficos/dendrograma_scout.png', dpi=300)
plt.show()