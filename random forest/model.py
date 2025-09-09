import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

def train_model():
    # 1. Đọc dữ liệu
    du_lieu = pd.read_csv("data.csv")

    # 2. Xử lý dữ liệu: bỏ cột id và cột trống
    du_lieu = du_lieu.drop(columns=["id", "Unnamed: 32"])

    # 3. Chuyển nhãn diagnosis từ chữ sang số (M=0, B=1)
    du_lieu["diagnosis"] = du_lieu["diagnosis"].map({"M": 0, "B": 1})

    # 4. Chọn 5 đặc trưng quan trọng nhất
    dac_trung_quan_trong = [
        "concave points_mean",
        "concave points_worst",
        "area_worst",
        "concavity_mean",
        "radius_worst"
    ]

    X = du_lieu[dac_trung_quan_trong]
    y = du_lieu["diagnosis"]

    # 5. Chia dữ liệu thành tập huấn luyện và kiểm tra
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=42
    )

    # 6. Khởi tạo mô hình Random Forest
    mo_hinh = RandomForestClassifier(
        n_estimators=100,
        max_features="sqrt",
        random_state=42
    )

    # 7. Huấn luyện mô hình
    mo_hinh.fit(X_train, y_train)
    
    return mo_hinh, dac_trung_quan_trong
