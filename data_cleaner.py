import csv

cleaned_data = []

rows_processed = 0
duplicates_removed = 0
missing_emails = 0
invalid_ages = 0

with open("messy_data.csv") as file:
    reader = csv.reader(file)
    next(reader)

    for row in reader:
        rows_processed += 1

        clean_name = row[0].strip().title()
        clean_email = row[1].strip().lower()

        if not clean_email:
            missing_emails += 1

        try:
            clean_age = int(row[2])
        except ValueError:
            clean_age = None
            invalid_ages += 1

        clean_row = [clean_name, clean_email, clean_age]

        if clean_row not in cleaned_data:
            cleaned_data.append(clean_row)
        else:
            duplicates_removed += 1

with open("cleaned_data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Email", "Age"])
    writer.writerows(cleaned_data)

print("\nData cleaning complete!")
print("Rows processed:", rows_processed)
print("Duplicates removed:", duplicates_removed)
print("Missing emails:", missing_emails)
print("Invalid ages:", invalid_ages)