import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

# НАСТРОЙКИ

SURNAME = "krivko"
FILE_ID = "1yQeGe-12L8FFZ-cdwGnRZm_LrzdKrN4J"
file_url = f"https://drive.google.com/uc?id={FILE_ID}"

dtype_map = {
    'Age': 'int64',
    'Gender': 'category',
    'BMI': 'float64',
    'Body_Weight': 'float64',
    'Obesity_Status': 'category',
    'Ethnicity': 'category',
    'Family_History': 'bool',
    'Genetic_Markers': 'int64',
    'Microbiome_Index': 'float64',
    'Autoimmune_Disorders': 'bool',
    'H_Pylori_Status': 'bool',
    'Fecal_Calprotectin': 'int64',
    'Occult_Blood_Test': 'bool',
    'CRP_ESR': 'float64',
    'Endoscopy_Result': 'bool',
    'Colonoscopy_Result': 'bool',
    'Stool_Culture': 'bool',
    'Diet_Type': 'category',
    'Food_Intolerance': 'bool',
    'Smoking_Status': 'bool',
    'Alcohol_Use': 'bool',
    'Stress_Level': 'int64',
    'Physical_Activity': 'int64',
    'Abdominal_Pain': 'bool',
    'Bloating': 'bool',
    'Diarrhea': 'bool',
    'Constipation': 'bool',
    'Rectal_Bleeding': 'bool',
    'Appetite_Loss': 'bool',
    'Weight_Loss': 'bool',
    'Bowel_Habits': 'category',
    'Bowel_Movement_Frequency': 'int64',
    'NSAID_Use': 'bool',
    'Antibiotic_Use': 'bool',
    'PPI_Use': 'bool',
    'Medications': 'bool',
    'Disease_Class': 'category',
}


# ОСНОВНОЙ КОД

try:
    # 1 Загружаем данные
    print("[1/4] Загружаем CSV...")
    df = pd.read_csv(file_url, dtype=dtype_map, on_bad_lines='skip')
    df = df.head(100)
    print(f"Загружено {len(df)} строк")

    # 2 Настраиваем подключение
    print("\n[2/4] Сдача: основная база Homeworks.")
    load_dotenv()  # загружаем переменные из .env
    db_user = os.getenv("DB_USER")
    db_pass = os.getenv("DB_PASSWORD")
    db_host = os.getenv("DB_URL")
    db_port = os.getenv("DB_PORT")
    db_name = os.getenv("DB_ROOT_BASE")

    if not all([db_user, db_pass, db_host, db_port, db_name]):
        raise ValueError("Отсутствуют переменные окружения! Проверь .env файл.")
    conn_str = f"postgresql+psycopg2://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}"

    # 3 Подключаемся
    from sqlalchemy import create_engine
    print("[3/4] Подключаемся к базе...")
    engine = create_engine(conn_str)
    print("Подключение успешно!")

    # 4 Загружаем данные
    print(f"[4/4] Создаём таблицу '{SURNAME}'...")
    df.to_sql(SURNAME, engine, if_exists="replace", index=False, schema="public")
    print("Готово: данные успешно загружены!")

except Exception as e:
    print("Ошибка:", e)
