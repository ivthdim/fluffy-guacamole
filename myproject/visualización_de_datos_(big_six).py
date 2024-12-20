# -*- coding: utf-8 -*-
"""Visualización de datos. (big six).ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1FI10qlZOJxGQgs8IwofQhBh-TdeikYyS

#Limpieza de datos
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df_2015 = pd.read_csv('resultados_premier_league_2015_2016.csv')
df_2016 = pd.read_csv('resultados_premier_league_2016_2017.csv')
df_2017 = pd.read_csv('resultados_premier_league_2017_2018.csv')
df_2018 = pd.read_csv('resultados_premier_league_2018_2019.csv')
df_2019 = pd.read_csv('resultados_premier_league_2019_2020.csv')
df_2020 = pd.read_csv('resultados_premier_league_2020_2021.csv')
df_2021 = pd.read_csv('resultados_premier_league_2021_2022.csv')
df_2022 = pd.read_csv('resultados_premier_league_2022_2023.csv')
df_2023 = pd.read_csv('resultados_premier_league_2023_2024.csv')

df_unido = pd.concat([df_2015,df_2016,df_2017,df_2018,df_2019,df_2020,df_2021,df_2022,df_2023], ignore_index=True)
df_unido

df_unido.to_csv('premier_league_2015_2023.csv', index=False)

df_unido = pd.read_csv('premier_league_2015_2023.csv')

df_unido.info()

"""## Jugar con el formato de fecha y hora."""

import re
def clean_ordinal_suffix(date_str):
    # Eliminar sufijos como 'th', 'st', 'nd', 'rd' y puntos u otros caracteres extraños
    date_str = re.sub(r'(\d+)(st|nd|rd|th)', r'\1', date_str)  # Eliminar sufijos ordinales
    return date_str.replace('.', '').strip()  # Eliminar puntos y espacios extra

# Limpiar la columna 'fecha'
df_unido['fecha_limpia'] = df_unido['Fecha'].apply(clean_ordinal_suffix)

# Convertir la columna limpia a formato de fecha
df_unido['fecha_formato'] = pd.to_datetime(df_unido['fecha_limpia'], format='%A %d %B %Y')

df_unido

df = df_unido.drop(columns=['fecha_limpia'])

df

df['Reloj mod'] = pd.to_datetime(df['Reloj'], format='%I:%M%p')
df['Hora'] = df['Reloj mod'].dt.time
df=df.drop(columns=['Reloj mod'])
df = df.sort_values(by=['fecha_formato', 'Hora'])

df = df.reset_index(drop=True)
df

df['Año'] = df['fecha_formato'].dt.year

"""## Remover NaN de la asistencia"""

df.info()

# Replace commas and convert 'Asistencia' column to numeric, handling NaNs
df['Asistencia'] = pd.to_numeric(df['Asistencia'].str.replace(',', ''), errors='coerce')

df.info()

"""### Primero vamos a ponerle a remplazar los NaN de los años 2020 y 2021 por 0, ya que en ese año no hubo asistencia en los partidos por el COVID"""

año_filtrado = 2020
df_filtrado = df[df['Año'] == año_filtrado]
df_filtrado

df.loc[df['Año'].isin([2020, 2021]), 'Asistencia'] = df.loc[df['Año'].isin([2020, 2021]), 'Asistencia'].fillna(0)

df

año_filtrado = 2021
df_filtrado = df[df['Año'] == año_filtrado]
df_filtrado

"""### Ahora a rellenar los NaN restantes con el promedio de los estadios en sus respectivos años.




"""

df['Estadio'] = df['Estadio'].astype("string")

promedio_asistencia = df.groupby(['Estadio', 'Año'])['Asistencia'].mean().reset_index()
promedio_asistencia

promedio_asistencia.rename(columns={'Asistencia': 'promedio_asistencia'}, inplace=True)
promedio_asistencia

df = df.merge(promedio_asistencia, on=['Estadio', 'Año'], how='left')

df['Estadio'] = df['Estadio'].str.rstrip('.')

df['Asistencia'] = df['Asistencia'].fillna(df['promedio_asistencia'])

df_with_nan = df[df.isna().any(axis=1)]

df_with_nan

df.info()

df.to_csv('Premier_League_20xx.csv', index=False)

df = pd.read_csv('Premier_League_20xx.csv')

df = df.drop(columns=['promedio_asistencia_x'])

df = df.drop(columns=['promedio_asistencia_y'])

df

"""Agregar codigo de distinción a cada equipo local."""

df

df['Codigo'] = pd.factorize(df['Equipo Local'])[0] + 1  # Sumar 1 para que los códigos empiecen en 1

df

"""Agregar columna de ganador"""

def ganador(row):
  if row['Goles Local'] > row['Goles Visitante']:
    return row['Equipo Local']
  elif row['Goles Local'] < row['Goles Visitante']:
    return row['Equipo Visitante']
  else:
    return 'Empate'

