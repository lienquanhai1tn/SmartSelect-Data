import requests

def lay_so():
    print("🚀 Robot SmartSelect đang bắt đầu...")
    url = "https://api.xoso.me/app/json-kqmb"
    headers = {'User-Agent': 'Mozilla/5.0'}
    try:
        r = requests.get(url, headers=headers, timeout=15)
        if r.status_code == 200:
            with open("ketqua.csv", "w", encoding="utf-8") as f:
                f.write(r.text)
            print("✅ Đã lưu kết quả thành công!")
    except Exception as e:
        print(f"❌ Lỗi: {e}")

if __name__ == "__main__":
    lay_so()
