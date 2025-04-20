def is_number(s):
    try:
        return int(s)
    except ValueError:
        try:
            return float(s)
        except ValueError:
            return None

def detect_arithmetic_pattern(sequence):
    if len(sequence) < 3:
        return None

    # Try numeric pattern first
    nums = [is_number(x) for x in sequence[-3:]]
    if all(n is not None for n in nums):
        diff1 = nums[1] - nums[0]
        diff2 = nums[2] - nums[1]
        if abs(diff1 - diff2) < 1e-9:  # stable step
            return str(nums[-1] + diff1)

    # Try alphabetical pattern
    chars = sequence[-3:]
    if all(len(x) == 1 and x.isalpha() for x in chars):
        ords = [ord(c) for c in chars]
        diff1 = ords[1] - ords[0]
        diff2 = ords[2] - ords[1]
        if diff1 == diff2:
            return chr(ords[-1] + diff1)

    return None