df['Ganador'] = df.apply(ganador, axis=1)
df

"""#PLAN"""

big_six = ['Manchester City', 'Manchester United', 'Liverpool', 'Chelsea', 'Arsenal', 'Tottenham Hotspur']

# Filtrar los partidos donde el equipo local o visitante es del Big Six
df_big_six = df[(df['Equipo Local'].isin(big_six)) | (df['Equipo Visitante'].isin(big_six))]

df_big_six

"""Estadisticas Locales"""

local_stats = df_big_six.groupby(['Año', 'Equipo Local']).agg({
    'Goles Local': 'sum',
    'Posesión Local': 'mean',
    'Tiros Locales Total': 'sum',
    'Tiros A Puerta Local': 'sum',
    'Oportunidades Local': 'sum',
    # Añadir más métricas según sea necesario
}).reset_index()


local_stats = local_stats[local_stats['Equipo Local'].isin(big_six)]

local_stats['promedio_tiros_por_gol_local']= local_stats['Tiros Locales Total']/local_stats['Goles Local'] #Cuantos tiros se necesitan para anotar gol en promedio
local_stats['promedio_tiros_puerta_local']= local_stats['Tiros Locales Total']/local_stats['Tiros A Puerta Local'] #Cuantos tiros se necesitan para que el tiro vaya a puerta
local_stats['tasa_de_conversión_local']= (local_stats['Goles Local']/local_stats['Tiros A Puerta Local'])*100 #Efectividad

local_stats_1=local_stats.copy()
local_stats_1.reset_index(drop=True, inplace=True)
local_stats_1

resultados_anuales = pd.DataFrame()

# Itera sobre cada año único en la columna 'Año'
for año in df['Año'].unique():
    # Filtra los partidos del año actual
    partidos_anuales = df[df['Año'] == año]

    # Filtra los partidos ganados por el equipo local
    partidos_ganados_local = partidos_anuales[partidos_anuales['Ganador'] == partidos_anuales['Equipo Local']]

    # Cuenta los partidos ganados por cada equipo local
    ganados_local = partidos_ganados_local['Equipo Local'].value_counts().reset_index()
    ganados_local.columns = ['Equipo', 'partidos_ganados_local']

    # Añade el año a los resultados
    ganados_local['Año'] = año

    # Concatena los resultados
    resultados_anuales = pd.concat([resultados_anuales, ganados_local], ignore_index=True)



df_big_six_gandos = resultados_anuales[(resultados_anuales['Equipo'].isin(big_six))]
df_big_six_gandos.reset_index(drop=True, inplace=True)

df_big_six_gandos

resultados_anuales

local_stats_1

local_stats_1['partidos_ganados_local'] = df_big_six_gandos['partidos_ganados_local']
local_stats_1

from matplotlib import pyplot as plt
import seaborn as sns
def _plot_series(series, series_name, series_index=0):
  palette = list(sns.palettes.mpl_palette('Dark2'))
  xs = series['Año']
  ys = series['partidos_ganados_local']

  plt.plot(xs, ys, label=series_name, color=palette[series_index % len(palette)])

fig, ax = plt.subplots(figsize=(10, 5.2), layout='constrained')
df_sorted = local_stats_1.sort_values('Año', ascending=True)
for i, (series_name, series) in enumerate(df_sorted.groupby('Equipo Local')):
  _plot_series(series, series_name, i)
  fig.legend(title='Equipo Local', bbox_to_anchor=(1, 1), loc='upper left')
sns.despine(fig=fig, ax=ax)
plt.xlabel('Año')
_ = plt.ylabel('Partidos ganados de local')

from matplotlib import pyplot as plt
import seaborn as sns
def _plot_series(series, series_name, series_index=0):
  palette = list(sns.palettes.mpl_palette('Dark2'))
  xs = series['Año']
  ys = series['Goles Local']

  plt.plot(xs, ys, label=series_name, color=palette[series_index % len(palette)])

fig, ax = plt.subplots(figsize=(10, 5.2), layout='constrained')
df_sorted = local_stats_1.sort_values('Año', ascending=True)
for i, (series_name, series) in enumerate(df_sorted.groupby('Equipo Local')):
  _plot_series(series, series_name, i)
  fig.legend(title='Equipo Local', bbox_to_anchor=(1, 1), loc='upper left')
sns.despine(fig=fig, ax=ax)
plt.xlabel('Año')
_ = plt.ylabel('Goles Local')

from matplotlib import pyplot as plt
import seaborn as sns
def _plot_series(series, series_name, series_index=0):
  palette = list(sns.palettes.mpl_palette('Dark2'))
  xs = series['Año']
  ys = series['tasa_de_conversión_local']

  plt.plot(xs, ys, label=series_name, color=palette[series_index % len(palette)])

