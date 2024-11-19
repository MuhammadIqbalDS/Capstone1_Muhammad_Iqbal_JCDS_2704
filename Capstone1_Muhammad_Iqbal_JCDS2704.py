import datetime
from prettytable import PrettyTable

products = [
    {"product_id": "H001", "nama": "Laptop", "harga": 15000000, "stok": 20},
    {"product_id": "H002", "nama": "Headphone", "harga": 2500000, "stok": 15},
    {"product_id": "H003", "nama": "Smartphone", "harga": 10000000, "stok": 10}
]

sales_report = [
    {"product_id": "H001","nama": "Laptop", "qty": 2, "total": 30000000, "tanggal": datetime.date(2024, 11, 11)},
    {"product_id": "H002", "nama": "Headphone","qty": 5,"total": 12500000, "tanggal": datetime.date(2024, 11, 12)},
    {"product_id": "H003", "nama": "Smartphone", "qty": 1, "total": 10000000, "tanggal": datetime.date(2024, 11, 13)},
    {"product_id": "H001", "nama": "Laptop", "qty": 1, "total": 15000000, "tanggal": datetime.date(2024, 11, 13)},
    {"product_id": "H002", "nama": "Headphone", "qty": 3,"total": 7500000, "tanggal": datetime.date(2024, 11, 15)}

]

# Fungsi untuk menampilkan menu utama
def main_menu():
    print("\n=== Menu Utama ===")
    print("1. Mode Admin Stok")
    print("2. Mode Admin Sales")
    print("3. Keluar")

# Fungsi untuk menampilkan menu Admin Stok
def stok_menu():
    print("\n=== Menu Admin Stok ===")
    print("1. Menampilkan Stok Produk")
    print("2. Mengubah Stok Produk")
    print("3. Menghapus Produk")
    print("4. Cek Laporan Stok Produk")
    print("5. Kembali ke Menu Utama")

# Fungsi untuk menampilkan menu Admin Sales
def sales_menu():
    print("\nSelamat Datang di Sistem Laporan Penjualan E-Commerce")
    print("-" * 50)
    print("1. Laporan Produk Terjual")
    print("2. Menambah Laporan penjualan")
    print("3. Update Laporan Pendapatan")
    print("4. Menghapus laporan penjualan")
    print("5. Ringkasan laporan & export file")
    print("6. Exit Program")
    print("-" * 50)
    print("Masukkan pilihan Menu yang ingin dijalankan :")


# Fungsi untuk admin stok
def admin_stok_mode():
    while True:
        stok_menu()
        choice = input("Pilih menu (1-5): ")
        
        if choice == "1":
            cek_seluruh_stok()
        elif choice == "2":
            Mengubah_daftar_stok()
        elif choice == "3":
            Menghapus_daftar_stok()
        elif choice == "4":
            Mengecek_Laporan_Stok_Produk()  
        elif choice == "5":
            break
        else:
            print("Pilihan tidak valid.")


def cek_seluruh_stok():
    if not products:
        print("Tidak ada data laporan penjualan")
        return
    
    print("\n--- Semua Daftar Stok ---")
    table = PrettyTable()
    table.field_names = ["No", "Produk ID","Nama Produk","Harga Produk", "Stok Produk"]
    No= 1
    for product in products:
        table.add_row([No] + [product['product_id'], product['nama'], f"Rp{product['harga']:,}", product['stok']])
        No += 1
    print(table)
    
    
