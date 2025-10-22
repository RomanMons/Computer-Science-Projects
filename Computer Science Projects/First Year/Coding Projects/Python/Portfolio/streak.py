def longest_streak(word,word_list):
    streak = 0
    max_streak = 0
    for a in word_list:
        if a == word:
            streak += 1
            max_streak = max(max_streak, streak)
        else:
            streak = 0
    return max_streak

if __name__ == "__main__":
    test = longest_streak('W', ['W', 'W', 'L', 'W'])
    print(test)
