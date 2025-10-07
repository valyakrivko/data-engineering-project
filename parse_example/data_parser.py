import requests
from bs4 import BeautifulSoup
import time 

# ----------------------------------------------------------------------
# 1. КОНФИГУРАЦИЯ
# ----------------------------------------------------------------------

URL = "https://vesna-city.ru/magazin/folder/gorshki-i-poddony-standart.html"
BASE_DOMAIN = "https://vesna-city.ru"

HEADERS = {
    # Имитируем обычный браузер Chrome
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36",
}

# ----------------------------------------------------------------------
# 2. ФУНКЦИЯ ДЛЯ ПАРСИНГА ОДНОЙ КАРТОЧКИ
# ----------------------------------------------------------------------

def parse_product_card(card_soup):
    """Извлекает название, цену и изображение из одной карточки товара."""
    
    # --- 2.1. Извлечение НАИМЕНОВАНИЯ ---
    # Название в <a> с классом 'noms-row-el-name'
    name_tag = card_soup.find('a', class_='noms-row-el-name')
    name = name_tag.text.strip() if name_tag else "N/A"

    # --- 2.2. Извлечение ЦЕНЫ ---
    # Цена в <span> с классом 'noms-row-el-price-item'
    price_tag = card_soup.find('span', class_='noms-row-el-price-item')
    
    price = "N/A"
    if price_tag:
        # Очистка: удаляем знак рубля (₽) и все пробелы
        price_text = price_tag.text.strip().replace('₽', '').replace('\xa0', '').replace(' ', '')
        price = price_text

    # --- 2.3. Извлечение ИЗОБРАЖЕНИЯ ---
    image_tag = card_soup.find('img')
    image_src = image_tag.get('src') if image_tag else "N/A"

    if image_src != 'N/A' and image_src.startswith('/'):
        image_src = BASE_DOMAIN + image_src
        
    # --- 2.4. Возвращаем результат ---
    return {
        "Name": name,
        "Price": price,
        "Image": image_src
    }

# ----------------------------------------------------------------------
# 3. ОСНОВНАЯ ЛОГИКА ПАРСЕРА
# ----------------------------------------------------------------------

def run_parser():
    
    try:
        print(f"Загрузка страницы: {URL}")
        response = requests.get(URL, headers=HEADERS, timeout=15)
        response.raise_for_status() 
        
    except requests.RequestException as e:
        print(f"Ошибка при загрузке страницы: {e}")
        return []

    soup = BeautifulSoup(response.text, "html.parser")

    # Ищем контейнеры товаров: 'noms-row-el'
    cards = soup.find_all('div', class_='noms-row-el')
    
    if not cards:
        print("Не удалось найти ни одной карточки товара. Проверьте селектор 'noms-row-el'.")
        return []

    print(f"Найдено {len(cards)} элементов. Начинаем парсинг...")
    print("-" * 40)

    all_products = []
    
    for card in cards:
        product_data = parse_product_card(card)
        all_products.append(product_data)
        
        # Вывод результата в консоль для контроля
        print(f"Товар: {product_data['Name']}")
        print(f"Цена: {product_data['Price']} руб.")
        print(f"Ссылка: {product_data['Image']}")
        print("-" * 40)
        
        time.sleep(0.1)
        
    return all_products

# ----------------------------------------------------------------------
# 4. ЗАПУСК
# ----------------------------------------------------------------------

if __name__ == "__main__":
    final_data = run_parser()
    
    if final_data:
        print(f"\nПарсинг завершен. Всего собрано товаров: {len(final_data)}")
    else:
        print("\nПарсинг не принес результатов.")