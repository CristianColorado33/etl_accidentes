import pandas as pd

# 1️⃣ Accidentes por año
def accidentes_por_anio():
    query = """
    SELECT t.anio, SUM(f.cantidad) AS total
    FROM dw.fact_accidentes f
    JOIN dw.dim_tiempo t ON f.tiempo_id = t.tiempo_id
    GROUP BY t.anio
    ORDER BY t.anio;
    """
    return query


# 2️⃣ Accidentes por municipio
def accidentes_por_municipio():
    query = """
    SELECT u.municipio, SUM(f.cantidad) AS total
    FROM dw.fact_accidentes f
    JOIN dw.dim_ubicacion u ON f.ubicacion_id = u.ubicacion_id
    GROUP BY u.municipio
    ORDER BY total DESC;
    """
    return query


# 3️⃣ Accidentes por tipo de vehículo
def accidentes_por_vehiculo():
    query = """
    SELECT v.tipo_vehiculo, SUM(f.cantidad) AS total
    FROM dw.fact_accidentes f
    JOIN dw.dim_vehiculo v ON f.vehiculo_id = v.vehiculo_id
    GROUP BY v.tipo_vehiculo
    ORDER BY total DESC;
    """
    return query


# 4️⃣ Accidentes por gravedad
def accidentes_por_gravedad():
    query = """
    SELECT g.gravedad, SUM(f.cantidad) AS total
    FROM dw.fact_accidentes f
    JOIN dw.dim_gravedad g ON f.gravedad_id = g.gravedad_id
    GROUP BY g.gravedad
    ORDER BY total DESC;
    """
    return query


# 5️⃣ Accidentes por rango de años
def accidentes_por_rango_anios(inicio, fin):
    query = f"""
    SELECT t.anio, SUM(f.cantidad) AS total
    FROM dw.fact_accidentes f
    JOIN dw.dim_tiempo t ON f.tiempo_id = t.tiempo_id
    WHERE t.anio BETWEEN {inicio} AND {fin}
    GROUP BY t.anio
    ORDER BY t.anio;
    """
    return query


# 6️⃣ Top 10 municipios
def top_municipios():
    query = """
    SELECT u.municipio, SUM(f.cantidad) AS total
    FROM dw.fact_accidentes f
    JOIN dw.dim_ubicacion u ON f.ubicacion_id = u.ubicacion_id
    GROUP BY u.municipio
    ORDER BY total DESC
    LIMIT 10;
    """
    return query


# 7️⃣ Accidentes por departamento
def accidentes_por_departamento():
    query = """
    SELECT u.departamento, SUM(f.cantidad) AS total
    FROM dw.fact_accidentes f
    JOIN dw.dim_ubicacion u ON f.ubicacion_id = u.ubicacion_id
    GROUP BY u.departamento
    ORDER BY total DESC;
    """
    return query


# 8️⃣ Accidentes por marca de vehículo
def accidentes_por_marca():
    query = """
    SELECT v.marca, SUM(f.cantidad) AS total
    FROM dw.fact_accidentes f
    JOIN dw.dim_vehiculo v ON f.vehiculo_id = v.vehiculo_id
    GROUP BY v.marca
    ORDER BY total DESC;
    """
    return query