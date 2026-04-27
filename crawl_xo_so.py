import requests

def lay_du_lieu():
    print("🚀 Robot SmartSelect đang bắt đầu...")
    url = "https://api.xoso.me/app/json-kqmb"
    headers = {'User-Agent': 'Mozilla/5.0'}
    try:
        response = requests.get(url, headers=headers, timeout=15)
        if response.status_code == 200:
            with open("ketqua.csv", "w", encoding="utf-8") as f:
                f.write(response.text)
            print("✅ Robot đã tạo file ketqua.csv thành công!")
    except Exception as e:
        print(f"❌ Lỗi rồi anh Hải ơi: {e}")

if __name__ == "__main__":
    lay_du_lieu()