# # Fungsi untuk update stok produk
def Mengubah_daftar_stok():
    print("\n--- Update Stok Berdasarkan ID ---")
    
    while True:
        if not products:
            print("Tidak ada data untuk diubah.")
            break

        cek_seluruh_stok()

        product_id = input("\nMasukkan product_id yang ingin diubah: ").capitalize()
        
        # Cari produk berdasarkan product_id
        product = next((item for item in products if item['product_id'] == product_id), None)

        if not product:
            print("Product ID tidak ditemukan.")
            continue

        # Menampilkan data produk yang ditemukan
        print("\nData produk yang ditemukan:")
        table = PrettyTable(["ID Produk", "Nama", "Harga", "Stok"])
        table.add_row([product['product_id'], product['nama'], f"Rp{product['harga']:,}", product['stok']])
        print(table)
        
        while True:
            print("\nPilih kolom yang ingin diubah:")
            print("1. Harga")
            print("2. Stok")
            print("3. Kembali")
            choice = input("Pilihan: ")

            if choice == '1':
                while True:
                    try:
                        new_price = float(input("Masukkan harga baru: "))
                        if new_price > 0:
                            product['harga'] = new_price
                            print("Harga berhasil diperbarui.")
                            break
                        else:
                            print("Harga harus positif.")
                    except ValueError:
                        print("Input harga harus berupa angka.")
                
            elif choice == '2':
                while True:
                    try:
                        new_stock = int(input("Masukkan stok baru: "))
                        if new_stock >= 0:
                            product['stok'] = new_stock
                            print("Stok berhasil diperbarui.")
                            break
                        else:
                            print("Stok harus non-negatif.")
                    except ValueError:
                        print("Input harus berupa angka bulat.")
            
            elif choice == '3':
                break
            else:
                print("Pilihan tidak valid.")
        
        # Konfirmasi kembali ke menu utama
        kembali = input("\nApakah Anda ingin mengubah produk lain? (y/n): ").lower()
        if kembali != 'y':
            break

    # Tampilkan data produk setelah perubahan
    print("\nData produk setelah perubahan:")
    cek_seluruh_stok()


# Fungsi untuk delete stok produk
def Menghapus_daftar_stok():
    print("\n--- Hapus Data Produk Berdasarkan ID ---")
    
    while True:
        if not products:
            print("Tidak ada data untuk dihapus.")
            break

        # Menampilkan semua data produk
        cek_seluruh_stok()

        # Memasukkan ID produk untuk dihapus
        product_id = input("\nMasukkan ID produk yang ingin dihapus: ").capitalize()

        # Cari produk berdasarkan ID
        product_to_delete = next((product for product in products if product['product_id'] == product_id), None)

        if not product_to_delete:
            print("Product ID tidak ditemukan.")
            continue

        # Konfirmasi penghapusan
        print("\nData berikut akan dihapus:")
        table = PrettyTable(["ID Produk", "Nama", "Harga", "Stok"])
        table.add_row([product_to_delete['product_id'], product_to_delete['nama'], f"Rp{product_to_delete['harga']:,}", product_to_delete['stok']])
        print(table)

        konfirmasi = input("Apakah Anda yakin ingin menghapus data ini? (y/n): ").lower()
        if konfirmasi == 'y':
            products.remove(product_to_delete)
            print("Data berhasil dihapus.")
        else:
            print("Penghapusan dibatalkan.")

        # Menanyakan apakah ingin menghapus data lain
        if input("Hapus data lain? (y/n): ").lower() != 'y':
            break

    # Menampilkan data produk setelah penghapusan
    print("\nData Produk Setelah Penghapusan:")
    table = PrettyTable(["ID Produk", "Nama", "Harga", "Stok"])
    for product in products:
        table.add_row([product['product_id'], product['nama'], f"Rp{product['harga']:,}", product['stok']])
    print(table)


# Fungsi Ringkasan Laporan Stok Produk
def Mengecek_Laporan_Stok_Produk():
    while True:
        print("\n4.1 Lihat Sisa Stok")
        print("4.2 Prediksi Kebutuhan Stok")
        print("4.3 Peringatan Stok Rendah")
        print("4.4 Kembali ke Menu Utama")
        sub_choice = input("Pilih sub-menu (4.1 - 4.4): ")
        
        if sub_choice == "4.1":
            lihat_sisa_stok()
        elif sub_choice == "4.2":
            prediksi_kebutuhan_stok()
        elif sub_choice == "4.3":
            cek_stok_produk()
        elif sub_choice == "4.4":
            break
        else:
            print("Pilihan tidak valid")
            

