from sqlalchemy import text

def load_data(df, engine):

    with engine.connect() as conn:
        conn.execute(text("CREATE SCHEMA IF NOT EXISTS dw;"))

    # 🔹 DIM TIEMPO
    dim_tiempo = df[['FECHA_ACCIDENTE', 'anio', 'mes', 'dia', 'hora', 'grupo_horario']].drop_duplicates()
    dim_tiempo.columns = ['fecha', 'anio', 'mes', 'dia', 'hora', 'grupo_horario']
    dim_tiempo.insert(0, 'tiempo_id', range(1, len(dim_tiempo)+1))

    # 🔹 DIM UBICACIÓN
    dim_ubicacion = df[['DEPARTAMENTO_ACCIDENTE', 'MUNICIPIO_ACCIDENTE']].drop_duplicates()
    dim_ubicacion.columns = ['departamento', 'municipio']
    dim_ubicacion.insert(0, 'ubicacion_id', range(1, len(dim_ubicacion)+1))

    # 🔹 DIM VEHÍCULO
    dim_vehiculo = df[['TIPO_VEHICULO', 'MARCA_VEHICULO', 'MODELO_VEHICULO', 'EDAD_VEHICULO']].drop_duplicates()
    dim_vehiculo.columns = ['tipo_vehiculo', 'marca', 'modelo', 'edad']
    dim_vehiculo.insert(0, 'vehiculo_id', range(1, len(dim_vehiculo)+1))

    # 🔹 DIM GRAVEDAD
    dim_gravedad = df[['GRAVEDAD_ACCIDENTE']].drop_duplicates()
    dim_gravedad.columns = ['gravedad']
    dim_gravedad.insert(0, 'gravedad_id', range(1, len(dim_gravedad)+1))

    # 🔹 CARGA DIMENSIONES
    dim_tiempo.to_sql('dim_tiempo', con=engine, schema='dw', if_exists='replace', index=False)
    dim_ubicacion.to_sql('dim_ubicacion', con=engine, schema='dw', if_exists='replace', index=False)
    dim_vehiculo.to_sql('dim_vehiculo', con=engine, schema='dw', if_exists='replace', index=False)
    dim_gravedad.to_sql('dim_gravedad', con=engine, schema='dw', if_exists='replace', index=False)

    print("✅ Dimensiones cargadas")

    # 🔹 MERGE PARA FACT TABLE
    fact = df.merge(dim_tiempo, left_on='FECHA_ACCIDENTE', right_on='fecha')
    fact = fact.merge(dim_ubicacion, left_on=['DEPARTAMENTO_ACCIDENTE', 'MUNICIPIO_ACCIDENTE'], right_on=['departamento', 'municipio'])
    fact = fact.merge(dim_vehiculo, left_on=['TIPO_VEHICULO', 'MARCA_VEHICULO', 'MODELO_VEHICULO', 'EDAD_VEHICULO'], right_on=['tipo_vehiculo', 'marca', 'modelo', 'edad'])
    fact = fact.merge(dim_gravedad, left_on='GRAVEDAD_ACCIDENTE', right_on='gravedad')

    fact_table = fact[['tiempo_id', 'ubicacion_id', 'vehiculo_id', 'gravedad_id']].copy()
    fact_table['cantidad'] = 1

    fact_table.to_sql('fact_accidentes', con=engine, schema='dw', if_exists='replace', index=False)

    print("✅ Tabla de hechos cargada")