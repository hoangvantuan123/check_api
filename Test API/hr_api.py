import requests
import json
from faker import Faker
import random

# Tạo đối tượng Faker
fake = Faker('vi_VN')  # Sử dụng 'vi_VN' để tạo dữ liệu phù hợp với Việt Nam

# Hàm tạo dữ liệu giả
def generate_fake_data():
    return {
        "full_name": fake.name(),
        "gender": random.choice(["Male", "Female"]),
        "interview_date": fake.iso8601(),
        "start_date": fake.iso8601(),
        "birth_date": fake.date_of_birth().isoformat(),
        "id_number": str(fake.random_number(digits=12, fix_len=True)),
        "id_issue_date": fake.iso8601(),
        "ethnicity": random.choice(["Kinh", "Tày", "Nùng", "Thái", "Mường"]),
        "id_issue_place": fake.city(),
        "insurance_number": str(fake.random_number(digits=6, fix_len=True)),
        "tax_number": str(fake.random_number(digits=6, fix_len=True)),
        "phone_number": fake.phone_number(),
        "email": fake.email(),
        "alternate_phone_number": fake.phone_number(),
        "alternate_name": fake.first_name(),
        "alternate_relationship": random.choice(["Bạn", "Người thân", "Đồng nghiệp"]),
        "birth_address": fake.address(),
        "birth_province": fake.city(),
        "birth_district": fake.street_name(),
        "birth_ward": fake.street_address(),
        "current_address": fake.address(),
        "current_province": fake.city(),
        "current_district": fake.street_name(),
        "current_ward": fake.street_address(),
        "families": [
            {
                "relationship": "Bố",
                "full_name": fake.name_male(),
                "birth_year": random.randint(1950, 1970),
                "workplace": fake.company(),
                "job": fake.job(),
                "phone_number": fake.phone_number(),
                "living_together": random.choice([True, False])
            },
            {
                "relationship": "Mẹ",
                "full_name": fake.name_female(),
                "birth_year": random.randint(1950, 1975),
                "workplace": fake.company(),
                "job": fake.job(),
                "phone_number": fake.phone_number(),
                "living_together": random.choice([True, False])
            },
            {
                "relationship": random.choice(["Vợ/chồng", "Anh/Em/Con"]),
                "full_name": fake.name(),
                "birth_year": random.randint(1975, 2000),
                "workplace": fake.company(),
                "job": fake.job(),
                "phone_number": fake.phone_number(),
                "living_together": random.choice([True, False])
            }
        ],
        "educations": [
            {
                "school": fake.company(),
                "major": fake.job(),
                "years": random.randint(3, 5),
                "start_year": random.randint(2010, 2015),
                "graduation_year": random.randint(2016, 2020),
                "grade": random.choice(["Xuất sắc", "Giỏi", "Khá", "Trung bình"])
            }
        ],
        "languages": [
            {
                "language": random.choice(["Tiếng Anh", "Tiếng Hàn", "Tiếng Nhật", "Tiếng Trung"]),
                "certificate_type": random.choice(["TOEIC", "IELTS", "JLPT", "TOPIK"]),
                "score": str(round(random.uniform(5.0, 9.0), 1)),
                "level": random.choice(["Sơ cấp", "Trung cấp", "Cao cấp"]),
                "start_date": fake.iso8601(),
                "end_date": fake.iso8601(),
                "has_bonus": random.choice(["Có", "Không"])
            }
        ],
        "experiences": [
            {
                "company_name": fake.company(),
                "position": fake.job(),
                "start_date": random.randint(2010, 2015),
                "end_date": random.randint(2016, 2020),
                "employee_scale": str(random.randint(50, 500)),
                "tasks": "Quản lý dự án",
                "salary": str(random.randint(500, 5000)) + " USD",
                "description": fake.text(max_nb_chars=200)
            }
        ]
    }

# Hàm gửi dữ liệu đến API
def send_data_to_api(data):
    url = "http://localhost:5050/api/sv4/hr-information/personnel"  # URL API của bạn
    headers = {'Content-Type': 'application/json'}  # Đặt Content-Type là application/json
    
    try:
        response = requests.post(url, headers=headers, json=data)
        if response.status_code == 200:
            print("Gửi dữ liệu thành công.")
        else:
            print(f"Đã xảy ra lỗi. Mã lỗi: {response.status_code}, Thông báo: {response.text}")
    except Exception as e:
        print(f"Lỗi khi kết nối tới API: {str(e)}")

# Gửi 1000 mẫu dữ liệu giả lên API
for i in range(5000):
    fake_data = generate_fake_data()
    print(f"Gửi dữ liệu số {i + 1}...")
    send_data_to_api(fake_data)
