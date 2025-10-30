# Подпроект API

## Информация

Файл README.md содержит документацию к скрипту `api_reader.py`, который демонстрирует считывание данных из внешнего публичного API и их преобразование в структуру **Pandas DataFrame** с помощью Python.

---

## Используемый API

Для выполнения задания был выбран API, предоставляющий данные о брендах, цене и типах косметических продуктов:

* **Название API:** [Makeup API](https://makeup-api.herokuapp.com/).
* **Конечная точка (Endpoint):** `http://makeup-api.herokuapp.com/api/v1/products.json`

---

## Запуск скрипта

Для успешного запуска проекта необходимо следовать стандартной процедуре:

1. Создайте виртуальное окружение:
```bash
   conda create -n env python=3.13 pip
   ```
2. Активируйте виртуальное окружение:
```bash
   conda activate env
   ```
3. Установите все необходимые зависимости:
```bash
   pip install -r requirements.txt
   ```
4. Запустите скрипт, находясь в корневой папке проекта (или внутри активированного виртуального окружения):
```bash
   python additionals/api_example/api_reader.py
   ```

## Скриншот вывода скрипта

<img width="959" height="388" alt="image" src="https://github.com/user-attachments/assets/995856ba-ccc8-48cc-a45c-70cef04ae168" />







