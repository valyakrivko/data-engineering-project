import pandas as pd

FILE_ID = "1-d3NKz-Fvt8fLyzPreleSHF_bLE13xpd"
file_url = f"https://drive.google.com/uc?id={FILE_ID}"

def load_data():
    try:
        raw_data = pd.read_csv(file_url)
        print("✅ Данные успешно загружены!")
        print(raw_data.head(10))  # выводим первые 10 строк
        return raw_data
    except Exception as e:
        print("❌ Ошибка при загрузке данных:", e)
        return None

if __name__ == "__main__":
    load_data()
