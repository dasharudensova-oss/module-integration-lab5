def is_same_sign(arr):
    if not arr:
        return False
    has_pos = any(x > 0 for x in arr)
    has_neg = any(x < 0 for x in arr)
    return not (has_pos and has_neg)