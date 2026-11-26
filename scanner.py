from price_analyzer import analyze_price
from main import send_telegram_message


def scan_products(products):

    for product in products:

        result = analyze_price(
            product["current_price"],
            product["reference_price"]
        )

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
