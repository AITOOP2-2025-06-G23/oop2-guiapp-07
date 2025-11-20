from PySide6.QtWidgets import QWidget, QPushButton, QVBoxLayout
from camera.camera_controller import photo  # ← あなたのコード
from image_processing.compose import process_image  # ← 加工関数


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Main Window")
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout()

        self.start_button = QPushButton("カメラ起動（qで撮影）")
        self.start_button.clicked.connect(self.on_camera_start_clicked)

        layout.addWidget(self.start_button)
        self.setLayout(layout)

    def on_camera_start_clicked(self):
        """
        compose.process_image を camera_controller.photo に渡す。
        """
        photo(self.on_capture_completed)

    def on_capture_completed(self, captured_frame):
        """
        compose.process_image が先に実行される。
        その後 GUI のプレビューも出す。
        """
        if captured_frame is None:
            print("⚠ 撮影画像がありません。")
            return

        print("GUI: 撮影画像を受け取りました。加工を開始します。")

        # ① 画像加工（OpenCVのウィンドウが出る）
        process_image(captured_frame)
