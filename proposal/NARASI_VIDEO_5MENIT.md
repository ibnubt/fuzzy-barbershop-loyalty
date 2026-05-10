# Narasi Presentasi Paper — 5 Menit

Versi naratif. Saya pakai dua karakter pelanggan tetap dari awal sampai akhir
sehingga penonton selalu punya konteks yang sama:

- **Pak Budi** — eksekutif, sebulan sekali ambil paket grooming Rp 350 ribu
- **Mas Andi** — karyawan marketing, ketemu klien sering, jadi tiga kali sebulan datang untuk paket cukur dan cuci Rp 110 ribu, total Rp 330 ribu

Kedua karakter ini muncul di pembuka, di pembahasan kelemahan, dan di hasil.
Penonton akan ingat mereka.

Format file:
- **NARASI** = teks yang Anda baca keras-keras, plain text
- **DI LAYAR** = posisi PDF saat narasi ini dibacakan
- **TUNJUK** = gerakan cursor / highlight, daftar pendek

Total durasi: 5 menit. Naskah teleprompter ~720 kata.

---

## Persiapan singkat

1. Buka `proposal/main.pdf` di Preview, set zoom Fit Width
2. Naskah ini di iPad sebagai teleprompter di samping kamera
3. Pakai QuickTime Cmd+Shift+5 untuk record
4. Pointer Size = Large (Accessibility settings)
5. Notifikasi off
6. Test rekam 30 detik dulu untuk cek audio

---

## Segmen 1 — Hook dan pembuka (0:00 – 0:40)

### NARASI

Coba bayangkan dua orang pelanggan barbershop di Jakarta.

Pelanggan pertama, sebut saja Pak Budi. Eksekutif muda. Sebulan sekali datang untuk paket grooming komplet, tarifnya 350 ribu rupiah.

Pelanggan kedua, Mas Andi. Karyawan di tim marketing yang sering ketemu klien, jadi harus selalu tampil rapi. Tiga kali sebulan dia datang untuk paket cukur dan cuci, tarifnya 110 ribu sekali datang. Total bulanannya 330 ribu.

Di program member yang umum dipakai barbershop sekarang, kedua orang ini mendapat diskon yang sama persis: sepuluh persen. Padahal profil loyalitas mereka jauh berbeda.

Halo, saya Ibnu Bagus Trisnandi dari Teknik Elektro UGM. Lima menit ke depan saya akan tunjukkan dua kelemahan program member barbershop yang umum dipakai, lalu rancangan sistem fuzzy yang bisa memperbaikinya, plus buktinya.

### DI LAYAR
Halaman 1 PDF, posisi paling atas — judul dan author block terlihat.

### TUNJUK
- 0:00 – 0:25: cukup tampilkan halaman judul, tidak perlu scroll
- 0:28: saat sebut nama Anda, klik nama di author block
- 0:35: saat sebut "fuzzy", drag cursor mengikuti judul paper

---

## Segmen 2 — Bagaimana program member sekarang bekerja (0:40 – 1:05)

### NARASI

Hampir semua barbershop di Jakarta punya program member yang skemanya mirip. Pelanggan dibagi tiga tingkatan: Bronze, Silver, Gold. Tingkatan ditentukan dari jumlah kunjungan atau total spending bulanan, lalu masing-masing tingkatan diberi diskon dengan nilai tetap.

Sebagai contoh konkret, sebuah jaringan barbershop yang saya amati di Sudirman menerapkan tiga ambang: spending 150 ribu memberi 5 persen, 250 ribu memberi 10 persen, dan 400 ribu memberi 20 persen.

### DI LAYAR
Halaman 1, scroll ke paragraf kedua Pendahuluan (yang dimulai dengan "Banyak gerai punya program loyalti...").

### TUNJUK
- Tunjuk tiga kata "Bronze, Silver, Gold" saat disebut
- Tunjuk angka-angka ambang (150, 250, 400) saat disebut

---

## Segmen 3 — Kelemahan pertama (1:05 – 1:35)

### NARASI

Skema ini punya dua kelemahan. Yang pertama, skema bertingkat tidak bisa membaca pelanggan dari dua sisi sekaligus.

Kembali ke contoh Pak Budi dan Mas Andi tadi. Pak Budi menyumbang 350 ribu untuk barbershop bulan ini, walau cuma sekali datang. Mas Andi menyumbang 330 ribu, lewat tiga kali kunjungan. Keduanya jelas pelanggan yang berharga, tapi dengan cara yang berbeda.

