from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import pandas as pd
import time

# Fungsi untuk mendapatkan data kendaraan dari halaman
def scrape_cars(driver):
    cars = []
    # Temukan semua elemen yang mengandung data kendaraan
    car_elements = driver.find_elements(By.XPATH, "//div[@class='list-card__item']")
    for car_element in car_elements:
        # Mendapatkan informasi yang diperlukan dari setiap elemen kendaraan
        car_info = {}
        # Mencoba menemukan elemen nama, jika tidak ditemukan, akan diberikan nilai 'Tidak ditemukan'
        try:
            car_info['Nama'] = car_element.find_element(By.XPATH, ".//a[contains(@class, 'mod-b-card__title')]/p[2]").text
        except:
            car_info['Nama'] = 'Tidak ditemukan'
        
        try:
            car_info['Model_Tahun'] = car_element.find_element(By.XPATH, ".//a[contains(@class, 'mod-b-card__title')]/p[1]").text
        except:
            car_info['Model_Tahun'] = 'Tidak ditemukan'
        
        try:
            car_info['Tipe'] = car_element.find_element(By.XPATH, ".//div[contains(@class, 'mod-b-card__car-other')]/span[2]").text
        except:
            car_info['Tipe'] = 'Tidak ditemukan'
                
        try:
            car_info['Lokasi'] = car_element.find_element(By.XPATH, ".//div[contains(@class, 'mod-b-card__car-other')]/span[3]").text
        except:
            car_info['Lokasi'] = 'Tidak ditemukan'
        
        try:
            car_info['Harga-Credit'] = car_element.find_element(By.XPATH, ".//div[contains(@class, 'mod-card__price')]/strong").text
        except:
            car_info['Harga-Credit'] = 'Tidak ditemukan'
        
        try:
            # Coba cari elemen div, kemudian ambil teksnya
            car_info['Harga-Cash'] = car_element.find_element(By.XPATH, ".//div[contains(@class, 'mod-card__price-cash')]").text
        except NoSuchElementException:
            # Tangani kasus di mana elemen tidak ditemukan
            car_info['Harga-Cash'] = 'Tidak ditemukan'

        cars.append(car_info)
    return cars

# Membuat instance WebDriver (Chrome)
driver = webdriver.Chrome()

# URL situs web untuk scraping
url = "https://www.carsome.id/beli-mobil-bekas?budget=150000000&year=2020,2022"

# Buka URL dalam browser
driver.get(url)

# Tunggu beberapa saat agar halaman dimuat sepenuhnya
time.sleep(5)

# Scraping data kendaraan dari halaman
cars_data = scrape_cars(driver)

# Menutup browser setelah selesai scraping
driver.quit()

# Menyimpan data ke dalam DataFrame pandas
df = pd.DataFrame(cars_data)

# Menyimpan data ke dalam file Excel
file_path = "data_kendaraan.xlsx"
df.to_excel(file_path, index=False)

print("Data telah berhasil disimpan dalam file Excel:", file_path)
