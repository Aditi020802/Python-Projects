def convert_units(value, source, target):
    factors = {"km": 1000, "m": 1, "cm": 0.01}
    if source not in factors or target not in factors:
        raise ValueError("Supported units are km, m, and cm.")
    return value * factors[source] / factors[target]

def calculate_area(shape, first, second=None):
    if shape == "circle":
        return 3.141592653589793 * first ** 2
    if shape == "rectangle":
        if second is None:
            raise ValueError("Rectangle requires length and width.")
        return first * second
    if shape == "triangle":
        if second is None:
            raise ValueError("Triangle requires base and height.")
        return 0.5 * first * second
    raise ValueError("Unsupported shape.")