Skema bertingkat memaksa kita memilih satu sumbu sebagai patokan. Hasilnya, satu sisi loyalitas pasti diabaikan. Pak Budi dan Mas Andi diperlakukan sama, padahal yang satu loyal di spending, yang satu loyal di frekuensi.

### DI LAYAR
Halaman 1-2, scroll ke paragraf "Kelemahan pertama".

### TUNJUK
- Highlight atau tunjuk judul paragraf "Kelemahan pertama" di awal
- Tunjuk angka 350 ribu saat sebut Pak Budi
- Tunjuk angka 280 ribu saat sebut Mas Andi
- Pause 1 detik setelah "yang satu loyal di spending, yang satu loyal di frekuensi"

---

## Segmen 4 — Kelemahan kedua (1:35 – 2:10)

### NARASI

Kelemahan kedua: ada loncatan tarif yang tajam di sekitar ambang batas.

Bayangkan dua pelanggan lain. Yang pertama spending 249 ribu sebulan, yang kedua spending 250 ribu. Selisih spending mereka cuma seribu rupiah. Tapi yang pertama dapat diskon 5 persen, sedangkan yang kedua langsung dapat 10 persen. Selisih seribu rupiah, beda diskon dua kali lipat.

Yang lebih ekstrem terjadi di ambang 400 ribu. Pelanggan yang spending 399 ribu dapat 10 persen, tapi pelanggan yang spending 400 ribu dapat 20 persen. Lagi-lagi karena selisih seribu rupiah saja.

### DI LAYAR
Halaman 2, scroll ke paragraf "Kelemahan kedua".

### TUNJUK
- Highlight judul paragraf "Kelemahan kedua"
- Tunjuk angka 249 dan 250 sebelahan
- Pause 1 detik setelah "beda diskon dua kali lipat"
- Tunjuk angka 399 dan 400

---

## Segmen 5 — Kenapa fuzzy bisa selesaikan keduanya (2:10 – 2:30)

### NARASI

Fuzzy logic bisa menyelesaikan kedua masalah ini sekaligus. Untuk masalah loncatan tarif, fuzzy memakai membership function yang overlap dengan tetangga, sehingga outputnya bergerak halus tanpa loncatan tajam. Untuk masalah profil multi-dimensi, fuzzy memakai aturan berbentuk IF X AND Y THEN Z yang menggabungkan dua sumbu sekaligus dalam satu aturan.

### DI LAYAR
Halaman 2, scroll ke paragraf "Saya berpendapat fuzzy logic cocok...".

### TUNJUK
- Tunjuk frase "menghilangkan loncatan tarif"
- Tunjuk frase "IF X AND Y THEN Z"

---

## Segmen 6 — Variabel sistem (2:30 – 3:00)

### NARASI

Sekarang ke rancangan sistem.

Sistemnya kecil. Dua input dan satu output. Input pertama: frekuensi kunjungan per bulan, dari nol sampai delapan. Input kedua: total spending bulan berjalan dalam ribu rupiah, dari nol sampai 600. Output: persentase diskon, dari nol sampai 25 persen.

Tiap input punya tiga kategori linguistik. Frekuensi dibagi rare, regular, frequent. Spending dibagi low, medium, high. Output punya empat kategori: none, small, medium, large. Bentuk membership function-nya bisa dilihat di Gambar 1.

### DI LAYAR
Halaman 3, ke section "III. Rancangan Sistem", lalu Gambar 1.

### TUNJUK
- Tunjuk daftar rare, regular, frequent saat disebut
- Tunjuk daftar low, medium, high saat disebut
- Saat sampai di Gambar 1, diam 4 detik supaya penonton bisa lihat bentuknya

---

## Segmen 7 — Tabel rule (3:00 – 3:50) ⭐ INTI

### NARASI

Inilah otak sistemnya, di Tabel II.

Sembilan aturan disusun sebagai grid tiga kali tiga. Sumbu kiri membaca kategori frekuensi: jarang, sedang, sering. Sumbu atas membaca kategori spending: hemat, standar, premium. Setiap sel di perpotongannya adalah satu aturan IF-THEN.

Pola tabel ini ada tiga, dan ini yang ingin saya jelaskan.

Yang pertama, dari pojok kiri atas ke pojok kanan bawah, output naik konsisten dari none ke large. Makin loyal di salah satu sumbu, makin besar diskonnya.

