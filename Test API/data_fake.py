from faker import Faker
import pandas as pd
import random

# Khởi tạo đối tượng Faker
fake = Faker('vi_VN')  # Sử dụng ngôn ngữ tiếng Việt

# Tạo một danh sách chứa các cột
columns = [
    "CID", "Name", "Đăng ký bp trên ERP", "Team", "Part", "Production", "Section", "Job field",
    "Position", "Entering day", "Leaving day", "PROBATION (day)", "Ngày ký HĐ lần 1",
    "Ngày ký HĐ lần 2", "Số chứng minh thư", "Ngày cấp", "Nơi cấp", "Date of birth", "Tuổi",
    "Đếm tháng", "Phone Number", "Gender", "Email", "Partner name", "Partner phone number",
    "Số con", "Children name 1", "Children birth date 1", "Children gender 1",
    "Children name 2", "Children birth date 2", "Children gender 2",
    "Children name 3", "Children birth date 3", "Children gender 3",
    "Father name", "Father phone number", "Mother name", "Mother phone number",
    "Xã 1", "Huyện 1", "Tỉnh 1", "Thôn xóm 2", "Xã 2", "Huyện 2", "Tỉnh 2", "Địa chỉ quê quán",
    "Địa chỉ đăng ký hộ khẩu", "Khoảng cách từ nơi đăng ký hộ khẩu đến công ty",
    "Highest level of education", "School name", "Major", "School year", "Year ended", 
    "Year of graduation", "Classification", "Working department 1", "Work responsibility 1",
    "Company name 1", "Entrance day 1", "Leaving day 1", "Salary 1", 
    "Working department 2", "Work responsibility 2", "Company name 2", "Entrance day 2", 
    "Leaving day 2", "Salary 2", "Language 1", "Certificate Type 1", "Score 1", "Level 1",
    "Language 2", "Certificate Type 2", "Score 2", "Level 2", "Language 3", 
    "Certificate Type 3", "Score 3", "Level 3", "Dân tộc", "ĐÓNG BHXH"
]

# Xác nhận tổng số cột
total_columns = len(columns)
print("Tổng số cột:", total_columns)  # Kiểm tra số cột

# Tạo một danh sách để chứa dữ liệu giả
data = []

# Danh sách xã, huyện, tỉnh mẫu
xa_list = ["Phú Lâm", "Tam Tảo", "Yên Phong", "Đồng Kỵ"]
huyen_list = ["Tiên Du", "Yên Phong", "Từ Sơn", "Quế Võ"]
tinh_list = ["Bắc Ninh", "Hà Nội", "Hải Dương", "Bắc Giang"]

# Số lượng bản ghi muốn tạo
num_records = 3

