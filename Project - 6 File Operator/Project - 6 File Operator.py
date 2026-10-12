import os
from datetime import datetime


class JournalManager:
    def __init__(self, filename="journal.txt"):
        self.filename = filename

    def add_entry(self):
        try:
            entry = input("\nEnter your journal entry: ").strip()

            if not entry:
                print("Journal entry cannot be empty.")
                return

            with open(self.filename, "a", encoding="utf-8") as file:
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                file.write(f"[{timestamp}]\n{entry}\n\n")

            print("Entry added successfully!")

        except PermissionError:
            print("Error: Permission denied while writing to the journal.")
        except OSError as error:
            print("Error while saving the entry:", error)

    def view_entries(self):
        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                entries = file.read()

            if entries.strip():
                print("\nYour Journal Entries:")
                print("--------------------------------")
                print(entries)
            else:
                print("No journal entries found. Start by adding a new entry!")

        except FileNotFoundError:
            print("Error: The journal file does not exist. Please add a new entry first.")
        except PermissionError:
            print("Error: Permission denied while reading the journal.")
        except OSError as error:
            print("Error while reading the journal:", error)

    def search_entry(self):
        try:
            keyword = input("\nEnter a keyword or date to search: ").strip()

            if not keyword:
                print("Search keyword cannot be empty.")
                return

            with open(self.filename, "r", encoding="utf-8") as file:
                entries = file.read()

            if not entries.strip():
                print("No journal entries found.")
                return

            matching_entries = []
            current_entry = []

            for line in entries.splitlines():
                if line.startswith("[") and line.endswith("]"):
                    if current_entry:
                        matching_entries.append("\n".join(current_entry))

                    current_entry = [line]
                else:
                    current_entry.append(line)

            if current_entry:
                matching_entries.append("\n".join(current_entry))

            results = [
                entry for entry in matching_entries
                if keyword.lower() in entry.lower()
            ]

            if results:
                print("\nMatching Entries:")
                print("--------------------------------")

                for entry in results:
                    print(entry)
                    print()
            else:
                print(f"No entries were found for the keyword: {keyword}.")

        except FileNotFoundError:
            print("Error: The journal file does not exist. Please add a new entry first.")
        except PermissionError:
            print("Error: Permission denied while searching the journal.")
        except OSError as error:
            print("Error while searching the journal:", error)

    def create_journal(self):
        try:
            with open(self.filename, "x", encoding="utf-8"):
                pass

            print("Journal file created successfully.")

        except FileExistsError:
            print("The journal file already exists.")
        except PermissionError:
            print("Error: Permission denied while creating the journal.")
        except OSError as error:
            print("Error while creating the journal:", error)

    def delete_entries(self):
        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                entries = file.read()

            if not entries.strip():
                print("No journal entries to delete.")
                return

            confirmation = input(
                "\nAre you sure you want to delete all entries? (yes/no): "
            ).strip().lower()

            if confirmation == "yes":
                os.remove(self.filename)
                print("All journal entries have been deleted.")

            elif confirmation == "no":
                print("Deletion cancelled.")

            else:
                print("Invalid confirmation. Please enter yes or no.")

        except FileNotFoundError:
            print("No journal entries to delete.")
        except PermissionError:
            print("Error: Permission denied while deleting the journal.")
        except OSError as error:
            print("Error while deleting the journal:", error)

    def run(self):
        while True:
            print("\nWelcome to Personal Journal Manager!")
            print("Please select an option:\n")
            print("1. Add a New Entry")
            print("2. View All Entries")
            print("3. Search for an Entry")
            print("4. Delete All Entries")
            print("5. Create Journal File")
            print("6. Exit")

            choice = input("\nEnter your choice: ").strip()

            if choice == "1":
                self.add_entry()

            elif choice == "2":
                self.view_entries()

            elif choice == "3":
                self.search_entry()

            elif choice == "4":
                self.delete_entries()

            elif choice == "5":
                self.create_journal()

            elif choice == "6":
                print("\nThank you for using Personal Journal Manager. Goodbye!")
                break

            else:
                print("Invalid option. Please select a valid option from the menu.")


def main():
    journal = JournalManager()
    journal.run()


if __name__ == "__main__":
    main()

