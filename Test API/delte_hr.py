import json
import requests

with open('hr_personnel_ids.json', 'r') as json_file:
    ids = json.load(json_file)

# Định nghĩa URL API và token
HOST_API_PUBLIC_HR = 'http://localhost:5050/api/sv4/'  # Thay đổi thành URL của bạn
url = f"{HOST_API_PUBLIC_HR}hr-information/personnel"


# Hàm gửi yêu cầu DELETE
def delete_hr_info_ids(ids):
    headers = {
        'Content-Type': 'application/json',
    }
    data = {'ids': ids}

    try:
        response = requests.delete(url, json=data, headers=headers)

        # Kiểm tra status code
        if response.status_code in [200, 201]:
            print('Xóa thành công:', response.json().get('message', 'Operation successful'))
        else:
            print('Có lỗi xảy ra:', response.status_code, response.json().get('message', 'Unexpected error'))

    except requests.exceptions.RequestException as e:
        print('Không thể kết nối tới server:', str(e))

# Gọi hàm xóa với ID đã đọc từ file JSON
delete_hr_info_ids(ids)
