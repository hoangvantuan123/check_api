import csv
from faker import Faker
from datetime import datetime
import random

# Khởi tạo đối tượng Faker
fake = Faker()

# Hàm để tạo dữ liệu giả lập
def create_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Họ và Tên": fake.name(),
            "Giới tính": random.choice(["Male", "Female"]),
            "Ngày phỏng vấn": fake.date_between(start_date='-50y', end_date='today').isoformat(),
            "Ngày tháng năm sinh": fake.date_of_birth(minimum_age=20, maximum_age=80).isoformat(),
            "CCCD": fake.ssn(),
            "Điện thoại": fake.phone_number(),
            "email": fake.email(),
            "Kiểu công nhân" : True
        }
        data.append(record)
    return data

# Hàm để xuất dữ liệu ra file CSV
def export_to_csv(data, filename):
    keys = data[0].keys()
    with open(filename, 'w', newline='', encoding='utf-8') as output_file:
        dict_writer = csv.DictWriter(output_file, fieldnames=keys)
        dict_writer.writeheader()
        dict_writer.writerows(data)

num_records = 10  # Số lượng bản ghi cần tạo
fake_data = create_fake_data(num_records)
export_to_csv(fake_data, 'fake_data.csv')

print("Dữ liệu giả lập đã được xuất ra file fake_data.csv.")
