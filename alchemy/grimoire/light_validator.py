from light_spellbook import light_spell_allowed_ingredients
def validate_ingredients(ingredients: str):
    lst = ingredients.split()
    allowed = light_spell_allowed_ingredients()
    print(allowed)
    for one in lst:
        print(one)
        for two in allowed:
            if (one.lower() == two):
                return {ingredients: "VALID"}
    return {ingredients: "INVALID"}

print(f"{validate_ingredients("cake water food spell idiot")}")
