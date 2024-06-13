# Dark and light theme stylesheets
dark_theme = """
/* General styling */
* {
    font-family: "Iosevka", "Monospace";
    color: #D0D0D0; /* Light gray text */
    background-color: #1E1E1E; /* Dark background */
}

/* QPushButton */
QPushButton {
    background-color: #2D2D2D; /* Slightly lighter than background */
    border: 1px solid #555555;
    padding: 5px;
    border-radius: 3px;
}

QPushButton:hover {
    background-color: #3D3D3D;
    border: 1px solid #777777;
}

QPushButton:pressed {
    background-color: #5D5D5D;
    border: 1px solid #AAAAAA;
}

/* QLabel */
QLabel {
    color: #D0D0D0;
    background-color: transparent; /* To keep the background consistent */
}

/* QLineEdit */
QLineEdit {
    background-color: #2D2D2D;
    border: 1px solid #555555;
    padding: 5px;
    color: #D0D0D0;
}

QLineEdit:focus {
    border: 1px solid #777777;
}

/* QComboBox */
QComboBox {
    background-color: #2D2D2D;
    border: 1px solid #555555;
    padding: 5px;
    color: #D0D0D0;
}

QComboBox:hover {
    border: 1px solid #777777;
}

/* QComboBox drop-down */
QComboBox QAbstractItemView {
    background-color: #1E1E1E;
    border: 1px solid #555555;
    color: #D0D0D0;
}

/* QMenuBar */
QMenuBar {
    background-color: #1E1E1E;
    color: #D0D0D0;
}

QMenuBar::item {
    background-color: #1E1E1E;
    color: #D0D0D0;
}

QMenuBar::item:selected {
    background-color: #3D3D3D;
    color: #FFFFFF;
}

/* QMenu */
QMenu {
    background-color: #2D2D2D;
    border: 1px solid #555555;
    color: #D0D0D0;
}

QMenu::item {
    background-color: #2D2D2D;
    padding: 5px 25px;
}

QMenu::item:selected {
    background-color: #3D3D3D;
}

/* QTabWidget */
QTabWidget::pane {
    border: 1px solid #555555;
}

QTabBar::tab {
    background-color: #2D2D2D;
    border: 1px solid #555555;
    padding: 5px;
}

QTabBar::tab:selected {
    background-color: #3D3D3D;
    border: 1px solid #777777;
}

/* QScrollBar */
QScrollBar:vertical {
    background-color: #2D2D2D;
    width: 15px;
    margin: 15px 3px 15px 3px;
    border: 1px solid #555555;
}

QScrollBar::handle:vertical {
    background-color: #555555;
    min-height: 20px;
}

QScrollBar::add-line:vertical,
QScrollBar::sub-line:vertical {
    background-color: #2D2D2D;
    border: 1px solid #555555;
    height: 15px;
}

QScrollBar::add-page:vertical,
QScrollBar::sub-page:vertical {
    background-color: #2D2D2D;
}

"""

light_theme = """
/* Paste the light theme QSS here */
/* General styling */
* {
    font-family: "Iosevka", "Monospace";
    color: #1E1E1E; /* Dark text */
    background-color: #F0F0F0; /* Light background */
}

/* QPushButton */
QPushButton {
    background-color: #E0E0E0; /* Slightly darker than background */
    border: 1px solid #CCCCCC;
    padding: 5px;
    border-radius: 3px;
}

QPushButton:hover {
    background-color: #D0D0D0;
    border: 1px solid #BBBBBB;
}

QPushButton:pressed {
    background-color: #B0B0B0;
    border: 1px solid #999999;
}

/* QLabel */
QLabel {
    color: #1E1E1E;
    background-color: transparent; /* To keep the background consistent */
}

/* QLineEdit */
QLineEdit {
    background-color: #E0E0E0;
    border: 1px solid #CCCCCC;
    padding: 5px;
    color: #1E1E1E;
}

QLineEdit:focus {
    border: 1px solid #BBBBBB;
}

/* QComboBox */
QComboBox {
    background-color: #E0E0E0;
    border: 1px solid #CCCCCC;
    padding: 5px;
    color: #1E1E1E;
}

QComboBox:hover {
    border: 1px solid #BBBBBB;
}

/* QComboBox drop-down */
QComboBox QAbstractItemView {
    background-color: #F0F0F0;
    border: 1px solid #CCCCCC;
    color: #1E1E1E;
}

/* QMenuBar */
QMenuBar {
    background-color: #F0F0F0;
    color: #1E1E1E;
}

QMenuBar::item {
    background-color: #F0F0F0;
    color: #1E1E1E;
}

QMenuBar::item:selected {
    background-color: #D0D0D0;
    color: #000000;
}

/* QMenu */
QMenu {
    background-color: #E0E0E0;
    border: 1px solid #CCCCCC;
    color: #1E1E1E;
}

QMenu::item {
    background-color: #E0E0E0;
    padding: 5px 25px;
}

QMenu::item:selected {
    background-color: #D0D0D0;
}

/* QTabWidget */
QTabWidget::pane {
    border: 1px solid #CCCCCC;
}

QTabBar::tab {
    background-color: #E0E0E0;
    border: 1px solid #CCCCCC;
    padding: 5px;
}

QTabBar::tab:selected {
    background-color: #D0D0D0;
    border: 1px solid #BBBBBB;
}

/* QScrollBar */
QScrollBar:vertical {
    background-color: #E0E0E0;
    width: 15px;
    margin: 15px 3px 15px 3px;
    border: 1px solid #CCCCCC;
}

QScrollBar::handle:vertical {
    background-color: #CCCCCC;
    min-height: 20px;
}

QScrollBar::add-line:vertical,
QScrollBar::sub-line:vertical {
    background-color: #E0E0E0;
    border: 1px solid #CCCCCC;
    height: 15px;
}

QScrollBar::add-page:vertical,
QScrollBar::sub-page:vertical {
    background-color: #E0E0E0;
}

"""
