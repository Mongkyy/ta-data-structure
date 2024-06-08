data_trans = []

class Node:
    def __init__(self, sku, nama_barang, harga_satuan, jumlah_stok):
        self.sku = sku
        self.nama_barang = nama_barang
        self.harga_satuan = harga_satuan
        self.jumlah_stok = jumlah_stok
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, sku, nama_barang, harga_satuan, jumlah_stok):
        new_node = Node(sku, nama_barang, harga_satuan, jumlah_stok)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while True:
            if sku == temp.sku:
                temp.nama_barang = nama_barang
                temp.harga_satuan = harga_satuan
                temp.jumlah_stok = jumlah_stok
                return True
            if sku < temp.sku:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

    def contains(self, sku):
        temp = self.root
        while temp is not None:
            if sku == temp.sku:
                return temp
            elif sku < temp.sku:
                temp = temp.left
            else:
                temp = temp.right
        return None

    def in_order_traversal(self, node, result):
        if node is not None:
            self.in_order_traversal(node.left, result)
            result.append(node)
            self.in_order_traversal(node.right, result)

    def get_data(self):
        result = []
        self.in_order_traversal(self.root, result)
        return result

def insertion_sort(data_trans, sub_total):
    for i in range(1, len(data_trans)):
        temp = data_trans[i]
        j = i - 1
        while j >= 0 and temp[sub_total] > data_trans[j][sub_total]:
            data_trans[j + 1] = data_trans[j]
            j -= 1
        data_trans[j + 1] = temp
    return data_trans

def input_data_stok_barang(bst):
    print("="*32)
    while True:
        sku = input("= Masukkan No.SKU: ")
        node = bst.contains(sku) #Mencari SKU inputan di BST agar tdk ada duplicate
        if len(sku) != 4 or node: #SKU harus 4 digit dan tak bole dup
            print("SKU Harus 4 digit, atau telah tersimpan")
            continue
        nama_barang = input("= Masukkan Nama Barang: ")
        harga_satuan = input("= Masukkan Harga Satuan (Rp): ")
        try:
            harga_satuan = float(harga_satuan) #Membuat harga menjadi berupa float
        except ValueError:
            print("Harga satuan harus berupa angka")
            continue
        try:
            jumlah_stok = int(input("= Masukkan Jumlah Stok: "))
        except ValueError:
            print("Jumlah stok harus berupa angka")
            continue
        bst.insert(sku, nama_barang, harga_satuan, jumlah_stok)
        print("Data barang berhasil disimpan")
        con_or_not = input("= Apakah anda ingin menambahkan lagi?(y/n): ").upper()
        if con_or_not == "Y": #Lanjut atau tidak?
            continue
        elif con_or_not == "N":
            print("=" * 32, "\n")
            break
        else:
            print("Pilihan tidak valid")

def restok_barang(bst):
    all_data = bst.get_data() #Mengambil data dari BST
    print("=" * 80,"\n= Data semua barang:")
    for data in all_data:
        print(f"SKU: {data.sku}, Nama Barang: {data.nama_barang}, Harga Satuan: Rp{data.harga_satuan}, Jumlah Stok: {data.jumlah_stok}")
    print("=" * 80)
    while True:
        cari_sku = input("= Masukkan SKU dari barang yang ingin di-restok: ")
        node = bst.contains(cari_sku) #Mencari inputan SKU di BST (tersimpan atau belum)
        if node: #Jika tersimpan SKU yang dicari di BST
            try:
                stok_baru = int(input("= Masukkan Jumlah Stok Baru yang ingin ditambahkan: "))
            except ValueError: #inputan stok harus angka
                print("Jumlah stok harus berupa angka")
                continue
            node.jumlah_stok += stok_baru
            print("Stok berhasil diperbarui")
            print("=" * 80, "\n")
            break
        else: #Jika tidak tersimpan SKU yang dicari di BST
            print("SKU tidak ditemukan")

def stok_barang(bst):
    while True:
        print("""====== Kelola Stok Barang ======
= 1. Input Data Stok Barang    =
= 2. Restok Barang             =
================================
= 0. Kembali ke Menu Utama     =
================================""")
        try:
            sub_pilihan = int(input("= Masukkan Pilihan anda(1/2/0): "))
            print("")
        except ValueError:
            print("Input tidak valid. Silahkan masukkan angka")
            continue
        if sub_pilihan == 1:
            input_data_stok_barang(bst)
        elif sub_pilihan == 2:
            restok_barang(bst)
        elif sub_pilihan == 0:
            break
        else:
            print("Pilihan tidak valid. Silahkan pilih kembali")

