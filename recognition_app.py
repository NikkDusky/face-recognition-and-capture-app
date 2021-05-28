from os import path, mkdir, curdir
from time import sleep
import time
import sys

from PyQt5.QtGui import QIntValidator, QPixmap, QImage
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QThread

dir_now = path.abspath(curdir)

def current_milli_time(): #Функция для получения миллисекунд
    return round(time.time() * 1000)

class Ui_Form(object): #Данный класс отвечает за создание интерфейса, а также функционал кнопок
    
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(380, 390)
        Form.setMinimumSize(QtCore.QSize(380, 390))
        Form.setMaximumSize(QtCore.QSize(380, 390))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(10, 40, 201, 25))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_cam = QtWidgets.QLabel(Form)
        self.label_cam.setGeometry(QtCore.QRect(380, 10, 657, 370))
        font_for_cam = QtGui.QFont()
        font_for_cam.setPointSize(16)
        self.label_cam.setFont(font_for_cam)
        self.label_cam.setStyleSheet("")
        self.label_cam.setTextFormat(QtCore.Qt.AutoText)
        self.label_cam.setAlignment(QtCore.Qt.AlignCenter)
        self.label_cam.setObjectName("label")
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_cam.setText(_translate("Form", "Последний захваченый снимок"))
        self.label_2.setFont(font)
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(10, 130, 201, 25))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_5.setFont(font)
        self.label_5.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(10, 70, 201, 25))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_3.setFont(font)
        self.label_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.lineCamHeight = QtWidgets.QLineEdit(Form)
        self.lineCamHeight.setGeometry(QtCore.QRect(220, 100, 150, 25))
        self.lineCamHeight.setObjectName("lineCamHeight")
        self.pushButtonStart = QtWidgets.QPushButton(Form)
        self.pushButtonStart.setGeometry(QtCore.QRect(9, 190, 361, 25))
        self.pushButtonStart.setObjectName("pushButtonStart")
        self.lineCamCaptures = QtWidgets.QLineEdit(Form)
        self.lineCamCaptures.setGeometry(QtCore.QRect(220, 10, 150, 25))
        self.lineCamCaptures.setObjectName("lineCamCaptures")
        self.lineDirectory = QtWidgets.QLineEdit(Form)
        self.lineDirectory.setGeometry(QtCore.QRect(220, 130, 150, 25))
        self.lineDirectory.setObjectName("lineDirectory")
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(10, 250, 361, 131))
        self.textBrowser.setObjectName("textBrowser")
        self.pushButtonStop = QtWidgets.QPushButton(Form)
        self.pushButtonStop.setGeometry(QtCore.QRect(9, 220, 361, 25))
        self.pushButtonStop.setObjectName("pushButtonStop")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 10, 201, 25))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(10, 160, 201, 25))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_6.setFont(font)
        self.label_6.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.lineCamTimerCaptures = QtWidgets.QLineEdit(Form)
        self.lineCamTimerCaptures.setGeometry(QtCore.QRect(220, 40, 150, 25))
        self.lineCamTimerCaptures.setObjectName("lineCamTimerCaptures")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(10, 100, 201, 25))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_4.setFont(font)
        self.label_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.lineCamID = QtWidgets.QLineEdit(Form)
        self.lineCamID.setGeometry(QtCore.QRect(220, 160, 150, 25))
        self.lineCamID.setObjectName("lineCamID")
        self.lineCamWidth = QtWidgets.QLineEdit(Form)
        self.lineCamWidth.setGeometry(QtCore.QRect(220, 70, 150, 25))
        self.lineCamWidth.setObjectName("lineCamWidth")
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.add_functions() #Регистрация функций кнопок
        self.pushButtonStop.setEnabled(False) #Отключаем кнопку
        
    def app_change_text_browser(self, text): #Функция для вывода информации в textBrowser
        self.textBrowser.append(str(text))
        self.textBrowser.moveCursor(QtGui.QTextCursor.End)

    def retranslateUi(self, Form): #Именуем
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Face Recognition & Capture App"))
        self.label_2.setText(_translate("Form", "Таймер сна после обнаружения"))
        self.label_5.setText(_translate("Form", "Дирректория для сохранения снимков"))
        self.label_3.setText(_translate("Form", "Ширина камеры"))
        self.lineCamHeight.setText(_translate("Form", "720"))
        self.pushButtonStart.setText(_translate("Form", "Start"))
        self.lineCamCaptures.setText(_translate("Form", "1"))
        self.lineDirectory.setText(_translate("Form", (dir_now + "\Captures")))
        self.pushButtonStop.setText(_translate("Form", "Stop"))
        self.label.setText(_translate("Form", "Количество снимков при обнаружении"))
        self.label_6.setText(_translate("Form", "Номер камеры в системе"))
        self.lineCamTimerCaptures.setText(_translate("Form", "15"))
        self.label_4.setText(_translate("Form", "Высота камеры"))
        self.lineCamID.setText(_translate("Form", "0"))
        self.lineCamWidth.setText(_translate("Form", "1280"))
        
        self.onlyInt = QIntValidator()
        self.lineCamHeight.setValidator(self.onlyInt)
        self.lineCamWidth.setValidator(self.onlyInt)
        self.lineCamTimerCaptures.setValidator(self.onlyInt)
        self.lineCamID.setValidator(self.onlyInt)
        self.lineCamCaptures.setValidator(self.onlyInt)
        
    def add_functions(self): #Добавляем функции кнопкам
        self.pushButtonStart.clicked.connect(lambda: self.recognition_app_start(1)) #Передаем число 1 в функцию, для последующего запуска потока
        self.pushButtonStop.clicked.connect(lambda: self.recognition_app_start(0))
        
    def resize_form(self, width, height):
        Form.resize(width, height)
        Form.setMinimumSize(QtCore.QSize(width, height))
        Form.setMaximumSize(QtCore.QSize(width, height))
        
    def set_pixmap(self, pixmap):
        self.label_cam.setGeometry(QtCore.QRect(380, 10, 657, 370))
        pixmap = pixmap.scaledToHeight(370)
        self.label_cam.setPixmap(QPixmap(pixmap))
        
    def recognition_app_start(self, state): #Проверяем переданные значения и запускаем поток
        
        if state == 1:
            self.resize_form(1047, 390)
            self.state = True
            self.pushButtonStart.setEnabled(False) #Активность кнопок
            self.pushButtonStop.setEnabled(True)
            self.rec_app = StartRecognition(self.lineCamCaptures.text(),
                                               self.lineCamTimerCaptures.text(),
                                               self.lineCamWidth.text(),
                                               self.lineCamHeight.text(),
                                               self.lineDirectory.text(),
                                               self.lineCamID.text()) #Запуск потока и передача параметров из формы
            
            self.rec_app.start() #Стартуем
            
        else:
            self.resize_form(380, 390)
            self.pushButtonStart.setEnabled(True) #Активность кнопок
            self.pushButtonStop.setEnabled(False)
            
            self.rec_app.stop()
          
