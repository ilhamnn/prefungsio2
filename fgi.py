expenses_data = [
    {"tanggal": "2023-07-25", "deskripsi": "Makan Siang", "jumlah": 50000},
    {"tanggal": "2023-07-25", "deskripsi": "Transportasi", "jumlah": 25000},
    {"tanggal": "2023-07-26", "deskripsi": "Belanja", "jumlah": 100000},
]


def add_expense(expenses, date, description, amount):
    new_expenses = expenses[:]
    new_expenses.append({"tanggal": date, "deskripsi": description, "jumlah": amount})
    return new_expenses


calculate_total_expenses = lambda expenses: sum(
    expense["jumlah"] for expense in expenses
)


def generate_expenses_report(expenses):
    for expense in expenses:
        yield f"{expense['tanggal']} - {expense['deskripsi']} - Rp {expense['jumlah']}"


get_user_input = lambda command: int(input(command))

get_expenses_by_date = lambda expenses, date: [
    expense for expense in expenses if expense["tanggal"] == date
]


def display_menu():
    print("\n===== Aplikasi Pencatat Pengeluaran Harian Versi Baru =====")
    print("1. Tambahkan Pengeluaran")
    print("2. Total Pengeluaran Harian")
    print("3. Lihat Pengeluaran Berdasarkan Tanggal")
    print("4. Lihat Laporan Pengeluaran Harian")
    print("5. Keluar")


def main():
    global expenses_data
    while True:
        display_menu()
        choice = get_user_input("Pilih menu (1/2/3/4/5): ")
        if choice == 1:
            date = input("Masukkan tanggal pengeluaran (YYYY-MM-DD): ")
            description = input("Masukkan deskripsi pengeluaran: ")
            amount = int(input("Masukkan jumlah pengeluaran: "))
            expenses_data = add_expense(expenses_data, date, description, amount)
            print("Pengeluaran berhasil ditambahkan.")
        elif choice == 2:
            total_expenses = calculate_total_expenses(expenses_data)
            print(f"\nTotal Pengeluaran Harian: Rp {total_expenses}")
        elif choice == 3:
            date = input("Masukkan tanggal (YYYY-MM-DD): ")
            expenses_on_date = get_expenses_by_date(expenses_data, date)
            print(f"\nPengeluaran pada tanggal {date}:")
            for expense in expenses_on_date:
                print(f"{expense['deskripsi']} - Rp {expense['jumlah']}")
        elif choice == 4:
            print("\nLaporan Pengeluaran Harian:")
            expenses_report = generate_expenses_report(expenses_data)
            for entry in expenses_report:
                print(entry)
        elif choice == 5:
            print("Terima kasih telah menggunakan aplikasi kami.")
            break
        else:
            print("Pilihan tidak valid. Silahkan pilih menu yang benar.")


if __name__ == "__main__":
    main()
