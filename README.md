# 🚗 Traffic Accidents ETL Project

This project implements an **ETL (Extract, Transform, Load) pipeline** for analyzing traffic accident data using **Python and PostgreSQL**.

The goal is to transform raw data into structured information stored in a **Data Warehouse**, allowing the analysis of traffic accidents through **Key Performance Indicators (KPIs)**.

---

# 📌 Project Objective

The objective of this project is to build a **data pipeline** that allows:

* Extracting accident data from raw data sources
* Cleaning and transforming the information
* Loading the processed data into a **Data Warehouse**
* Performing analysis through **queries and KPIs**

This project applies concepts from:

* Data Engineering
* Data Warehousing
* Dimensional Modeling
* ETL Pipelines

---

# 🏗 Project Architecture

The system follows a classic **ETL architecture**:

Data Source
↓
Extraction (Python)
↓
Transformation (Pandas)
↓
Loading (PostgreSQL)
↓
Data Warehouse
↓
KPIs and Analytical Queries

---

# 🗄 Data Warehouse Model

The project uses a **Star Schema dimensional model**.

### Fact Table

**fact_accidentes**

This table contains the main metrics of the system.

Main variables include:

* accident counts
* references to dimension tables

---

### Dimension Tables

**dim_tiempo**

Allows analysis of accidents by:

* hour
* day
* month
* year

---

**dim_vehiculo**

Describes vehicle characteristics such as:

* vehicle type
* brand
* model
* vehicle age

---

**dim_ubicacion**

Contains geographical information:

* department
* municipality
* location attributes

---

**dim_gravedad**

Classifies accidents based on their severity.

---

# 📊 KPIs Analyzed

The system allows the analysis of several indicators, including:

* Number of accidents by **vehicle type**
* Accidents by **vehicle brand**
* Accidents by **location**
* Accidents by **severity level**
* Accident trends over time

These indicators help identify **patterns and risk factors related to traffic accidents**.

---

# 🧰 Technologies Used

* Python
* Pandas
* SQLAlchemy
* PostgreSQL
* Jupyter Notebook

---

# 📁 Project Structure

etl_accidentes/

data/
Raw data files

notebooks/
Exploratory analysis and visualizations

src/
ETL scripts and SQL queries

main.py
Main script to execute the ETL pipeline

requirements.txt
Project dependencies

README.md
Project documentation

.gitignore
Ignored files for Git

venv/
Python virtual environment

---

# ⚙ Installation

Clone the repository:

git clone https://github.com/CristianColorado33/etl_accidentes.git

Move into the project directory:

cd etl_accidentes

Create a virtual environment:

python3 -m venv venv

Activate the virtual environment:

Mac / Linux

source venv/bin/activate

Install dependencies:

pip install -r requirements.txt

---

# ▶ Running the Project

To execute the main ETL pipeline:

python3 main.py

If the project includes an interactive KPI menu:

python3 -m src.menu_kpis

---

# 🔄 ETL Process

### 1️⃣ Extract

Data is extracted from files located in the:

data/

directory.

---

### 2️⃣ Transform

Data cleaning and transformation steps include:

* removing duplicates
* handling missing values
* normalizing variables
* preparing the data for the dimensional model

---

### 3️⃣ Load

The transformed data is loaded into a **PostgreSQL Data Warehouse**, creating the following tables:

* dim_tiempo
* dim_vehiculo
* dim_ubicacion
* dim_gravedad
* fact_accidentes

---

# 📈 Example KPI Query

Example query to analyze accidents by vehicle type:

SELECT v.tipo_vehiculo, SUM(f.cantidad) AS total_accidents
FROM dw.fact_accidentes f
JOIN dw.dim_vehiculo v
ON f.vehiculo_id = v.vehiculo_id
GROUP BY v.tipo_vehiculo
ORDER BY total_accidents DESC;

---

# 👨‍💻 Author

**Cristian Alexis Colorado Muñoz**

Academic project focused on **Data Engineering and Data Analytics**.

---

# 📄 License

This project was developed for **educational and academic purposes**.
