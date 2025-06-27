def scale_gibson_mastermix(num_reactions, hot_fusion=False):
    """Scale Gibson Assembly Master Mix ingredients based on desired number of reactions."""

    base_reactions = 40
    scale_factor = num_reactions / base_reactions

    recipe = {
        "5x Isothermal reaction buffer": 160.0,
        "1/10 T5 exonuclease (1U/uL)": 3.2,
        "Phusion DNA polymerase (2U/uL)": 10.0,
        "Taq DNA ligase (40U/uL)": 80.0,
        "Molecular biology grade H2O": 346.8
    }

    if hot_fusion:
        # Remove ligase and reassign its volume to water
        ligase_volume = recipe.pop("Taq DNA ligase (40U/uL)")
        recipe["Molecular biology grade H2O"] += ligase_volume

    scaled_recipe = {}
    adjustments = {}

    for ingredient, amount in recipe.items():
        scaled_amount = round(amount * scale_factor, 2)
        if scaled_amount < 1.0:
            adjustments[ingredient] = scaled_amount
            scaled_amount = 1.0
        scaled_recipe[ingredient] = scaled_amount

    scaled_recipe["Total volume (uL)"] = round(sum(scaled_recipe.values()), 2)
    scaled_recipe["Aliquot size (uL)"] = 15
    scaled_recipe["Number of aliquots"] = int(scaled_recipe["Total volume (uL)"] // 15)

    return scaled_recipe, adjustments, hot_fusion


def calculate_gibson(config):
    num_reactions = config.get("num_reactions", 40)
    hot_fusion = config.get("hot_fusion", False)

    # Scale and get adjustments
    scaled, adjustments, hot_fusion_used = scale_gibson_mastermix(num_reactions, hot_fusion)

    return scaled, adjustments, hot_fusion_used