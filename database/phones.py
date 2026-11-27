from .db import read_data


def get_brands() -> list[str]:
    phones: list[dict] = read_data("phones.json")

    brands = []
    for phone in phones:
        if phone["brand"] not in brands:
            brands.append(phone["brand"])

    return brands


def get_phones_by_brand(brand: str) -> list[dict]:
    phones: list[dict] = read_data("phones.json")

    result = []
    for phone in phones:
        if phone["brand"] == brand:
            result.append(phone)

    return result
