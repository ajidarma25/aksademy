# Tuple kategori barang (tetap)
kategori = ("Makanan", "Minuman", "Alat Rumah Tangga", "Elektronik")

# List untuk menyimpan daftar belanja
daftar_belanja = []

def tampilkan_menu():
    print("\n=== Menu Daftar Belanja ===")
    print("1. Tambah Barang")
    print("2. Lihat Daftar Belanja")
    print("3. Slicing Daftar Belanja")
    print("4. Hapus Barang")
    print("5. Edit Barang")
    print("6. Search Barang")
    print("7. Save ke TXT")
    print("8. Load dari TXT")
    print("9. Keluar")

def tambah_barang():
    print("\nPilih kategori:")
    for i, k in enumerate(kategori):
        print(f"{i}. {k}")
    try:
        kategori_index = int(input("Masukkan nomor kategori: "))
        nama_barang = input("Masukkan nama barang: ")
        if 0 <= kategori_index < len(kategori):
            daftar_belanja.append((nama_barang, kategori[kategori_index]))
            print(f"{nama_barang} ditambahkan ke daftar belanja.")
        else:
            print("Kategori tidak valid!")
    except ValueError:
        print("Input harus berupa angka!")

def tampilkan_belanja():
    print("\n=== Daftar Belanja ===")
    if not daftar_belanja:
        print("Belum ada barang.")
    else:
        for i, item in enumerate(daftar_belanja):
            print(f"{i+1}. {item[0]} ({item[1]})")

def slicing_belanja():
    if not daftar_belanja:
        print("Daftar belanja kosong.")
        return
    try:
        start = int(input("Index mulai (0): "))
        end = int(input("Index akhir: "))
        potongan = daftar_belanja[start:end]
        print("\n=== Hasil Slicing ===")
        for i, item in enumerate(potongan):
            print(f"{i+1}. {item[0]} ({item[1]})")
    except ValueError:
        print("Input harus berupa angka!")

def hapus_barang():
    tampilkan_belanja()
    if not daftar_belanja:
        return
    try:
        index = int(input("Masukkan nomor barang yang ingin dihapus: ")) - 1
        if 0 <= index < len(daftar_belanja):
            barang = daftar_belanja.pop(index)
            print(f"{barang[0]} berhasil dihapus dari daftar belanja.")
        else:
            print("Nomor barang tidak valid!")
    except ValueError:
        print("Input harus berupa angka!")

def edit_barang():
    tampilkan_belanja()
    if not daftar_belanja:
        return
    try:
        index = int(input("Masukkan nomor barang yang ingin diedit: ")) - 1
        if 0 <= index < len(daftar_belanja):
            nama_baru = input("Masukkan nama baru (kosongkan jika tidak diubah): ")
            print("\nPilih kategori baru (kosongkan jika tidak diubah):")
            for i, k in enumerate(kategori):
                print(f"{i}. {k}")
            kategori_input = input("Masukkan nomor kategori: ")

            nama_lama, kategori_lama = daftar_belanja[index]

            if nama_baru.strip():
                nama_lama = nama_baru

            if kategori_input.strip():
                try:
                    kategori_index = int(kategori_input)
                    if 0 <= kategori_index < len(kategori):
                        kategori_lama = kategori[kategori_index]
                    else:
                        print("Kategori tidak valid, tetap menggunakan kategori lama.")
                except ValueError:
                    print("Input kategori harus berupa angka, tetap menggunakan kategori lama.")

            daftar_belanja[index] = (nama_lama, kategori_lama)
            print("Barang berhasil diperbarui.")
        else:
            print("Nomor barang tidak valid!")
    except ValueError:
        print("Input harus berupa angka!")

def search_barang():
    if not daftar_belanja:
        print("Daftar belanja kosong.")
        return
    keyword = input("Masukkan nama barang yang dicari: ").lower()
    hasil = [item for item in daftar_belanja if keyword in item[0].lower()]
    print("\n=== Hasil Pencarian ===")
    if hasil:
        for i, item in enumerate(hasil):
            print(f"{i+1}. {item[0]} ({item[1]})")
    else:
        print("Barang tidak ditemukan.")

def save_txt():
    try:
        with open("daftar_belanja.txt", "w") as f:
            for item in daftar_belanja:
                f.write(f"{item[0]},{item[1]}\n")
        print("Daftar belanja berhasil disimpan ke 'daftar_belanja.txt'.")
    except Exception as e:
        print("Terjadi kesalahan saat menyimpan:", e)

def load_txt():
    try:
        with open("daftar_belanja.txt", "r") as f:
            daftar_belanja.clear()
            for line in f:
                data = line.strip().split(",")
                if len(data) == 2:
                    daftar_belanja.append((data[0], data[1]))
        print("Daftar belanja berhasil dimuat dari 'daftar_belanja.txt'.")
    except FileNotFoundError:
        print("File 'daftar_belanja.txt' tidak ditemukan.")
    except Exception as e:
        print("Terjadi kesalahan saat memuat:", e)

# --- Program utama ---
while True:
    tampilkan_menu()
    pilihan = input("Pilih menu: ")
    if pilihan == "1":
        tambah_barang()
    elif pilihan == "2":
        tampilkan_belanja()
    elif pilihan == "3":
        slicing_belanja()
    elif pilihan == "4":
        hapus_barang()
    elif pilihan == "5":
        edit_barang()
    elif pilihan == "6":
        search_barang()
    elif pilihan == "7":
        save_txt()
    elif pilihan == "8":
        load_txt()
    elif pilihan == "9":
        print("Program selesai. Terima kasih!")
        break
    else:
        print("Pilihan tidak valid.")
