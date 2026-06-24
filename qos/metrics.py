import math


def percentile(values, p):

    if not values:

        return 0


    values = sorted(values)

    index = (p / 100) * (len(values)-1)

    lower = math.floor(index)

    upper = math.ceil(index)


    if lower == upper:

        return values[int(index)]


    fraction = index - lower


    return values[lower] + (

        values[upper] - values[lower]

    ) * fraction