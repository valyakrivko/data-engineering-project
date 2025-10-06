# Подпроект API

## Информация

Файл README.md содержит документацию к скрипту `api_reader.py`, который демонстрирует считывание данных из внешнего публичного API и их преобразование в структуру **Pandas DataFrame** с помощью Python.

---

## Используемый API

Для выполнения задания был выбран API, предоставляющий данные о брендах, цене и типах косметических продуктов:

* **Название API:** Makeup API
* **Конечная точка (Endpoint):** `http://makeup-api.herokuapp.com/api/v1/products.json`

---

## Запуск скрипта

Для успешного запуска проекта необходимо следовать стандартной процедуре:

1. Создайте виртуальное окружение:
```bash
   python -m venv venv
   ```
2. Активируйте виртуальное окружение (для CMD):
```bash
   venv\Scripts\activate.bat
   ```
3. Установите все необходимые зависимости:
```bash
   pip install -r requirements.txt
   ```
4. Запустите скрипт, находясь в корневой папке проекта (или внутри активированного виртуального окружения):
```bash
   python api_example/api_reader.py
   ```

## Исходный код (`api_reader.py`)

```python
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
```

## Скриншот вывода скрипта

<img width="959" height="388" alt="image" src="https://github.com/user-attachments/assets/995856ba-ccc8-48cc-a45c-70cef04ae168" />







