import pandas as pd

#Se va a cargar el CSV de salud mental
ruta = r'C:\Users\USER\OneDrive\Escritorio\ActividadesBIT\Datasets'
tabla_1 = pd.read_csv(ruta + '\Salud_Mental_20240728.csv', sep=',', encoding = 'utf-8')
#print(tabla_1)

#Se van a cargar resultados de Análisis de suelos
ruta= ruta = r'C:\Users\USER\OneDrive\Escritorio\ActividadesBIT\Datasets'
tabla_2 = pd.read_csv(ruta + '\Resultados_de_An_lisis_de_Laboratorio_Suelos_en_Colombia_20240728.csv', sep=',', encoding = 'utf-8')
#print(tabla_2)

#Se va a cargar cargar el csv de usuarios de Masterclass de Arte y Oficios
ruta = r'C:\Users\USER\OneDrive\Escritorio\ActividadesBIT\Actividad 1\Datasets'
tabla_3 = pd.read_csv(ruta + '\Caracterizaci_n_usuarios_Master_Class_Escuela_Municipal_de_Artes_y_Oficios_-_EMA_20240728.csv', sep=',', encoding = 'utf-8')
print(tabla_3)
