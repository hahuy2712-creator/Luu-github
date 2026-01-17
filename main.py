from datetime import datetime

with open("log.txt", "a", encoding="utf-8") as f:
    f.write(f"Chạy lúc: {datetime.now()}\n")

print("Done")