fig, ax = plt.subplots(figsize=(10, 5.2), layout='constrained')
df_sorted = local_stats_1.sort_values('Año', ascending=True)
for i, (series_name, series) in enumerate(df_sorted.groupby('Equipo Local')):
  _plot_series(series, series_name, i)
  fig.legend(title='Equipo Local', bbox_to_anchor=(1, 1), loc='upper left')
sns.despine(fig=fig, ax=ax)
plt.xlabel('Año')
_ = plt.ylabel('tasa_de_conversión_local')

"""Estadistica Visitante"""

# Para equipos visitantes
away_stats = df_big_six.groupby(['Año', 'Equipo Visitante']).agg({
    'Goles Visitante': 'sum',
    'Posesión Visitante': 'mean',
    'Tiros Visitante Local': 'sum',
    'Tiros A Puerta Visitante': 'sum',
    'Oportunidades Visitante': 'sum',
    # Añadir más métricas según sea necesario
}).reset_index()

away_stats = away_stats[away_stats['Equipo Visitante'].isin(big_six)]

away_stats['promedio_tiros_por_gol_visitante']= away_stats['Tiros Visitante Local']/away_stats['Goles Visitante']
away_stats['promedio_tiros_puerta_visitante']= away_stats['Tiros Visitante Local']/away_stats['Tiros A Puerta Visitante']
away_stats['tasa_de_conversión_visitante']= (away_stats['Goles Visitante']/away_stats['Tiros A Puerta Visitante'])*100

away_stats_1=away_stats.copy()

resultados_anuales_1 = pd.DataFrame()

# Itera sobre cada año único en la columna 'Año'
for año in df['Año'].unique():
    # Filtra los partidos del año actual
    partidos_anuales = df[df['Año'] == año]

    # Filtra los partidos ganados por el equipo local
    partidos_ganados_visitante = partidos_anuales[partidos_anuales['Ganador'] == partidos_anuales['Equipo Local']]

    # Cuenta los partidos ganados por cada equipo local
    ganados_visitante = partidos_ganados_visitante['Equipo Local'].value_counts().reset_index()
    ganados_visitante.columns = ['Equipo', 'partidos_ganados_visitante']

    # Añade el año a los resultados
    ganados_visitante['Año'] = año

    # Concatena los resultados
    resultados_anuales_1 = pd.concat([resultados_anuales_1, ganados_visitante], ignore_index=True)



df_big_six_gandos_visitante = resultados_anuales_1[(resultados_anuales_1['Equipo'].isin(big_six))]
df_big_six_gandos_visitante.reset_index(drop=True, inplace=True)
df_big_six_gandos_visitante

from matplotlib import pyplot as plt
import seaborn as sns
def _plot_series(series, series_name, series_index=0):
  palette = list(sns.palettes.mpl_palette('Dark2'))
  xs = series['Año']
  ys = series['partidos_ganados_visitante']

  plt.plot(xs, ys, label=series_name, color=palette[series_index % len(palette)])

fig, ax = plt.subplots(figsize=(10, 5.2), layout='constrained')
df_sorted = df_big_six_gandos_visitante.sort_values('Año', ascending=True)
for i, (series_name, series) in enumerate(df_sorted.groupby('Equipo')):
  _plot_series(series, series_name, i)
  fig.legend(title='Equipo Visitante', bbox_to_anchor=(1, 1), loc='upper left')
sns.despine(fig=fig, ax=ax)
plt.xlabel('Año')
_ = plt.ylabel('Ganado Visitante')

away_stats_1.reset_index(drop=True, inplace=True)
away_stats_1['partidos_ganados_visitante'] = df_big_six_gandos_visitante['partidos_ganados_visitante']
away_stats_1

from matplotlib import pyplot as plt
import seaborn as sns
def _plot_series(series, series_name, series_index=0):
  palette = list(sns.palettes.mpl_palette('Dark2'))
  xs = series['Año']
  ys = series['Goles Visitante']

  plt.plot(xs, ys, label=series_name, color=palette[series_index % len(palette)])

fig, ax = plt.subplots(figsize=(10, 5.2), layout='constrained')
df_sorted = away_stats_1.sort_values('Año', ascending=True)
for i, (series_name, series) in enumerate(df_sorted.groupby('Equipo Visitante')):
  _plot_series(series, series_name, i)
  fig.legend(title='Equipo Visitante', bbox_to_anchor=(1, 1), loc='upper left')
sns.despine(fig=fig, ax=ax)
plt.xlabel('Año')
_ = plt.ylabel('Goles Visitante')

from matplotlib import pyplot as plt
import seaborn as sns
def _plot_series(series, series_name, series_index=0):
  palette = list(sns.palettes.mpl_palette('Dark2'))
  xs = series['Año']
  ys = series['tasa_de_conversión_visitante']

  plt.plot(xs, ys, label=series_name, color=palette[series_index % len(palette)])

