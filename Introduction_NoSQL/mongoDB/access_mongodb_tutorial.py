from pymongo import MongoClient

# import thư viện trên để có MongoClient

# Tiếp theo tạo ra đối tượng MongoClient để kết nối tới csdl 
# bằng cách cung cấp URI (Uniform Resource Identifier) của csdl

client = MongoClient('mongodb://AdminCherry:090924@localhost:27017/')

# ta chỉ cần tạo client 1 lần trong code
# -------------------------------------------------------------

# Giả sử ta có một csdl quản lý sinh viên campus_management. Để truy cập:

db = client["campus_management"]

# Cuối cùng để thao tác với Collection, ta chỉ cần tham chiếu đến Collection đó:

students = db["students"]

# -------------------------------------------------------------

# Thao tác insert

## Thêm một tài liệu

student = {
    "studentId": 1,
    "name": "John Doe",
    "email": "john.doe@example.com"
}
students.insert_one(student)

## Thêm nhiều tài liệu

many_students = [
    {"studentId": 2, "name": "Jane Smith", "email": "jane.smith@example.com"},
    {"studentId": 3, "name": "Alice Johnson", "email": "alice.johnson@example.com"}
]
students.insert_many(many_students)

# -------------------------------------------------------------

# Thao tác read

## Lấy một tài liệu duy nhất

student = students.find_one()


student = students.find_one({"email": "john.doe@example.com"})


## Lấy nhiều tài liệu

many_students = students.find({"name": {"$regex": "Doe$"}})

## Đếm số tài liệu

count = students.count_documents({})

# -------------------------------------------------------------

# Thao tác update

## Cập nhật một tài liệu

new_student_data = {
    "studentId": 1,
    "name": "John Doe",
    "email": "john.doe@campus.edu",
    "status": "online"
}
students.replace_one({"name": "John Doe"}, new_student_data)

## Cập nhật một phần tài liệu

students.update_one(
    {"name": "John Doe"},
    {"$set": {"email": "john.doe@campus.edu"}}
)

## Cập nhật nhiều tài liệu

students.update_many({}, {"$set": {"status": "online"}})

# -------------------------------------------------------------

# Thao tác xóa

## Xóa một tài liệu

students.delete_one({"email": "john.doe@campus.edu"})

## Xóa nhiều tài liệu

students.delete_many({"status": "offline"})

# -------------------------------------------------------------

# Đóng kết nối

client.close()