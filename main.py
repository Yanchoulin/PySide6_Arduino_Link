from PySide6.QtWidgets import QApplication, QWidget,QLabel,QPushButton,QMessageBox,QInputDialog, QMenuBar,QMenu
from PySide6.QtGui import QColor,QAction,QIcon,QBrush
import sys
from led_ui import Ui_led_ui
import serial
import msvcrt  # msvcrt模組用於在Windows上檢測鍵盤按鍵
import threading
import time
import mysql.connector
from datetime import datetime
from PySide6.QtCore import Qt,QTimer
from PySide6.QtCharts import QChartView, QChart, QLineSeries, QValueAxis, QScatterSeries
import pyautogui  
import psutil
import qdarkstyle

class led(QWidget,Ui_led_ui):
    def __init__(self):
        super().__init__()
        self.ui = Ui_led_ui()
        self.setupUi(self)
        self.init_sql()
       
        
        self.led1 = True
        self.led2 = True
        self.led3 = True
        self.led4 = True
        self.led5 = True
        self.led6 = True
        self.ser = serial.Serial('com3',115200)
        self.led1P.clicked.connect(self.led1_on_off)
        # self.led1P.clicked.connect(self.get_color)
        self.led2P.clicked.connect(self.led2_on_off)
        self.LD3P.clicked.connect(self.LD3P_on_off)
        self.LD4P.clicked.connect(self.LD4P_on_off)
        self.LD5P.clicked.connect(self.LD5P_on_off)
        self.LD6P.clicked.connect(self.LD6P_on_off)  
        self.getdataP.clicked.connect(self.Get_Data) 
        self.exitP.clicked.connect(app.quit) 
         # 初始化 chart
        self.chart = QChart()
        self.chart.setBackgroundBrush(QColor('black'))
        self.brush = QBrush(QColor("#455364")) # 設置標題筆刷 (文字顏色)
        self.chart.setPlotAreaBackgroundBrush(self.brush)
        self.series1 = QLineSeries()
        self.series2 = QLineSeries()
        self.chart.addSeries(self.series1)
        self.chart.addSeries(self.series2)
        self.chart.createDefaultAxes()
        # self.chart.axisX().setTitleText("X Axis")
        # self.chart.axisY().setTitleText("Y Axis")
        self.chargraph.setChart(self.chart)
        
        self.setStyleSheet(qdarkstyle.load_stylesheet())
        self.menubar = QMenuBar(self)     # 建立 menubar
        

        
        self.menu_file = QMenu('檔案(F)')    # 建立一個 File 選項 ( QMenu )
        self.menu_file .grabShortcut('Ctrl+F')
        # self.menubar.addMenu(self.menu_file)
        self.menu_edit = QMenu('編輯(E)')
        # self.menu_file.setIcon(QIcon('database-pngrepo-com.png'))
        self.menu_save = QMenu('選取項目(S)')
        self.menu_view = QMenu('檢視(V)')
        self.menu_run = QMenu('執行(R)')
        


        self.action_open = QAction('Get_Chart')    # 建立一個 Open 選項 ( QAction )
        self.action_open.setIcon(QIcon('D:\JSON\Link_Arduino_Ui\Get_Chart.png'))
        self.action_open.triggered.connect(self.Get_Chart)
        self.menu_file.addAction(self.action_open)  # 將 Open 選項放入 File 選項裡
        self.action_open.setShortcut('Ctrl+O')
        self.menu_file.addSeparator()

        self.action_close = QAction('Exit')  # 建立一個 Close 選項 ( QAction )
        self.action_close.triggered.connect(self.Exit)
        self.action_close.setIcon(QIcon('D:\JSON\Link_Arduino_Ui\Exit.png'))
        self.menu_file.addAction(self.action_close) # 將 Close 選項放入 File 選項裡
        self.action_close.setShortcut('Ctrl+C')
        self.menu_file.addSeparator()
        self.action_Reini_serial = QAction('Reini_serial')  # 建立一個 Reini_serial 選項 ( QAction )
        self.action_Reini_serial.triggered.connect(self.Reini_serial)
        self.menu_file.addAction(self.action_Reini_serial) # 將 Reini_serial 選項放入 File 選項裡
        self.menu_file.addSeparator()
        self.menubar.addMenu(self.menu_file)        # 將 File 選項放入 menubar 裡
        self.menubar.addMenu(self.menu_edit)
        self.menubar.addMenu(self.menu_save)
        self.menubar.addMenu(self.menu_view)
        self.menubar.addMenu(self.menu_run)
        
       
        
        # 獲取標籤的背景色
        palette = self.led1P.palette()
        background_color = palette.color(palette.ColorGroup.Normal, palette.ColorRole.Window)

        print(background_color.name())  # 印出背景色的名稱，例如 "#00ff00"

        
        if psutil.Process().as_dict(attrs=['status'])['status'] == 'stopped':
            print("sleeping")
            self.timer = QTimer()   
            self.timer.timeout.connect(self.LD4P_on_off)   # 設定定時要執行的 function
            self.timer.start(10)  
    
    # def get_color(self):
    #     palette = self.LD3P.palette()
    #     background_color = palette.color(palette.ColorGroup.Normal, palette.ColorRole.Window)
    #     print(background_color.name())  # 印出背景色的名稱，例如 "#00ff00"
        
        
    # 移動滑鼠游標到指定座標位置   

    
    def Exit(self):
        app.quit()
    def Get_Chart(self):
        self.Get_Data()
        
        
    def Reini_serial(self):
        self.ser.close()
        
        self.ser.open()
        self.read_port()
        
                
    def led1_on_off(self):
        if self.led1 == True:
            self.ser.write(b'1')
            self.led1P.setStyleSheet("color:black;background-color: orange")
            self.show_dialog() 
            
        else:
            self.ser.write(b'a')
            self.led1P.setStyleSheet("color:white;background-color: #455364")
        self.led1 = not self.led1
        
            
    def led2_on_off(self):
        if self.led2 == True:
            self.ser.write(b'2')
            self.led2P.setStyleSheet("color:black;background-color: orange")
        else:
            self.ser.write(b'b')     
            self.led2P.setStyleSheet("color:white;background-color: #455364")   
        self.led2 = not self.led2      
        
    def LD3P_on_off(self):
        if self.led3 == True:
            self.ser.write(b'3')
            self.LD3P.setStyleSheet("color:black;background-color: orange")
            self.show_message()
        else:
            self.ser.write(b'c') 
            self.LD3P.setStyleSheet("color:white;background-color: #455364")
        self.led3 = not self.led3     
        
    def LD4P_on_off(self):
        if self.led4 == True:
            self.ser.write(b'4')
            self.LD4P.setStyleSheet("color:black;background-color: orange")
        else:
            self.ser.write(b'd') 
            self.LD4P.setStyleSheet("color:white;background-color: #455364")
        self.led4 = not self.led4    
        
    def LD5P_on_off(self):
        if self.led5 == True:
            self.ser.write(b'5')
            self.LD5P.setStyleSheet("color:black;background-color: orange")
        else:
            self.ser.write(b'e') 
            self.LD5P.setStyleSheet("color:white;background-color: #455364")
        self.led5 = not self.led5  
        
    def LD6P_on_off(self):
        if self.led6 == True:
            self.ser.write(b'6')
            self.LD6P.setStyleSheet("color:black;background-color: orange")
        else:
            self.ser.write(b'f') 
            self.LD6P.setStyleSheet("color:white;background-color: #455364")
        self.led6 = not self.led6     
    
    
            
    def Get_Data(self):
        conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="kisama0310",
        database='temperature_humidity')
        cur = conn.cursor()
        # 準備 SQL 查詢語句
        sql = "SELECT id, temperature, humidity FROM record"
        # 執行查詢
        cur.execute(sql)
        # 取得查詢結果
        results = cur.fetchall()
        id = []
        temperature=[]
        humidity=[]
        for row in results:
            id.append(row[0])
            temperature.append(row[1])
            humidity.append(row[2])
        # 關閉Cursor和資料庫連線
        cur.close()
        conn.close()
        # 呼叫update_chart函數來更新圖表
        self.update_chart(id, temperature, humidity)
 
        