def input_data_transaksi_baru(bst):
    nama_konsumen = input("= Masukkan Nama Anda: ")
    while True:
        sku = input("= Masukkan SKU dari barang yang anda inginkan: ")
        node = bst.contains(sku) #mencari SKU inputan di BST
        if node: #jika terdapat SKU inputan di BST
            while True:
                try:
                    jumlah_beli = int(input("= Masukkan Jumlah barang yang ingin dibeli: "))
                except ValueError:
                    print("Jumlah beli harus berupa angka")
                    continue
                if node.jumlah_stok >= jumlah_beli:
                    node.jumlah_stok -= jumlah_beli
                    sub_total = node.harga_satuan * jumlah_beli
                    data_trans.append({"nama_konsumen": nama_konsumen, "sku": sku, "jumlah_beli": jumlah_beli, "sub_total": sub_total})
                    print("=" * 48 ,f"\nTransaksi berhasil: {jumlah_beli} {node.nama_barang} dengan subtotal Rp{sub_total}")
                    print("Data Transaksi Konsumen Berhasil Diinputkan")
                    return
                else:
                    print("Jumlah Stok No.SKU yang Anda beli tidak mencukupi")
                    con_or_not = input("= Apakah anda ingin melanjutkan transaksi (Y/N)? ").upper()
                    if con_or_not == "N":
                        return
        else:
            print("SKU tidak ditemukan")

def lihat_data_transaksi_konsumen():
    if not data_trans: #jika list data transaksi kosong
        print("\nBelum ada transaksi")
    print("=" * 48, "\n= Data Transaksi: ")
    for data in data_trans:
        print(f"= Nama Konsumen: {data['nama_konsumen']}, No. SKU barang yang dibeli: {data['sku']}, Jumlah Beli: {data['jumlah_beli']}, SubTotal: Rp{data['sub_total']}")
    print("=" * 48,"\n") 

def lihat_data_transaksi_berdasarkan_subtotal():
    if not data_trans: #jika list data transaksi kosong
        print("\nBelum ada transaksi")
        return
    sorted_data = insertion_sort(data_trans, sub_total='sub_total') #meng-sort list data_trans berdasarkan sub_total (asc)
    print("=" * 48, "\n= Data Transaksi Berdasarkan Subtotal: ")
    for data in sorted_data:
        print(f"= Nama Konsumen: {data['nama_konsumen']}, No. SKU barang yang dibeli: {data['sku']}, Jumlah Beli: {data['jumlah_beli']}, Sub Total: {data['sub_total']}")
    print("=" * 48,"\n") 

def transaksi_konsumen(bst):
    while True:
        print("""========== Kelola Transaksi Konsumen ===========
= 1. Input Data Transaksi Baru                 =
= 2. Lihat Data Seluruh Transaksi Konsumen     =
= 3. Lihat Data Transaksi Berdasarkan Subtotal =
================================================
= 0. Kembali ke Menu Utama                     =
================================================""")
        try:
            sub_pilihan = int(input("= Masukkan Pilihan Anda(1/2/3/0): "))
        except ValueError:
            print("Input tidak valid. Silahkan masukkan angka")
            continue
        print("")
        if sub_pilihan == 1:
            input_data_transaksi_baru(bst)
        elif sub_pilihan == 2:
            lihat_data_transaksi_konsumen()
        elif sub_pilihan == 3:
            lihat_data_transaksi_berdasarkan_subtotal()
        elif sub_pilihan == 0:
            break
        else:
            print("Pilihan tidak valid. Silahkan pilih kembali.")

def main_menu():
    bst = BinarySearchTree()
    print("=" * 32, "\n======== Selamat Datang ========")
    while True:
        print("""================================
= 1. Kelola Stok Barang        =
= 2. Kelola Transaksi Konsumen =
================================
= 0. Keluar                    =
================================""")
        try:
            pilih = int(input("= Masukkan pilihan anda(1/2/0): "))
        except ValueError:
            print("Input tidak valid. Silahkan masukkan angka")
            continue
        print("")
        
        if pilih == 1:
            stok_barang(bst)
        elif pilih == 2:
            transaksi_konsumen(bst)
        elif pilih == 0:
            print("Terimakasih <3, By Zakki Farian")
            break
        else:
            print("Pilihan tidak valid. Silahkan pilih kembali")

if __name__ == "__main__":
    main_menu()