Yang kedua, dan ini kunci dari sistem. Sel kanan atas, jarang tapi premium, saya beri output medium. Sel kiri bawah, sering tapi hemat, juga saya beri medium. Saya samakan keduanya. Pesannya: pelanggan jarang dengan spending tinggi saya anggap setara dengan pelanggan sering dengan spending rendah. Inilah yang tidak bisa dilakukan skema bertingkat.

Yang ketiga, dua sel di sudut kanan bawah saya beri output large. Diskon mencapai plateau di pelanggan VIP, supaya margin bisnis tetap aman.

### DI LAYAR
Halaman 3-4, scroll ke Tabel II. Tampilkan tabel di tengah layar. Diam 3 detik sebelum mulai bicara.

### TUNJUK (segmen ini paling penting)
- 3:00: scroll ke Tabel II, diam 3 detik
- 3:08: drag cursor mengikuti sumbu kiri, tunjuk "rare", "regular", "frequent" satu per satu
- 3:13: pindah ke sumbu atas, tunjuk "low", "medium", "high"
- 3:23: saat bicara "Pola pertama", drag cursor diagonal dari pojok kiri-atas ke pojok kanan-bawah, pelan, 3 detik
- 3:33: saat sebut "sel kanan atas", letakkan cursor di sel itu, diam 1 detik
- 3:37: pindah cursor ke sel kiri bawah, diam 1 detik
- 3:43: pause 1 detik setelah "tidak bisa dilakukan skema bertingkat"
- 3:47: tunjuk dua sel kanan-bawah

---

## Segmen 8 — Kembali ke Pak Budi dan Mas Andi (3:50 – 4:20)

### NARASI

Sekarang kita lihat hasilnya pada lima profil pelanggan contoh, di Tabel III.

Saya tunjukkan Pak Budi dan Mas Andi yang sama dari awal. Pak Budi, baris ketiga di tabel: jarang dengan spending besar. Sistem fuzzy memberi 15 persen, sedangkan skema bertingkat hanya 10 persen.

Mas Andi, baris keempat: tiga kali sebulan dengan spending sedang. Sistem fuzzy memberi 19,4 persen, sementara skema bertingkat tetap 10 persen.

Inilah perbedaannya. Skema bertingkat memberi keduanya 10 persen yang sama. Sistem fuzzy memberi 15 persen ke yang loyal-spending dan 19,4 persen ke yang loyal-frekuensi. Dua profil yang berbeda mendapat penghargaan yang berbeda.

### DI LAYAR
Halaman 4-5, scroll ke Tabel III.

### TUNJUK
- Cursor di baris ketiga (Eksekutif). Tunjuk angka 15 persen di kolom fuzzy, lalu 10 persen di kolom tier
- Pindah ke baris keempat (Marketing rapi). Tunjuk angka 19,4 persen, lalu 10 persen
- Pause 1 detik setelah "Dua profil yang berbeda mendapat penghargaan yang berbeda"

---

## Segmen 9 — Bukti loncatan tarif hilang (4:20 – 4:45)

### NARASI

Untuk kelemahan kedua tadi, soal loncatan tarif, buktinya ada di Gambar 3.

Saya men-sweep variabel spending dari nol sampai 500 ribu, sambil menahan frekuensi tetap di dua kunjungan per bulan.

Garis merah putus-putus adalah skema bertingkat. Bentuknya tangga, dengan loncatan tajam di tiga titik: 150 ribu, 250 ribu, dan 400 ribu.

Garis biru adalah sistem fuzzy. Bergerak halus tanpa loncatan, melewati ketiga ambang itu dengan transisi yang gradual.

### DI LAYAR
Halaman 5, scroll ke Gambar 3.

### TUNJUK
- Drag cursor mengikuti garis merah dari kiri ke kanan, pause sebentar di setiap loncatan
- Drag cursor mengikuti garis biru dari kiri ke kanan, smooth
- Tunjuk loncatan paling tajam di 400 ribu

---

## Segmen 10 — Penutup (4:45 – 5:00)

### NARASI

Singkatnya, sistem fuzzy ini kecil. Sembilan aturan, dua input, satu output. Tapi cukup untuk menyelesaikan dua masalah konkret yang tadi saya tunjukkan: profil multi-dimensi yang tidak terbaca, dan loncatan tarif di ambang batas.

Source code dan dataset saya rilis di GitHub. Linknya ada di section Reproducibility. Terima kasih.

### DI LAYAR
Halaman 6, scroll ke section Penutup, lalu ke section Reproducibility.

### TUNJUK
- Highlight URL GitHub
- Pause 1 detik setelah "Terima kasih"

