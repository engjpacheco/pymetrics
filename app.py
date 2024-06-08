import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QComboBox, QVBoxLayout, 
    QLineEdit, QTextEdit, QPushButton, QDateEdit, QGridLayout)
from PyQt5.QtCore import QDate
import csv
import os
from variables import *

class MaintenanceForm(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Summit Planta Leon - Maintenance Form")
        self.setGeometry(100, 100, 400, 400)

        layout = QGridLayout()

        # Machine type combo box
        self.machine_type_label = QLabel("Select Machine Type:")
        self.machine_type_combo = QComboBox()
        self.machine_type_combo.addItems([str(equipment) for equipment in EQUIPMENT])
        self.machine_type_combo.currentIndexChanged.connect(self.update_machine_id_combo)
        layout.addWidget(self.machine_type_label, 0, 0)
        layout.addWidget(self.machine_type_combo, 0, 1)

        # Machine ID combo box
        self.machine_id_label = QLabel("Select Machine ID:")
        self.machine_id_combo = QComboBox()
        self.update_machine_id_combo()
        layout.addWidget(self.machine_id_label, 1, 0)
        layout.addWidget(self.machine_id_combo, 1, 1)

        # Technician combo box
        self.technician_label = QLabel("Select Technician:")
        self.technician_combo = QComboBox()
        self.technician_combo.addItems([str(tec) for tec in TECS])
        layout.addWidget(self.technician_label, 2, 0)
        layout.addWidget(self.technician_combo, 2, 1)

        # Date field
        self.date_label = QLabel("Date:")
        self.date_edit = QDateEdit()
        self.date_edit.setCalendarPopup(True)
        self.date_edit.setDate(QDate.currentDate())
        layout.addWidget(self.date_label, 3, 0)
        layout.addWidget(self.date_edit, 3, 1)

        # Work order number
        self.work_order_label = QLabel("Work Order Number:")
        self.work_order_edit = QLineEdit()
        layout.addWidget(self.work_order_label, 4, 0)
        layout.addWidget(self.work_order_edit, 4, 1)

        # Technician notes
        self.notes_label = QLabel("Technician Notes:")
        self.notes_edit = QTextEdit()
        layout.addWidget(self.notes_label, 5, 0)
        layout.addWidget(self.notes_edit, 5, 1)

        # Time spent field
        self.time_spent_label = QLabel("Time Spent (minutes):")
        self.time_spent_edit = QLineEdit()
        layout.addWidget(self.time_spent_label, 6, 0)
        layout.addWidget(self.time_spent_edit, 6, 1)

        # Downtime field
        self.downtime_label = QLabel("Downtime (minutes):")
        self.downtime_edit = QLineEdit()
        layout.addWidget(self.downtime_label, 7, 0)
        layout.addWidget(self.downtime_edit, 7, 1)

        # Buttons
        self.submit_button = QPushButton("Submit")
        self.submit_button.clicked.connect(self.submit)
        layout.addWidget(self.submit_button, 8, 0)

        self.clear_button = QPushButton("Clear")
        self.clear_button.clicked.connect(self.clear_fields)
        layout.addWidget(self.clear_button, 8, 1)

        self.close_button = QPushButton("Close")
        self.close_button.clicked.connect(self.close_application)
        layout.addWidget(self.close_button, 9, 0, 1, 2)

        self.setLayout(layout)

    def update_machine_id_combo(self):
        machine_type = self.machine_type_combo.currentText()
        self.machine_id_combo.clear()

        if machine_type == "IMM":
            self.machine_id_combo.addItems([str(imm + 100) for imm in range(1, moldeo + 1)])
        elif machine_type == "ROBOT":
            self.machine_id_combo.addItems([str(robot + 200) for robot in range(1, moldeo + 1)])
        elif machine_type == "THERMO":
            self.machine_id_combo.addItems([str(thermo + 300) for thermo in range(1, moldeo + 1)])
        elif machine_type == "MAGUIRE":
            self.machine_id_combo.addItems([str(maguire + 400) for maguire in range(1, moldeo + 1)])
        elif machine_type == "SOFT-TRIM":
            self.machine_id_combo.addItems([str(softtrim + 500) for softtrim in range(1, softrim + 1)])
        elif machine_type == "BOOTH":
            self.machine_id_combo.addItems([str(booth + 600) for booth in range(1, booth + 1)])
        elif machine_type == "VINIL":
            self.machine_id_combo.addItems([str(vinil + 700) for vinil in range(1, vinil + 1)])
        elif machine_type == "T1XX":
            self.machine_id_combo.addItems([str(t1xx + 800) for t1xx in range(1, t1xx + 1)])
        elif machine_type == "CX483":
            self.machine_id_combo.addItems([str(fixture + 900) for fixture in range(1, cx483 + 1)])
        elif machine_type == "U725":
            self.machine_id_combo.addItems([str(fixture + 1000) for fixture in range(1, u725 + 1)])
        elif machine_type == "KXX/KM":
            self.machine_id_combo.addItems([str(fixture + 1100) for fixture in range(1, kxx + 1)])
        elif machine_type == "BT1CG/PERFCAR/P708":
            self.machine_id_combo.addItems([str(fixture + 1200) for fixture in range(1, bt1cg + 1)])
        elif machine_type == "GAP HIDDER":
            self.machine_id_combo.addItems([str(fixture + 1300) for fixture in range(1, gap_hidder + 1)])
        elif machine_type == "OTROS":
            self.machine_id_combo.addItems([str(fixture + 1400) for fixture in range(1, otros + 1)])

    def submit(self):
        machine_type = self.machine_type_combo.currentText()
        machine_id = self.machine_id_combo.currentText()
        technician = self.technician_combo.currentText()
        date = self.date_edit.date().toString("yyyy-MM-dd")
        work_order = self.work_order_edit.text()
        notes = self.notes_edit.toPlainText()
        time_spent = self.time_spent_edit.text()
        downtime = self.downtime_edit.text()

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
        self.work_order_edit.clear()
        self.notes_edit.clear()
        self.time_spent_edit.clear()
        self.downtime_edit.clear()
        self.machine_type_combo.setCurrentIndex(0)
        self.technician_combo.setCurrentIndex(0)
        self.date_edit.setDate(QDate.currentDate())
        self.update_machine_id_combo()

    def close_application(self):
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = MaintenanceForm()
    form.show()
    sys.exit(app.exec_())
