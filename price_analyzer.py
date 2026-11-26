def analyze_price(current_price, reference_price):
    """
    Analizza il prezzo corrente rispetto a un prezzo storico
    o di riferimento attendibile.
    """

    if current_price <= 0 or reference_price <= 0:
        return {
            "status": "DATI NON VALIDI",
            "discount": 0
        }

    discount = (
        (reference_price - current_price)
        / reference_price
    ) * 100

    discount = round(discount, 1)

    if discount >= 60:
        status = "POSSIBILE ERRORE DI PREZZO"
    elif discount >= 40:
        status = "SCONTO ECCEZIONALE"
    elif discount >= 20:
        status = "OFFERTA"
    else:
        status = "PREZZO NORMALE"

    return {
        "status": status,
        "discount": discount,
        "current_price": current_price,
        "reference_price": reference_price
    }


if __name__ == "__main__":

    # Prodotto dimostrativo, non un'offerta reale
    result = analyze_price(100, 250)

    print("AMAZON DEAL HUNTER")
    print("------------------")
    print("Prezzo attuale:", result["current_price"], "€")
    print("Prezzo di riferimento:", result["reference_price"], "€")
    print("Sconto:", result["discount"], "%")
    print("Classificazione:", result["status"])
