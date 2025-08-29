def longest_unique_substring(s: str) -> int:
    seen = set()
    left = 0
    max_len = 0

    for right in range(len(s)):
        
        while s[right] in seen:
            seen.remove(s[left])
            left += 1
        
        seen.add(s[right])
        
        max_len = max(max_len, right - left + 1)

    return max_len



s = "pwwkew"
print("Input:", s)
print("Longest substring length:", longest_unique_substring(s))