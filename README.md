# oop2-guiapp-07
画像処理GUIアプリケーション

## ディレクトリ構造
project/  
 ├── main.py   # GUIの起動.  
 ├── gui/  
 │    └── main.py   # ① GUI担当.  
 ├── camera/.    
 │    └── camera_controller.py  # ② カメラ担当.  
 ├── image_processing/   
 │    └── compose.py       # ③ 画像処理担当.  
 ├── images/  
 │    ├── google.png  
 │    └── output.png  
 └── my_module/...   

 ## 役割分担
 | 担当           | 主な作業                                    | 必要な関数/クラス                                 |
 | -------------- | ------------------------------------------- | ------------------------------------------------- |
 | ① GUI担当      | PySide6画面作成・ボタン操作・プレビュー表示 | MainWindow, ボタンイベントハンドラー              |
 | ② カメラ担当   | カメラ起動・停止・1フレーム取得・QImage変換 | CameraController.start(), read_frame(), stop()    |
 | ③ 画像処理担当 | 合成ロジック・ファイル保存                  | compose_images(), save_image(), load_base_image() |


## 処理の流れ
1. 起動するとGUIが立ち上がる(カメラ起動ボタン)  
2. 起動ボタンが押されたら，カメラが起動する(別ウィンドウ)
3. 撮影ボタンが押されたら，プレビューを出す．
4. 画像合成のyes/noボタンを実装
5. yesの場合:加工して保存yes/noボタン実装
6. noの場合: 保存yes/noボタン実装
7. 保存の選択をしたら，logの表示とスタート画面に戻る

## GPTリンク
https://chatgpt.com/share/691ea706-1200-8008-96fd-33d2c8f1000a