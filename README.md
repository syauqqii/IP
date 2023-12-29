## **IP**
> Program ini bertujuan untuk edukasi, mengambil alamat berdasarkan IP dari target (Tidak akurat 100%).
#### Gunakan Port Forwarding Service untuk menjalankan program, seperti :
> - Ngrok
> - Serveo
> - Tunneling

## **Contoh Penggunaan dengan Serveo**
```bash
git clone https://github.com/syauqqii/IP
```
```bash
cd IP
```
```php
php -S localhost:666
```
```bash
ssh -R test:80:localhost:666 serveo.net
```
- kirim link hasil running ssh dari poin 4 ke target
- buka file `hasil.txt`, muncul ip
```python3
python main.py -ip {ip}
```
