from concurrent.futures import ThreadPoolExecutor
from selenium import webdriver
from functions.create_sale import create_transaction
from functions.login import login


# Function to handle transactions in a separate browser tab
def process_transaction(transaction_type, amount):
    # Initialize a separate Chrome instance
    driver = webdriver.Chrome()

    try:
        # Login and create the transaction
        login(driver)
        print(f"Logged in for {transaction_type}")
        create_transaction(driver, transaction_type, amount)
        print(f"{transaction_type} transaction created with amount {amount}")
    except Exception as e:
        print(f"Error processing {transaction_type}: {e}")
    finally:
        driver.quit()
        print(f"Closed browser for {transaction_type}")


# Main function to execute multiple transactions
def main():
    # Define transaction types and amounts
    transactions = [
        ("sale", 20),
        ("purchase", 20),
        ("sale_return", 20),
        ("purchase_return", 20),
    ]

    # Run tasks concurrently with ThreadPoolExecutor
    with ThreadPoolExecutor(max_workers=4) as executor:
        # Submit tasks for concurrent execution
        for transaction_type, amount in transactions:
            executor.submit(process_transaction, transaction_type, amount)


if __name__ == "__main__":
    main()
