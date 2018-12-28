from polymer import get_polymer

def each_cons(l, n):
    for i in range(0, len(l) - n):
        yield l[i:i+n], i

def are_same_type(unit1, unit2):
    return unit1.lower() == unit2.lower()

def are_same_polarity(unit1, unit2):
    return unit1.islower() == unit2.islower()

def are_opposite_polarity(unit1, unit2):
    return not are_same_polarity(unit1, unit2)

def do_react(unit1, unit2):
    return (
        are_same_type(unit1, unit2) and
        are_opposite_polarity(unit1, unit2)
    )

def apply_unit_reaction(polymer):
    new_polymer = polymer
    any_reaction = False
    for (unit1, unit2), i in each_cons(polymer, 2):
        if do_react(unit1, unit2):
            new_polymer = polymer[:i] + polymer[i+2:]
            any_reaction = True
            break
    return new_polymer, any_reaction

def trigger_polymer(polymer):
    any_reaction = True
    while any_reaction:
        polymer, any_reaction = apply_unit_reaction(polymer)
    return polymer

print(len(trigger_polymer(get_polymer())))