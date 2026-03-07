import pandas as pd

def extract_data(path):
    df = pd.read_csv(path, low_memory=False)

    print("\n📊 Columnas del dataset:")
    print(df.columns)

    print("\n📌 Primeras filas:")
    print(df.head())

    return df