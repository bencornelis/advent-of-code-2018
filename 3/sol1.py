from claims import parse_claims

def apply_claims(claims, dim=1000):
    grid = [[0 for _ in range(dim)] for _ in range(dim)]
    for claim in claims:
        for row in range(claim.top_offset, claim.top_offset + claim.height):
            for col in range(claim.left_offset, claim.left_offset + claim.width):
                grid[row][col] += 1

    return sum(
        [1 if grid[row][col] >= 2 else 0 for row in range(dim) for col in range(dim)]
    )

print(apply_claims(parse_claims()))