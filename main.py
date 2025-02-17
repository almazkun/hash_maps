from collections import Counter


# 1. Two Sum
def find_two_sum(nums, target):
    hash_map = {}
    # Complete the function to return indices of two numbers that add up to target
    for i, n in enumerate(nums):
        complement = target - n
        if complement in hash_map:
            return [hash_map[complement], i]
        hash_map[n] = i
    return []


# 2. First Non-Repeating Character
def first_unique_char(s):
    freq = {}
    # Return index of first non-repeating character
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1

    for i, ch in enumerate(s):
        if freq[ch] == 1:
            return i
    return -1


# 3. Valid Anagram
def is_anagram(s, t):
    char_count = {}
    # Check if t is anagram of s
    if len(s) != len(t):
        return False

    for ch_s, ch_t in zip(s, t):
        char_count[ch_s] = char_count.get(ch_s, 0) + 1
        char_count[ch_t] = char_count.get(ch_t, 0) - 1

    return all(count == 0 for count in char_count.values())


# 4. Intersection of Arrays
def find_intersection(nums1, nums2):
    # Return array of elements present in both arrays
    hmap = {n: True for n in nums1}
    res = []
    for n in nums2:
        if n in hmap:
            res.append(n)
            hmap.pop(n)
    return res


# 5. Group Anagrams
def group_anagrams(strs):
    groups = {}
    # Group strings by their anagram pattern
    for s in strs:
        key = "".join(sorted(s))
        if key in groups:
            groups[key].append(s)
        else:
            groups[key] = [s]
    return list(groups.values())


# 6. Longest Substring Without Repeats
def length_of_longest_substring(s):
    char_pos = {}
    longest = 0
    start = 0

    for i, ch in enumerate(s):
        if ch in char_pos and char_pos[ch] >= start:
            start = char_pos[ch] + 1
        char_pos[ch] = i
        longest = max(longest, i - start + 1)
    return longest


# 7. Subarray Sum Equals K
def subarray_sum(nums, k):
    sum_map = {0: 1}
    # Count subarrays with sum equal to k
    current_sum = 0
    count = 0

    for n in nums:
        current_sum += n
        diff = current_sum - k
        if diff in sum_map:
            count += sum_map[diff]
        sum_map[current_sum] = sum_map.get(current_sum, 0) + 1
    return count


# 8. Isomorphic Strings
def is_isomorphic(s, t):
    if len(s) != len(t):
        return False

    if not s and not t:
        return True
    s_map, t_map = {}, {}
    # Check if strings follow same pattern

    for i in range(len(s)):
        if not s[i] in s_map:
            s_map[s[i]] = t[i]
        else:
            if s_map[s[i]] != t[i]:
                return False

        if not t[i] in t_map:
            t_map[t[i]] = s[i]
        else:
            if t_map[t[i]] != s[i]:
                return False

    return True


# 9. Word Pattern
def word_pattern(pattern, str):
    words = str.split()
    if len(pattern) != len(words):
        return False

    char_to_word = {}
    word_to_char = {}

    for ch, word in zip(pattern, words):
        if ch in char_to_word:
            if char_to_word[ch] != word:
                return False
        else:
            if word in word_to_char:
                return False
            char_to_word[ch] = word
            word_to_char[word] = ch

    return True


# 10. LRU Cache
class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.order = []

    def get(self, key):
        if key not in self.cache:
            return -1
        self.order.remove(key)
        self.order.append(key)
        return self.cache[key]

    def put(self, key, value):
        if key in self.cache:
            self.order.remove(key)
        elif len(self.cache) >= self.capacity:
            lru = self.order.pop(0)
            self.cache.pop(lru)
        self.cache[key] = value
        self.order.append(key)


# 11. Logger Rate Limiter
class Logger:
    def __init__(self):
        self.msg_times = {}
        # Log messages with rate limiting


# 12. Four Sum II
def four_sum_count(A, B, C, D):
    sum_map = {}
    # Count tuples (i,j,k,l) where sum = 0


# 13. Longest Palindrome
def longest_palindrome(s):
    char_count = {}
    # Find length of longest possible palindrome


# 14. Copy List with Random Pointer
def copy_random_list(head):
    node_copy = {}
    # Deep copy linked list with random pointers


# 15. Minimum Window Substring
def min_window(s, t):
    target_map = {}
    # Find smallest window containing all characters


# 16. Find All Anagrams
def find_anagrams(s, p):
    p_map = {}
    # Find all anagrams of p in s


# 17. Equal Row and Column Pairs
def equal_pairs(grid):
    row_patterns = {}
    # Count equal row and column patterns


# 18. Reconstruct Original Array
def find_original(changed):
    num_freq = {}
    # Reconstruct original array from doubled array


# 19. Valid Sudoku
def is_valid_sudoku(board):
    rows, cols, boxes = {}, {}, {}
    # Validate Sudoku board state


# 20. Time Based Key-Value Store
class TimeMap:
    def __init__(self):
        self.store = {}
        # Implement get/set with timestamps


