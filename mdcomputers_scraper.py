import requests
from bs4 import BeautifulSoup
from urllib.parse import quote_plus
import sys


def scrape_mdcomputers(search_term):
    url = (
        "https://mdcomputers.in/"
        "?route=product/search&search=" + quote_plus(search_term)
    )

    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/120.0 Safari/537.36"
        )
    }

    try:
        response = requests.get(url, headers=headers, timeout=15)
        response.raise_for_status()
    except requests.RequestException as error:
        print(f"Error fetching MDComputers: {error}")
        return

    soup = BeautifulSoup(response.text, "html.parser")

    products = soup.select(".product-layout, .product-thumb")

    if not products:
        print("No products found.")
        return

    print(f"\nSearch results for: {search_term}\n")
    print("-" * 80)

    count = 0

    for product in products:
        name_element = product.select_one(
            ".name a, h4 a, .caption h4 a"
        )

        price_element = product.select_one(
            ".price, .price-new"
        )

        availability_element = product.select_one(
            ".stock, .availability"
        )

        if not name_element:
            continue

        name = name_element.get_text(" ", strip=True)
        product_url = name_element.get("href", "N/A")

        price = (
            price_element.get_text(" ", strip=True)
            if price_element
            else "N/A"
        )

        availability = (
            availability_element.get_text(" ", strip=True)
            if availability_element
            else "Check product page"
        )

        count += 1

        print(f"Product {count}")
        print(f"Name         : {name}")
        print(f"Price        : {price}")
        print(f"Availability : {availability}")
        print(f"URL          : {product_url}")
        print("-" * 80)

    if count == 0:
        print("No product details could be extracted.")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        search_term = " ".join(sys.argv[1:])
    else:
        search_term = input("Enter product to search: ").strip()

    if not search_term:
        print("Please enter a valid search term.")
        sys.exit(1)

    scrape_mdcomputers(search_term)
