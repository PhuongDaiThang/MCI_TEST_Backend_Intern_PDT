# Django CRM Project

## 📌 Mục đích

Xây dựng một hệ thống **CRM đơn giản** bao gồm:
- 📂 **Quản lý khách hàng (Customer)**
- 📦 **Quản lý sản phẩm (Product)**
- 👨‍💼 **Quản lý nhân sự (Employee)**
- 📂 **Quản lý bảng công việc (Task Board)** theo phong cách **Trello**

Dự án được phát triển bằng **Python** 🐍 và **Django**, kết hợp với **Django REST Framework (DRF)** để xây dựng các API.

---

## 🚀 Tính năng chính

### ✅ Xây dựng API với Django REST Framework
- **Khách hàng (Customer)**: CRUD (Create, Read, Update, Delete)
- **Sản phẩm (Product)**: CRUD
- **Nhân sự (Employee)**: CRUD
- **Bảng công việc (Task Board)**: CRUD, có chức năng **lọc (filter)** theo trạng thái công việc và nhân sự được phân công

### ✅ Trang Admin Django
- Truy cập **`/admin`** để quản lý dữ liệu.
- Cung cấp tính năng **tìm kiếm** và **lọc dữ liệu**.

### ✅ Hệ thống xác thực và tài liệu API
- **JWT**: Tích hợp **JSON Web Token** để xác thực người dùng.
- **Swagger**: Sử dụng **drf-spectacular** hoặc **drf-yasg** để tạo tài liệu API.

### ✅ CI/CD và Deploy
- **Đẩy code lên GitHub** và triển khai lên **Heroku, Render, AWS** hoặc các nền tảng khác.
- **Bảo mật**: Không đẩy thông tin nhạy cảm lên GitHub.

---

## 🔧 Hướng dẫn cài đặt

### 1️⃣ Clone dự án & tạo môi trường ảo
```bash
git clone https://github.com/PhuongDaiThang/MCI_TEST_Backend_Intern_PDT.git
cd django_crm_project
```
- **Windows**:
  ```bash
  python -m venv env
  env\Scripts\activate
  ```
- **Linux/macOS**:
  ```bash
  python3 -m venv env
  source env/bin/activate
  ```

### 2️⃣ Cài đặt thư viện
```bash
pip install -r requirements.txt
```

### 3️⃣ Cấu hình `.env`
Tạo file `.env` chứa thông tin cấu hình:
```
SECRET_KEY="your-secret-key"
DEBUG=True
DB_NAME="mcitest"
DB_USER="root"
DB_PASSWORD="your-db-password"
DB_HOST="localhost"
DB_PORT="3306"
```
> ⚠️ **Lưu ý:** Không commit file `.env` lên GitHub!

### 4️⃣ Thiết lập Database
- Tạo database trùng với `DB_NAME` trong MySQL.
- Cấp quyền truy cập cho `DB_USER`.

### 5️⃣ Chạy migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6️⃣ Tạo tài khoản admin (tùy chọn)
```bash
python manage.py createsuperuser
```
> Sau đó, truy cập **http://127.0.0.1:8000/admin** để đăng nhập.

### 7️⃣ Chạy server
```bash
python manage.py runserver
```
Mặc định server chạy tại **http://127.0.0.1:8000**.

---

## 🌐 Triển khai lên Server

Triển khai trên **Heroku, Render, AWS, DigitalOcean**. Thiết lập biến môi trường (`SECRET_KEY, DB_*`), cài đặt Gunicorn + Nginx nếu cần.

---

## 🎉 Liên hệ
👨‍💻 **Tác giả**: _Your Name_
📧 **Email**: your.email@example.com
📂 **GitHub**: [Your GitHub](https://github.com/your-username)

---
🚀 **Happy Coding!** 🚀

