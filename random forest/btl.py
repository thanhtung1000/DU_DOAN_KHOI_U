import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# 1. Đọc dữ liệu
du_lieu = pd.read_csv("data.csv")

# 2. Xử lý dữ liệu: bỏ cột id và cột trống
du_lieu = du_lieu.drop(columns=["id", "Unnamed: 32"])

# 3. Chuyển nhãn diagnosis từ chữ sang số (M=0, B=1)
du_lieu["diagnosis"] = du_lieu["diagnosis"].map({"M": 0, "B": 1})

# 4. Chọn 5 đặc trưng quan trọng nhất
dac_trung_quan_trong = [
    "concave points_mean",   # Trung bình số điểm lõm
    "concave points_worst",  # Số điểm lõm nhiều nhất
    "area_worst",            # Diện tích lớn nhất
    "concavity_mean",        # Trung bình độ lõm
    "radius_worst"           # Bán kính lớn nhất
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

# 8. Dự đoán trên tập kiểm tra
du_doan = mo_hinh.predict(X_test)

# 9. Đánh giá mô hình
do_chinh_xac = accuracy_score(y_test, du_doan)
print(f"🎯 Độ chính xác (chỉ với 5 đặc trưng): {do_chinh_xac*100:.2f}%\n")

print("📊 Báo cáo phân loại:")
print(classification_report(y_test, du_doan, target_names=["Ác tính", "Lành tính"]))

print("🔍 Ma trận nhầm lẫn:")
print(confusion_matrix(y_test, du_doan))

# =============================
# 10. Dự đoán từ dữ liệu nhập console
# =============================

print("\n📝 Nhập thông tin xét nghiệm để dự đoán:")

gia_tri_nhap = []
for ten in dac_trung_quan_trong:
    nhap = float(input(f"Nhập giá trị cho '{ten}': "))
    gia_tri_nhap.append(nhap)

# Chuyển thành DataFrame 1 hàng để dự đoán
du_lieu_moi = pd.DataFrame([gia_tri_nhap], columns=dac_trung_quan_trong)
du_doan_moi = mo_hinh.predict(du_lieu_moi)

if du_doan_moi[0] == 0:
    print("🩸 Kết quả dự đoán: ❌ Khối u ÁC TÍNH")
else:
    print("🩸 Kết quả dự đoán: ✅ Khối u LÀNH TÍNH")