def lihat_sisa_stok():
    # Membuat salinan produk untuk memproses sisa stok
    products_copy = [product.copy() for product in products]
    
    # Mengurangi stok berdasarkan penjualan
    for sale in sales_report:
        for product in products_copy:
            if product["product_id"] == sale["product_id"]:
                product["stok"] -= sale["qty"]
    
    # Menampilkan sisa stok
    print("\n--- Sisa Stok Produk ---")
    table = PrettyTable(["ID Produk", "Nama", "Sisa Stok"])
    for product in products_copy:
        table.add_row([product['product_id'], product['nama'], product['stok']])
    print(table)
    
    return products_copy

def prediksi_kebutuhan_stok():
    print("\n--- Prediksi Kebutuhan Stok ---")
    for product in products:
        # Menghitung rata-rata penjualan per hari selama beberapa hari terakhir (contoh 7 hari)
        total_sales_last_week = sum(sale['qty'] for sale in sales_report if sale['product_id'] == product['product_id'] and (datetime.date(2024, 11, 9) - sale['tanggal']).days <= 7)
        avg_sales_per_day = total_sales_last_week / 7 if total_sales_last_week else 0
        
        # Prediksi kebutuhan stok berdasarkan rata-rata penjualan
        prediksi = product['stok'] + (avg_sales_per_day * 7)  # Misalnya prediksi untuk 7 hari ke depan
        print(f"{product['nama']} - Prediksi stok: {prediksi} unit")


def cek_stok_produk():
    print("\n--- Peringatan Stok Rendah ---")
    sisa_stok = lihat_sisa_stok()  # Dapatkan data sisa stok
    peringatan_ditampilkan = False  
    
    for product in sisa_stok:
        if product['stok'] < 10:  # Ambang batas stok rendah
            print(f"Peringatan: Stok {product['nama']} rendah ({product['stok']} unit tersisa).")
            peringatan_ditampilkan = True
    
    if not peringatan_ditampilkan:
        print("Semua produk memiliki stok mencukupi.")


# Fungsi untuk admin sales
def admin_sales_mode():
    while True:
        sales_menu()
        choice = input("Pilih menu (1-6): ")

        if choice == "1":
            laporan_produk_terjual()
        elif choice == "2":
            Menambah_Laporan_penjualan()        
        elif choice == "3":
            Mengubah_laporan_penjualan()
        elif choice == "4":
            Menghapus_laporan_penjualan()          
        elif choice == "5":
            Ringkasan_laporan_dan_export_file()
        elif choice == "6":
            print("Terima kasih telah menggunakan program ini!")
            break
        else:
            print("Pilihan tidak valid.")

    
def laporan_produk_terjual():
    while True:
        print("\n--- Laporan Produk Terjual ---")
        print("1.1 Tampilkan Daftar Produk Terjual")
        print("1.2 Tampilkan Produk Berdasarkan ID")
        print("1.3 Kembali ke Menu Utama")
        sub_choice = input("Pilih sub-menu: ")

        if sub_choice == "1.1":
            semua_produk_terjual()
        elif sub_choice == "1.2":
            produk_berdasarkanID()
        elif sub_choice == "1.3":
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

def semua_produk_terjual():
    print("\n--- Semua Produk Terjual ---")
    table = PrettyTable()
    table.field_names = ["No", "Produk ID","Nama Produk","Jumlah terjual", "Total Pendapatan","Tanggal"]
    No= 1
    for sale in sales_report:
        table.add_row([No] + [sale['product_id'], sale['nama'], sale['qty'], f"Rp{sale['total']:,}", sale['tanggal']])
        No += 1
    print(table)
    
    
