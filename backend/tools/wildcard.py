def calculate_wildcard(mask):

    parts = mask.split(".")

    wildcard = []

    for p in parts:
        wildcard.append(str(255 - int(p)))

    return {
        "wildcard_mask": ".".join(wildcard)
    }