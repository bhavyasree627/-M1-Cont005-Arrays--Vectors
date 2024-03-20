def most_frequent_character(s):
    sorted_chars = sorted(s)
    max_freq_char = sorted_chars[0]
    max_freq = 1
    current_char = sorted_chars[0]
    current_freq = 1
    for i in range(1, len(sorted_chars)):
        if sorted_chars[i] == current_char:
            current_freq += 1
        else:
            if current_freq > max_freq or (current_freq == max_freq and current_char < max_freq_char):
                max_freq_char = current_char
                max_freq = current_freq
            current_char = sorted_chars[i]
            current_freq = 1
    if current_freq > max_freq or (current_freq == max_freq and current_char < max_freq_char):
        max_freq_char = current_char
        max_freq = current_freq
    return max_freq_char

s = input().strip()
print(most_frequent_character(s))