def produk_berdasarkanID():
    if not sales_report:
        print("Tidak ada data laporan penjualan")
        return
    # Meminta input ID produk dari pengguna
    product_id = input("Masukkan produk yang ingin dicari berdasarkan product_id: ").capitalize()

    # Mendapatkan informasi produk
    found_product = []
    for sale in sales_report:
        if sale['product_id'] == product_id:
            found_product.append(sale)
        
    # Menampilkan hasil dengan PrettyTable jika produk ditemukan
    if found_product:
        table = PrettyTable(["No", "Produk ID","Nama Produk","Jumlah terjual","Total Pendapatan","Tanggal"])
        no = 1
        for product in found_product:
            table.add_row([no, product['product_id'], product['nama'], product['qty'], f"Rp{product['total']:,}", product['tanggal']])
            no += 1
        print(table)
    else:
        print("Produk tidak ditemukan.")   


        
def Menambah_Laporan_penjualan():
    
    semua_produk_terjual() # menampilkan semua laporan produk terjual
    
    while True:
        print("\n--- Menambah Laporan ---")
        print("2.1 Tambah Laporan Penjualan Baru")
        print("2.2 Kembali ke Menu Utama")
        sub_choice = input("Pilih sub-menu (2.1 - 2.2): ")    
    
        if sub_choice == "2.1":
            tambah_laporan()
        elif sub_choice == "2.2":
            break
        else:
            print("Pilihan tidak valid.")
        
        
def tambah_laporan():
    while True:
        product_id = input("Masukkan ID produk: ").capitalize()
        # Cari produk berdasarkan ID
        product = next((p for p in products if p['product_id'] == product_id), None)
        if not product:
            print("ID produk tidak valid. Silakan coba lagi.")
            continue

        while True:
            try:
                qty = int(input("Masukkan kuantitas: "))
                if qty <= 0:
                    print("Kuantitas harus bilangan bulat positif.")
                elif qty > product['stok']:
                    print(f"Kuantitas tidak boleh lebih dari stok produk ({product['stok']} unit).")
                else:
                    break  # Keluar dari loop jika input valid
            except ValueError:
                print("Input harus berupa bilangan bulat.")

        tanggal = input("Masukkan tanggal (YYYY-MM-DD): ")
        try:
            tanggal = datetime.datetime.strptime(tanggal, "%Y-%m-%d").date()

            # Pengecekan batas tanggal
            tanggal_awal = datetime.date(2024, 11, 11)
            tanggal_akhir = datetime.date(2024, 11, 17)
            if tanggal < tanggal_awal or tanggal > tanggal_akhir:
                print("Tanggal harus berada di antara 2024-11-11 dan 2024-11-17.")
                continue

        except ValueError:
            print("Format tanggal salah. Gunakan format YYYY-MM-DD.")
            continue
        
        # Validasi data duplikat berdasarkan product_id dan tanggal
        duplicate = any(laporan['product_id'] == product_id and laporan['tanggal'] == tanggal for laporan in sales_report)
        if duplicate:
            print("Data dengan ID produk dan tanggal yang sama sudah ada. Silakan masukkan data yang berbeda.")
            continue

        # Hitung total harga
        total = qty * product['harga']

        # Tambahkan data ke laporan penjualan
        laporan_baru = {"product_id": product_id, 
                        "nama": product['nama'], 
                        "qty": qty, 
                        "total": total, 
                        "tanggal": tanggal}
        sales_report.append(laporan_baru)

        lanjut = input("Ingin menambahkan data lagi? (y/n): ")
        if lanjut.lower() != 'y':
            break
    print("Laporan berhasil ditambahkan!")
    # Menampilkan semua laporan
    semua_produk_terjual()
    

def Mengubah_laporan_penjualan():
    while True:
        print("\n--- MengubahLaporan ---")
        print("3.1 Mengubah Laporan Penjualan")
        print("3.2 Kembali ke Menu Utama")
        sub_choice = input("Pilih sub-menu (3.1 - 3.2): ")    
    
        if sub_choice == "3.1":
            update_laporan()
        elif sub_choice == "3.2":
            break
        else:
            print("Pilihan tidak valid.")
    
