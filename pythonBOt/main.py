from logging import setLoggerClass
import random
import time

from datetime import datetime

from selenium.webdriver import Chrome

from selenium.webdriver.support.select import Select

file = open('Input/input.txt', 'r')
out = open('Output/out.txt', 'w')

# open page

driver = Chrome(r'Driver/chromedriver.exe')

link = "https://www.supremenewyork.com/shop/all/" + file.readline().strip()

driver.get(link)

keyword = '"' + file.readline().strip() + '"'
size1 = file.readline().strip()
size2 = file.readline().strip()
name_src = file.readline().strip()
mail_src = file.readline().strip()
phone_src = file.readline().strip()
house_src = file.readline().strip()
city_src = file.readline().strip()
postcode_src, country_src = file.readline().strip().split()
number_src = file.readline().strip()
month_src = file.readline().strip()
year_src = file.readline().strip()
cvv_src = file.readline().strip()


def find_thing():
    thing = driver.find_element_by_xpath(
        f'//a[contains(text(), {keyword})]'
    )
    thing.click()





def size_select():

    script = f'let sel = document.getElementById("size"); let f = 1; \
        for (option of sel.options) {{ if (option.value == "{size1}") {{sel.selectedIndex = option.index; f=0}} }}; \
            if (f) {{ for (option of sel.options) {{ if (option.value == "{size2}") {{sel.selectedIndex = option.index;}} }} }}'
    
    if size1 != 'No size':
       driver.execute_script(script)
        
        

def checkout():
    add = 0
    while add == 0:
        try:
            add = driver.find_element_by_name('commit')
        except:
            continue
    add.click()


thing = 10
while thing == 10:
    try:
        thing = driver.find_element_by_xpath(
            f'//a[contains(text(), {keyword})]'
        )
        thing.click()
    except:
        thing = 10
        driver.refresh()
    time.sleep(random.randint(1, 2))

time_start_drop = datetime.now().time()
start = time.time()
print(f'Start drop {time_start_drop}')
out.write(f'Start drop {time_start_drop}' + '\n')


size_select()
checkout()
time.sleep(0.5)

driver.get('https://www.supremenewyork.com/checkout')


def fill_forms():
    script = f'document.getElementById("order_billing_name").value = "{name_src}"; document.getElementById("order_email").value = "{mail_src}"; \
        document.getElementById("order_tel").value = "{phone_src}"; document.getElementById("bo").value = "{house_src}"; \
            document.getElementById("order_billing_city").value = "{city_src}"; document.getElementById("order_billing_zip").value = "{postcode_src}"; \
                document.getElementById("cnb").value = "{number_src}"; document.getElementById("vval").value = "{cvv_src}"; \
                    sel = document.getElementById("order_billing_country"); \
                        for (option of sel.options) {{ if (option.value == "{country_src}") {{sel.selectedIndex = option.index}} }} \
                            sel = document.getElementById("credit_card_month"); \
                                for (option of sel.options) {{ if (option.value == "{month_src}") {{sel.selectedIndex = option.index}} }} \
                                    sel = document.getElementById("credit_card_year"); \
                                        for (option of sel.options) {{ if (option.value == "{year_src}") {{sel.selectedIndex = option.index}} }}'
    driver.execute_script(script)

    # name = driver.find_element_by_name('order[billing_name]')
    # name.send_keys(file.readline().strip())
    # mail = driver.find_element_by_name('order[email]')
    # mail.send_keys(file.readline().strip())
    # tel = driver.find_element_by_name('order[tel]')
    # tel.send_keys(file.readline().strip())
    # adress = driver.find_element_by_name('order[billing_address]')
    # adress.send_keys(file.readline().strip())
    # city = driver.find_element_by_name('order[billing_city]')
    # city.send_keys(file.readline().strip())
    # post = driver.find_element_by_name('order[billing_zip]')
    # post.send_keys(file.readline().strip())
    # card = driver.find_element_by_name('credit_card[cnb]')
    # card.send_keys(file.readline().strip())
    # card_month = driver.find_element_by_id('credit_card_month')
    # card_month_object = Select(card_month)
    # card_month_object.select_by_value(month_src)
    # card_year = driver.find_element_by_id('credit_card_year')
    # card_year_object = Select(card_year)
    # card_year_object.select_by_value(year_src)
    # cvv = driver.find_element_by_name('credit_card[ovv]')
    # cvv.send_keys(file.readline().strip())

        

def submit():
    agree = driver.find_elements_by_class_name("iCheck-helper")
    agree[1].click()
    but = driver.find_element_by_name("commit")
    but.click()



fill_forms()
time.sleep(1)
submit()

time_stop_bot = datetime.now().time()

print(f'End bot {time_stop_bot}')
out.write(f'End bot {time_stop_bot}' + '\n')
end = time.time()
print(f'Timing {round(end - start, 2)}')
out.write(f'Timing {round(end - start, 2)}' + '\n')
out.close()