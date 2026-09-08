# Estudos de Clusterizacao

Projeto de estudos praticos de aprendizado de maquina nao supervisionado com
Python. Os exemplos aplicam diferentes tecnicas de agrupamento a dados de
musicas, jogadores de futebol e uso de recursos de um sistema.

## Tecnicas estudadas

- **K-Means**: agrupa musicas por BPM, energia e agressividade, gerando
  playlists semelhantes.
- **DBSCAN**: identifica comportamentos normais e anomalias em metricas de
  uso do sistema.
- **Agrupamento hierarquico**: organiza jogadores por atributos de scout e
  gera um dendrograma para visualizar a distancia entre os perfis.

Todos os exemplos padronizam as variaveis numericas antes do agrupamento,
evitando que uma feature domine as demais por estar em uma escala diferente.

## Estrutura

```text
clusterizacao/
|-- data/
|   |-- jogadores.csv
|   |-- musicas.csv
|   `-- sistema.csv
|-- graficos/
|-- src/
|   |-- models/
|   |   |-- agrupamento_hierarquico.py
|   |   |-- dbscan.py
|   |   `-- kmeans.py
|   `-- services/
|       |-- agr_hier_graph.py
|       `-- kmeans_graph.py
|-- utils/
|   |-- agr_hier_data.py
|   |-- dbscan_data.py
|   `-- kmeans_data.py
|-- requirements.txt
`-- README.md
```

Os scripts em `utils/` recriam os datasets ficticios. Os scripts em
`src/models/` executam os algoritmos e exibem os resultados no terminal. Os
scripts em `src/services/` geram visualizacoes.

## Requisitos

- Python 3.12 ou superior
- pip

As dependencias estao fixadas em `requirements.txt`, incluindo pandas,
scikit-learn, SciPy, Matplotlib e Plotly.

## Instalacao

No diretorio raiz do projeto, crie e ative um ambiente virtual:

### Windows (PowerShell)

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

Caso o ambiente `.venv` ja exista, basta ativa-lo e instalar as dependencias.

## Como executar

Execute os comandos a partir da raiz do projeto, pois os scripts usam caminhos
relativos para acessar a pasta `data/`.

### K-Means: playlists

```powershell
python src\models\kmeans.py
```

### DBSCAN: deteccao de anomalias

```powershell
python src\models\dbscan.py
```

O DBSCAN usa o rotulo `-1` para registros classificados como anomalias.

### Agrupamento hierarquico: perfis de jogadores

```powershell
python src\models\agrupamento_hierarquico.py
```

### Grafico 3D do K-Means

```powershell
python src\services\kmeans_graph.py
```

Esse comando abre um grafico 3D interativo no navegador.

### Dendrograma

```powershell
python src\services\agr_hier_graph.py
```

O dendrograma e salvo em `graficos/dendrograma_scout.png` e tambem exibido
em uma janela do Matplotlib.

## Recriando os dados

Para recriar os datasets de musicas e jogadores:

```powershell
python utils\kmeans_data.py
python utils\agr_hier_data.py
```

O script `utils\dbscan_data.py` contem a geracao do dataset de sistema em
memoria como material de estudo; a linha que exportaria `data/sistema.csv`
esta desativada. O arquivo CSV usado pelo modelo ja esta versionado no
diretorio `data/`.

## Objetivos de estudo

- Entender a importancia da padronizacao de features.
- Comparar agrupamentos baseados em centroides, densidade e hierarquia.
- Interpretar clusters e outliers em dados ficticios.
- Explorar visualizacoes para avaliar os resultados dos algoritmos.