fig, ax = plt.subplots(figsize=(10, 5.2), layout='constrained')
df_sorted = away_stats_1.sort_values('Año', ascending=True)
for i, (series_name, series) in enumerate(df_sorted.groupby('Equipo Visitante')):
  _plot_series(series, series_name, i)
  fig.legend(title='Equipo Visitante', bbox_to_anchor=(1, 1), loc='upper left')
sns.despine(fig=fig, ax=ax)
plt.xlabel('Año')
_ = plt.ylabel('tasa_de_conversión_visitante')

"""Local vs Visitante"""

numerin=[2015,2016,2017,2018,2019,2020,2021,2022,2023]

for numero in numerin:

    season_local = local_stats_1[local_stats_1['Año'] == numero]
    season_visitante= away_stats_1[away_stats_1['Año'] == numero]

    # Gráfico de barras comparando goles y posesión
    fig, ax1 = plt.subplots(figsize=(15, 6))

    season_local.plot(kind='bar', x='Equipo Local', y='Goles Local', ax=ax1, position=0, width=0.2, label='Goles Local', color='b')
    season_visitante.plot(kind='bar', x='Equipo Visitante', y='Goles Visitante', ax=ax1, position=1, width=0.2, label='Goles Visitante', color='r')

    ax1.set_title(f'Comparación de Goles Local y Goles Visitante (Año {numero})')
    ax1.set_ylabel('Goles')

    plt.show()

# Cambiar los nombres de columnas para diferenciarlas

local_stats.columns = ['Año', 'team', 'Goles', 'Posesión', 'Tiros Totales', 'Tiros A Puerta', 'Oportunidades','promedio_tiros','promedio_tiros_puerta','tasa_de_conversión']
away_stats.columns = ['Año', 'team', 'Goles', 'Posesión', 'Tiros Totales', 'Tiros A Puerta', 'Oportunidades','promedio_tiros','promedio_tiros_puerta','tasa_de_conversión']

# Combinar ambas tablas
big_six_stats = pd.concat([local_stats, away_stats])
big_six_stats_season = big_six_stats.groupby(['Año', 'team']).mean().reset_index()

"""Promedio de estadisticas por temporada."""

big_six_stats_season

# Gráfico de líneas para los goles marcados por temporada
plt.figure(figsize=(15, 6))
sns.lineplot(x='Año', y='Goles', hue='team', data=big_six_stats_season, marker='o')
plt.title('Evolución de Goles por Temporada (Big Six)')
plt.xticks(rotation=45)
plt.ylabel('Goles Promedio por Temporada')
plt.show()

# Gráfico de líneas para los goles marcados por temporada
plt.figure(figsize=(15, 6))
sns.lineplot(x='Año', y='tasa_de_conversión', hue='team', data=big_six_stats_season, marker='o')
plt.title('Tasa de conversión (Big Six)')
plt.xticks(rotation=45)
plt.ylabel('Tasa de conversión por Temporada')
plt.show()

año_filtro = [2015,2016,2017,2018,2019,2020,2021,2022,2023]

for año in año_filtro:

    df_filtrado = big_six_stats_season[big_six_stats_season['Año'] == año]

    # Crear un diccionario para asignar colores a cada equipo
    colores = {
        'Arsenal': 'red',
        'Chelsea': 'blue',
        'Liverpool': 'green',
        'Manchester City': 'orange',
        'Manchester United': 'purple',
        'Tottenham Hotspur': 'cyan'
    }

    # Crear la gráfica
    plt.figure(figsize=(10, 5))

    # Graficar cada equipo con su respectivo color
    for equipo, color in colores.items():
        equipo_data = df_filtrado[df_filtrado['team'] == equipo]
        plt.scatter(equipo_data['Oportunidades'], equipo_data['Goles'], s=100, color=color, label=equipo)

    # Etiquetas y título
    plt.title(f'Oportunidades vs Goles en {año}')
    plt.xlabel('Oportunidades Creadas')
    plt.ylabel('Goles')
    plt.xlim(0, 60)  # Limitar el eje X si es necesario
    plt.ylim(0, df_filtrado['Goles'].max()+5 )  # Limitar el eje Y

    # Agregar leyenda
    plt.legend(title='Equipos')

    # Mostrar la gráfica
    plt.grid()
    plt.show()

año_filtro = [2015,2016,2017,2018,2019,2020,2021,2022,2023]

