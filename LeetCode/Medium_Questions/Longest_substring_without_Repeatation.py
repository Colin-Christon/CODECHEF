class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        char_index_map = {}  # Store the index of characters in the string
        max_length = 0
        left = 0  # Left pointer of the sliding window

        for right in range(len(s)):
            if s[right] in char_index_map and char_index_map[s[right]] >= left:
                # If the character is seen again within the current window, move the left pointer to the right of the duplicate character
                left = char_index_map[s[right]] + 1

            char_index_map[s[right]] = right  # Update the index of the character
            max_length = max(max_length, right - left + 1)

        return max_length
