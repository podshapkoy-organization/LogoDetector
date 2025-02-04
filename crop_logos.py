import os
import cv2
import pandas as pd

csv_path = "dataset/logos.csv"
image_dir = "OpenLogo/JPEGImages"
output_dir = "dataset/reference_logos"
os.makedirs(output_dir, exist_ok=True)
df = pd.read_csv(csv_path)

for index, row in df.iterrows():
    image_path = os.path.join(image_dir, row["file_name"] + ".jpg")
    brand = row["brand"]
    img = cv2.imread(image_path)
    if img is None:
        print(f"не загрузилось {image_path}")
        continue
    xmin, ymin, xmax, ymax = row["xmin"], row["ymin"], row["xmax"], row["ymax"]
    cropped_logo = img[ymin:ymax, xmin:xmax]

    brand_dir = os.path.join(output_dir, brand)
    os.makedirs(brand_dir, exist_ok=True)

    output_path = os.path.join(brand_dir, f"{row['file_name']}.jpg")
    cv2.imwrite(output_path, cropped_logo)

print("finish")
