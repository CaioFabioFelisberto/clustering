import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# 1. Nosso dataset fictício com a nata do peso
dados = {
    'Música': [
        'Master of Puppets', 'One', 'Enter Sandman',  # Thrash/Heavy
        'War Pigs', 'Iron Man', 'Paranoid',           # Heavy/Doom raiz
        'Blood Fire Death', 'A Fine Day to Die', 'Enter the Eternal Fire',  # Black Metal épico
        'Hell Awaits', 'Show no Mercy', 'Postmortem',  # Thrash Metal clássico
        'The Trooper', 'Hallowed Be Thy Name', 'Fear of the Dark',  # New Wave of British Heavy Metal clássico
        'Breaking the Law', 'Painkiller', 'Electric Eye'  # Heavy Metal clássico
    ],
    'Banda': [
        'Metallica', 'Metallica', 'Metallica',
        'Black Sabbath', 'Black Sabbath', 'Black Sabbath',
        'Bathory', 'Bathory', 'Bathory',
        'Slayer', 'Slayer', 'Slayer',
        'Iron Maiden', 'Iron Maiden', 'Iron Maiden',
        'Judas Priest', 'Judas Priest', 'Judas Priest'
    ],
    'BPM': [212, 104, 123, 90, 100, 163, 140, 130, 125, 220, 210, 200, 160, 150, 155, 180, 190, 175],
    'Energia': [95, 70, 85, 60, 65, 80, 90, 85, 88, 92, 90, 95, 85, 80, 75, 88, 90, 85],
    'Agressividade': [90, 80, 75, 55, 60, 65, 98, 95, 100, 85, 90, 88, 80, 75, 70, 85, 90, 80]
}

df = pd.DataFrame(dados)
df.to_csv('data/musicas.csv', index=False)