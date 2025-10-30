import requests
import pandas as pd
from pandas import json_normalize
import time

API_URL = "http://makeup-api.herokuapp.com/api/v1/products.json"

def fetch_and_load_makeup_data(url):
    
    print(f"*** Выполнение запроса к API: {url} ***")
    
    try:
        # 1. Запрос данных
        response = requests.get(url, timeout=15) 
        response.raise_for_status() 
        data = response.json()
        
        # 2. Преобразование JSON-массива в DataFrame
        df = json_normalize(data)
        
        # 3. Переименование и выбор столбцов
        df.rename(columns={
            'id': 'Product_ID', 
            'name': 'Product_Name', 
            'product_type': 'Type', 
            'price': 'Price_USD'
        }, inplace=True)
        
        # 4. Добавление временной метки
        df['Timestamp_UTC'] = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
        
        return df

    except requests.exceptions.Timeout:
        print("Ошибка: Превышен таймаут ожидания ответа от сервера API.")
        return None
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при выполнении HTTP-запроса: {e}")
        return None
    except Exception as e:
        print(f"Произошла непредвиденная ошибка: {e}")
        return None

if __name__ == "__main__":
    df = fetch_and_load_makeup_data(API_URL)
    if df is not None:
        print("\n--- DataFrame с данными о косметических продуктах ---")
        # Выводим первые 10 строк и ключевые столбцы
        output_cols = ['Product_Name', 'brand', 'Type', 'Price_USD', 'rating']
        print(df[output_cols].head(10).to_markdown(index=False, stralign="left")) 
        print("------------------------------------------")
        print(f"Данные успешно загружены. Общее количество строк: {len(df)}")
