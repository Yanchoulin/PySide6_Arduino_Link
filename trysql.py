# import mysql.connector
# from datetime import datetime


# # # 連接資料庫（如果不存在，會自動創建）
# # conn = mysql.connector.connect(host='localhost', user='root', password='kisama0310')

# # # 創建游標
# # cur = conn.cursor()

# # # 創建資料庫（如果不存在）
# # cur.execute('CREATE DATABASE IF NOT EXISTS temperature_humidity')

# # # 關閉游標
# # cur.close()

# # # 重新連接到資料庫
# # conn = mysql.connector.connect(host='localhost', user='root', password='kisama0310', database='temperature_humidity')

# # # 創建游標
# # cur = conn.cursor()

# # # 創建表
# # cur.execute('''CREATE TABLE record
# #                 (datetime DATETIME PRIMARY KEY,
# #                 temperature FLOAT,
# #                 humidity FLOAT);''')

# # # 關閉游標和資料庫連接
# # cur.close()
# # conn.close()

# # conn = mysql.connector.connect(host='localhost', user='root', password='kisama0310', database='temperature_humidity')
# # # 連接資料庫

# # # 創建游標
# # cur = conn.cursor()

# # # 插入資料
# # now = datetime.now()
# # datetime_string = now.strftime("%Y-%m-%d %H:%M:%S")
# # temperature = 25.0
# # humidity = 50.0
# # cur.execute("INSERT INTO record (datetime, temperature, humidity) VALUES (%s, %s, %s)", (datetime_string, temperature, humidity))

# # # 提交事務
# # conn.commit()

# # # 關閉游標和資料庫連接
# # cur.close()
# # conn.close()



# # def init_sql(x):
# #     print(x)
# #     conn = mysql.connector.connect(
# #     host="localhost",
# #     user="root",
# #     password="kisama0310")
# #     cur = conn.cursor()
# #     cur.execute('CREATE DATABASE IF NOT EXISTS temperature_humidity')
# #     cur.close()
        
# # init_sql('test') 


# from PySide6 import QtWidgets, QtCore, QtGui, QtCharts

# class Ui_Form(object):
#     def setupUi(self, Form):
#         Form.setObjectName("Form")
#         Form.resize(800, 600)
#         self.chart_view = QtCharts.QChartView(Form)
#         self.chart_view.setGeometry(QtCore.QRect(10, 10, 780, 580))
#         self.chart_view.setObjectName("chart_view")
#         self.series = QtCharts.QLineSeries(Form)
#         self.series.setName("Line 1")

#         # 添加数据点
#         self.series.append(0, 6)
#         self.series.append(2, 4)
#         self.series.append(3, 8)
#         self.series.append(7, 4)
#         self.series.append(10, 5)

#         self.series2 = QtCharts.QLineSeries(Form)
#         self.series2.setName("Line 2")

#         # 添加数据点
#         self.series2.append(0, 3)
#         self.series2.append(1, 2)
#         self.series2.append(3, 1)
#         self.series2.append(8, 5)
#         self.series2.append(10, 3)

#         self.chart = QtCharts.QChart()
#         self.chart.addSeries(self.series)
#         self.chart.addSeries(self.series2)
#         self.chart.setTitle("Line Chart Example")
#         self.chart.createDefaultAxes()
        
#         # 设置 x 轴范围
#         axis_x = QtCharts.QValueAxis()
#         axis_x.setRange(0, 10)
#         axis_x.setTickCount(11)
#         self.chart.setAxisX(axis_x, self.series)
#         self.chart.setAxisX(axis_x, self.series2)

#         # 设置 y 轴范围
#         axis_y = QtCharts.QValueAxis()
#         axis_y.setRange(0, 10)
#         axis_y.setTickCount(11)
#         self.chart.setAxisY(axis_y, self.series)
#         self.chart.setAxisY(axis_y, self.series2)

#         self.chart.legend().setVisible(True)
#         self.chart.legend().setAlignment(QtCore.Qt.AlignBottom)

#         self.chart_view.setChart(self.chart)

#         self.retranslateUi(Form)
#         QtCore.QMetaObject.connectSlotsByName(Form)

#     def retranslateUi(self, Form):
#         _translate = QtCore.QCoreApplication.translate
#         Form.setWindowTitle(_translate("Form", "Form"))

# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     Form = QtWidgets.QWidget()
#     ui = Ui_Form()
#     ui.setupUi(Form)
#     Form.show()
#     sys.exit(app.exec_())

# import sys
# from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
# from PySide6.QtGui import QIcon
# import qdarkstyle

# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.init_ui()
    
#     def init_ui(self):
#         # 設置窗口圖標
#         self.setWindowIcon(QIcon('D:\JSON\Link_Arduino_Ui\Exit.png'))

#         # 創建按鈕
#         button = QPushButton('Click me', self)
#         button.move(50, 50)

#         # 設置樣式表
#         self.setStyleSheet(qdarkstyle.load_stylesheet())

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec_())


# import PySide6.QtGui as QtGui
# import PySide6.QtCharts as QtCharts
# import sys
# from PySide6.QtWidgets import QApplication
# from PySide6.QtGui import QPainter
# from PySide6.QtCore import Qt
# # 創建一個 QChart 物件
# chart = QtCharts.QChart()

# # 創建一個 QLineSeries 物件 (示例)
# series = QtCharts.QLineSeries()
# series.append(0, 0)
# series.append(1, 1)

# # 將數據系列添加到圖表中
# chart.addSeries(series)

# # 設置數據系列和軸之間的關聯
# x_axis = QtCharts.QValueAxis()
# y_axis = QtCharts.QValueAxis()
# chart.addAxis(x_axis, QtCharts.Qt.AlignBottom)
# chart.addAxis(y_axis, QtCharts.Qt.AlignLeft)
# series.attachAxis(x_axis)
# series.attachAxis(y_axis)

# # 設置網格線的筆刷 (即背景筆刷)
# brush = QtGui.QBrush(QtGui.QColor("gray"))
# chart.setPlotAreaBackgroundBrush(brush)
import PySide6.QtGui as QtGui
import PySide6.QtWidgets as QtWidgets
import PySide6.QtCharts as QtCharts

# 創建一個 QChart 物件
chart = QtCharts.QChart()

# 創建一個 QLineSeries 物件 (示例)
series = QtCharts.QLineSeries()
series.append(0, 0)
series.append(1, 1)

# 將數據系列添加到圖表中
chart.addSeries(series)

# 設置數據系列和軸之間的關聯
x_axis = QtCharts.QValueAxis()
y_axis = QtCharts.QValueAxis()
chart.addAxis(x_axis, QtCharts.Qt.AlignBottom)
chart.addAxis(y_axis, QtCharts.Qt.AlignLeft)
series.attachAxis(x_axis)
series.attachAxis(y_axis)

# 創建 QChartView 物件，將 QChart 添加到其中
chart_view = QtCharts.QChartView(chart)

# 修改底色為藍色
chart_view.setStyleSheet("background-color: blue;")

# 創建一個主窗口並顯示 QChartView
app = QtWidgets.QApplication()
main_window = QtWidgets.QMainWindow()
main_window.setCentralWidget()

main_window.show()




# your code here

app.exec_()

