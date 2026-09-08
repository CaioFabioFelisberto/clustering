import pandas as pd

# 1. Dataset de Jogadores (Atributos de 0 a 100)
dados_jogadores = {
    'Jogador': [
        'Aníbal Moreno (Volante Raiz)', 'Zé Rafael (Motor do Time)', 'Richard Ríos (Dinâmico)', # Palmeiras
        'Matheus Bilong (Camisa 10)', 'Larson (Camisa 8)', 'Luis Pacheco (Camisa 5)', # As apostas
        'Rodri (Manchester City)', 'Kante (Estilo Corredor)', 'De Bruyne (Jogador de Alta Classe)', # Os monstros europeus
        'Jorginho (Passador)', 'Andreas Pereira (Terceiro MC)', 'Marlon Freitas (Lançador)', # Ousadia Brasileira
        'Lucas Evangelitas (Volante esforçado)', 'Emiliano Martinez (Volante comum)', 'Facundo Torres (Camisa 10)' # Jogadores comuns
    ],
    'Desarme': [90, 85, 78, 88, 86, 82, 94, 80, 92, 95, 70, 75, 68, 60, 65],
    'Passe': [82, 85, 88, 75, 78, 96, 85, 90, 92, 80, 88, 84, 70, 75, 78],
    'Velocidade': [75, 78, 85, 80, 89, 74, 88, 92, 90, 70, 75, 80, 85, 78, 82],
    'Resistencia': [95, 90, 88, 92, 94, 91, 98, 85, 90, 87, 80, 75, 78, 82, 88]
}
df_jogadores = pd.DataFrame(dados_jogadores)
df_jogadores.to_csv('data/jogadores.csv', index=False)