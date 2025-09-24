import pandas as pd
import pyarrow as pa
import numpy as np

# Замените этот ID на ID вашего файла с Google Drive
FILE_ID = "1yQeGe-12L8FFZ-cdwGnRZm_LrzdKrN4J"
file_url = f"https://drive.google.com/uc?id={FILE_ID}"

# Словарь для явного указания типов данных для каждой колонки
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

try:
    # Загружаем данные из CSV.
    # Если вы хотите указать типы данных, раскомментируйте 'dtype=dtype_map'.
    raw_data = pd.read_csv(file_url, dtype=dtype_map, on_bad_lines='skip')

    # Выводим первые 10 строк для проверки
    print("Первые 10 строк датафрейма:")
    print(raw_data.head(10))

    # Выводим типы данных
    print("\nТипы данных в датафрейме:")
    print(raw_data.dtypes)

    # Сохраняем датафрейм в формат Parquet
    raw_data.to_parquet('data.parquet', index=False)
    print("\nДатафрейм успешно сохранен в файл data.parquet")

except Exception as e:
    print(f"Произошла ошибка: {e}")
