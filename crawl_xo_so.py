import requests

def lay_so_tu_dong():
    print("🚀 Robot SmartSelect đang lấy số từ vệ tinh...")
    url = "https://api.xoso.me/app/json-kqmb"
    headers = {'User-Agent': 'Mozilla/5.0'}
    
    try:
        response = requests.get(url, headers=headers, timeout=15)
        if response.status_code == 200:
            data = response.text
            with open("ketqua.csv", "w", encoding="utf-8") as f:
                f.write(data)
            print("✅ Đã lưu dữ liệu vào file ketqua.csv thành công!")
        else:
            print(f"❌ Lỗi kết nối: {response.status_code}")
    except Exception as e:
        print(f"❌ Robot gặp sự cố: {e}")

if __name__ == "__main__":
    lay_so_tu_dong()
