from ..db.index import db
import matplotlib.pyplot as pl

df = db()

def plot():
    pl.figure(figsize=(10, 10))  
    pl.scatter(df['nombre'], df['puntos'], color='green', marker='o')  

    
    for i, row in df.iterrows():
        pl.text(row['nombre'], row['puntos'], str(row['puntos']), fontsize=10, ha='center', va='bottom')

    
    pl.xlabel('Nombre de los jugadores')
    pl.ylabel('Puntos')
    pl.title('Grafico puntos por jugador')

    
    pl.xticks(rotation=35)  
    pl.tight_layout()
    pl.show()