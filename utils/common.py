def select_date(driver, date):
    """Selects date from the calendar."""
    locaters = {
        "left": "//div[contains(@class,'pt-1 justify-center')]//button[1]",
        "right": "//div[contains(@class,'pt-1 justify-center')]//button[2]",
        "date": "//div[@class='grid grid-cols-7']",
        "yearMonth": "//div[contains(@class,'text-14 text-default')]",
    }
    year, month, day = date.split("-")


select_date("driver", "2021-Magh-1")