# Tạo dữ liệu giả
for _ in range(num_records):
    # Số con
    num_children = fake.random_int(min=0, max=3)

    # Tạo danh sách trẻ em
    children_names = [fake.first_name() for _ in range(num_children)]
    children_birth_dates = [fake.date_between(start_date='-18y', end_date='today').strftime('%Y-%m-%d') for _ in range(num_children)]
    children_genders = [fake.random_element(elements=("NAM", "NỮ")) for _ in range(num_children)]

    # Tạo từng bản ghi với dữ liệu giả
    record = [
        fake.unique.bothify(text='VM######'),  # CID
        fake.name(),  # Name
        fake.random_element(elements=("ITM SEMI", "HR", "Finance", "Marketing")),  # Đăng ký bp trên ERP
        fake.random_element(elements=("RM", "PM", "SM", "Sales")),  # Team
        fake.random_element(elements=("SALE", "DEV", "IT")),  # Part
        fake.random_element(elements=("COMMON", "SPECIFIC")),  # Production
        fake.random_element(elements=("Sale", "HR", "Accounting")),  # Section
        fake.job(),  # Job field
        fake.job(),  # Position
        fake.date_between(start_date='-10y', end_date='today').strftime('%Y-%m-%d'),  # Entering day
        fake.date_between(start_date='-10y', end_date='today').strftime('%Y-%m-%d'),  # Leaving day
        fake.random_int(min=30, max=90),  # PROBATION (day)
        fake.date_between(start_date='-10y', end_date='today').strftime('%Y-%m-%d'),  # Ngày ký HĐ lần 1
        fake.date_between(start_date='-10y', end_date='today').strftime('%Y-%m-%d'),  # Ngày ký HĐ lần 2
        fake.ssn(),  # Số chứng minh thư
        fake.date_between(start_date='-30y', end_date='-10y').strftime('%Y-%m-%d'),  # Ngày cấp
        fake.city(),  # Nơi cấp
        fake.date_of_birth(minimum_age=20, maximum_age=60).strftime('%Y-%m-%d'),  # Date of birth
        fake.random_int(min=20, max=60),  # Tuổi
        fake.random_int(min=1, max=12),  # Đếm tháng
        fake.phone_number(),  # Phone Number
        fake.random_element(elements=("NAM", "NỮ")),  # Gender
        fake.email(),  # Email
        fake.name(),  # Partner name
        fake.phone_number(),  # Partner's phone number
        num_children,  # Số con
        children_names[0] if num_children > 0 else "",  # Children name 1
        children_birth_dates[0] if num_children > 0 else "",  # Children birth date 1
        children_genders[0] if num_children > 0 else "",  # Children gender 1
        children_names[1] if num_children > 1 else "",  # Children name 2
        children_birth_dates[1] if num_children > 1 else "",  # Children birth date 2
        children_genders[1] if num_children > 1 else "",  # Children gender 2
        children_names[2] if num_children > 2 else "",  # Children name 3
        children_birth_dates[2] if num_children > 2 else "",  # Children birth date 3
        children_genders[2] if num_children > 2 else "",  # Children gender 3
        fake.name(),  # Father name
        fake.phone_number(),  # Father phone number
        fake.name(),  # Mother name
        fake.phone_number(),  # Mother phone number
        random.choice(xa_list),  # Xã 1
        random.choice(huyen_list),  # Huyện 1
        random.choice(tinh_list),  # Tỉnh 1
        random.choice(xa_list),  # Thôn xóm 2
        random.choice(xa_list),  # Xã 2
        random.choice(huyen_list),  # Huyện 2
        random.choice(tinh_list),  # Tỉnh 2
        fake.address(),  # Địa chỉ quê quán
        fake.address(),  # Địa chỉ đăng ký hộ khẩu
        fake.random_int(min=1, max=50),  # Khoảng cách từ nơi đăng ký hộ khẩu đến công ty
        fake.random_element(elements=["Đại học", "Cao đẳng", "THPT"]),  # Highest level of education
        fake.company(),  # School name
        fake.random_element(elements=["Electrical", "Business", "IT"]),  # Major
        fake.random_int(min=1, max=5),  # School year
        fake.random_int(min=2000, max=2024),  # Year ended
        fake.random_int(min=2000, max=2024),  # Year of graduation
        fake.random_element(elements=["Giỏi", "Khá", "Trung bình"]),  # Classification
        fake.random_element(elements=("HR", "IT", "Sales")),  # Working department 1
        fake.job(),  # Work responsibility 1
        fake.company(),  # Company name 1
        fake.date_between(start_date='-10y', end_date='today').strftime('%Y-%m-%d'),  # Entrance day 1
        fake.date_between(start_date='-10y', end_date='today').strftime('%Y-%m-%d'),  # Leaving day 1
        fake.random_int(min=3000000, max=20000000),  # Salary 1
        fake.random_element(elements=("HR", "IT", "Sales")),  # Working department 2
        fake.job(),  # Work responsibility 2
        fake.company(),  # Company name 2
        fake.date_between(start_date='-10y', end_date='today').strftime('%Y-%m-%d'),  # Entrance day 2
        fake.date_between(start_date='-10y', end_date='today').strftime('%Y-%m-%d'),  # Leaving day 2
        fake.random_int(min=3000000, max=20000000),  # Salary 2
        fake.random_element(elements=["Tiếng Anh", "Tiếng Pháp", "Tiếng Nhật"]),  # Language 1
        fake.random_element(elements=["Chứng chỉ A", "Chứng chỉ B", "Chứng chỉ C"]),  # Certificate Type 1
        fake.random_int(min=1, max=10),  # Score 1
        fake.random_element(elements=["Cơ bản", "Trung cấp", "Nâng cao"]),  # Level 1
        fake.random_element(elements=["Tiếng Anh", "Tiếng Pháp", "Tiếng Nhật"]),  # Language 2
        fake.random_element(elements=["Chứng chỉ A", "Chứng chỉ B", "Chứng chỉ C"]),  # Certificate Type 2
        fake.random_int(min=1, max=10),  # Score 2
        fake.random_element(elements=["Cơ bản", "Trung cấp", "Nâng cao"]),  # Level 2
        fake.random_element(elements=["Tiếng Anh", "Tiếng Pháp", "Tiếng Nhật"]),  # Language 3
        fake.random_element(elements=["Chứng chỉ A", "Chứng chỉ B", "Chứng chỉ C"]),  # Certificate Type 3
        fake.random_int(min=1, max=10),  # Score 3
        fake.random_element(elements=["Cơ bản", "Trung cấp", "Nâng cao"]),  # Level 3
        fake.random_element(elements=["Kinh", "Tày", "Thái"]),  # Dân tộc
        fake.random_element(elements=["Có", "Không"])  # ĐÓNG BHXH
    ]
    
    # Kiểm tra số lượng giá trị trong bản ghi
    print("Số lượng giá trị trong bản ghi:", len(record))  # Kiểm tra số lượng giá trị

    # Thêm bản ghi vào danh sách dữ liệu
    data.append(record)

# Tạo DataFrame từ dữ liệu giả
df = pd.DataFrame(data, columns=columns)

# Xuất dữ liệu ra file CSV
df.to_csv('du_lieu_gia.csv', index=False, encoding='utf-8-sig')

print("Đã tạo file du_lieu_gia.csv với số bản ghi:", num_records)
