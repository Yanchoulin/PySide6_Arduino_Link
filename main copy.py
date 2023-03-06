from PySide6.QtWidgets import QApplication, QWidget,QLabel,QPushButton
from PySide6.QtGui import QColor
import sys
from led_ui import Ui_led_ui
import serial
import msvcrt  # msvcrt模組用於在Windows上檢測鍵盤按鍵
import threading
import time
import mysql.connector
from datetime import datetime
from PySide6.QtCore import Qt
from PySide6.QtCharts import QChartView, QChart, QLineSeries, QValueAxis, QScatterSeries

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
        self.led2P.clicked.connect(self.led2_on_off)
        self.LD3P.clicked.connect(self.LD3P_on_off)
        self.LD4P.clicked.connect(self.LD4P_on_off)
        self.LD5P.clicked.connect(self.LD5P_on_off)
        self.LD6P.clicked.connect(self.LD6P_on_off)  
        self.getdataP.clicked.connect(self.Get_Data) 
        self.exitP.clicked.connect(app.quit) 
         # 初始化 chart
        self.chart = QChart()
        self.chart.setBackgroundBrush(QColor('lightgray'))
        self.series1 = QLineSeries()
        self.series2 = QLineSeries()
        self.chart.addSeries(self.series1)
        self.chart.addSeries(self.series2)
        self.chart.createDefaultAxes()
        self.chart.axisX().setTitleText("X Axis")
        self.chart.axisY().setTitleText("Y Axis")
        self.chargraph.setChart(self.chart)
        # self.ui.chargraph = QtCharts.QChartView(self.ui.centralwidget)  # 將 chargraph 設置為 Ui_led_ui 的屬性
       
            
    def led1_on_off(self):
        if self.led1 == True:
            self.ser.write(b'1')
            self.led1P.setStyleSheet("color:white;background-color: red")
        else:
            self.ser.write(b'a')
            self.led1P.setStyleSheet("color:black;background-color: white")
        self.led1 = not self.led1
        
            
    def led2_on_off(self):
        if self.led2 == True:
            self.ser.write(b'2')
            self.led2P.setStyleSheet("color:white;background-color: red")
        else:
            self.ser.write(b'b')     
            self.led2P.setStyleSheet("color:black;background-color: white")   
        self.led2 = not self.led2      
        
    def LD3P_on_off(self):
        if self.led3 == True:
            self.ser.write(b'3')
            self.LD3P.setStyleSheet("color:white;background-color: red")
        else:
            self.ser.write(b'c') 
            self.LD3P.setStyleSheet("color:black;background-color: white")
        self.led3 = not self.led3     
        
    def LD4P_on_off(self):
        if self.led4 == True:
            self.ser.write(b'4')
            self.LD4P.setStyleSheet("color:white;background-color: red")
        else:
            self.ser.write(b'd') 
            self.LD4P.setStyleSheet("color:black;background-color: white")
        self.led4 = not self.led4    
        
    def LD5P_on_off(self):
        if self.led5 == True:
            self.ser.write(b'5')
            self.LD5P.setStyleSheet("color:white;background-color: red")
        else:
            self.ser.write(b'e') 
            self.LD5P.setStyleSheet("color:black;background-color: white")
        self.led5 = not self.led5  
        
    def LD6P_on_off(self):
        if self.led6 == True:
            self.ser.write(b'6')
            self.LD6P.setStyleSheet("color:white;background-color: red")
        else:
            self.ser.write(b'f') 
            self.LD6P.setStyleSheet("color:black;background-color: white")
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





    
    def update_chart(self, x, y1, y2):
        self.series1.clear()
        self.series2.clear()

        for i in range(len(x)):
            self.series1.append(x[i], y1[i])
            self.series2.append(x[i], y2[i])
        self.series1.setName("溫度")
        self.series2.setName("濕度")
        self.chart = QChart()
        self.chart.addSeries(self.series1)
        self.chart.addSeries(self.series2)
        self.chart.legend().setVisible(True)
        self.chart.legend().setAlignment(Qt.AlignBottom)

        axis_x = QValueAxis()
        axis_x.setTickCount(len(x))
        axis_x.setLabelFormat("%d")
        axis_x.setTitleText("次數")
        axis_x.setRange(0, len(x))

        axis_y = QValueAxis()
        axis_y.setLabelFormat("%.2f")
        axis_y.setTitleText("溫溼度")
        min_y = min(min(y1), min(y2))
        max_y = max(max(y1), max(y2))
        axis_y.setRange(min_y, max_y)

        self.chart.addAxis(axis_x, Qt.AlignBottom)
        self.series1.attachAxis(axis_x)
        self.series2.attachAxis(axis_x)

        self.chart.addAxis(axis_y, Qt.AlignLeft)
        self.series1.attachAxis(axis_y)
        self.series2.attachAxis(axis_y)

        self.chargraph.setChart(self.chart)
    
          


    def read_port(self):
        data='qqqq'
        oldtemp = ""
        oldhumi = ""
        while True:
            # if msvcrt.kbhit():  # 如果有鍵盤按鍵被按下
            #     break  # 離開 while loop
            if self.ser.in_waiting > 0:
                
                # print(self.ser.in_waiting )
                data = self.ser.readline().decode('utf-8')
                print(data)
                time.sleep(0.005)
                if ('temp' and 'humi' not in data):
                    if data[0] == 'a':
                        
                        self.SW1.setStyleSheet("background-color: green")
                        print('a')
                    else:
                        self.SW1.setStyleSheet("background-color: white")
                        
                    if data[1] == 'b':
                        
                        self.pushButton_2.setStyleSheet("background-color: green")
                        print('b')
                    else:
                        self.pushButton_2.setStyleSheet("background-color: white")
                        
                    if data[2] == 'c':
                        
                        self.SW3.setStyleSheet("background-color: green")
                        print('c')
                    else:
                        self.SW3.setStyleSheet("background-color: white")

                    if data[3] == 'd':
                        
                        self.SW4.setStyleSheet("background-color: green")
                        print('d')
                    else:
                        self.SW4.setStyleSheet("background-color: white")
                        
                if 'temp' in data:
                
                    oldtemp = data.strip('temp:')
                    self.tempL.setText(data.strip('temp:'))
                   
                    
                if 'humi' in data:
                    print(data.strip('humi:'))
                    oldhumi = data.strip('humi:')
                    self.humiL.setText(data.strip('humi:'))
                   
                    
                if oldtemp != "" and  oldhumi != "":  
                    conn = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="kisama0310",
                    database='temperature_humidity')
                    cur = conn.cursor()
                    # cur.execute("CREATE TABLE record (id INT AUTO_INCREMENT PRIMARY KEY, datetime DATETIME, temperature FLOAT, humidity FLOAT)")
                    now = datetime.now()
                    datetime_string = now.strftime("%Y-%m-%d %H:%M:%S")
                    temperature = oldtemp
                    humidity = oldhumi
                    cur.execute("INSERT INTO record (datetime, temperature, humidity) VALUES (%s, %s, %s)", (datetime_string, temperature, humidity))
                    conn.commit()
                    cur.close()
                    conn.close()
                
               
                    
                    
                    
         
        self.ser.close()              
                    
                    
    def init_sql(self):
        conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="kisama0310")
        cur = conn.cursor()
        cur.execute('CREATE DATABASE IF NOT EXISTS temperature_humidity')
        cur.close()
        print('init pass')
        
        
    def write_sql(self,temp,humi):
        conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="kisama0310",
        database='temperature_humidity')
        cur = conn.cursor()
        cur.execute("CREATE TABLE record (id INT AUTO_INCREMENT PRIMARY KEY, datetime DATETIME, temperature FLOAT, humidity FLOAT)")
        now = datetime.now()
        datetime_string = now.strftime("%Y-%m-%d %H:%M:%S")
        temperature = temp
        humidity = humi
        cur.execute("INSERT INTO record (datetime, temperature, humidity) VALUES (%s, %s, %s)", (datetime_string, temperature, humidity))
        conn.commit()
        cur.close()
        conn.close()
        
        # conn = mysql.connector.connect(host='localhost', user='root', password='kisama0310', database='temperature_humidity')
        # # 連接資料庫

        # # 創建游標
        # cur = conn.cursor()

        # # 插入資料
        # now = datetime.now()
        # datetime_string = now.strftime("%Y-%m-%d %H:%M:%S")
        # temperature = 25.0
        # humidity = 50.0
        # cur.execute("INSERT INTO record (datetime, temperature, humidity) VALUES (%s, %s, %s)", (datetime_string, temperature, humidity))

        # # 提交事務
        # conn.commit()

        # # 關閉游標和資料庫連接
        # cur.close()
        # conn.close()
    
    
          
        
                    
                                                   
        
        
                
        
        








app = QApplication(sys.argv)
window = led()

window.setWindowTitle("PyQt_Arduino_Link_Ui")

window.show()
s = threading.Thread(target = window.read_port,daemon=True )
s.start()
app.exec() #監視所有事件消息