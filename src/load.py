import pandas as pd
import os
from sqlalchemy import create_engine
from contextlib import closing

DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_URL")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_ROOT_BASE")
TABLE_NAME = os.getenv("SURNAME")

# Проверяем наличие всех необходимых переменных при импорте модуля
if not all([DB_USER, DB_PASS, DB_HOST, DB_PORT, DB_NAME, TABLE_NAME]):
    raise EnvironmentError("Отсутствуют необходимые переменные окружения! Проверьте файл .env.")

CONN_STR = f"postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
ENGINE = create_engine(CONN_STR)
TABLE_SCHEMA = 'public'

def load_data(df: pd.DataFrame, output_dir: str = 'data/processed') -> None:
    """
    Выгружает данные в Parquet (полный датасет) и в базу данных (max 100 строк).
    Проводит валидацию выходных параметров.
    """
    os.makedirs(output_dir, exist_ok=True)
    
    # 1. Сохранение в Parquet
    print("Шаг 3.1. Сохранение обработанных данных в Parquet...")
    parquet_path = os.path.join(output_dir, 'processed_data.parquet')
    df.to_parquet(parquet_path, index=False)
    print(f"Полный датасет сохранен в: {parquet_path}")

    # 2. Выгрузка в базу данных
    print(f"Шаг 3.2. Выгрузка в базу данных (Таблица: {TABLE_NAME}, max 100 строк)...")
    
    df_to_db = df.head(100)
    
    if "id" not in df_to_db.columns:
        df_to_db.insert(0, "id", range(1, len(df_to_db) + 1))
    
    try:
        with ENGINE.begin() as conn:
            df_to_db.to_sql(TABLE_NAME, conn, if_exists="replace", index=False, schema=TABLE_SCHEMA)
        print(f"Успешно записано {len(df_to_db)} строк в таблицу '{TABLE_NAME}' в схеме '{TABLE_SCHEMA}'.")
    except Exception as e:
        raise RuntimeError(f"Ошибка при записи в базу данных (проверьте настройки в .env и драйвер psycopg2): {e}")
    
    # 3. Валидация выходных параметров
    print("Шаг 4. Валидация выходных параметров...")
    
    if os.path.exists(parquet_path) and os.path.getsize(parquet_path) > 0:
        print("Проверка Parquet файла: Успешно.")
    else:
        raise FileNotFoundError("Ошибка валидации: Parquet файл не был создан или пуст.")
        
    # Проверка базы данных
    try:
        with closing(ENGINE.connect()) as conn:
            db_count = pd.read_sql(f"SELECT COUNT(*) FROM {TABLE_SCHEMA}.{TABLE_NAME}", conn).iloc[0, 0]
    except Exception as e:
        raise RuntimeError(f"Ошибка при проверке БД: Не удалось считать данные из таблицы '{TABLE_SCHEMA}.{TABLE_NAME}'. Убедитесь, что таблица создана. {e}")
        
    
    if db_count == len(df_to_db) and db_count <= 100:
        print(f"Проверка БД: Записано {db_count} строк. Ограничение (max 100 строк) соблюдено. Успешно.")
    else:
        raise ValueError(f"Ошибка валидации БД: Ожидалось {len(df_to_db)} строк, найдено {db_count}.")

    print("\nETL-процесс завершен.")