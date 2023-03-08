import sys
import serial
from PyQt5 import QtWidgets, uic, QtCore, QtGui 
from openpyxl import Workbook
import datetime
import pandas as pd

class ArduinoUI(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__() # Call the inherited classes __init__ method
        uic.loadUi(r'C:\Users\WS-2\Desktop\LED BLINKER\Combined\mainwindow_v1.ui', self)
        
     
       #page change
        self.stackedWidget.setCurrentWidget(self.findChild(QtWidgets.QWidget, 'home'))

        self.UV_TOOL_BTN = self.findChild(QtWidgets.QToolButton, 'UV_TOOL_BTN')
        self.UV_TOOL_BTN.clicked.connect(self.UV_PAGE)

        def show(self):
            self.main_win.show()

        
        '''self.ser = serial.Serial('COM4',9600) #replace the 'COM3' with the serial port the arduino is connected to 
        self.push_on = self.findChild(QtWidgets.QPushButton,'push_on') #find the push button on the ui
        self.push_off = self.findChild(QtWidgets.QPushButton,'push_off') #find the push button on the ui
        self.push_blink = self.findChild(QtWidgets.QPushButton,'push_blink') #find the push button on the ui
        self.push_on.clicked.connect(self.switch_on) # connect the button to the function
        self.push_off.clicked.connect(self.switch_off) # connect the button to the function
        self.push_blink.clicked.connect(self.blink) # connect the button to the function
        self.led_status = False # initialize the led status as off
        self.led_status = False # initialize the led status as off
        self.timer = QtCore.QTimer()
        self.blink_timer = QtCore.QTimer()
        self.blink_timer.setSingleShot(True) # The timer will only run once
        self.blink_timer.timeout.connect(self.switch_off) # when the timer expires, switch off the led
        #self.reading_label = self.findChild(QtWidgets.QLabel,'temp_label') # find the label to display the readings
        self.timer.timeout.connect(self.update_data)
        self.timer.start(1000) #update data every 1s
        
        self.show() # Show the GUI


    def update_data(self):
        data = self.ser.readline().decode() #read data from the serial port and decode it
        #self.temp_label.setText(data) #update the label's text with the new data
       

    def switch_on(self):
        self.ser.write(b'1') # send '1' to turn on the led
        self.led_status = True

    def switch_off(self):
        self.ser.write(b'0') # send '0' to turn off the led
        self.led_status = False

    def blink(self):
        self.ser.write(b'2') # send '2' to blink the led
        self.blink_timer.start(10000) # start the blink timer for 10 seconds

    def generate_excel_file(self):
        #get the current timestamp
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        #get the temperature reading from the sensor
        temperature = self.ser.readline().decode()

        #create the new Excel file 
        wb = workbook()
        sheet = wb.active

        #write the timestamp and temperature reading to the first row
        sheet['A1'] = "Timestamp"
        sheet['B1'] = "Temperature (C)"
        sheet['A2'] = timestamp
        sheet['B2'] = temperature

        #save the file
        wb.save("data readings.xlsx")


    self.push_data = self.findChild(QtWidgets.QPushButton,'push_data') #find the push button on the ui to generate data sheet
    self.push_data.clicked.connect(self.generate_excel_file)
'''
app = QtWidgets.QApplication(sys.argv)
window = ArduinoUI()
window.show()
sys.exit(app.exec_())

