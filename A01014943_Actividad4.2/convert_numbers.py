""" Module to convert a decimal number to binary and hexadecimal."""
import sys
import time

# Function to convert decimal to binary
def decimal_to_binary(n):
    """Convert a decimal number to binary."""
    if n == 0:
        return '0'
    binary = ""
    n = abs(n)
    while n > 0:
        binary = str(n % 2) + binary
        n = n // 2
    return binary

# Function to convert decimal to hexadecimal
def decimal_to_hexadecimal(n):
    """Convert a decimal number to hexadecimal."""
    hexadecimal = ""
    hex_map = "0123456789ABCDEF"
    n = abs(n)
    while n > 0:
        hexadecimal = hex_map[n % 16] + hexadecimal
        n = n // 16
    return hexadecimal

def convert_numbers_in_files(file_paths):
    """Convert numbers in files to binary and hexadecimal."""
    try:
        converted_numbers = {}
        for path in file_paths:
            with open(path, 'r', encoding='utf-8') as current_file:
                numbers = []
                results = {}
                for line in current_file:
                    try:
                        number = int(line.strip())
                        numbers.append(number)
                    except ValueError:
                        print(f"Invalid data: {line.strip()}")
                if numbers:
                    results['Original'] = numbers
                    results['Binary'] = [decimal_to_binary(num) for num in numbers]
                    results['Hexadecimal'] = [decimal_to_hexadecimal(num) for num in numbers]
                    converted_numbers[path] = results
                    print_results(results)
                else:
                    print("No valid data found in the file.")
        write_results_to_file(converted_numbers)
    except FileNotFoundError:
        print("File not found.")

def print_results(results):
    """Print the results to the console."""
    for key, value in results.items():
        print(f"{key}: {value}")

# Write the results to a file
def write_results_to_file(results):
    """Write the results to a file in a tabular format."""    
    with open('ConvertionResults.txt', 'w', encoding='utf-8') as file:
        # Write the headers
        for key, value in results.items():
            file.write(f"File: {key}\n")
            file.write('|'.join(['NUMBER', 'Bin', 'Hex']) + '\n')
            for index, original in enumerate(value['Original']):
                file.write(str(original) + '\t')
                file.write(value['Binary'][index] + '\t')
                file.write(value['Hexadecimal'][index] + '\t')
                file.write('\n')

if __name__ == "__main__":
    start_time = time.time()
    if len(sys.argv) < 2:
        print("Usage: python program.py <file_path>")
    else:
        numbers_file_path = sys.argv[1:]
        convert_numbers_in_files(numbers_file_path)
    end_time = time.time()
    elapsed_time = end_time - start_time
    with open('ConvertionResults.txt', 'a', encoding='utf-8') as f:
        f.write(f'Elapsed time: {elapsed_time}\n')
    print(f"Elapsed time: {elapsed_time} seconds ") # End-of-file (EOF)
