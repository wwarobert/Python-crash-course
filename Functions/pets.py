def describe_pet(pet_name, animal_type="dog"):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}")
    print(f"My {animal_type}'s name is {pet_name.title()}.")


describe_pet("harry", "hamster")
describe_pet("willie", "dog")

describe_pet(animal_type="hamster", pet_name="harry")
describe_pet(pet_name="willie", animal_type="dog")

describe_pet("willie")
describe_pet(pet_name="willie")
