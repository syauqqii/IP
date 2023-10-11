### IP
Gunakan Port Forwarding untuk menjalankan program diatas.
> Seperti :
- Ngrok
- Serveo
- Tunneling

### Contoh Penggunaan dengan Serveo
1. `git clone https://github.com/syauqqii/IP`
2. `cd IP`
3. `php -S localhost:666`
4. `ssh -R test:80:localhost:666 serveo.net`
5. kirim link hasil running ssh dari poin 4 ke target
6. buka file `hasil.txt`, muncul ip
7. `python main.py -ip {ip}`
