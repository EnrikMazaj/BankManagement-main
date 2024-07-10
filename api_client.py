import requests

BASE_URL = 'http://127.0.0.1:5000'

def get_all_banks():
    response = requests.get(f'{BASE_URL}/', headers={'Accept': 'application/json'})
    if response.status_code == 200 and response.headers['Content-Type'] == 'application/json':
        return response.json()
    else:
        return f"Failed to get banks. Status code: {response.status_code}, Response: {response.text}"

def get_bank_details(bank_id):
    response = requests.get(f'{BASE_URL}/bank/{bank_id}', headers={'Accept': 'application/json'})
    if response.status_code == 200 and response.headers['Content-Type'] == 'application/json':
        return response.json()
    else:
        return f"Failed to get bank. Status code: {response.status_code}, Response: {response.text}"

def add_bank(name, location):
    data = {
        'name': name,
        'location': location
    }
    response = requests.post(f'{BASE_URL}/add_bank', data=data, headers={'Accept': 'application/json'})
    if response.status_code == 201:  # Created status
        return "Bank added successfully"
    else:
        return f"Failed to add bank. Status code: {response.status_code}, Response: {response.text}"

def update_bank(bank_id, name, location):
    data = {
        'name': name,
        'location': location
    }
    response = requests.post(f'{BASE_URL}/edit_bank/{bank_id}', data=data, headers={'Accept': 'application/json'})
    if response.status_code == 200:  # OK status
        return "Bank updated successfully"
    else:
        return f"Failed to update bank. Status code: {response.status_code}, Response: {response.text}"

def delete_bank(bank_id):
    response = requests.post(f'{BASE_URL}/delete_bank/{bank_id}', headers={'Accept': 'application/json'})
    if response.status_code == 200:  # OK status
        return "Bank deleted successfully"
    else:
        return f"Failed to delete bank. Status code: {response.status_code}, Response: {response.text}"


# Main function with an interactive menu
def main_menu():
    while True:
        print("\n--- Bank Management Menu ---")
        print("1. List all banks")
        print("2. Add new bank")
        print("3. View bank details")
        print("4. Update bank")
        print("5. Delete bank")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")
        
        if choice == '1':
            banks = get_all_banks()
            if banks:
                for bank in banks:
                    print(f"ID: {bank['id']}, Name: {bank['name']}, Location: {bank['location']}")
        elif choice == '2':
            name = input("Enter bank name: ")
            location = input("Enter bank location: ")
            add_bank(name, location)
        elif choice == '3':
            bank_id = input("Enter bank ID: ")
            result = get_bank_details(bank_id)
            print(result)
        elif choice == '4':
            bank_id = input("Enter bank ID: ")
            name = input("Enter new bank name: ")
            location = input("Enter new bank location: ")
            update_bank(bank_id, name, location)
        elif choice == '5':
            bank_id = input("Enter bank ID: ")
            delete_bank(bank_id)
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == '__main__':
    main_menu()
