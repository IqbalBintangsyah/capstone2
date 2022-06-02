# Capstone Project | Volcano Hazard Maping Zone

Project Website sistem informasi dengan menggunakan framework Django
## Installation
Dalam persiapan project, ikuti langkah-langkah berikut ini :

- Buat Virtual Environtment dan masuk pada venv yang sudah dibuat
```bash
python -m venv /path/to/new/virtual/environment
```
```bash
dir [nama env]\scripts\activate.bat
```
- Install Django dan Library lainnya

```bash
pip install django, requests
```
- Clone repositori ini dan jalankan dengan perintah :
```bash
python manage.py runserver
```

## Feature
1. Persebaran lava.
   - Menghitung persebaran lava dengan memasukkan input pada kolom yang tersedia
2. Persebaran lahar.
   - Melihat persebaran lahar  dan melihat lokasi pada map leaflet untuk memastikan kategori zona.
   - Mendownload rentang persebaran lahar berdasarkan keinginan pengguna
3. Persebaran piroklastik
   - Melihat dan memastikan persebaran piroklastik (awan panas)


## Pengembang
- [Muhammad Iqbal B](https://github.com/IqbalBintangsyah)
- [Septian Hesti K](https://github.com/septianhk)

## License
[MIT LICENSE](https://github.com/rivaldynaiborhu/capstone/blob/master/LICENSE)
