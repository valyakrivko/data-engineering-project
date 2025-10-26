# data-engineering-project

## Описание

Репозиторий по проекту **"Инжиниринг управления данными"**, посвященный анализу данных пациентов с заболеваниями ЖКТ.  

### Ссылки на датасеты

**Источник датасета**: [Kaggle](https://www.kaggle.com/datasets/amanik000/gastrointestinal-disease-dataset)

**Ссылка на датасет**: [Google Drive](https://drive.google.com/file/d/1yQeGe-12L8FFZ-cdwGnRZm_LrzdKrN4J/view?usp=sharing)  

## Начало работы

### Настройка виртуального окружения

1. **Создание виртуального окружения:**
   ```bash
   conda create -n my_env python=3.13 pip
   ```

2. **Активация виртуального окружения:**
  
   ```bash
   conda activate my_env
   ```

3. **Установка необходимых зависимостей:**
   ```bash
   pip install -r requirements.txt
   ```

### Запуск скрипта загрузки данных

Для выполнения скрипта ввести следующую команду в терминал VS Code:

```bash
python data_loader.py
```

### Домашнее задание №2

Скриншот вывода действия скрипта:
<img width="820" height="342" alt="Screenshot_12" src="https://github.com/user-attachments/assets/cbdae811-74a9-4808-9ade-eb8bbd82faa9" />

**P.S. Датасет был изменен 24.09.2025, скриншот вывода скрипта предыдущего датасета неактуален.**

## Подготовка данных и их визуализация

Для проекта был выполнен Исследовательский анализ данных (EDA), ноутбук расположен в папке notebooks.

**Ссылка на рендер ноутбука**: [NBViewer](https://nbviewer.org/github/valyakrivko/data-engineering-project/blob/main/notebooks/EDA.ipynb)
