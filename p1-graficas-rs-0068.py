import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
print("Christian Garcia Jimenez Nc = 0068")
print("Fecha = jueves/05/Noviembre/19/2026 ")
#crearemos nuestra tabla y la guardaremos con pandas
# Tenemos 5 listas de redes sociales con 4 elementos por lista
fb = ['Facebook', 8833, True, 2006] 
twt = ['Twitter', 8575, False, 2008]
ig = ['Instagram', 7575, True, 2010]
wsp = ['Whatsapp', 8828, True, 2009]
tel = ['Telegram', 2992, False, 2010]
lkn = ['Linkdin', 7277, False, 2012]
# Creamo una lista de listas (conformando la tabla)
lista_redes_sociales = [fb, twt, ig, wsp, tel, lkn]
# print(lista_redes_sociales)
# Utilizar pandas para utilizar la tabla (dataframe o marco de datos)
# A cada columna la ponemos nombre
df_redes_sociales = pd.DataFrame(lista_redes_sociales, columns=["nombre", "cantidad", "es_fa", "año"])
print(df_redes_sociales)
# Crear el archivo CSV y lo guarda en CSV
# df_redes_sociales.to_csv("rdes sociales.CSV", index=False)
# Crear grafica de lineas 
# Donde x es nombre en el eje  horizontal
# Donde y es cantidad en el eje vertical
plt.plot(df_redes_sociales["nombre"],df_redes_sociales["cantidad"])
plt.title(" Grafica de redes sociales  Nc = 0068")
plt.xlabel("Nombre de redes")
plt.ylabel("Cantidad de usuarios")
plt.show()
# Creamos una grafica de puntos 
plt.scatter(df_redes_sociales["nombre"],df_redes_sociales["cantidad"])
plt.title("Redes sociales 0068")
plt.xlabel("Las redes")
plt.ylabel("cantidad de usuarios")
plt.show()

# Generar la gráfica de barras
plt.bar(df_redes_sociales["nombre"], df_redes_sociales["cantidad"])
# Personalización con título y etiquetas
plt.title("Redes sociales 0068")
plt.xlabel("Las redes")
plt.ylabel("cantidad de usuarios")
# Mostrar la gráfica con paréntesis ()
plt.show()
# Ordenar Grafica de barras de manera desendente 
# De la mas grande a la pequeña
df_rs_ordenar = df_redes_sociales.sort_values("cantidad", ascending = False)
plt.bar(df_rs_ordenar["nombre"],df_rs_ordenar["cantidad" ])
plt.title("Redes sociales 0068")
plt.xlabel("Las redes")
plt.ylabel("cantidad de usuarios")
plt.show()
# Coloreado la grafica
plt.bar(df_rs_ordenar["nombre"],df_rs_ordenar["cantidad" ],
        color = ["b","g","c","m","y","r"])
plt.title("Redes sociales 0068")
plt.xlabel("Las redes")
plt.ylabel("cantidad de usuarios")
plt.show()
# Grafica de pastel
# plt.pie(df_rs_ordenar["nombre"],df_rs_ordenar["cantidad" ],
plt.pie(df_rs_ordenar["cantidad" ],labels = df_rs_ordenar["nombre"])
plt.title("Redes sociales 0068")
plt.xlabel("Las redes")
plt.ylabel("cantidad de usuarios")
plt.show()