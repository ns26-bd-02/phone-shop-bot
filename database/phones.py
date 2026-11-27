from .db import read_data


def get_brands() -> list[str]:
    phones: list[dict] = read_data("phones.json")

    brands = []
    for phone in phones:
        if phone["brand"] not in brands:
            brands.append(phone["brand"])

    return brands
