# image_processing/compose.py
import os
import cv2
import numpy as np


def process_image(captured_frame: np.ndarray):
    # ファイルパス取得
    current_file_path = os.path.abspath(__file__)
    script_dir = os.path.dirname(current_file_path)
    project_root = os.path.dirname(script_dir)

    # 画像パス
    google_path = os.path.join(project_root, "images", "google.png")
    output_dir = os.path.join(project_root, "images")
    output_path = os.path.join(output_dir, "output_google_replace.png")

    # デバッグ
    print(f"\n[DEBUG] 実行ファイルパス: {current_file_path}")
    print(f"[DEBUG] 想定プロジェクトルート: {project_root}")
    print(f"[DEBUG] Google画像パス: {google_path}")

    # Google画像読み込み
    google_img = cv2.imread(google_path)

    if google_img is None:
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print("⚠️ Google画像が読み込めません。パスを確認してください。")
        if not os.path.exists(google_path):
            print("❌ エラー: 指定されたパスにファイルが存在しません。")
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        return

    # キャプチャ画像
    capture_img = captured_frame

    output_img = google_img.copy()
    g_height, g_width, _ = google_img.shape
    c_height, c_width, _ = capture_img.shape

    print("Google画像サイズ:", google_img.shape)
    print("キャプチャ画像サイズ:", capture_img.shape)

    # 白部分置換
    for y in range(g_height):
        for x in range(g_width):
            b, g, r = google_img[y, x]
            if b > 250 and g > 250 and r > 250:
                cx = x % c_width
                cy = y % c_height
                output_img[y, x] = capture_img[cy, cx]

    # 保存
    os.makedirs(output_dir, exist_ok=True)
    result = cv2.imwrite(output_path, output_img)

    print("--- 処理結果 ---")
    print("加工後の保存結果:", result)
    print(f"画像を保存しました → {output_path}")

    # 表示
    cv2.imshow("Processed Image", output_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
