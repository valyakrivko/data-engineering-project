# data-engineering-project

## Описание

Репозиторий по проекту **"Инжиниринг управления данными"**, посвященный анализу данных пациентов с заболеваниями ЖКТ. В ходе выполнения проекта был написан ETL-пакет и проведен EDA приведенного датафрейма в виде ноутбука с динамической визуализацией (Plotly Express).

### Ссылки на датасеты

**Источник датасета**: [Kaggle](https://www.kaggle.com/datasets/amanik000/gastrointestinal-disease-dataset)

**Ссылка на датасет**: [Google Drive](https://drive.google.com/file/d/1yQeGe-12L8FFZ-cdwGnRZm_LrzdKrN4J/view?usp=sharing)  

---

## ETL-пакет: Структура и роли модулей

Пакет расположен в директории `src/`. Обратите внимание, что старые скрипты (`data_loader.py` и `write_to_db.py`) были удалены и их функциональность перенесена в модули пакета.

* `extract.py`: **Извлечение и валидация**. Загрузка и валидация сырых данных (Pandera), сохранение датасета в формате `.csv` в директорию `data/raw`.
* `transform.py`: **Трансформация**. Приведение типов с целью уменьшения объема занимаемой ими памяти.
* `load.py`: **Загрузка в БД и валидация выходных параметров**. Выгрузка датафрейма в БД (max 100 строк) и сохранение `data.parquet` в `data/processed`. Проверка выходных параметров.
* `main.py`: **Сборка и CLI-интерфейс**. Собирает все этапы ETL и предоставляет интерфейс запуска.

---

## Начало работы и запуск ETL

Для запуска проекта вам потребуется **Python 3.9+** и учетные данные для их записи первых 100 строк датафрейма на сервер **PostgreSQL** для работы модуля `load.py`.

### Настройка проекта

Следуйте нижеприведенной последовательности введения команд в терминал:

1.  **Клонирование репозитория:**
    ```bash
    git clone https://github.com/valyakrivko/data-engineering-project
    cd data-engineering-project
    ```

2.  **Создание и активация виртуального окружения (пример с Conda):**
    ```bash
    conda create -n env python=3.10 pip
    conda activate env
    ```

3.  **Установка необходимых зависимостей:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Настройка переменных окружения:**
    Создайте в корне проекта файл `.env` для конфигурации подключения к базе данных. Переменные используются модулем `etl/load.py`.

    ```bash
    # .env file content (пример)
    DB_USER="your_user"
    DB_PASSWORD="your_password"
    DB_URL="localhost"
    DB_PORT="5432"
    DB_ROOT_BASE="etl_db"
    SURNAME="gastro_data_table" 
    ```

5. **Запуск пакета ETL:**

Запуск осуществляется с помощью `main.py` внутри пакета, который принимает Google Drive File ID в качестве опционального аргумента.

**Формат запуска:**

```bash
python etl/main.py --file-id "1yQeGe-12L8FFZ-cdwGnRZm_LrzdKrN4J"
```

## Визуализация данных

Для проекта был выполнен Исследовательский анализ данных (EDA), ноутбук расположен в папке notebooks.

**Ссылка на рендер ноутбука**: [NBViewer](https://nbviewer.org/github/valyakrivko/data-engineering-project/blob/main/notebooks/EDA.ipynb)








