import os

for folder in ["syllables", "jamo"]:
    if os.path.exists(folder):
        for filename in os.listdir(folder):
            if filename.endswith(".svg") and "_" in filename:
                # Đổi tên từ '00224_고.svg' thành '고.svg'
                new_name = filename.split("_", 1)[1]
                os.rename(
                    os.path.join(folder, filename),
                    os.path.join(folder, new_name)
                )

print("Đã đổi tên xong toàn bộ thư viện!")