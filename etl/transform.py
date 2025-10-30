import pandas as pd
from .extract import DTYPE_MAP

def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Выполняет минимальные трансформации, включая обязательное приведение типов, 
    согласно карте DTYPE_MAP.
    """
    print("Шаг 2. Выполнение трансформаций (приведение типов)...")
    
    transformed_df = df.copy()

    try:
        for col, dtype in DTYPE_MAP.items():
            if col in transformed_df.columns:
                try:
                    if dtype == 'category':
                        transformed_df[col] = transformed_df[col].astype('object').astype(dtype) 
                    else:
                        transformed_df[col] = transformed_df[col].astype(dtype)
                except Exception as conv_err:
                    print(f"Предупреждение: Не удалось привести колонку '{col}' к типу {dtype}: {conv_err}")
        print("Типы данных приведены.")
    except Exception as e:
        raise RuntimeError(f"Ошибка при приведении типов: {e}")
    
    return transformed_df