#在上面的示例代碼中，我們首先使用 mysql.connector 模組建立資料庫連線，然後建立資料庫游標，
# 並使用 SELECT 語句從 "record" 資料表中檢索所有資料行的 "datetime_string"、"temperature" 
# 和 "humidity" 欄位。接著使用 fetchall() 方法將查詢結果儲存在 results 變數中，最後使用迴圈
# 逐行處理查詢結果，並將 "datetime_string"、"temperature" 和 "humidity" 欄位的值儲存在相應的
# 變數中，可以在這裡對資料進行進一步的處理。最後，我們使用 close() 方法關閉資料庫連線和游標。
    

    def mousePressEvent(self, event):
        print('press')


    
    def update_chart(self, x, y1, y2):
        self.series1.clear()
        self.series2.clear()
        
        

        for i in range(len(x)):
            self.series1.append(x[i], y1[i])
            self.series2.append(x[i], y2[i])
        self.series1.setName("溫度")
        self.series2.setName("濕度")
        self.chart = QChart()
        self.chart.setBackgroundBrush(QColor('black'))
        self.chart.addSeries(self.series1)
        self.chart.addSeries(self.series2)
        self.chart.legend().setVisible(True)
        self.chart.legend().setAlignment(Qt.AlignBottom)
        self.brush = QBrush(QColor("gray")) # 設置標題筆刷 
        self.chart.setPlotAreaBackgroundBrush(self.brush)
        self.chart_view = QChartView(self.chart)
        self.chart_view.setStyleSheet("background-color: black;")

        self.axis_x = QValueAxis()
        self.axis_x.setTickCount(len(x))
        self.axis_x.setLabelFormat("%d")
        # self.axis_x.setTitleText("次數")
        self.axis_x.setLabelsColor(QColor("white"))
        self.axis_x.setRange(0, len(x))

        self.axis_y = QValueAxis()
        self.axis_y.setLabelFormat("%.2f")
        # self.axis_y.setTitleText("溫溼度")
        self.axis_y.setLabelsColor(QColor("white"))
        self.min_y = min(min(y1), min(y2))
        self.max_y = max(max(y1), max(y2))
        self.axis_y.setRange(self.min_y, self.max_y)

        self.chart.addAxis(self.axis_x, Qt.AlignBottom)
        self.series1.attachAxis(self.axis_x)
        self.series2.attachAxis(self.axis_x)

        self.chart.addAxis(self.axis_y, Qt.AlignLeft)
        self.series1.attachAxis(self.axis_y)
        self.series2.attachAxis(self.axis_y)
        

        self.chargraph.setChart(self.chart)
        print("平均溫度: ",sum(y1)/len(y1) )
        print("平均濕度: ",sum(y2)/len(y2) )
    
        
        
    
          


    def read_port(self):
        data='qqqq'
        old_data = 'qqqq'
        oldtemp = ""
        oldhumi = ""
        self.humiL.setStyleSheet("color:red")
        self.tempL.setStyleSheet("color:red")
        while True:
            # if msvcrt.kbhit():  # 如果有鍵盤按鍵被按下
            #     break  # 離開 while loop
            if self.ser.in_waiting > 0:
                
                # print(self.ser.in_waiting )
                data = self.ser.readline().decode('utf-8')
                print(data)
                print('olddata',old_data)
                # time.sleep(0.005)
                print('len data: ',len(data))
                # if ('temp' and 'humi' not in data): #and (old_data != data) and len(old_data) == 6 and len(data) == 6):
                if data[0] == 'a':
                    
                    self.SW1.setStyleSheet("color:black;background-color: orange")
                    print('a')
                    
                if  data[0] == 'q':
                    self.SW1.setStyleSheet("color:white;background-color: #455364")
                    
                if data[1] == 'b':
                    
                    self.pushButton_2.setStyleSheet("color:black;background-color: orange")
                    
                    print('b')
                    # time.sleep(0.001)
                if  data[1] == 'q':
                    self.pushButton_2.setStyleSheet("color:white;background-color: #455364")
                    
                    
                if data[2] == 'c':
                    
                    self.SW3.setStyleSheet("color:black;background-color: orange")
                    print('c')
                    # time.sleep(0.001)
                if  data[2] == 'q':
                    self.SW3.setStyleSheet("color:white;background-color: #455364")

                if data[3] == 'd':
                    
                    self.SW4.setStyleSheet("color:black;background-color: orange")
                    print('d')
                    # time.sleep(0.001)
                if  data[3] == 'q':
                    self.SW4.setStyleSheet("color:white;background-color: #455364")
                        
                if 'temp' in data:
                
                    oldtemp = data.strip('temp:')
                    self.tempL.setText(data.strip('temp:'))
                   
                    
                if 'humi' in data:
                    print(data.strip('humi:'))
                    oldhumi = data.strip('humi:')
                    self.humiL.setText(data.strip('humi:'))
                   
                    
                if data != 'qqqq' and oldtemp != "" and  oldhumi != "": 
                    self.write_data(oldtemp,oldhumi) 
                
                old_data = data
                
      
        self.ser.close() 
        
                
    def write_data(self,temp,humi):
        conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="kisama0310",
        database='temperature_humidity')
        cur = conn.cursor()    
        cur.execute("CREATE TABLE IF NOT EXISTS record (id INT AUTO_INCREMENT PRIMARY KEY, datetime DATETIME, temperature INT, humidity INT)")       
        now = datetime.now()
        datetime_string = now.strftime("%Y-%m-%d %H:%M:%S")
        temperature = temp
        humidity = humi
        cur.execute("INSERT INTO record (datetime, temperature, humidity) VALUES (%s, %s, %s)", (datetime_string, temperature, humidity))
        conn.commit()
        cur.close()
        conn.close() 
        print('Write DATA pass')           
                    
                    
         
                 
                    
                    
    def init_sql(self):
        conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="kisama0310")
        cur = conn.cursor()
        cur.execute('CREATE DATABASE IF NOT EXISTS temperature_humidity')
        cur.close()
        print('SQL init pass')
        
        
    def write_sql(self,temp,humi):
        # 連接資料庫
        conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="kisama0310",
        database='temperature_humidity')
        # 創建游標
        cur = conn.cursor()
        
        cur.execute("CREATE TABLE IF NOT EXISTS record (id INT AUTO_INCREMENT PRIMARY KEY, datetime DATETIME, temperature INT, humidity INT)")
        now = datetime.now()
        datetime_string = now.strftime("%Y-%m-%d %H:%M:%S")
        temperature = temp
        humidity = humi
        # 插入資料
        cur.execute("INSERT INTO record (datetime, temperature, humidity) VALUES (%s, %s, %s)", (datetime_string, temperature, humidity))
        # 提交事務
        conn.commit()
        # 關閉游標和資料庫連接
        cur.close()
        conn.close()
        print('Write SQL pass')
    
    def closeEvent(self, event):
        print("run event")
        print(self.chart.axes())
        for axis in self.chart.axes():
            if axis == self.axis_x:
                self.chart.removeAxis(axis)
        print(self.chart.axes())
        for axis in self.chart.axes():
            if axis == self.axis_y:
                self.chart.removeAxis(axis)
        print(self.chart.axes())
        # del self.chartView
        del self.chart
        del self.axis_x
        del self.axis_y
        # self.chart.removeAxis(self.axis_x)
        # self.chart.removeAxis(self.axis_y)
        super().closeEvent(event)
    
    
    def show_message(self):
        self.mbox = QMessageBox(self)   
        # self.mbox.information(self, '提示:', '再按壓一次LED3按鍵,取消輸出保持\n押OK鍵後離開提示介面') 
        self.mbox.setText("再按壓一次LED3按鍵,取消輸出保持\n押OK鍵後離開提示介面")
        self.mbox.setIcon(QMessageBox.Icon.Information)
        self.mbox.exec()

    def show_dialog(self):
        its = ['A','B', 'C', 'D', 'F', 'G']
        text, ok =QInputDialog().getItem(self, 'Get_Item', '請輸入一段文字',its,5)
        print(text, ok)



    
app = QApplication(sys.argv)
icon = QIcon('D:/JSON/Link_Arduino_Ui/wth.png')
app.setWindowIcon(icon)
window = led()

window.setWindowTitle("PyQt_Arduino_Link_Ui")

window.show()
s = threading.Thread(target = window.read_port,daemon=True )
s.start()

sys.exit(app.exec()) #監視所有事件消息