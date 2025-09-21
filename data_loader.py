import pandas as pd

FILE_ID = "1-d3NKz-Fvt8fLyzPreleSHF_bLE13xpd"
file_url = f"https://drive.google.com/uc?id={FILE_ID}"

raw_data = pd.read_csv(file_url)     # Читаем файл
print(raw_data.head(10))             # Выводим первые 10 строк