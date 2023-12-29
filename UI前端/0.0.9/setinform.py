from PIL import Image
import base64
from io import BytesIO
import requests
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QIcon, QImage
from PyQt5.QtWidgets import QFileDialog, QPushButton, QMessageBox, QWidget

class SetInform(QWidget):
    def __init__(self, ui):
        super().__init__()
        self.ui = ui
        self.image_path = "头像.png"
        print(self.ui.Bt_change)

    def inform(self, user_data):
        self.ui.text_id.setPlainText(str(user_data["id"]))
        self.ui.text_user.setPlainText(user_data["user_name"])
        self.ui.text_phone.setPlainText(user_data["phone_number"])
        self.ui.text_email.setPlainText(user_data["user_email"])
        self.avatar(user_data)
        self.avatar(user_data)
        self.ui.text_id.setReadOnly(True)     # 用户id不可修改，设为只读
    def set_information(self, user_data):

        url = "http://172.29.1.106:8000/edit/"

        user_name = self.ui.text_user.toPlainText()
        phone = self.ui.text_phone.toPlainText()
        email = self.ui.text_email.toPlainText()

        params = {"user_id": user_data["id"], "phone_number": phone, "user_name": user_name, "user_email": email}
        res = requests.post(url=url, data=params)
        if res.text == "\"OK\"":
            # 创建一个消息框
            message_box = QMessageBox()
            # 设置消息框的属性
            message_box.setWindowTitle("研题提醒")  # 设置窗口标题
            message_box.setText("修改成功")  # 设置文本内容
            custom_icon = QIcon('对勾-解除.png')
            message_box.setIcon(QMessageBox.Information)  # 设置图标为警告
            message_box.setStandardButtons(QMessageBox.Ok)  # 设置按钮为确定
            # 显示消息框
            message_box.exec()
        else:
            # 创建一个消息框
            message_box = QMessageBox()
            # 设置消息框的属性
            message_box.setWindowTitle("研题提醒")  # 设置窗口标题
            message_box.setText(list(res.json().values())[0][0])  # 设置文本内容
            message_box.setIcon(QMessageBox.Critical)  # 设置图标为警告
            message_box.setStandardButtons(QMessageBox.Ok)  # 设置按钮为确定
            # 显示消息框
            message_box.exec()

    # 用户修改头像
    def select_image(self):
        print("Button clicked")
        options = QFileDialog.Options()
        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.ExistingFiles)

        files, _ = file_dialog.getOpenFileNames(self, "选择图片", "", "Image Files (*.png *.jpg *.jpeg *.bmp *.gif)")


        if files:
            # 选择了图片文件
            image_path = files[0]  # 这里假设用户只选取了一张图片
            self.image_path = image_path  # 保存图片路径
            self.show_image()
        else:
            # 创建一个消息框
            message_box = QMessageBox()
            # 设置消息框的属性
            message_box.setWindowTitle("研题提醒")  # 设置窗口标题
            message_box.setText("图片选择失败！")  # 设置文本内容
            message_box.setIcon(QMessageBox.Critical)  # 设置图标为警告
            message_box.setStandardButtons(QMessageBox.Ok)  # 设置按钮为确定
            # 显示消息框
            message_box.exec()

    # 用户修改头像并显示
    def show_image(self):
        if hasattr(self, 'image_path'):
            pixmap = QPixmap(self.image_path)
            pixmap = pixmap.scaledToHeight(self.ui.Bt_change.height())  # 调整图像大小以适应按钮高度
            pixmap = pixmap.scaledToWidth(self.ui.Bt_change.width())  # 调整图像大小以适应按钮宽度
            icon = QIcon(pixmap)  # 将QPixmap转换为QIcon
            self.ui.Bt_change.setIcon(icon)
            self.ui.Bt_change.setIconSize(pixmap.size())  # 设置图标尺寸为图片大小
            # 设置按钮的QSS样式
            style_sheet = """
                        QPushButton {
                            border-radius: 50px; /* 设置按钮的边界半径，使其呈圆形 */
                            background-color: rgb(255, 255, 255); /* 设置按钮的背景颜色 */
                        }
                    """
            self.ui.Bt_change.setStyleSheet(style_sheet)
            self.upload_to_backend()
            self.avatar(None)
        else:
            # 创建一个消息框
            message_box = QMessageBox()
            # 设置消息框的属性
            message_box.setWindowTitle("研题提醒")  # 设置窗口标题
            message_box.setText("出错，请稍后再试")  # 设置文本内容
            message_box.setIcon(QMessageBox.Critical)  # 设置图标为警告
            message_box.setStandardButtons(QMessageBox.Ok)  # 设置按钮为确定
            # 显示消息框
            message_box.exec()

    def avatar(self, user_data):
        if user_data["user_picture"] is not None:
            # 将头像应用于个人页面的显示
            image_data = base64.b64decode(user_data["user_picture"])
            # image_data = BytesIO(image_data)
            # 把获取到的图片保存在当前目录下
            with open("user_image.png", "wb") as file:  # 保存名为user_image的png文件，如果有一样名字的则直接覆盖
                file.write(image_data)
            self.image_path = "user_image.png"
        # label的样式
        style_sheet = f"""
                    border-radius: 50px; /* 设置边界半径，使其呈圆形 */
                    background-color: rgb(255, 255, 255); /* 设置背景颜色 */
                    image: url({self.image_path});
                """
        button_style = f'''
            QPushButton {{
                border-radius: 60px;
                background-color: rgb(255, 255, 255);
                icon: url({self.image_path});
            }}

            QPushButton:pressed {{
                padding-left: 5px;
                padding-top: 5px;
            }}
        '''
        pixmap = QPixmap(self.image_path)
        pixmap = pixmap.scaledToHeight(self.ui.Bt_change.height())  # 调整图像大小以适应按钮高度
        pixmap = pixmap.scaledToWidth(self.ui.Bt_change.width())  # 调整图像大小以适应按钮宽度
        icon = QIcon(pixmap)  # 将QPixmap转换为QIcon
        self.ui.Bt_change.setIcon(icon)
        self.ui.Bt_change.setIconSize(pixmap.size())  # 设置图标尺寸为图片大小
        self.ui.Bt_change.setStyleSheet(button_style)
        self.ui.label_profile_3.setStyleSheet(style_sheet)

    def upload_to_backend(self):
        if hasattr(self, 'image_path'):
            with open(self.image_path, 'rb') as file:
                files = {'file': file.read()}  # 读取图片文件内容并转换为二进制格式
            # 发送图片数据到后端
            print(files)
            print(type(files["file"]))
            response = requests.post('http://172.29.1.106:8000/picture/', data={"user_id": 10}, files=files)
            # 处理后端返回的响应数据
            print(response.text)  # 在控制台打印后端返回的响应数据
            if response.text == "\"OK\"":
                # 创建一个消息框
                message_box = QMessageBox()
                # 设置消息框的属性
                message_box.setWindowTitle("研题提醒")  # 设置窗口标题
                message_box.setText("头像修改成功")  # 设置文本内容
                # custom_icon = QIcon('对勾-解除.png')  # 设置标题栏图像
                message_box.setIcon(QMessageBox.Information)  # 设置图标为警告
                message_box.setStandardButtons(QMessageBox.Ok)  # 设置按钮为确定

            else:
                # 创建一个消息框
                message_box = QMessageBox()
                # 设置消息框的属性
                message_box.setWindowTitle("研题提醒")  # 设置窗口标题
                message_box.setText(list(response.json().values())[0][0])  # 设置文本内容
                message_box.setIcon(QMessageBox.Critical)  # 设置图标为错误
                message_box.setStandardButtons(QMessageBox.Ok)  # 设置按钮为确定
                # 显示消息框
                message_box.exec()