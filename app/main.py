def get_human_age(cat_age: int, dog_age: int) -> list:

    human_age_from_cat = 0
    human_age_from_dog = 0

    if cat_age >= 15:
        human_age_from_cat += 1
        cat_age -= 15
    if cat_age >= 9:
        human_age_from_cat += 1
        cat_age -= 9

    if cat_age > 0:
        human_age_from_cat += cat_age // 4

    if dog_age >= 15:
        human_age_from_dog += 1
        dog_age -= 15
    if dog_age >= 9:
        human_age_from_dog += 1
        dog_age -= 9

    if dog_age > 0:
        human_age_from_dog += dog_age // 5

    return [human_age_from_cat, human_age_from_dog]
