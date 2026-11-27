def format_phone(phone: dict) -> str:
    condition = {
        "new": "🆕 Yangi",
        "used": "♻️ Ishlatilgan",
    }.get(phone.get("condition"), "❓ Noma'lum")

    return (
        f"📱 <b>{phone.get('brand', 'N/A')} {phone.get('model', 'N/A')}</b>\n"
        f"━━━━━━━━━━━━━━━━━━\n"
        f"💰 <b>Narxi:</b> {phone.get('price', 'N/A')} {phone.get('currency', '')}\n"
        f"🎨 <b>Rangi:</b> {phone.get('color', 'N/A')}\n"
        f"🧠 <b>RAM:</b> {phone.get('ram', 'N/A')}\n"
        f"💾 <b>Xotirasi:</b> {phone.get('storage', 'N/A')}\n"
        f"📅 <b>Yili:</b> {phone.get('year', 'N/A')}\n"
        f"📦 <b>Holati:</b> {condition}\n"
        f"━━━━━━━━━━━━━━━━━━\n"
        f"📝 <b>Qo'shimcha ma'lumot:</b>\n"
        f"{phone.get('description') or 'Maʼlumot mavjud emas'}"
    )
