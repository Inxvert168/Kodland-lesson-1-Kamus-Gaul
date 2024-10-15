import random
meme_dict = {
            "CRINGE": "Sesuatu yang sangat aneh atau memalukan",
            "LOL": "Tanggapan umum terhadap sesuatu yang lucu",
            "ROFL": "tanggapan terhadap lelucon",
            "CREEPY": "menakutkan, tidak menyenangkan",
            "SHEESH": "sedikit ketidaksetujuan",
            "AGGRO": "untuk menjadi agresif/marah",
            }
while True:
    word = input("Ketik kata yang tidak Kamu mengerti (gunakan huruf kapital semua!): ")
    if word in meme_dict.keys():
        # Apa yang harus kita lakukan jika kata itu ditemukan?
        print(meme_dict[word])
    else:
        # Apa yang harus kita lakukan jika kata itu tidak ditemukan?
        print("maaf, kata tersebut tidak ada dalam kamus ini, apakah anda menulis asal dan jika memang, cari di google aja.")
    print("=======================================================================\n")
