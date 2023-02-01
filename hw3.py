def find_pair_naive(l1, target):
    result = set()

    for x in l1:
        for y in l1:
            if x + y == target:
                result.add( (x, y) )

    return result

def find_pairs_optimized(l1, target):
    