---

## Tabel timing untuk dilihat sekilas

| Segmen | Topik | Mulai | Selesai |
|---|---|---|---|
| 1 | **Hook** Pak Budi & Mas Andi | 0:00 | 0:40 |
| 2 | Skema member umum | 0:40 | 1:05 |
| 3 | Kelemahan 1 (Pak Budi & Mas Andi) | 1:05 | 1:35 |
| 4 | Kelemahan 2 (loncatan tarif) | 1:35 | 2:10 |
| 5 | Kenapa fuzzy bisa | 2:10 | 2:30 |
| 6 | Variabel & MF | 2:30 | 3:00 |
| 7 | Tabel rule | 3:00 | 3:50 |
| 8 | Hasil (Pak Budi & Mas Andi lagi) | 3:50 | 4:20 |
| 9 | Bukti chart loncatan | 4:20 | 4:45 |
| 10 | Penutup | 4:45 | 5:00 |

---

## Lima titik pause yang penting

Ucapkan kalimat-kalimat ini lalu diam 0,7 sampai 1 detik. Ini punchline.

1. "yang satu loyal di spending, yang satu loyal di frekuensi" (Segmen 3)
2. "Selisih seribu rupiah, beda diskon dua kali lipat" (Segmen 4)
3. "Inilah yang tidak bisa dilakukan skema bertingkat" (Segmen 7)
4. "Dua profil yang berbeda mendapat penghargaan yang berbeda" (Segmen 8)
5. "Terima kasih" (Segmen 10)

---

## Yang tidak boleh dilakukan

- Scroll mendadak di tengah kalimat. Tunggu kalimat selesai dulu
- Cursor berkeliaran tanpa tujuan saat bicara
- Bicara cepat di angka penting (350 ribu, 330 ribu, 19,4 persen). Lambatkan
- Lupa diam setelah punchline
- Membaca naskah dengan intonasi datar. Variasikan tinggi-rendah suara

---

## Naskah lengkap untuk teleprompter

Coba bayangkan dua orang pelanggan barbershop di Jakarta.

Pelanggan pertama, sebut saja Pak Budi. Eksekutif muda. Sebulan sekali datang untuk paket grooming komplet, tarifnya 350 ribu rupiah.

Pelanggan kedua, Mas Andi. Karyawan di tim marketing yang sering ketemu klien, jadi harus selalu tampil rapi. Tiga kali sebulan dia datang untuk paket cukur dan cuci, tarifnya 110 ribu sekali datang. Total bulanannya 330 ribu.

Di program member yang umum dipakai barbershop sekarang, kedua orang ini mendapat diskon yang sama persis: sepuluh persen. Padahal profil loyalitas mereka jauh berbeda.

Halo, saya Ibnu Bagus Trisnandi dari Teknik Elektro UGM. Lima menit ke depan saya akan tunjukkan dua kelemahan program member barbershop yang umum dipakai, lalu rancangan sistem fuzzy yang bisa memperbaikinya, plus buktinya.

Hampir semua barbershop di Jakarta punya program member yang skemanya mirip. Pelanggan dibagi tiga tingkatan: Bronze, Silver, Gold. Tingkatan ditentukan dari jumlah kunjungan atau total spending bulanan, lalu masing-masing tingkatan diberi diskon dengan nilai tetap.

Sebagai contoh konkret, sebuah jaringan barbershop yang saya amati di Sudirman menerapkan tiga ambang: spending 150 ribu memberi 5 persen, 250 ribu memberi 10 persen, dan 400 ribu memberi 20 persen.

Skema ini punya dua kelemahan. Yang pertama, skema bertingkat tidak bisa membaca pelanggan dari dua sisi sekaligus.

Kembali ke contoh Pak Budi dan Mas Andi tadi. Pak Budi menyumbang 350 ribu untuk barbershop bulan ini, walau cuma sekali datang. Mas Andi menyumbang 330 ribu, lewat tiga kali kunjungan. Keduanya jelas pelanggan yang berharga, tapi dengan cara yang berbeda.

Skema bertingkat memaksa kita memilih satu sumbu sebagai patokan. Hasilnya, satu sisi loyalitas pasti diabaikan. Pak Budi dan Mas Andi diperlakukan sama, padahal yang satu loyal di spending, yang satu loyal di frekuensi.

Kelemahan kedua: ada loncatan tarif yang tajam di sekitar ambang batas.

