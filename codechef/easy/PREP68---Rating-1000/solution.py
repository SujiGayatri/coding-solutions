def hasPairWithDifference(A: list[int], N: int, B: int) -> int:
    # write your code here 
    seen = set()
    for x in A:
        if x - B in seen or x + B in seen:
            return 1
        seen.add(x)
    return 0