# image_processing/compose.py
import os
import cv2
import numpy as np


def process_image(captured_frame: np.ndarray):
    """
    撮影画像を4分の1に縮小 → 2×2 タイル化して背景を作り、
    google.png を白抜きキー合成する。
    """

    # ================================
    # パス設定
    # ================================
    current_file_path = os.path.abspath(__file__)
    script_dir = os.path.dirname(current_file_path)
    project_root = os.path.dirname(script_dir)

    google_path = os.path.join(project_root, "images", "google.png")
    output_dir = os.path.join(project_root, "images")
    output_path = os.path.join(output_dir, "output_google_replace.png")

    print(f"\n[DEBUG] project_root = {project_root}")
    print(f"[DEBUG] google_path = {google_path}")

    # ================================
    # ロゴ画像読み込み
    # ================================
    google_img = cv2.imread(google_path, cv2.IMREAD_UNCHANGED)
    if google_img is None:
        print("❌ google.png が読み込めません")
        return

    # RGBA → BGR に変換（4chの場合）
    if google_img.shape[2] == 4:
        print("[DEBUG] google.png は RGBA → BGR に変換します")
        google_img = cv2.cvtColor(google_img, cv2.COLOR_BGRA2BGR)

    # ================================
    # 撮影画像を 1/2 × 1/2 に縮小し 1/4 サイズにする
    # ================================
    h, w, _ = captured_frame.shape
    small = cv2.resize(captured_frame, (w // 2, h // 2))

    # ================================
    # 2×2 タイル画像を作成
    # ================================
    top = np.hstack([small, small])
    bottom = np.hstack([small, small])
    tiled = np.vstack([top, bottom])  # これが背景

    th, tw, _ = tiled.shape

    # ================================
    # ロゴ画像を背景サイズにリサイズ
    # ================================
    logo_resized = cv2.resize(google_img, (tw, th))

    # ================================
    # 白抜きキー合成（白色＝背景を残す）
    # ================================
    output = tiled.copy()

    # NumPy 高速版マスク処理（白画素のみ背景のまま）
    mask = np.all(logo_resized > 250, axis=2)  # True = 白

    # 白以外の画素だけロゴを貼る
    output[~mask] = logo_resized[~mask]

    # ================================
    # 保存と表示
    # ================================
    os.makedirs(output_dir, exist_ok=True)
    cv2.imwrite(output_path, output)
    print(f"保存完了 → {output_path}")

    # 表示
    cv2.imshow("Processed Image", output)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
