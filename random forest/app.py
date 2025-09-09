from flask import Flask, render_template, request
import pandas as pd
from model import train_model

app = Flask(__name__)

# Huấn luyện mô hình khi ứng dụng khởi động
mo_hinh, dac_trung_quan_trong = train_model()

@app.route('/')
def home():
    return render_template('index.html', features=dac_trung_quan_trong)

@app.route('/predict', methods=['POST'])
def predict():
    gia_tri_nhap = []
    for feature in dac_trung_quan_trong:
        value = request.form.get(feature)
        if value:
            gia_tri_nhap.append(float(value))
        else:
            # Xử lý trường hợp giá trị không được cung cấp
            return render_template('index.html', features=dac_trung_quan_trong, error="Vui lòng nhập đầy đủ giá trị.")

    du_lieu_moi = pd.DataFrame([gia_tri_nhap], columns=dac_trung_quan_trong)
    du_doan_moi = mo_hinh.predict(du_lieu_moi)

    if du_doan_moi[0] == 0:
        ket_qua = "Khối u ÁC TÍNH"
    else:
        ket_qua = "Khối u LÀNH TÍNH"

    return render_template('index.html', features=dac_trung_quan_trong, prediction=ket_qua, submitted_values=request.form)

if __name__ == '__main__':
    app.run(debug=True)
