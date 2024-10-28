import cv2
import pytesseract

gray_image = cv2.imread('img/namem.png')

custom_oem_psm_config = r"--oem 3 --psm 6 -l eng+jpn"

text = pytesseract.image_to_string(gray_image, lang=custom_oem_psm_config)  # 日本語の場合

# 認識したテキストをファイルに保存
with open('recognized_text.txt', 'w', encoding='utf-8') as file:
    file.write(text)   



# ウィンドウを閉じる
cv2.waitKey(0)
cv2.destroyAllWindows()