for año in año_filtro:

    df_filtrado = big_six_stats_season[big_six_stats_season['Año'] == año]

    # Crear un diccionario para asignar colores a cada equipo
    colores = {
        'Arsenal': 'red',
        'Chelsea': 'blue',
        'Liverpool': 'green',
        'Manchester City': 'orange',
        'Manchester United': 'purple',
        'Tottenham Hotspur': 'cyan'
    }

    # Crear la gráfica
    plt.figure(figsize=(10, 5))

    # Graficar cada equipo con su respectivo color
    for equipo, color in colores.items():
        equipo_data = df_filtrado[df_filtrado['team'] == equipo]
        plt.scatter(equipo_data['Posesión'], equipo_data['Oportunidades'], s=100, color=color, label=equipo)

    # Etiquetas y título
    plt.title(f'Posesión vs Oportunidades de Equipos en {año}')
    plt.xlabel('Posesión (%)')
    plt.ylabel('Oportunidades Creadas')
    plt.xlim(0, 100)  # Limitar el eje X si es necesario
    plt.ylim(0, df_filtrado['Oportunidades'].max() + 5)  # Limitar el eje Y

    # Agregar leyenda
    plt.legend(title='Equipos')

    # Mostrar la gráfica
    plt.grid()
    plt.show()

año_filtro = [2015,2016,2017,2018,2019,2020,2021,2022,2023]

for año in año_filtro:

    df_filtrado = big_six_stats_season[big_six_stats_season['Año'] == año]

    # Crear un diccionario para asignar colores a cada equipo
    colores = {
        'Arsenal': 'red',
        'Chelsea': 'blue',
        'Liverpool': 'green',
        'Manchester City': 'orange',
        'Manchester United': 'purple',
        'Tottenham Hotspur': 'cyan'
    }

    # Crear la gráfica
    plt.figure(figsize=(10, 5))

    # Graficar cada equipo con su respectivo color
    for equipo, color in colores.items():
        equipo_data = df_filtrado[df_filtrado['team'] == equipo]
        plt.scatter(equipo_data['tasa_de_conversión'], equipo_data['Goles'], s=100, color=color, label=equipo)

    # Etiquetas y título
    plt.title(f'Goles vs Tasa de conversión en {año}')
    plt.xlabel('Tasa de conversión')
    plt.ylabel('Goles')
    plt.xlim(0, 50)  # Limitar el eje X si es necesario
    plt.ylim(0, 70)  # Limitar el eje Y

    # Agregar leyenda
    plt.legend(title='Equipos')

    # Mostrar la gráfica
    plt.grid()
    plt.show()

df

"""Resumen"""

df.head() #dataframe con todos los equipos de la premierleague y todos los partidos

df_big_six.head() #Es el df pero filtrado solo por los big six.

big_six_stats.reset_index(drop=True, inplace=True) #Son temporadas del BIGSIX la primeras 60 sfilas son de local y el resto de visitante.
big_six_stats.info()

big_six_stats_season.head(6) #Agrupa y saca promedios de big_six_stats.

import seaborn as sns
import matplotlib.pyplot as plt

# Distribución de goles marcados por equipos locales
plt.figure(figsize=(10, 6))
sns.histplot(df['Goles Local'], kde=True, bins=10,kde_kws={'bw_adjust': 1.5})
plt.title('Distribución de Goles Marcados por el Equipo Local (Premier League)')
plt.show()

from scipy import stats

#Prueba Kolmogorov pa ver si es una distribución normal

Goles_Local = df['Goles Local']  # Extract the column into a variable

alpha = 0.05 # define el nivel de significancia

stat, p_value = stats.kstest(Goles_Local, 'norm', args=(Goles_Local.mean(), Goles_Local.std()))

print('Estadístico de la prueba:', stat)
print('Valor p:', p_value)


if p_value > alpha:
    print('Los datos parecen seguir una distribución normal (no se rechaza H0)')
else:
    print('Los datos no parecen seguir una distribución normal (se rechaza H0)')

# Distribución de goles marcados por equipos locales
plt.figure(figsize=(10, 6))
sns.histplot(df_big_six['Goles Local'],kde=True, bins=10,kde_kws={'bw_adjust': 1.7} )
plt.title('Distribución de Goles Marcados por el Equipo Local (Big Six)')
plt.show()

#Prueba Kolmogorov pa ver si es una distribución normal

Goles_Local = df_big_six['Goles Local']  # Extract the column into a variable

alpha = 0.05 # define el nivel de significancia

stat, p_value = stats.kstest(Goles_Local, 'norm', args=(Goles_Local.mean(), Goles_Local.std()))

print('Estadístico de la prueba:', stat)
print('Valor p:', p_value)


if p_value > alpha:
    print('Los datos parecen seguir una distribución normal (no se rechaza H0)')
else:
    print('Los datos no parecen seguir una distribución normal (se rechaza H0)')

import seaborn as sns
import matplotlib.pyplot as plt