class StartRecognition(QThread): #Новый поток запускаем cv2
    
    def __init__(self, captures, time_sleep, cam_width, cam_height, directory, cam_id): #Инициализируем параметры
        self.captures = int(captures)
        self.time_sleep = int(time_sleep)
        self.cam_width = int(cam_width)
        self.cam_height = int(cam_height)
        self.directory = str(directory)
        
        ui.app_change_text_browser("Проверяю наличие дирректории.") #Просто лог в textBrowser
        
        if path.exists(self.directory): #Проверка наличия дирректории
            ui.app_change_text_browser(f"Дирректория {self.directory} существует.")
            pass
        
        else:
            ui.app_change_text_browser(f"Дирректория {self.directory} не существует.")
            ui.app_change_text_browser(f"Создаю дирректорию.")
            mkdir(self.directory)
            ui.app_change_text_browser(f"Дирректория создана.")
        
        self.cam_id = int(cam_id)
        self.state = True
        QThread.__init__(self)
        
    def img_sender(self, piximg):
        height, width, channel = piximg.shape
        bytesPerLine = 3 * width
        qImg = QImage(piximg.data, width, height, bytesPerLine, QImage.Format_RGB888)
        ui.set_pixmap(qImg)
        
    def run(self):
        
        import os
        import time
        
        import cv2
        
        i = 1
        
        ui.app_change_text_browser("Создаю поток.")
        while self.state:

            face_cascade_db = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml") #Загружаем обученные каскады
            
            cap = cv2.VideoCapture(self.cam_id) #Выбираем источник изображения
            cap.set(cv2.CAP_PROP_FRAME_WIDTH, self.cam_width) #Задаем размеры источника
            cap.set(cv2.CAP_PROP_FRAME_HEIGHT, self.cam_height)

            path = self.directory

            ui.app_change_text_browser("Поток создан.")
            
            while self.state:
                success, img = cap.read() #Читаем изображение

                img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #Переводим в оттенки серого
                faces = face_cascade_db.detectMultiScale(img_gray, 1.1, 19) #Детектим лица
                
                for (x, y, w, h) in faces: #Это наши лица, отрисовываем квадраты
                    
                    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 255, 0), 4) #Квадрат и выбор его цвета

                    milli_time = current_milli_time() #Получаем миллисекунды
                    time_now = time.strftime(f"%d %B %Y %H-%M-%S-{milli_time}", time.localtime()) #Получаем дату и время
                    
                    ui.app_change_text_browser(f"[{milli_time}] Лицо обнаружено, создаю запись.")
                    cv2.imwrite(os.path.join(path, f'{time_now} Person.jpg'), cv2.flip(img, 1)) #Логируем (сохраняем фрейм)
                    
                    img_to_send = cv2.cvtColor(cv2.flip(img, 1), cv2.COLOR_BGR2RGB)
                    self.img_sender(img_to_send)
                    
                    i += 1
                    
                    if i > self.captures: #Данная конструкция служит для быстрого выхода из потока при нажатии на кнопку стоп
                        ui.app_change_text_browser(f"Лицо захвачено, задержка захвата на {self.time_sleep} с.")
                        x = 0.0
                        
                        while x < self.time_sleep:
                            sleep(0.01)
                            x += 0.01
                            if self.state == False:
                                ui.app_change_text_browser("Поток остановлен.")
                                break
                            
                        i = 1

            cap.release() #Свободу источнику изображения!
            cv2.destroyAllWindows() #Уничтожаем окна, я полагаю это мне нужно было для вывода изображения при дебаге
            
    def stop(self): #Функция остановки потока
        self.quit()
        self.state = False
        ui.app_change_text_browser("Остановка потока.")

if __name__ == "__main__": #Инициализация приложения
    
    import sys
    
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())