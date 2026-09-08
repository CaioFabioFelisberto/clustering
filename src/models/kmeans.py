import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler


df = pd.read_csv('data/musicas.csv')

# 2. Separando só as features numéricas pro algoritmo mastigar
X = df[['BPM', 'Energia', 'Agressividade']]

# 3. Padronização (O Pulo do Gato)
# K-Means usa distância, então precisamos colocar tudo na mesma escala
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 4. Instanciando e treinando o K-Means bolado
# Vamos pedir 4 grupos (K=4) pra ver se ele separa as "vibes"
kmeans = KMeans(n_clusters=4, random_state=42, n_init=10)
df['Playlist_ID'] = kmeans.fit_predict(X_scaled)

# 5. Imprimindo os resultados
print("🤘 PLAYLISTS GERADAS PELA IA 🤘\n")
for playlist in range(4):
    print(f"--- Playlist {playlist+1} ---")
    musicas = df[df['Playlist_ID'] == playlist]
    for index, row in musicas.iterrows():
        print(f"🎵 {row['Música']} ({row['Banda']})")
    print("\n")