# Distribución de goles marcados por equipos visitantes
plt.figure(figsize=(10, 6))
sns.histplot(df['Goles Visitante'], kde=True, bins=11,kde_kws={'bw_adjust': 2.1})
plt.title('Distribución de Goles Marcados por el Equipo Visitante (Premier League)')
plt.show()

#Prueba Kolmogorov pa ver si es una distribución normal

Goles_Visitante = df['Goles Visitante']  # Extract the column into a variable

alpha = 0.05 # define el nivel de significancia

stat, p_value = stats.kstest(Goles_Visitante, 'norm', args=(Goles_Visitante.mean(), Goles_Local.std()))

print('Estadístico de la prueba:', stat)
print('Valor p:', p_value)


if p_value > alpha:
    print('Los datos parecen seguir una distribución normal (no se rechaza H0)')
else:
    print('Los datos no parecen seguir una distribución normal (se rechaza H0)')

# Distribución de goles marcados por equipos visitantes
plt.figure(figsize=(10, 6))
sns.histplot(df_big_six['Goles Visitante'], kde=True, bins=10,kde_kws={'bw_adjust': 2.1})
plt.title('Distribución de Goles Marcados por el Equipo Visitante (Big Six)')
plt.show()

#Prueba Kolmogorov pa ver si es una distribución normal

Goles_Visitante = df_big_six['Goles Visitante']  # Extract the column into a variable

alpha = 0.05 # define el nivel de significancia

stat, p_value = stats.kstest(Goles_Visitante, 'norm', args=(Goles_Visitante.mean(), Goles_Local.std()))

print('Estadístico de la prueba:', stat)
print('Valor p:', p_value)


if p_value > alpha:
    print('Los datos parecen seguir una distribución normal (no se rechaza H0)')
else:
    print('Los datos no parecen seguir una distribución normal (se rechaza H0)')

import statsmodels.api as sm
from statsmodels.formula.api import ols

anova_data = df[['Equipo Local', 'Posesión Local']].dropna()


anova_data = anova_data.rename(columns={
    'Equipo Local': 'Equipo_Local',
    'Posesión Local': 'Posesion_Local'
})

model = ols('Posesion_Local ~ C(Equipo_Local)', data=anova_data).fit()
anova_table = sm.stats.anova_lm(model, typ=2)

print(anova_table)

anova_data = df_big_six[['Equipo Local', 'Posesión Local']].dropna()


anova_data = anova_data.rename(columns={
    'Equipo Local': 'Equipo_Local',
    'Posesión Local': 'Posesion_Local'
})

model = ols('Posesion_Local ~ C(Equipo_Local)', data=anova_data).fit()
anova_table = sm.stats.anova_lm(model, typ=2)

print(anova_table)

df.columns

columnas_numericas = df.select_dtypes(include=['float64', 'int64']).columns.tolist()
print(columnas_numericas)

# Correlación entre posesión y goles
correlation = df[columnas_numericas].corr()

plt.figure(figsize=(30, 30))
sns.heatmap(correlation, annot=True, cmap='coolwarm')
plt.title('Matriz de Correlación entre Posesión, Goles y Tiros a Puerta (Equipos Locales)')
plt.show()

# Correlación entre posesión y goles
correlation = df_big_six[columnas_numericas].corr()

plt.figure(figsize=(30, 30))
sns.heatmap(correlation, annot=True, cmap='coolwarm')
plt.title('Matriz de Correlación entre Posesión, Goles y Tiros a Puerta (Equipos Locales)')
plt.show()

# Correlación de estadísticas en Manchester City

for grandes in big_six:

    mc_stats = df[df['Equipo Local'] == grandes][['Goles Local', 'Posesión Local', 'Tiros A Puerta Local', 'Tiros Locales Total','Asistencia']].corr()

    sns.heatmap(mc_stats, annot=True, cmap='coolwarm')
    plt.title(f'Correlación de Métricas en {grandes}')
    plt.show()

from scipy.stats import ttest_ind
ttest_ind(df['Goles Local'], df['Goles Visitante'])

"""Dado que el valor p es mucho menor que 0.05, podemos concluir que hay una diferencia estadísticamente significativa entre los goles anotados por los equipos locales y los visitantes."""

from scipy.stats import ttest_ind
ttest_ind(df_big_six['Goles Local'], df_big_six['Goles Visitante'])

"""Dado que el valor p es mucho menor que 0.05, podemos concluir que hay una diferencia estadísticamente significativa entre los goles anotados por los equipos locales y los visitantes."""

sns.boxplot(data=df_big_six[['Goles Local', 'Goles Visitante']])
plt.title('Distribución de goles: Local vs Visitante')
plt.show()

import pandas as pd
from math import pi
import matplotlib.pyplot as plt
import numpy as np # Import numpy for numerical operations

