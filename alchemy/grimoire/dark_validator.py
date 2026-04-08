from .dark_spellbook import dark_spell_allowed_ingredients

def dark_validate_ingredients(ingredients: str) -> str:
    allowed = [item.lower() for item in dark_spell_allowed_ingredients()]

    for raw_word in ingredients.split():
        word = raw_word.strip(" ,.!?;:").lower()
        if word in allowed:
            return f"{ingredients} - VALID"

    return f"{ingredients} - INVALID"
