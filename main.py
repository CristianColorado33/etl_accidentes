from src.extract import extract_data
from src.transform import transform_data
from src.load import load_data
from src.db_connection import get_connection

def run_etl():

    path = "data/accidentes.csv"

    df = extract_data(path)

    df = transform_data(df)

    engine = get_connection()

    if engine is None:
        print("❌ No hay conexión a la base de datos")
        return

    load_data(df, engine)


if __name__ == "__main__":
    run_etl()