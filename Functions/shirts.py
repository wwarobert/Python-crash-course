def make_tshirt(tshirt_size="L", tshirt_message="I love Python"):
    """Display tshirt size and message"""
    print(f"\nTshirt size is: {tshirt_size.upper()}")
    print(f"Message printed on it: {tshirt_message.title()}")


make_tshirt("xl", "lol")
make_tshirt(tshirt_size="l", tshirt_message="it's my tshirt")

make_tshirt()
make_tshirt(tshirt_size="m")

make_tshirt(tshirt_message="Random")
make_tshirt(tshirt_size="m", tshirt_message="Totally random")
