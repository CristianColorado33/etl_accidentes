import pandas as pd

def transform_data(df):

    # Convertir fecha
    df['FECHA_ACCIDENTE'] = pd.to_datetime(
        df['FECHA_ACCIDENTE'],
        errors='coerce'
    )

    # Crear columnas de tiempo
    df['anio'] = df['FECHA_ACCIDENTE'].dt.year
    df['mes'] = df['FECHA_ACCIDENTE'].dt.month
    df['dia'] = df['FECHA_ACCIDENTE'].dt.day
    df['hora'] = df['FECHA_ACCIDENTE'].dt.hour

    # Grupo horario
    df['grupo_horario'] = pd.cut(
        df['hora'],
        bins=[0, 6, 12, 18, 24],
        labels=['Madrugada', 'Mañana', 'Tarde', 'Noche'],
        right=False
    )

    print("✅ Transformación completa")

    return df