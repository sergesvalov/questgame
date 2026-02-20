import os

def main():
    with open('data.py', 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # The SCENARIOS dict starts at line 58 (index 57)
    scenarios_lines = lines[57:]
    data_lines = lines[:57]

    with open('scenarios.py', 'w', encoding='utf-8') as f:
        f.writelines(scenarios_lines)

    with open('data.py', 'w', encoding='utf-8') as f:
        f.writelines(data_lines)

    print("Successfully extracted scenarios.py and updated data.py")

if __name__ == '__main__':
    main()
