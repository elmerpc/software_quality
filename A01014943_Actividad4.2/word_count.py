""" Module to count the number of words in a file. """
import sys
import time

def count_words(file_path):
    """Count the number of words in a file."""
    word_count = {}
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                words = line.strip().split()
                for word in words:
                    word_count[word] = word_count.get(word, 0) + 1
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return

    return word_count

def print_results(word_count):
    """Print the results to the console."""
    for word, count in word_count.items():
        print(f"{word}: {count}")

def save_results(word_count, file_path):
    """Save the results to a file."""
    with open(file_path, 'w', encoding='utf-8') as file:
        total_count = 0
        for word, count in word_count.items():
            file.write(f"{word}: {count}\n")
            total_count += count
        file.write(f"Total: {total_count}\n")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Error: Invalid number of arguments.")
        print("Usage: python wordCount.py fileWithData.txt")
        sys.exit(1)

    start_time = time.time()
    file_paths = sys.argv[1]
    word_counts = count_words(file_paths)
    end_time = time.time()

    if word_counts:
        print_results(word_counts)
        save_results(word_counts, "WordCountResults.txt")

    print(f"Execution time: {end_time - start_time} seconds")