categories = ['Goles', 'Tiros a puerta', 'Oportunidades','Paradas', 'Amarillas', 'Rojas']
# Ensure all values are numerical using .astype(float) or applying a function if needed
local_values = [
    df['Goles Local'].mean(),
    df['Tiros A Puerta Local'].mean(),
    # Convert 'Oportunidades Local' to numeric, handling potential errors
    pd.to_numeric(df['Oportunidades Local'], errors='coerce').fillna(0).mean(),
    df['Paradas Local'].mean(),
    df['Amarillas Local'].mean(),
    df['Rojas Local'].mean()
    ]
away_values = [
    df['Goles Visitante'].mean(),
    df['Tiros A Puerta Visitante'].mean(),
    # Convert 'Oportunidades Visitante' to numeric, handling potential errors
    pd.to_numeric(df['Oportunidades Visitante'], errors='coerce').fillna(0).mean(),
    df['Paradas Local'].mean(),
    df['Amarillas Visitante'].mean(),
    df['Rojas Visitante'].mean()
]


fig, ax = plt.subplots(figsize=(5, 5), subplot_kw=dict(polar=True))
ax.plot([n for n in range(len(categories))], local_values, label='Local', color='b')
ax.fill([n for n in range(len(categories))], local_values, 'b', alpha=0.1)
ax.plot([n for n in range(len(categories))], away_values, label='Visitante', color='r')
ax.fill([n for n in range(len(categories))], away_values, 'r', alpha=0.1)

plt.title('Comparación de Rendimiento Local vs Visitante')
ax.set_xticks([n for n in range(len(categories))])
ax.set_xticklabels(categories)
plt.legend(loc='lower right')
plt.show()
plt.close()

import pandas as pd
from math import pi
import matplotlib.pyplot as plt
import numpy as np # Import numpy for numerical operations

categories = ['Goles', 'Tiros a puerta', 'Oportunidades','Paradas', 'Amarillas', 'Rojas']
# Ensure all values are numerical using .astype(float) or applying a function if needed
local_values = [
    df_big_six['Goles Local'].mean(),
    df_big_six['Tiros A Puerta Local'].mean(),
    # Convert 'Oportunidades Local' to numeric, handling potential errors
    pd.to_numeric(df_big_six['Oportunidades Local'], errors='coerce').fillna(0).mean(),
    df_big_six['Paradas Local'].mean(),
    df_big_six['Amarillas Local'].mean(),
    df_big_six['Rojas Local'].mean()
    ]
away_values = [
    df_big_six['Goles Visitante'].mean(),
    df_big_six['Tiros A Puerta Visitante'].mean(),
    # Convert 'Oportunidades Visitante' to numeric, handling potential errors
    pd.to_numeric(df['Oportunidades Visitante'], errors='coerce').fillna(0).mean(),
    df_big_six['Paradas Local'].mean(),
    df_big_six['Amarillas Visitante'].mean(),
    df_big_six['Rojas Visitante'].mean()
]


fig, ax = plt.subplots(figsize=(5, 5), subplot_kw=dict(polar=True))
ax.plot([n for n in range(len(categories))], local_values, label='Local', color='b')
ax.fill([n for n in range(len(categories))], local_values, 'b', alpha=0.1)
ax.plot([n for n in range(len(categories))], away_values, label='Visitante', color='r')
ax.fill([n for n in range(len(categories))], away_values, 'r', alpha=0.1)

plt.title('Comparación de Rendimiento Local vs Visitante (Big Six)')
ax.set_xticks([n for n in range(len(categories))])
ax.set_xticklabels(categories)
plt.legend(loc='lower right')
plt.show()
plt.close()

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Equipos del Big Six
big_six
# Categorías a comparar
categories = ['Goles', 'Tiros a puerta', 'Oportunidades','Paradas', 'Amarillas', 'Rojas']

# Crear un diccionario para almacenar los valores de cada equipo
big_six_values = {}

for team in big_six:
    # Filtrar los datos por equipo
    team_data = df[df['Equipo Local'] == team]

    # Calcular las métricas promedio para el equipo
    values = [
        team_data['Goles Local'].mean(),
        team_data['Tiros A Puerta Local'].mean(),
        pd.to_numeric(team_data['Oportunidades Local'], errors='coerce').fillna(0).mean(),
        team_data['Paradas Local'].mean(),
        team_data['Amarillas Local'].mean(),
        team_data['Rojas Local'].mean()
    ]

    big_six_values[team] = values

# Inicializar la figura y los ejes
fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))

# Angulos de las categorías (número de variables)
angles = np.linspace(0, 2 * np.pi, len(categories), endpoint=False).tolist()
angles += angles[:1]  # Completar el círculo

# Graficar para cada equipo del Big Six
for team, values in big_six_values.items():
    values += values[:1]  # Repetir el primer valor para cerrar el gráfico
    ax.plot(angles, values, label=team)
    ax.fill(angles, values, alpha=0.1)  # Relleno de la gráfica

