def next_higher_peak(heights):
    # Write your code here
    n = len(heights)
    result = [-1] * n
    stack = []
    for i in range(n - 1, -1, -1):
        while stack and stack[-1] <= heights[i]:
            stack.pop()

        if stack:
            result[i] = stack[-1]

        stack.append(heights[i])

    return result