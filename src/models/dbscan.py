import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import DBSCAN

df_sistema = pd.read_csv('data/sistema.csv')

# 2. Separando as features e normalizando (Lei universal do Machine Learning)
X = df_sistema[['CPU_Uso', 'RAM_Uso','GPU_Uso','Disco_Uso','Temperatura_CPU','Temperatura_GPU']]
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 3. Aplicando o DBSCAN bolado
# eps: tamanho da vizinhança | min_samples: quantos pontos formam um cluster denso
dbscan = DBSCAN(eps=0.4, min_samples=3)
df_sistema['Cluster'] = dbscan.fit_predict(X_scaled)

# 4. Analisando os resultados (O rótulo -1 significa que a IA achou um Outlier!)
print("💻 RADAR DE ANOMALIAS - DBSCAN EM AÇÃO 💻\n")

anomalias = df_sistema[df_sistema['Cluster'] == -1]
normais = df_sistema[df_sistema['Cluster'] != -1]

print(f"🟢 Status do Sistema: {len(normais)} registros dentro do comportamento normal.")
print(f"🚨 Alerta de Anomalias Detectadas: {len(anomalias)} picos suspeitos encontrados!\n")

for _, row in anomalias.iterrows():
    print(f"⚠️ [ANOMALIA] Horário: {row['Timestamp']} | CPU: {row['CPU_Uso']}% | RAM: {row['RAM_Uso']}%")