# Configurar etiquetas
ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories)

# Título y leyenda
plt.title('Comparación del Rendimiento de los Equipos del Big Six')
plt.legend(loc='lower right', bbox_to_anchor=(1.1, 0.1))

# Mostrar la gráfica
plt.show()

df_oportunidades_vs_local=df.groupby('Equipo Local').agg({
    'Oportunidades Visitante': 'mean',
    'Tiros A Puerta Visitante': 'mean',
    'Goles Visitante': 'mean',
    'Posesión Visitante': 'mean'
}).reset_index()


df_oportunidades_vs_local

df_oportunidades_vs_visitante=df.groupby('Equipo Visitante').agg({
    'Oportunidades Local': 'mean',
    'Tiros A Puerta Local': 'mean',
    'Goles Local': 'mean',
    'Posesión Local': 'mean'
}).reset_index()
df_oportunidades_vs_visitante

df_oportunidades_vs_local.columns = ['Equipo','Oportunidades','Tiros a Puerta', 'Goles','Posesión']
df_oportunidades_vs_visitante.columns = ['Equipo','Oportunidades','Tiros a Puerta', 'Goles','Posesión']

# Combinar ambas tablas
cuanto_les_generan = pd.concat([df_oportunidades_vs_local, df_oportunidades_vs_visitante])

cuanto_les_generan = cuanto_les_generan.groupby('Equipo').mean().reset_index()

cuanto_les_generan_big_six=cuanto_les_generan[cuanto_les_generan['Equipo'].isin(big_six)].reset_index(drop=True)

cuanto_les_generan_big_six

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Equipos del Big Six
big_six
# Categorías a comparar
categories = ['Oportunidades en contra', 'Tiros a puerta en contra', 'Goles en contra', 'Posesión que cede']

# Crear un diccionario para almacenar los valores de cada equipo
big_six_values = {}

for team in big_six:
    # Filtrar los datos por equipo
    team_data = cuanto_les_generan_big_six[cuanto_les_generan_big_six['Equipo'] == team]

    # Calcular las métricas promedio para el equipo
    values = [
        team_data['Oportunidades'].mean(),
        team_data['Tiros a Puerta'].mean(),
        team_data['Goles'].mean(),
        team_data['Posesión'].mean(),

    ]

    big_six_values[team] = values

# Inicializar la figura y los ejes
fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))

# Angulos de las categorías (número de variables)
angles = np.linspace(0, 2 * np.pi, len(categories), endpoint=False).tolist()
angles += angles[:1]  # Completar el círculo

# Graficar para cada equipo del Big Six
for team, values in big_six_values.items():
    values += values[:1]  # Repetir el primer valor para cerrar el gráfico
    ax.plot(angles, values, label=team)
    ax.fill(angles, values, alpha=0.1)  # Relleno de la gráfica

# Configurar etiquetas
ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories)

# Título y leyenda
plt.title('Comparación del Rendimiento en Defensa de los Equipos del Big Six')
plt.legend(loc='lower right', bbox_to_anchor=(1.1, 0.1))

# Mostrar la gráfica
plt.show()



import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Equipos del Big Six
big_six
# Categorías a comparar
categories = ['Oportunidades en contra', 'Tiros a puerta en contra', 'Goles en contra', ]

# Crear un diccionario para almacenar los valores de cada equipo
big_six_values = {}

for team in big_six:
    # Filtrar los datos por equipo
    team_data = cuanto_les_generan_big_six[cuanto_les_generan_big_six['Equipo'] == team]

    # Calcular las métricas promedio para el equipo
    values = [
        team_data['Oportunidades'].mean(),
        team_data['Tiros a Puerta'].mean(),
        team_data['Goles'].mean()

    ]

    big_six_values[team] = values

# Inicializar la figura y los ejes
fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))

# Angulos de las categorías (número de variables)
angles = np.linspace(0, 2 * np.pi, len(categories), endpoint=False).tolist()
angles += angles[:1]  # Completar el círculo

# Graficar para cada equipo del Big Six
for team, values in big_six_values.items():
    values += values[:1]  # Repetir el primer valor para cerrar el gráfico
    ax.plot(angles, values, label=team)
    ax.fill(angles, values, alpha=0.1)  # Relleno de la gráfica

# Configurar etiquetas
ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories)

# Título y leyenda
plt.title('Comparación del Rendimiento en Defensa de los Equipos del Big Six')
plt.legend(loc='lower right', bbox_to_anchor=(1.1, 0.1))

# Mostrar la gráfica
plt.show()

import seaborn as sns
import matplotlib.pyplot as plt

SoloAlgunosTipos=df[df['Equipo Local'].isin(big_six)]


sns.pairplot(SoloAlgunosTipos[['Goles Local','Posesión Local','Faltas Cometidas Local']])
plt.show()