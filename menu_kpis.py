import pandas as pd
from src.db_connection import get_engine
import src.queries as q


def ejecutar_query(engine, query):

    df = pd.read_sql(query, engine)

    print("\n📊 RESULTADO:\n")
    print(df.head(20))


def menu():

    engine = get_engine()

    print("\nℹ️ Datos disponibles entre 2022 y 2026")

    while True:

        print("\n📊 MENÚ DE KPIs")
        print("1. Accidentes por año")
        print("2. Accidentes por municipio")
        print("3. Accidentes por tipo de vehículo")
        print("4. Accidentes por gravedad")
        print("5. Accidentes por rango de años")
        print("6. Top 10 municipios con más accidentes")
        print("7. Accidentes por departamento")
        print("8. Accidentes por marca de vehículo")
        print("0. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            ejecutar_query(engine, q.accidentes_por_anio())

        elif opcion == "2":
            ejecutar_query(engine, q.accidentes_por_municipio())

        elif opcion == "3":
            ejecutar_query(engine, q.accidentes_por_vehiculo())

        elif opcion == "4":
            ejecutar_query(engine, q.accidentes_por_gravedad())

        elif opcion == "5":

            print("\n📅 Rango disponible: 2022 - 2026")

            inicio = input("Año inicial: ")
            fin = input("Año final: ")

            ejecutar_query(engine, q.accidentes_por_rango_anios(inicio, fin))

        elif opcion == "6":
            ejecutar_query(engine, q.top_municipios())

        elif opcion == "7":
            ejecutar_query(engine, q.accidentes_por_departamento())

        elif opcion == "8":
            ejecutar_query(engine, q.accidentes_por_marca())

        elif opcion == "0":
            print("👋 Saliendo...")
            break

        else:
            print("❌ Opción inválida")


if __name__ == "__main__":
    menu()