def compare_materials(m1, m2):
    return {
        "co2_like_score_diff": m1.density - m2.density,
        "strength_diff": m1.strength - m2.strength,
        "best_strength": m1.name if m1.strength > m2.strength else m2.name,
        "best_weight": m1.name if m1.density < m2.density else m2.name
    }