import re

CLAIM_REGEX = r'^#(\d+)\s@\s(\d+),(\d+):\s(\d+)x(\d+)$'

class Claim:
    def __init__(self, claim_id, left_offset, top_offset, width, height):
        self.id = claim_id
        self.left_offset = left_offset
        self.top_offset = top_offset
        self.width = width
        self.height = height

def parse_claims():
    claims = []
    with open('claims.txt', 'r') as f:
        for line in f:
            claim_parts = [int(part) for part in re.match(CLAIM_REGEX, line.strip()).groups()]
            claim = Claim(*claim_parts)
            claims.append(claim)
    return claims