from claims import parse_claims

def partition_on_each_item(l):
    for i in range(len(l)):
        yield l[i], l[:i] + l[i+1:]

def intervals_overlap(interval1, interval2):
    # determines whether two closed intervals (i.e. [1, 3] and [2, 4]) overlap
    a1, b1 = interval1
    a2, b2 = interval2
    return b1 >= a2 and a1 <= b2

def claims_overlap(claim1, claim2):
    x_interval1 = (claim1.left_offset, claim1.left_offset + claim1.width - 1)
    y_interval1 = (claim1.top_offset, claim1.top_offset + claim1.height - 1)
    x_interval2 = (claim2.left_offset, claim2.left_offset + claim2.width - 1)
    y_interval2 = (claim2.top_offset, claim2.top_offset + claim2.height - 1)

    return (
        intervals_overlap(x_interval1, x_interval2) and
        intervals_overlap(y_interval1, y_interval2)
    )

def find_non_overlapping_claim_id(claims):
    for claim, rest_of_claims in partition_on_each_item(claims):
        is_non_overlapping = all(
            not claims_overlap(claim, other_claim) for other_claim in rest_of_claims
        )

        if is_non_overlapping:
            return claim.id

print(find_non_overlapping_claim_id(parse_claims()))