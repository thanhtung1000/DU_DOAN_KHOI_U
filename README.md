# Breast Cancer Prediction using Random Forest

##  Mô tả dự án / Project Description

Đây là một ứng dụng web sử dụng thuật toán Random Forest để dự đoán ung thư vú (lành tính hoặc ác tính) dựa trên các đặc trưng của tế bào. Ứng dụng được xây dựng với Flask và cung cấp giao diện web thân thiện cho người dùng.

This is a web application that uses Random Forest algorithm to predict breast cancer (benign or malignant) based on cell features. The application is built with Flask and provides a user-friendly web interface.

##  Tính năng / Features

-  Dự đoán ung thư vú bằng thuật toán Random Forest
-  Giao diện web đơn giản và thân thiện
-  Sử dụng 5 đặc trưng quan trọng nhất:
  - Concave points mean (Trung bình số điểm lõm)
  - Concave points worst (Số điểm lõm nhiều nhất)
  - Area worst (Diện tích lớn nhất)
  - Concavity mean (Trung bình độ lõm)
  - Radius worst (Bán kính lớn nhất)
-  Kết quả dự đoán nhanh chóng và chính xác

##  Công nghệ sử dụng / Technologies Used

- **Python 3.x**
- **Flask** - Web framework
- **scikit-learn** - Machine learning library
- **pandas** - Data manipulation
- **HTML/CSS** - Frontend

##  Cài đặt / Installation

### Yêu cầu hệ thống / Requirements
```
Flask
pandas
scikit-learn
```

### Các bước cài đặt / Installation Steps

1. Clone repository:
```bash
git clone <repository-url>
cd random-forest-breast-cancer
```

2. Cài đặt thư viện cần thiết:
```bash
pip install flask pandas scikit-learn
```

3. Chạy ứng dụng:
```bash
python app.py
```

4. Mở trình duyệt và truy cập: `http://localhost:5000`

##  Cấu trúc dự án / Project Structure

```
random forest/
│
├── app.py              # Ứng dụng Flask chính
├── model.py            # Mô hình Random Forest
├── btl.py              # Script training và evaluation
├── data.csv            # Dữ liệu ung thư vú
├── templates/
│   └── index.html      # Giao diện web
└── README.md           # Tài liệu dự án
```

##  Sử dụng / Usage

1. Khởi động ứng dụng bằng cách chạy `python app.py`
2. Truy cập giao diện web tại `http://localhost:5000`
3. Nhập các giá trị đặc trưng vào form:
   - Concave points mean
   - Concave points worst
   - Area worst
   - Concavity mean
   - Radius worst
4. Nhấn nút "Dự đoán" để xem kết quả
5. Hệ thống sẽ hiển thị kết quả: "Khối u ÁC TÍNH" hoặc "Khối u LÀNH TÍNH"

##  Dữ liệu / Dataset

Dự án sử dụng bộ dữ liệu Breast Cancer Wisconsin với các đặc trưng:
- **M (Malignant)**: Ác tính (được mã hóa thành 0)
- **B (Benign)**: Lành tính (được mã hóa thành 1)

##  Hiệu suất mô hình / Model Performance

Mô hình Random Forest được cấu hình với:
- `n_estimators=100`: 100 cây quyết định
- `max_features="sqrt"`: Căn bậc hai của tổng số đặc trưng
- `random_state=42`: Đảm bảo kết quả có thể tái tạo

##  Đóng góp / Contributing

1. Fork dự án
2. Tạo branch mới (`git checkout -b feature/AmazingFeature`)
3. Commit thay đổi (`git commit -m 'Add some AmazingFeature'`)
4. Push lên branch (`git push origin feature/AmazingFeature`)
5. Mở Pull Request


##  Lời cảm ơn / Acknowledgments

- Bộ dữ liệu Breast Cancer Wisconsin từ UCI Machine Learning Repository
- Thư viện scikit-learn cho các thuật toán machine learning
- Flask framework cho việc phát triển web

##  Tính năng tương lai / Future Features

- [ ] Thêm nhiều thuật toán machine learning khác
- [ ] Cải thiện giao diện người dùng
- [ ] Thêm biểu đồ visualization
- [ ] API REST cho việc tích hợp
- [ ] Triển khai lên cloud platform

---

<img width="1131" height="881" alt="image" src="https://github.com/user-attachments/assets/2488b8b6-6ded-47cc-9af9-0005a45fec30" />

