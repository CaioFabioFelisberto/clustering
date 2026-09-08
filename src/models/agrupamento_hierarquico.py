import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from scipy.cluster.hierarchy import linkage, fcluster


df_jogadores = pd.read_csv('data/jogadores.csv')

# 2. Padronização das features (obrigatório pro algoritmo não pender pra escala errada)
X = df_jogadores[['Desarme', 'Passe', 'Velocidade', 'Resistencia']]
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 3. Calculando a Matriz de Linkage (Ward)
linked = linkage(X_scaled, method='ward')

# 4. Cortando a árvore automaticamente
# O 't' representa o limiar (threshold) de distância. Ajustando ele, criamos mais ou menos grupos.
limiar_distancia = 2.5
df_jogadores['Cluster_Hierarquico'] = fcluster(linked, t=limiar_distancia, criterion='distance')

# 5. Exibindo os resultados organizados no terminal
print("🌳 ANÁLISE DE SCOUT HIERÁRQUICO - CLONES TÁTICOS 🌳\n")

clustersUnicos = sorted(df_jogadores['Cluster_Hierarquico'].unique())

for cluster_id in clustersUnicos:
    print(f"--- Grupo / Cluster Tático {cluster_id} ---")
    membros = df_jogadores[df_jogadores['Cluster_Hierarquico'] == cluster_id]
    for _, row in membros.iterrows():
        print(f"⚽ {row['Jogador']} (Desarme: {row['Desarme']} | Passe: {row['Passe']} | Vel: {row['Velocidade']} | Res: {row['Resistencia']})")
    print("\n")