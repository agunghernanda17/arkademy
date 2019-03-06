# arkademy-

untuk bahasa pemrograman menggunakan python dengan versi 3.7.2  
untuk framework menggunakan flask (koneksi flask ke mysql menggunakan library pymysql)  
untuk database menggunakan mysql server versi 8  
untuk bootstrap menggunakan bootstrap versi 2.3.2

pengerjaan soal 1-5 menggunakan IDE notepad++  
pengerjaan soal 6 menggunakan CMD  
pengerjaan soal 7 menggunakan IDE PyCharm dengan memanfaatkan framework flask   
(untuk fitur Insert masih berupa tombol dan belum berfungsi)  

  cara menjalankan flask melalui IDE Pycharm
1. buka flask
2. buka interface terminal
3. masuk direktory project flask yang sudah otomatis dibuat saat 'New Project' melalui terminal di IDE Pycharm
4. kemudian ketik 'python -m flask run' untuk menjalankan project pada localhost dengan ip 127.0.0.1:5000 
(5000 merupakan port default flask)
5. jika muncul error 'could not locate a flask application' maka ketikkan 'set FLASK_APP=app.py' pada terminal Pycharm untuk mengeset environment
6. Jika muncul status running at 127.0.0.1:5000, maka web berhasil dijalankan
7. selanjutnya buka browser dan ketikkan 127.0.0.1:5000 pada address bar untuk melihat tampilan web yang sudah dibuat

---------------------------------Update---------------------------------------------------  
Requirements  
Python 3.7.2  
MySQL Server 8  
Bootstrap version 2.3.2  
Flask Framework ( Sudah Include di PyCharm IDE )  
library tambahan pada flask  
-pymysql  
cara install libnya adalah dengan mengetikkan 'pip install pymsql' pada terminal PyCharm IDE  

Untuk menjalankan project no 7 yaitu sebagai berikut:
1. Buka IDE PyCharm
2. File-> New Project -> Flask
3. Pilih New Environment using 'Virtualenv'
4. Tentukan juga direktory workspace yang digunakan sesuai keinginan
5. Kemudian klik Create
6. Tunggu proses pembuatan workspace selesai
7. Selanjutnya Masuk ke direktory workspace project dengan cara mengklik folder sesuai nama project
8. Paste dan replace seluruh isi folder soal7 di github ini pada direktory workspace yang sudah dibuat sebelumnya
9. kemudian ketik 'python -m flask run' di terminal IDE PyCharm untuk menjalankan project pada localhost dengan ip 127.0.0.1:5000 
   (5000 merupakan port default flask)
10. jika muncul error 'could not locate a flask application' maka ketikkan 'set FLASK_APP=app.py' pada terminal Pycharm untuk mengeset       environment, kemudian ketik ulang 'python -m flask run' pada terminal
11. Jika muncul status running at 127.0.0.1:5000, maka web berhasil dijalankan
12. selanjutnya buka browser dan ketikkan 127.0.0.1:5000 pada address bar untuk melihat tampilan web yang sudah dibuat