if __name__ == "__main__":
    print("start")
    print("# 1")
    assert find_two_sum([2, 7, 11, 15], 9) == [0, 1]
    assert find_two_sum([0, 0], 0) == [0, 1]
    assert find_two_sum([-1, -2, -3, -4], -7) == [2, 3]
    assert find_two_sum([3, 3, 3, 3], 6) == [0, 1]
    assert find_two_sum([1, 2, 3, 4], 7) == [2, 3]
    assert find_two_sum([1, 2, 3], 10) == []
    assert find_two_sum([2], 4) == []
    assert find_two_sum([1000000, 2000000], 3000000) == [0, 1]
    print("# 2")
    assert first_unique_char("leetcode") == 0, "'l' is first unique"
    assert first_unique_char("loveleetcode") == 2, "'v' is first unique"
    assert first_unique_char("aabb") == -1, "no unique chars"
    assert first_unique_char("") == -1, "empty string"
    assert first_unique_char("a") == 0, "single char"
    assert first_unique_char("aaa") == -1, "all same chars"
    assert first_unique_char("aAaA") == -1, "case sensitive"
    assert first_unique_char("z") == 0, "last letter"
    assert first_unique_char("dddccdbba") == 8, "unique char at end"
    assert first_unique_char("abcdefg") == 0, "all unique chars"
    assert first_unique_char("  ") == -1, "spaces only"
    print("# 3")
    assert is_anagram("anagram", "nagaram") == True
    assert is_anagram("rat", "car") == False
    assert is_anagram("listen", "silent") == True
    assert is_anagram("", "") == True
    assert is_anagram("a", "a") == True
    assert is_anagram("a", "") == False
    assert is_anagram("", "a") == False
    assert is_anagram("aacc", "ccac") == False
    assert is_anagram("ab", "a") == False
    assert is_anagram("aabbcc", "abcabc") == True
    assert is_anagram("🙂🙂", "🙂🙂") == True
    assert is_anagram("ab ", "ba") == False
    assert is_anagram("Tea", "Eat") == False
    assert is_anagram("eat", "tea") == True
    assert is_anagram("aabb", "aabbc") == False
    print("# 4")
    assert find_intersection([1, 2, 3], [2, 3, 4]) == [
        2,
        3,
    ], "Common elements should be returned"
    assert (
        find_intersection([4, 5, 6], [1, 2, 3]) == []
    ), "No common elements should return an empty list"
    assert (
        find_intersection([], [1, 2, 3]) == []
    ), "Empty first list should return empty"
    assert (
        find_intersection([1, 2, 3], []) == []
    ), "Empty second list should return empty"
    assert find_intersection([], []) == [], "Both lists empty should return empty"
    assert find_intersection([1, 1, 2, 2, 3, 3], [2, 2, 3, 3, 4, 4]) == [
        2,
        3,
    ], "Output should not have duplicates"
    assert find_intersection([1, 2, 3], [1, 2, 3]) == [
        1,
        2,
        3,
    ], "Identical lists should return the same elements"
    assert find_intersection([1], [1]) == [
        1
    ], "Single common element should return that element"
    assert (
        find_intersection([1], [2]) == []
    ), "No common single elements should return empty"
    assert find_intersection(list(range(1000)), list(range(500, 1500))) == list(
        range(500, 1000)
    ), "Should work for large inputs"
    print("# 5")
    assert group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) == [
        ["eat", "tea", "ate"],
        ["tan", "nat"],
        ["bat"],
    ], f"Group anagrams correctly"
    assert group_anagrams([]) == [], "Empty list should return empty list"
    assert group_anagrams(["a"]) == [
        ["a"]
    ], "Single element should be a group by itself"
    assert group_anagrams(["abc", "acb", "bac", "bca", "cab"]) == [
        ["abc", "acb", "bac", "bca", "cab"]
    ], "All anagrams should be grouped together"
    assert group_anagrams(["dog", "cat", "fish"]) == [
        ["dog"],
        ["cat"],
        ["fish"],
    ], "No anagrams should return separate groups"
    assert group_anagrams(
        ["".join(chr((i % 26) + 97) for i in range(1000))] * 1000
    ) == [
        ["".join(chr((i % 26) + 97) for i in range(1000))] * 1000
    ], "Large input with same strings should be grouped"
    assert group_anagrams(["listen", "silent", "enlist", "inlets", "netsil"]) == [
        ["listen", "silent", "enlist", "inlets", "netsil"]
    ], "Anagrams with mixed characters should be grouped"
    print("# 6")
    # Basic cases
    assert (
        length_of_longest_substring("abcabcbb") == 3
    ), "Longest substring without repeating characters is 'abc'"
    assert (
        length_of_longest_substring("bbbbb") == 1
    ), "Longest substring without repeating characters is 'b'"
    assert (
        length_of_longest_substring("pwwkew") == 3
    ), "Longest substring without repeating characters is 'wke'"
    assert length_of_longest_substring("") == 0, "Empty string should return 0"
    assert (
        length_of_longest_substring("a") == 1
    ), "Single character string should return 1"
    assert (
        length_of_longest_substring("abcdef") == 6
    ), "All unique characters, longest substring is the entire string"
    assert (
        length_of_longest_substring("abcdeabc") == 5
    ), "Longest substring without repeating characters is 'abcde'"
    assert (
        length_of_longest_substring("aaabcde") == 5
    ), "Longest substring without repeating characters is 'abcde'"
    assert (
        length_of_longest_substring("abc123abc") == 6
    ), "Longest substring without repeating characters is 'abc123'"
    print("# 7")
    assert subarray_sum([1, 1, 1], 2) == 2, "Expected 2"  # [1, 1], [1, 1]
    assert subarray_sum([1, 2, 3], 3) == 2, "Expected 2"  # [1, 2], [3]
    assert subarray_sum([1, 2, 3], 7) == 0, "Expected 0"  # No subarrays summing to 7
    assert subarray_sum([], 0) == 0, "Expected 0"  # Empty array, no subarrays
    assert subarray_sum([1], 1) == 1, "Expected 1"  # [1] matches sum 1
    assert subarray_sum([1, -1, 1], 1) == 3, "Expected 3"  # [1], [-1, 1], [1]
    assert subarray_sum([1, 2, 3, -2, 5], 5) == 2, "Expected 2"  # [2, 3], [5]
    assert subarray_sum([1, 1, 1], 0) == 0, "Expected 0"  # No subarrays summing to 0
    assert subarray_sum([1, -1, 1, -1], 0) == 4, "Expected 4"  # All subarrays sum to 0
    assert subarray_sum([10, 5, 2, 7, 1], 15) == 2
    assert subarray_sum([1, 2, 3, 4, 5], 5) == 2, "Expected 2"  # [2, 3], [5]
    assert subarray_sum([5, 5, 5], 5) == 3, "Expected 3"  # [5], [5], [5]
    print("# 8")
    # 8. Isomorphic Strings
    assert is_isomorphic("egg", "add") == True, "Test case 1 failed"
    assert is_isomorphic("foo", "bar") == False, "Test case 2 failed"
    assert is_isomorphic("paper", "title") == True, "Test case 3 failed"
    assert is_isomorphic("abc", "xyz") == True, "Test case 4 failed"
    assert is_isomorphic("ab", "aa") == False, "Test case 5 failed"
    assert is_isomorphic("aabb", "xxyy") == True, "Test case 6 failed"
    assert is_isomorphic("abc", "def") == True, "Test case 7 failed"
    assert is_isomorphic("a", "b") == True, "Test case 8 failed"
    assert is_isomorphic("aa", "ab") == False, "Test case 9 failed"
    assert is_isomorphic("", "") == True, "Test case 10 failed"
    print("# 9")
    assert word_pattern("abba", "dog cat cat dog") == True, "Test case 1 failed"
    assert word_pattern("abba", "dog cat cat fish") == False, "Test case 2 failed"
    assert word_pattern("aaaa", "dog dog dog dog") == True, "Test case 3 failed"
    assert word_pattern("abba", "dog dog dog dog") == False, "Test case 4 failed"
    assert word_pattern("abc", "dog cat fish") == True, "Test case 5 failed"
    assert word_pattern("abc", "dog dog dog") == False, "Test case 6 failed"
    assert word_pattern("a", "dog") == True, "Test case 7 failed"
    assert word_pattern("a", "dog cat") == False, "Test case 8 failed"
    assert word_pattern("", "") == True, "Test case 9 failed"
    assert word_pattern("aabb", "dog cat dog cat") == False, "Test case 10 failed"
    print("# 10")
    # Basic operations
    cache = LRUCache(2)
    cache.put(1, 1)
    assert cache.get(1) == 1
    assert cache.get(2) == -1

    # Capacity limit
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    cache.put(3, 3)  # This should evict key 1
    assert cache.get(1) == -1
    assert cache.get(2) == 2
    assert cache.get(3) == 3

    # Update existing key
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(1, 10)
    assert cache.get(1) == 10

    # LRU eviction order
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    cache.get(1)  # Makes 1 most recently used
    cache.put(3, 3)  # Should evict 2, not 1
    two = cache.get(2)
    assert two == -1, f"two should be {two}"
    assert cache.get(1) == 1
    assert cache.get(3) == 3

    # Edge cases
    cache = LRUCache(1)
    cache.put(1, 1)
    cache.put(2, 2)
    assert cache.get(1) == -1
    assert cache.get(2) == 2

    # Complex access pattern
    cache = LRUCache(3)
    cache.put(1, 1)
    cache.put(2, 2)
    cache.put(3, 3)
    cache.get(1)
    cache.put(4, 4)  # Should evict 2
    assert cache.get(2) == -1
    assert cache.get(1) == 1
    assert cache.get(3) == 3
    assert cache.get(4) == 4
    print("all good")
