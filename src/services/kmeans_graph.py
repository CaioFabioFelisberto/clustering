import plotly.express as px
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

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

# 1. Juntando os dados padronizados de volta no DataFrame principal pro Plotly ler liso
df['BPM_Pad'] = X_scaled[:, 0]
df['Energia_Pad'] = X_scaled[:, 1]
df['Agressividade_Pad'] = X_scaled[:, 2]

# 2. Transformando o ID em string. 
# Se deixar como número, o Plotly acha que é uma escala contínua, mas queremos categorias (grupos).
df['Playlist_ID'] = df['Playlist_ID'].astype(str)

# 3. Criando o gráfico 3D interativo bolado
fig = px.scatter_3d(
    df, 
    x='BPM_Pad', 
    y='Energia_Pad', 
    z='Agressividade_Pad',
    color='Playlist_ID',
    hover_name='Música',          # O título da caixinha que aparece no mouse!
    hover_data=['Banda', 'BPM'],  # Outros dados pra aparecerem embaixo
    title='Agrupamento de Metal: K-Means Interativo 🤘',
    color_discrete_sequence=px.colors.qualitative.Vivid
)

if __name__ == "__main__":
    # Renderiza a nave no navegador!
    fig.show()
    # Salva a imagem do gráfico
    # fig.write_image("graficos/cluster_metal.png", width=1920, height=1080, scale=2)