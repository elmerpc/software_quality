""" Module to compute the mean, median, mode, std deviation and variance of a list of numbers."""
import sys
import time

def compute_mean(numbers):
    """Compute the mean of a list of numbers."""
    return sum(numbers) / len(numbers)

def compute_median(numbers):
    """Compute the median of a list of numbers."""
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    if n % 2 == 0:
        return (sorted_numbers[n//2 - 1] + sorted_numbers[n//2]) / 2
    else:
        return sorted_numbers[n//2]

def compute_mode(numbers):
    """Compute the mode of a list of numbers."""
    counts = {}
    for num in numbers:
        counts[num] = counts.get(num, 0) + 1
    max_count = max(counts.values())
    if max_count == 1:
        return 'N/A'
    modes = [num for num, count in counts.items() if count == max_count]
    return modes

def compute_standard_deviation(numbers):
    """Compute the standard deviation of a list of numbers."""
    mean = compute_mean(numbers)
    squared_diffs = [(num - mean) ** 2 for num in numbers]
    variance = sum(squared_diffs) / len(numbers)
    return variance ** 0.5

def compute_variance(numbers):
    """Compute the variance of a list of numbers."""
    mean = compute_mean(numbers)
    squared_diffs = [(num - mean) ** 2 for num in numbers]
    return sum(squared_diffs) / len(numbers)

def compute_descriptive_statistics(file_path):
    """Compute the mean, median, mode, standard deviation, and variance of a list of numbers."""
    try:
        stats = {}
        for file in file_path:
            with open(file, 'r', encoding='utf-8') as current_file:
                numbers = []
                results = {}
                for line in current_file:
                    try:
                        number = float(line.strip())
                        numbers.append(number)
                    except ValueError:
                        print(f"Invalid data: {line.strip()}")
                if numbers:
                    results['Mean'] = compute_mean(numbers)
                    results['Median'] = compute_median(numbers)
                    results['Mode'] = compute_mode(numbers)
                    results['Standard Deviation'] = compute_standard_deviation(numbers)
                    results['Variance'] = compute_variance(numbers)
                    stats[file] = results
                    print_results(results)
                else:
                    print("No valid data found in the file.")
        write_results_to_file(stats)
    except FileNotFoundError:
        print("File not found.")

def print_results(results):
    """Print the results to the console."""
    for key, value in results.items():
        print(f"{key}: {value}")


def write_results_to_file(stats):
    """Write the results to a file in a tabular format."""    
    with open('StatisticsResults.txt', 'w', encoding='utf-8') as file:
        # Write the headers
        file.write('|'.join(['Statistics'] + list(stats.keys())) + '\n')

        # Write the rows
        for statistic in ['Mean', 'Median', 'Mode', 'Standard Deviation', 'Variance']:
            file.write('|'.join([statistic] + [str(stats[file].get(statistic, '')) for file in stats.keys()]) + '\n')

if __name__ == "__main__":
    start_time = time.time()
    if len(sys.argv) < 2:
        print("Usage: python program.py <file_path>")
    else:
        numbers_file_path = sys.argv[1:]
        compute_descriptive_statistics(numbers_file_path)
    end_time = time.time()
    elapsed_time = end_time - start_time
    with open('StatisticsResults.txt', 'a', encoding='utf-8') as f:
        f.write(f'Elapsed time: {elapsed_time}\n')
    print(f"Elapsed time: {elapsed_time} seconds ") # End-of-file (EOF)
