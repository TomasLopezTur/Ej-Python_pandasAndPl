import pandas as pd

def db():
    df = pd.read_csv('D:\Estudio_Program\Fab-lab-vla\AI\Clases-IA_9-8\Ej\ej_nba\db/nba.csv')

    """ df.loc[df['nombre'] == 'malone', 'nombre'] = 'karl malone' """

    name = df[df['nombre'] == 'malone'].index[0] 
    df.at[name, 'nombre'] = 'karl malone'

    return df