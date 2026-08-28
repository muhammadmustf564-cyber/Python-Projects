keywords = ["error", "failed", "warning"]

with open("log-file.txt", "r") as file:
    for line_number, line in enumerate(file, start=1):
        if any(word in line.lower() for word in keywords):
            print(f"Line {line_number}: {line.strip()}")