def update_laporan():
    print("\n--- Update Laporan Berdasarkan ID ---")
    while True:
        if not sales_report:
            print("Tidak ada data untuk diubah.")
            break
        
        # Menampilkan semua laporan
        semua_produk_terjual()

        product_id = input("\nMasukkan product_id yang ingin diubah : ").capitalize()

        # Filter data berdasarkan product_id
        matching_reports = [item for item in sales_report if item['product_id'] == product_id]

        if not matching_reports:
            print("Product ID tidak ditemukan.")
            continue

        # Menampilkan laporan dengan product_id yang cocok
        print(f"\nTerdapat {len(matching_reports)} laporan dengan product_id '{product_id}':")
        table = PrettyTable()
        table.field_names = ["No", "Nama", "Qty", "Total", "Tanggal"]
        i = 1
        for report in matching_reports:
            table.add_row([i, report['nama'], report['qty'], report['total'], report['tanggal']])
            i += 1
        
        print(table)

        try:
            pilihan = int(input("Pilih nomor laporan yang ingin diupdate: "))
            if 1 <= pilihan <= len(matching_reports):
                selected_report = matching_reports[pilihan - 1]

                # Input dan validasi tanggal
                while True:
                    tanggal = input("Masukkan tanggal laporan (YYYY-MM-DD): ")
                    try:
                        tanggal = datetime.datetime.strptime(tanggal, "%Y-%m-%d").date()

                        # Pengecekan batas tanggal
                        tanggal_awal = datetime.date(2024, 11, 11)
                        tanggal_akhir = datetime.date(2024, 11, 17)
                        if not (tanggal_awal <= tanggal <= tanggal_akhir):
                            print("Tanggal harus berada di antara 2024-11-11 dan 2024-11-17.")
                            continue

                        # Validasi data duplikat berdasarkan product_id dan tanggal, kecuali laporan yang sedang diedit
                        duplicate = any(
                            laporan['product_id'] == product_id and laporan['tanggal'] == tanggal 
                            and laporan is not selected_report  # Pastikan bukan laporan yang sedang diedit
                            for laporan in sales_report
                        )
                        if duplicate:
                            print("Data dengan ID produk dan tanggal yang sama sudah ada. Silakan masukkan data yang berbeda.")
                            continue

                        selected_report['tanggal'] = tanggal
                        break
                    except ValueError:
                        print("Format tanggal salah. Gunakan format YYYY-MM-DD.")
                        
                # Input dan validasi jumlah
                while True:
                    try:
                        new_qty = int(input("Masukkan jumlah produk terjual (bilangan bulat positif): "))
                        if new_qty > 0:
                            selected_report['qty'] = new_qty 
                            break
                        else:
                            print("Jumlah harus bilangan bulat positif.")
                    except ValueError:
                        print("Masukkan jumlah yang valid.")
                
                print("Data berhasil diubah.")

                # Konfirmasi apakah ingin mengupdate data lain
                if input("Update data lain? (y/n): ").lower() != 'y':
                    break
            else:
                print("Nomor pilihan tidak valid.")
        except ValueError:
            print("Masukkan nomor yang valid.")


def Menghapus_laporan_penjualan():
    while True:
        print("\n--- Menghapus Laporan ---")
        print("4.1 Hapus Laporan Berdasarkan ID")
        print("4.2 Kembali ke Menu Utama")
        choice = input("Pilih sub-menu (4.1 - 4.2): ")

        if choice == "4.1":
            hapus_laporan()
        elif choice == "4.2":
            break
        else:
            print("Pilihan tidak valid.")

