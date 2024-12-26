import time
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from data.data import party_list_20, item_list_20

locators = {
    "billToField": "//input[@placeholder='Search for party']",
    "dateField": "//label[text()='Invoice Date']/following-sibling::button",
    "itemField": "//input[contains(@placeholder,'Enter Item Name')]",
    "discountBtn": "//button[contains(text(), 'Add Discount')]",
    "discountField": "//li/div/div/div/input",
    "taxBtn": "//button[contains(text(), 'Add Tax')]",
    "totalAmount": "//input[@name = 'totalAmount']",
    "paymentBtn": "//button[@id=':r1j:-form-item']",
    "receivedAmount": "//input[@name='receivedAmount']",
    "saveAddBtn": "//button[contains(.,'Save & Add New')]",
}

items = item_list_20
parties = party_list_20


def wait_for_element(driver, xpath, timeout=10):
    return WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located((By.XPATH, xpath))
    )


def fill_item_details(driver, index, item_count):
    item_field = wait_for_element(
        driver, f"//input[contains(@name,'invoiceItems.{index}.name')]"
    )
    item_field.send_keys(Keys.DOWN * index)
    item_field.send_keys(Keys.ENTER)

    qty = wait_for_element(
        driver, f"(//div[@class='relative h-full']//input)[{index + 1}]"
    )
    qty.send_keys(round(random.uniform(1, 25), 2))

    rate = wait_for_element(
        driver,
        f"(//span[contains(@class,'absolute text-default')]/following-sibling::input)[{item_count}]",
    )
    rate.clear()
    rate.send_keys(round(random.uniform(1, 30), 2))

    return item_count + 2


def apply_discount(driver, index):
    discount = wait_for_element(driver, f"//tr[{index + 1}]/td[4]/div/div[1]/input")
    discount.send_keys(round(random.uniform(0, 100), 2))


def create_transaction(driver, link, count, is_quotation=False):
    driver.get(link)
    for _ in range(count):
        time.sleep(3)
        bill_to = wait_for_element(driver, locators["billToField"])
        party = random.choice(parties)
        bill_to.send_keys(party)
        time.sleep(1)
        bill_to.send_keys(Keys.ENTER)

        item_count = 1
        for i in range(random.randint(1, len(items) - 1)):
            prob = random.uniform(0, 1)
            item_count = fill_item_details(driver, i, item_count)
            if prob > 0.8:
                apply_discount(driver, i)

        if random.uniform(0, 1) > 0.5:
            overall_discount_btn = wait_for_element(driver, locators["discountBtn"])
            overall_discount_btn.click()
            overall_discount_field = wait_for_element(driver, locators["discountField"])
            overall_discount_field.send_keys(round(random.uniform(0, 100), 2))

        if random.uniform(0, 1) > 0.3:
            tax_btn = wait_for_element(driver, locators["taxBtn"])
            tax_btn.click()

        total_amount = wait_for_element(driver, locators["totalAmount"]).get_attribute(
            "value"
        )
        if is_quotation is not True:
            received_amount = wait_for_element(driver, locators["receivedAmount"])
            if random.uniform(0, 1) > 0.6:
                received_amount.send_keys(total_amount)
            else:
                received_amount.send_keys(
                    round(random.uniform(0, float(total_amount)), 2)
                )

        save_add_btn = wait_for_element(driver, locators["saveAddBtn"], timeout=20)
        save_add_btn.click()
        print(f"- {party} \t {total_amount}")
