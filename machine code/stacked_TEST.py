from PyQt5.QtWidgets import QApplication, QMainWindow, QStackedWidget
from mainwindow_v1 import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Set up the user interface from Designer.
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # Default Home pane to the slot that switches to the other panes as per the toolbutton clicked
        self.ui.stackedWidget.setCurrentWidget(self.ui.nav_home)
        # Connect the clicked signal of the toolButtons of the module manager that switches to the LED pane
        self.ui.led_btn.clicked.connect(self.switch_to_led_pane)
        # Connect the clicked signal of the toolButtons of the module manager that switches to the UV pane
        self.ui.uv_btn.clicked.connect(self.switch_to_uv_pane)
        # Connect the clicked signal of the toolButtons of the module manager that 0switches to the IR pane
        self.ui.ir_btn.clicked.connect(self.switch_to_ir_pane)
         # Connect the clicked signal of the toolButtons of the module manager that switches to the CA pane
        self.ui.cv_btn.clicked.connect(self.switch_to_cv_pane)
         # Connect the clicked signal of the toolButtons of the module manager that switches to the CQW pane
        self.ui.sqw_btn.clicked.connect(self.switch_to_sqw_pane)
         # Connect the clicked signal of the toolButtons of the module manager that switches to the CA pane
        self.ui.ca_btn.clicked.connect(self.switch_to_ca_pane)

    def switch_to_led_pane(self):
        # Switch to the LED pane
        self.ui.stackedWidget.setCurrentWidget(self.ui.led_pane)
    def switch_to_uv_pane(self):
        # Switch to the UV pane
        self.ui.stackedWidget.setCurrentWidget(self.ui.uv_pane)
    def switch_to_ir_pane(self):
        # Switch to the IR pane
        self.ui.stackedWidget.setCurrentWidget(self.ui.ir_pane)
    def switch_to_cv_pane(self):
        # Switch to the CV pane
        self.ui.stackedWidget.setCurrentWidget(self.ui.cv_pane)
    def switch_to_sqw_pane(self):
        # Switch to the SQW pane
        self.ui.stackedWidget.setCurrentWidget(self.ui.sqw_pane)
    def switch_to_ca_pane(self):
        # Switch to the CA pane
        self.ui.stackedWidget.setCurrentWidget(self.ui.ca_pane)


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
