# camera/camera_controller.py
import cv2
import numpy as np

# 元の MyVideoCapture クラスをそのまま移動
class MyVideoCapture:
    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        self.captured_img = None

    def run(self):
        while True:
            ret, frame = self.cap.read()
            if not ret:
                break

            cv2.imshow("Camera", frame)

            # q キーで撮影
            key = cv2.waitKey(1) & 0xFF
            if key == ord('q'):
                self.captured_img = frame.copy()
                break

        self.cap.release()
        cv2.destroyAllWindows()

    def get_img(self):
        return self.captured_img


# -------------------------
# photo(): カメラ→画像処理
# -------------------------
def photo(process_func):
    """
    process_func: captured_frame を受け取り実行する関数
                  （compose.process_image が渡される想定）
    """
    app = MyVideoCapture()
    app.run()

    captured_frame = app.get_img()

    if captured_frame is not None:
        print("\nカメラキャプチャを終了しました。画像加工を開始します。")
        process_func(captured_frame)
    else:
        print("\n⚠️ キャプチャされたフレームがありませんでした。画像加工はスキップします。")
