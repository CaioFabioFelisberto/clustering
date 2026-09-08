import pandas as pd

# 1. Simulando logs de uso do sistema (CPU% e Memória%)
# A maioria dos dados fica na faixa normal, mas injetamos alguns picos bizarros (anomalias)
dados_sistema = {
    'Timestamp': [f'12:0{i}' for i in range(30)],
    'CPU_Uso': [15, 18, 12, 20, 16, 95, 19, 17, 14, 18, 98, 15, 16, 17, 85, 15, 18, 12, 20, 16, 95, 19, 17, 14, 18, 98, 15, 16, 17, 85], # Picos em 95, 98, 85
    'RAM_Uso': [40, 42, 41, 39, 40, 92, 42, 41, 40, 39, 95, 41, 40, 42, 90, 40, 42, 41, 39, 40, 92, 42, 41, 40, 39, 95, 41, 40, 42, 90], # Picos em 92, 95, 90
    'GPU_Uso': [30, 32, 31, 29, 30, 88, 32, 31, 30, 29, 90, 31, 30, 32, 85, 30, 32, 31, 29, 30, 88, 32, 31, 30, 29, 90, 31, 30, 32, 85], # Picos em 88, 90, 85
    'Disco_Uso': [50, 52, 51, 49, 50, 80, 52, 51, 50, 49, 82, 51, 50, 52, 78, 50, 52, 51, 49, 50, 80, 52, 51, 50, 49, 82, 51, 50, 52, 78], # Picos em 80, 82, 78
    'Temperatura_CPU': [60, 62, 61, 59, 60, 85, 62, 61, 60, 59, 88, 61, 60, 62, 83, 60, 62, 61, 59, 60, 85, 62, 61, 60, 59, 88, 61, 60, 62, 83], # Picos em 85, 88, 83
    'Temperatura_GPU': [55, 57, 56, 54, 55, 82, 57, 56, 55, 54, 85, 56, 55, 57, 80, 55, 57, 56, 54, 55, 82, 57, 56, 55, 54, 85, 56, 55, 57, 80], # Picos em 82, 85, 80
}

df_sistema = pd.DataFrame(dados_sistema)
# df_sistema.to_csv('data/sistema.csv', index=False)