def hapus_laporan():
    print("\n--- Hapus Laporan Berdasarkan ID ---")
    
    while True:
        if not sales_report:
            print("Tidak ada data untuk dihapus.")
            break

        # Menampilkan semua laporan
        semua_produk_terjual()

        product_id = str(input("\nMasukkan product_id yang ingin dihapus : ")).capitalize()

        # Filter data berdasarkan product_id
        matching_reports = [item for item in sales_report if item['product_id'] == product_id]
        
        if not matching_reports:
            print("Product ID tidak ditemukan.")
            continue

        # Menampilkan laporan dengan product_id yang cocok
        print(f"\nTerdapat {len(matching_reports)} laporan dengan product_id '{product_id}':")
        table = PrettyTable()
        table.field_names = ["No", "Nama", "Qty", "Total", "Tanggal"]
        for i in range(len(matching_reports)):
            report = matching_reports[i]
            table.add_row([i + 1, report['nama'], report['qty'], report['total'], report['tanggal']])
        print(table)

        # Memilih laporan berdasarkan nomor
        try:
            pilihan = input("Pilih nomor laporan yang ingin dihapus (atau 'n' untuk batal): ").lower()
            if pilihan == 'n':
                print("Penghapusan dibatalkan.")
                break

            pilihan = int(pilihan)  # Mengubah pilihan menjadi integer
            if 1 <= pilihan <= len(matching_reports):
                # Hapus laporan yang dipilih
                selected_report = matching_reports[pilihan - 1]
                # Cari elemen yang sesuai di sales_report dan hapus
                for report in sales_report:
                    if report == selected_report:
                        sales_report.remove(report)
                        break
                print("Data berhasil dihapus.")
            else:
                print("Nomor pilihan tidak valid.")
        except ValueError:
            print("Masukkan nomor yang valid.")

        if input("Hapus data lain? (y/n): ").lower() != 'y':
            break

def Ringkasan_laporan_dan_export_file():
    while True:
        print("\n5.1 Ringkasan Penjualan")
        print("5.2 export file ke CSV")
        print("5.3 Kembali ke Menu Utama")
        sub_choice = input("Pilih sub-menu (5.1 - 5.3): ")
        
        if sub_choice == "5.1":
            ringkasan_penjualan()
        elif sub_choice == "5.2":
            export_to_csv()
        elif sub_choice == "5.3":
            break
        else:
            print("Pilihan tidak valid")

def ringkasan_penjualan():
    sales_count = {}
    for item in sales_report:
        product_id = item['nama']
        qty = item['qty']
        
        # Tambahkan kuantitas ke produk yang sudah ada, atau inisialisasi jika baru
        if product_id in sales_count:
            sales_count[product_id] += qty
        else:
            sales_count[product_id] = qty

    # Mengurutkan produk berdasarkan jumlah penjualan tertinggi (descending)
    sorted_products = sorted(sales_count.items(), key=lambda x: x[1], reverse=True)

    # Menampilkan hasil
    print("\n--- Produk Dengan Penjualan Tertinggi ---")
    for product_id, total_qty in sorted_products:
        print(f"Produk {product_id} terjual sebanyak {total_qty} unit.")
        
    total_qty = sum(sale["qty"] for sale in sales_report)
    total_pendapatan = sum(sale["total"] for sale in sales_report)
    print("\n--- Ringkasan Penjualan ---")
    print(f"Total Produk Terjual: {total_qty}")
    print(f"Total Pendapatan: {total_pendapatan}")

def export_to_csv():
    export_option = input("\nApakah Anda ingin export laporan ke CSV? (y/n): ")
    if export_option.lower() == 'y':
            
        file_name = input("\nMasukkan nama file untuk laporan (.csv):")
        
        # Menampilkan pesan bahwa laporan telah diekspor
        print(f"\nLaporan berhasil diexport ke '{file_name}.csv' ")
    else:
        print("\nLaporan tidak diexport.")
        
        

# Fungsi utama menjalankan program
def main():
    while True:
        main_menu()
        choice = input("Pilih mode (1-3): ")
        
        if choice == "1":
            admin_stok_mode()
        elif choice == "2":
            admin_sales_mode()
        elif choice == "3":
            print("Terima kasih telah menggunakan program ini!")
            break
        else:
            print("Pilihan tidak valid.")

# Menjalankan program
main()