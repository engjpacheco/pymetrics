import sys, csv, os
from PyQt5.QtWidgets import ( QApplication, QMainWindow, QMainWindow, QMessageBox)
from PyQt5.QtCore import QDate
from PyQt5.uic import loadUi
from variables import *
from mainform import *
from themes import dark_theme, light_theme

class Window(QMainWindow, Ui_mainForm):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        # Set initial theme to dark
        self.current_theme = "dark"
        self.setStyleSheet(dark_theme)

        #Machine type selector.
        self.cb_machine.addItems([str(equipment) for equipment in EQUIPMENT])
        self.cb_machine.currentIndexChanged.connect(self.update_cb_id)
        # ID selector
        self.update_cb_id()
        # technician selector
        self.cb_tech.addItems([str(tec) for tec in TECS])
        # Date selector
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setDate(QDate.currentDate())
        # Submit button
        self.pb_submit.clicked.connect(self.submit)
        # Clear fields button
        self.pb_clear.clicked.connect(self.clear_fields)
        # Toggle theme
        self.pb_theme.clicked.connect(self.switch_theme)


    def update_cb_id(self):
        machine_type = self.cb_machine.currentText()
        self.cb_id.clear()

        machine_ranges = {
            "IMM": (1, moldeo, 100),
            "ROBOT": (1, moldeo, 200),
            "THERMO": (1, moldeo, 300),
            "MAGUIRE": (1, moldeo, 400),
            "SOFT-TRIM": (1, softrim, 500),
            "BOOTH": (1, booth, 600),
            "VINIL": (1, vinil, 700),
            "T1XX": (1, t1xx, 800),
            "CX483": (1, cx483, 900),
            "U725": (1, u725, 1000),
            "KXX/KM": (1, kxx, 1100),
            "BT1CG/PERFCAR/P708": (1, bt1cg, 1200),
            "GAP HIDDER": (1, gap_hidder, 1300),
            "OTROS": (1, otros, 1400)
        }

        if machine_type in machine_ranges:
            start, end, base = machine_ranges[machine_type]
            self.cb_id.addItems([str(i + base) for i in range(start, end + 1)])


    def submit(self):
        machine_type = self.cb_machine.currentText()
        machine_id = self.cb_id.currentText()
        technician = self.cb_tech.currentText()
        date = self.dateEdit.date().toString("yyyy-MM-dd")
        work_order = self.textWorkorder.toPlainText()
        notes = self.textDescription.toPlainText()
        time_spent = self.repairSpinbox.text()
        downtime = self.downSpinbox.text()

        data = [machine_type, machine_id, technician, date, work_order, notes, time_spent, downtime]

        file_path = "maintenance_log.csv"
        file_exists = os.path.exists(file_path)

        with open(file_path, mode='a', newline='') as file:
            writer = csv.writer(file)
            if os.stat(file_path).st_size == 0:
                writer.writerow(["Machine Type", "Machine ID", "Technician", "Date", "Work Order Number", "Technician Notes", "Time Spent (minutes)", "Downtime (minutes)"])
            writer.writerow(data)
        
        self.clear_fields()

    def clear_fields(self):
        self.textWorkorder.clear()
        self.textDescription.clear()
        self.repairSpinbox.setValue(self.repairSpinbox.minimum())
        self.downSpinbox.setValue(self.downSpinbox.minimum())
        self.cb_machine.setCurrentIndex(0)
        self.cb_tech.setCurrentIndex(0)
        self.dateEdit.setDate(QDate.currentDate())
        self.update_cb_id()

    def switch_theme(self):
        if self.current_theme == "dark":
            self.setStyleSheet(light_theme)
            self.pb_theme.setText("Toggle Theme")
            self.current_theme = "light"
        else:
            self.setStyleSheet(dark_theme)
            self.pb_theme.setText("Toggle Theme")
            self.current_theme = "dark"

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())
