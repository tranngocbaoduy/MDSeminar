# Seminar Mobile Developing
# Link GitHub: https://github.com/tranngocbaoduy/MDSeminar
- JP App là folder chứa code chương trình minh hoạ ứng dụng Học ngoại ngữ
    * Để chạy được folder này chúng ta cần:
    1. Chạy npm install để cài đặt hết tất cả package cần thiết để build được chương trình
    2. Mở expo app (down trên google play - app store) 
    3. Kết nối Expo với app của mình sau đó gọi: npm start để start 
    4. Dùng điện thoại vào phần chụp ảnh để quét mã QR sau đó đợi load chương trình
- JP App Server là folder chứa server để gọi app lấy data cho JP App 
    * Để chạy được folder này chúng ta cần:
    1. Cài python - tốt nhất tải conda để tạo environment riêng để quản lí package ổn định
    2. Tạo một môi trường mới từ conda và kích hoạt môi trường đó theo lệnh:
        - conda create -n jpapp python==3.6 
        - conda deactivate
        - conda activate jpapp 
    3. cd vào thư mục Seminar, sau đó gọi lệnh: 
        - pip install -r requirements.txt
        - python run.py

    * Vì React Native sẽ không chấp nhận các đường link api là http nên chúng ta phải config thêm ngrok để tạo 1 tunnel, trong tunnel này chúng ta tạo đường link https để gọi api, bằng cách gọi câu lệnh: 

        - Window: ngrok http http://127.0.0.1:5000/
        - IOS/ Ubuntu/ Linux:  ./ngrok http http://127.0.0.1:5000/

        - Sau khi chạy xong sẽ ra 2 dòng forwarding: chúng ta copy url https của dòng forwarding bên dưới và paste vào đường dẫn sau: 
        "JPApp/screens/VocabularyScreen.js" sửa const URL lại tương ứng với cái vừa copy

        - Start lại server và app nếu cần thiết, sau khi reload thì chúng ta có thể lấy dữ liệu từ phía backend 

