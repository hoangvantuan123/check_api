import numpy as np
import pandas as pd
import psycopg2
import json
# Kết nối đến cơ sở dữ liệu PostgreSQL
conn = psycopg2.connect(
    host='103.75.180.66',        
    database='itm_db', 
    user='tuanhoang',    
    password='tienhung-admin@admin.com'  # Mật khẩu
)

# Truy vấn để lấy dữ liệu
query = "SELECT id FROM hr_personnel;"
df = pd.read_sql(query, conn)

# Đóng kết nối
conn.close()

# Chuyển đổi cột 'id' thành một danh sách kiểu chuỗi
id_list = df['id'].astype(str).tolist()

# Lưu danh sách vào file JSON
with open('hr_personnel_ids.json', 'w') as json_file:
    json.dump(id_list, json_file)

# In danh sách ra màn hình (tuỳ chọn)
print(id_list)