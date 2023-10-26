def konversi(minggu=0):
    def hari(hari=0):
        def jam(jam=0):
            def menit(menit=0):
                return ((((minggu*7)+hari)*24)+jam)*60+menit
            return menit
        return jam
    return hari

data = ["3 minggu 3 hari 7 jam 21 menit",
        "5 minggu 5 hari 8 jam 11 menit",
        "7 minggu 1 hari 5 jam 33 menit"]

def konversi_data(data):
    # kita split data untuk mendapatkan nilai jam, menit, dan detik
    data_split = data.split()

    # kita simpan masing-masing valuenya dalam variabel terpisah
    minggu = int(data_split[0])
    hari = int(data_split[2])
    jam = int(data_split[4])
    menit = int(data_split[6])
    return konversi(minggu)(hari)(jam)(menit)

output = list(map(konversi_data, data))

print("output data= ", output)