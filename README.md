# Scraping_web_otomotif
Program ini adalah sebuah web scraping program yang menggunakan Selenium untuk mengambil data kendaraan dari halaman web https://www.carsome.id/beli-mobil-bekas?budget=150000000&year=2020,2022. Berikut adalah ringkasan fungsionalitas utamanya:

1. Menggunakan Selenium WebDriver untuk mengotomatisasi interaksi dengan browser web.
2. Membuka URL situs web yang akan di-scrape.
3. Menunggu beberapa detik untuk memastikan halaman telah dimuat sepenuhnya.
4. Membuat fungsi `scrape_cars(driver)` untuk mengambil data kendaraan dari halaman web.
5. Dalam fungsi `scrape_cars`, menggunakan XPath untuk menemukan dan mengekstrak informasi dari elemen-elemen HTML yang mengandung data kendaraan.
6. Setiap informasi yang diambil (nama, model tahun, tipe, lokasi, harga kredit, dan harga tunai) disimpan dalam kamus Python sebagai objek `car_info`.
7. Semua objek `car_info` dikumpulkan dalam bentuk list `cars`.
8. Setelah scraping selesai, menutup browser.
9. Data yang dikumpulkan kemudian disimpan dalam DataFrame pandas.
10. DataFrame pandas kemudian disimpan dalam file Excel dengan nama "data_kendaraan.xlsx".
11. Program mencetak pesan konfirmasi ke konsol bahwa data telah berhasil disimpan dalam file Excel.

Program ini memanfaatkan Selenium untuk menavigasi halaman web dan mengekstrak data, serta menggunakan pandas untuk mengelola data dan menyimpannya dalam format file yang diinginkan.
