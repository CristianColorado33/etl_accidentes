from sqlalchemy import create_engine

def get_engine():
    user = "cristiancolorado"
    password = "1234"   # 👈 pon tu contraseña real
    host = "localhost"
    port = "5432"
    database = "etl_accidentes"

    url = f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}"
    
    engine = create_engine(url)
    
    print("✅ Conexión a PostgreSQL lista")
    
    return engine