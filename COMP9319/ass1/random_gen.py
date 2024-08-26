import random
import string


def generate_large_test_file(file_path, target_size):
    with open(file_path, 'w') as file:
        while file.tell() < target_size:
            pattern = ''.join(random.choices(string.ascii_letters + string.digits, k=20))
            file.write(pattern * 10)


if __name__ == '__main__':
    size = input()

    if 'KB' in size:
        target_file_size = int(size.replace('KB', '')) * 1024
    elif 'MB' in size:
        target_file_size = int(size.replace('MB', '')) * 1024 * 1024
    elif 'GB' in size:
        target_file_size = int(size.replace('GB', '')) * 1024 * 1024 * 1024
    elif 'B' in size:
        target_file_size = int(size.replace('B', ''))
    else:
        print("Invalid size. Please provide a valid size in B, KB, MB or GB.")
        exit(1)

    generate_large_test_file(f"random_{size}.txt", target_file_size)
