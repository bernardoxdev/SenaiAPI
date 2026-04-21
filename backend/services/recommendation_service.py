def score_material(m):
    return (
        (5 - m.density) * 2 +
        m.strength * 2 +
        m.recyclability if hasattr(m, "recyclability") else 0
    )

def best_material(materials):
    return max(materials, key=score_material)