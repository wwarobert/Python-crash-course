def order_sandwitches(*fillings):
    """Print list of sandwich fillings"""
    print("\nYou ordered sandwitch with:")
    for filling in fillings:
        print(f"- {filling}")


order_sandwitches('peppers', 'chicken', 'tzatziki')
order_sandwitches('carmelised onion', 'mustard', 'cumin')
order_sandwitches('spinata romana')
