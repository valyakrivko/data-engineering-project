import pandas as pd
import pandera as pa
from pandera import DataFrameModel 
from pandera.typing import Series
import os

# Карта типов
DTYPE_MAP = {
    'Age': 'int64', 'Gender': 'category', 'BMI': 'float64', 'Body_Weight': 'float64',
    'Obesity_Status': 'category', 'Ethnicity': 'category', 'Family_History': 'bool',
    'Genetic_Markers': 'int64', 'Microbiome_Index': 'float64', 'Autoimmune_Disorders': 'bool',
    'H_Pylori_Status': 'bool', 'Fecal_Calprotectin': 'int64', 'Occult_Blood_Test': 'bool',
    'CRP_ESR': 'float64', 'Endoscopy_Result': 'bool', 'Colonoscopy_Result': 'bool',
    'Stool_Culture': 'bool', 'Diet_Type': 'category', 'Food_Intolerance': 'bool',
    'Smoking_Status': 'bool', 'Alcohol_Use': 'bool', 'Stress_Level': 'int64',
    'Physical_Activity': 'int64', 'Abdominal_Pain': 'bool', 'Bloating': 'bool',
    'Diarrhea': 'bool', 'Constipation': 'bool', 'Rectal_Bleeding': 'bool',
    'Appetite_Loss': 'bool', 'Weight_Loss': 'bool', 'Bowel_Habits': 'category',
    'Bowel_Movement_Frequency': 'int64', 'NSAID_Use': 'bool', 'Antibiotic_Use': 'bool',
    'PPI_Use': 'bool', 'Medications': 'bool', 'Disease_Class': 'category',
}

# Схема Pandera: проверка всех 37 столбцов
class RawDataSchema(DataFrameModel):
    # Числовые колонки с ограничениями
    Age: Series[int] = pa.Field(ge=0) 
    BMI: Series[float] = pa.Field(ge=5.0) 
    Body_Weight: Series[float] = pa.Field(ge=2.0)
    Genetic_Markers: Series[int] = pa.Field(ge=0)
    Microbiome_Index: Series[float] = pa.Field(ge=0.0, le=1.0)
    Fecal_Calprotectin: Series[int] = pa.Field(ge=0)
    CRP_ESR: Series[float] = pa.Field(ge=0.0)
    Stress_Level: Series[int] = pa.Field(ge=1, le=10)
    Physical_Activity: Series[int] = pa.Field(ge=0)
    Bowel_Movement_Frequency: Series[int] = pa.Field(ge=0)

    # Категориальные колонки
    Gender: Series[str] = pa.Field(nullable=True)
    Obesity_Status: Series[str] = pa.Field(nullable=True)
    Ethnicity: Series[str] = pa.Field(nullable=True)
    Diet_Type: Series[str] = pa.Field(nullable=True)
    Bowel_Habits: Series[str] = pa.Field(nullable=True)
    Disease_Class: Series[str] = pa.Field(nullable=True)

    # Bool колонки
    Family_History: Series[int] = pa.Field(isin=[0, 1], nullable=False) 
    Autoimmune_Disorders: Series[int] = pa.Field(isin=[0, 1], nullable=False)
    H_Pylori_Status: Series[int] = pa.Field(isin=[0, 1], nullable=False)
    Occult_Blood_Test: Series[int] = pa.Field(isin=[0, 1], nullable=False)
    Endoscopy_Result: Series[int] = pa.Field(isin=[0, 1], nullable=False)
    Colonoscopy_Result: Series[int] = pa.Field(isin=[0, 1], nullable=False)
    Stool_Culture: Series[int] = pa.Field(isin=[0, 1], nullable=False)
    Food_Intolerance: Series[int] = pa.Field(isin=[0, 1], nullable=False)
    Smoking_Status: Series[int] = pa.Field(isin=[0, 1], nullable=False)
    Alcohol_Use: Series[int] = pa.Field(isin=[0, 1], nullable=False)
    Abdominal_Pain: Series[int] = pa.Field(isin=[0, 1], nullable=False)
    Bloating: Series[int] = pa.Field(isin=[0, 1], nullable=False)
    Diarrhea: Series[int] = pa.Field(isin=[0, 1], nullable=False)
    Constipation: Series[int] = pa.Field(isin=[0, 1], nullable=False)
    Rectal_Bleeding: Series[int] = pa.Field(isin=[0, 1], nullable=False)
    Appetite_Loss: Series[int] = pa.Field(isin=[0, 1], nullable=False)
    Weight_Loss: Series[int] = pa.Field(isin=[0, 1], nullable=False)
    NSAID_Use: Series[int] = pa.Field(isin=[0, 1], nullable=False)
    Antibiotic_Use: Series[int] = pa.Field(isin=[0, 1], nullable=False)
    PPI_Use: Series[int] = pa.Field(isin=[0, 1], nullable=False)
    Medications: Series[int] = pa.Field(isin=[0, 1], nullable=False)

    class Config:
        strict = False

def extract_and_validate(file_id: str, output_dir: str = 'data/raw') -> pd.DataFrame:
    """
    Загружает данные с Google Drive, валидирует с помощью Pandera и сохраняет в data/raw.
    """
    file_url = f"https://drive.google.com/uc?id={file_id}"
    print(f"Шаг 1. Загрузка данных из Google Drive (ID: {file_id})...")
    
    try:
        df = pd.read_csv(file_url, on_bad_lines='skip')
        print("Датасет успешно загружен.")
    except Exception as e:
        raise RuntimeError(f"Ошибка при загрузке CSV с URL: {e}")

    print("Проверка Pandera-схемы (37 столбцов)...")
    try:
        # Валидация
        validated_df = RawDataSchema.validate(df, lazy=True)
        print("Структурная валидация успешно пройдена.")
    except pa.errors.SchemaErrors as err:
        print("\nОШИБКА ВАЛИДАЦИИ PANDERA:")
        print(err.failure_cases.to_string())
        raise ValueError("Валидация данных не пройдена.")

    os.makedirs(output_dir, exist_ok=True)
    output_file = os.path.join(output_dir, 'raw_data.csv')
    validated_df.to_csv(output_file, index=False)
    print(f"Сырые данные сохранены в: {output_file}")
    
    return validated_df

DTYPE_MAP = DTYPE_MAP