Bayangkan dua pelanggan lain. Yang pertama spending 249 ribu sebulan, yang kedua spending 250 ribu. Selisih spending mereka cuma seribu rupiah. Tapi yang pertama dapat diskon 5 persen, sedangkan yang kedua langsung dapat 10 persen. Selisih seribu rupiah, beda diskon dua kali lipat.

Yang lebih ekstrem terjadi di ambang 400 ribu. Pelanggan yang spending 399 ribu dapat 10 persen, tapi pelanggan yang spending 400 ribu dapat 20 persen. Lagi-lagi karena selisih seribu rupiah saja.

Fuzzy logic bisa menyelesaikan kedua masalah ini sekaligus. Untuk masalah loncatan tarif, fuzzy memakai membership function yang overlap dengan tetangga, sehingga outputnya bergerak halus tanpa loncatan tajam. Untuk masalah profil multi-dimensi, fuzzy memakai aturan berbentuk IF X AND Y THEN Z yang menggabungkan dua sumbu sekaligus dalam satu aturan.

Sekarang ke rancangan sistem.

Sistemnya kecil. Dua input dan satu output. Input pertama: frekuensi kunjungan per bulan, dari nol sampai delapan. Input kedua: total spending bulan berjalan dalam ribu rupiah, dari nol sampai 600. Output: persentase diskon, dari nol sampai 25 persen.

Tiap input punya tiga kategori linguistik. Frekuensi dibagi rare, regular, frequent. Spending dibagi low, medium, high. Output punya empat kategori: none, small, medium, large. Bentuk membership function-nya bisa dilihat di Gambar 1.

Inilah otak sistemnya, di Tabel II.

Sembilan aturan disusun sebagai grid tiga kali tiga. Sumbu kiri membaca kategori frekuensi: jarang, sedang, sering. Sumbu atas membaca kategori spending: hemat, standar, premium. Setiap sel di perpotongannya adalah satu aturan IF-THEN.

Pola tabel ini ada tiga, dan ini yang ingin saya jelaskan.

Yang pertama, dari pojok kiri atas ke pojok kanan bawah, output naik konsisten dari none ke large. Makin loyal di salah satu sumbu, makin besar diskonnya.

Yang kedua, dan ini kunci dari sistem. Sel kanan atas, jarang tapi premium, saya beri output medium. Sel kiri bawah, sering tapi hemat, juga saya beri medium. Saya samakan keduanya. Pesannya: pelanggan jarang dengan spending tinggi saya anggap setara dengan pelanggan sering dengan spending rendah. Inilah yang tidak bisa dilakukan skema bertingkat.

Yang ketiga, dua sel di sudut kanan bawah saya beri output large. Diskon mencapai plateau di pelanggan VIP, supaya margin bisnis tetap aman.

Sekarang kita lihat hasilnya pada lima profil pelanggan contoh, di Tabel III.

Saya tunjukkan Pak Budi dan Mas Andi yang sama dari awal. Pak Budi, baris ketiga di tabel: jarang dengan spending besar. Sistem fuzzy memberi 15 persen, sedangkan skema bertingkat hanya 10 persen.

Mas Andi, baris keempat: tiga kali sebulan dengan spending sedang. Sistem fuzzy memberi 19,4 persen, sementara skema bertingkat tetap 10 persen.

Inilah perbedaannya. Skema bertingkat memberi keduanya 10 persen yang sama. Sistem fuzzy memberi 15 persen ke yang loyal-spending dan 19,4 persen ke yang loyal-frekuensi. Dua profil yang berbeda mendapat penghargaan yang berbeda.

Untuk kelemahan kedua tadi, soal loncatan tarif, buktinya ada di Gambar 3.

Saya men-sweep variabel spending dari nol sampai 500 ribu, sambil menahan frekuensi tetap di dua kunjungan per bulan.

Garis merah putus-putus adalah skema bertingkat. Bentuknya tangga, dengan loncatan tajam di tiga titik: 150 ribu, 250 ribu, dan 400 ribu.

Garis biru adalah sistem fuzzy. Bergerak halus tanpa loncatan, melewati ketiga ambang itu dengan transisi yang gradual.

Singkatnya, sistem fuzzy ini kecil. Sembilan aturan, dua input, satu output. Tapi cukup untuk menyelesaikan dua masalah konkret yang tadi saya tunjukkan: profil multi-dimensi yang tidak terbaca, dan loncatan tarif di ambang batas.

Source code dan dataset saya rilis di GitHub. Linknya ada di section Reproducibility. Terima kasih.
