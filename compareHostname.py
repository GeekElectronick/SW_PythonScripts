import re

def extract_hostnames(file_path):
    hostname_pattern = r'hostname="([^"]+)"'
    hostnames = set()  # Use a set to avoid duplicates within the same file

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                matches = re.findall(hostname_pattern, line)
                hostnames.update(matches)
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

    return hostnames

if __name__ == "__main__":
    file1 = "rawFiles/file1.txt"
    file2 = "rawFiles/file2.txt"

    hostnames_file1 = extract_hostnames(file1)
    hostnames_file2 = extract_hostnames(file2)

    # Find unduplicated hostnames
    unique_to_file1 = hostnames_file1 - hostnames_file2
    unique_to_file2 = hostnames_file2 - hostnames_file1

    print("Hostnames unique to file1:")
    for hostname in unique_to_file1:
        print(hostname)

    print("\nHostnames unique to file2:")
    for hostname in unique_to_file2:
        print(hostname)