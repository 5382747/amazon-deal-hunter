from price_analyzer import analyze_price
from main import send_telegram_message


def scan_products(products):

    print("AMAZON DEAL HUNTER")
    print("------------------")

    for product in products:

        result = analyze_price(
            product["current_price"],
            product["reference_price"]
        )

        print(f"\nProdotto: {product['name']}")
        print(f"Prezzo: {result['current_price']} €")
        print(f"Sconto: {result['discount']}%")
        print(f"Classificazione: {result['status']}")

        if result["discount"] >= 20:

            message = (
                "AMAZON DEAL HUNTER\n\n"
                f"Prodotto: {product['name']}\n"
                f"Prezzo attuale: {result['current_price']} €\n"
                f"Prezzo di riferimento: {result['reference_price']} €\n"
                f"Sconto: {result['discount']}%\n"
                f"Classificazione: {result['status']}\n"
                f"Link: {product['url']}"
            )

            send_telegram_message(message)


if __name__ == "__main__":

    products = [
        {
            "name": "PC portatile dimostrativo",
            "current_price": 400,
            "reference_price": 700,
            "url": "https://www.amazon.it/"
        },
        {
            "name": "Monitor dimostrativo",
            "current_price": 150,
            "reference_price": 200,
            "url": "https://www.amazon.it/"
        },
        {
            "name": "Mouse dimostrativo",
            "current_price": 30,
            "reference_price": 35,
            "url": "https://www.amazon.it/"
        }
    ]

    scan_products(products)
