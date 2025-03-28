def main():
    with open("CodingChallenges/MasteryChallenge/Challenge2Text.txt", "r") as file:
        lines = file.readlines()
        total_words = 0
        word_count = {}
        for line in lines:
            line = line.strip()
            line = line.split()
            
            total_words += len(line)
            
            for word in line:
                if word.lower() in word_count:
                    word_count[word.lower()] += 1
                else:
                    word_count[word.lower()] = 1

        print(f"Total words: {total_words}")
        print("Most frequent Words:")
        sorted_frequent_words = sorted(word_count.items(), key=lambda item: item[1], reverse=True)
        print(sorted_frequent_words)

if __name__ == "__main__":
    main()