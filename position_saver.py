cities_positions = {
    'Lisboa': (-9.1393, 38.7223),
    'Cadiz': (-6.2921, 36.5298),
    'Madrid': (-3.7038, 40.4168),
    'Barcelona': (2.1734, 41.3851),
    'Pamplona': (-1.6458, 42.8125),
    'Marseille': (5.3698, 43.2965),
    'Paris': (2.3522, 48.8566),
    'Brest': (-4.4861, 48.3904),
    'Dieppe': (1.0792, 49.9252),
    'Zurich': (8.5417, 47.3769),
    'London': (-0.1280, 51.5074),
    'Edinburgh': (-3.1883, 55.9533),
    'Venezia': (12.3155, 45.4408),
    'Roma': (12.4964, 41.9028),
    'Munchen': (11.5819, 48.1351),
    'Frankfurt': (8.6821, 50.1109),
    'Bruxelles': (4.3517, 50.8503),
    'Amsterdam': (4.8975, 52.3779),
    'Essen': (7.0146, 51.4584),
    'Berlin': (13.4050, 52.5200),
    'Wien': (16.3738, 48.2082),
    'Zagrab': (15.9819, 45.8150),
    'Budapest': (19.0402, 47.4979),
    'Brindisi': (17.9253, 40.6368),
    'Palermo': (13.3613, 38.1157),
    'Sarajevo': (18.4131, 43.8563),
    'Athina': (23.7275, 37.9838),
    'Sofia': (23.7275, 42.6977),
    'Smyrna': (27.1428, 38.4192),
    'Constantinople': (28.9795, 41.0082),
    'Bucuresti': (26.1025, 44.4268),
    'Kiev': (30.5238, 50.4501),
    'Warzawa': (21.0122, 52.2297),
    'Sevastopol': (33.5067, 44.6166),
    'Angora': (32.8597, 39.9334),
    'Erzerum': (41.2670, 39.9334),
    'Sochi': (39.7359, 43.5855),
    'Rostov': (39.6916, 47.2357),
    'Kharkov': (36.2304, 49.9935),
    'Moskva': (37.6176, 55.7558),
    'Smolensk': (32.0434, 54.7867),
    'Wilno': (25.2797, 54.6872),
    'Petrograd': (30.3351, 59.9343),
    'Stockholm': (18.0686, 59.3293),
    'Riga': (24.1052, 56.9496),
    'Danzig': (18.6466, 54.3520),
    'Khobenhaven': (12.5683, 55.6761),
}

import pandas as pd

# Créer un DataFrame à partir du dictionnaire
df = pd.DataFrame.from_dict(cities_positions, orient='index', columns=['Longitude', 'Latitude'])

# Sauvegarder le DataFrame dans un fichier CSV
df.to_csv('cities_positions.csv', header=True)

