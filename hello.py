from functions.create_sale import create_transaction
from functions.login import login
from selenium import webdriver

sale = "https://pilot.karobarapp.com/sales-invoices/create"
purchase = "https://pilot.karobarapp.com/purchase/create"
sale_return = "https://pilot.karobarapp.com/sales-return/create"
purchase_return = "https://pilot.karobarapp.com/purchase-return/create"
quotation = "https://pilot.karobarapp.com/quotations/create"


def main():
    # Configure ChromeOptions
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)
    try:
        # Perform actions
        login(driver)
        print("Logged in")
        # create_transaction(driver, sale, 30)
        # print("Sale created")
        # create_transaction(driver, purchase, 30)
        # print("Purchase created")
        # create_transaction(driver, sale_return, 30)
        # print("Sale return created")
        # create_transaction(driver, purchase_return, 30)
        # print("Purchase return created")
        create_transaction(driver, quotation, 10, is_quotation=True)
        print("Quotation created")

    except Exception as e:
        print(e)
    # Quit driver
    driver.quit()


if __name__ == "__main__":
    main()
