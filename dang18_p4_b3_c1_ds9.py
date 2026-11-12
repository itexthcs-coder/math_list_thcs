import sys
from PyQt5.QtWidgets import QApplication, QColorDialog, QMainWindow, QSplitter, QTreeWidget, QSpacerItem, QSizePolicy, QTreeWidgetItem, QCheckBox, QFileDialog, QVBoxLayout, QTextEdit, QPushButton, QWidget, QLabel, QLineEdit, QDialog, QAction, QMessageBox, QScrollBar, QHeaderView, QMenu, QGridLayout
from sympy import *
from sympy.abc import x
import sympy as sp
from sympy import symbols,sqrt,evaluate,Subs,latex, Rational, expand, simplify, integrate
import random
import math
from sympy import Rational
from fractions import Fraction as frac
from random import randint
from PyQt5.QtGui import QTextCursor
from PyQt5.QtGui import QFont
import hashlib
import uuid
import os
from sympy import symbols, Eq, solve
import numpy as np
from PyQt5.QtGui import QIcon
from math import factorial
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QTextDocument
from subprocess import run, CalledProcessError
import shutil
from PyQt5.QtWidgets import QProgressBar
from docx import Document
from PyQt5 import QtGui
import re
import pandas as pd
from PyQt5.QtGui import QPixmap
import subprocess
import platform
import json
from decimal import Decimal, ROUND_HALF_UP
from PyQt5.QtWidgets import QComboBox, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QSpinBox, QTreeWidget, QTreeWidgetItem, QCheckBox, QTextEdit, QPushButton, QHBoxLayout
from random import randint, choice, shuffle
from sympy import latex
from fractions import Fraction
from collections import Counter
from random import sample
import shutil
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt
import qrcode
import json
import glob
import os
import platform
import subprocess
import hashlib
import base64
from datetime import datetime, timedelta
from PyQt5.QtWidgets import (QApplication, QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox)
from sympy import symbols, solve, Lt
#from PyQt5.QtWebEngineWidgets import QWebEngineView
#from PyQt5.QtCore import QUrl
#from sympy import latex
import re
import pyperclip
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

import google.generativeai as genai
from sympy.abc import x, y, z, t
import sys
import os
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QFileDialog, QMessageBox
)
from pdf2image import convert_from_path
from math import degrees
import openpyxl
from openpyxl import Workbook
from openpyxl.styles import Alignment, Font
from openpyxl.utils import get_column_letter
from sympy import simplify, collect
from itertools import combinations
import itertools
from PyQt5.QtCore import QSettings
import sys
import os
import platform
import subprocess
import hashlib
import time
from datetime import datetime, timedelta
# Bổ sung các widget và core cho Splash Screen
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QDialog, QLabel, QLineEdit, 
    QPushButton, QComboBox, QCheckBox, QTextEdit, QVBoxLayout, 
    QHBoxLayout, QGridLayout, QMessageBox, QColorDialog,
    QSplashScreen, QProgressBar  # <-- BỔ SUNG 2 CÁI NÀY
)
from PyQt5.QtCore import Qt, QSettings, QThread, pyqtSignal  # <-- BỔ SUNG QThread, pyqtSignal
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtGui import QFont, QBrush, QColor
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QSplitter, QTreeWidget, QTreeWidgetItem, QTextEdit, QLabel, 
    QSpacerItem, QSizePolicy, QStackedWidget, QPushButton, QCheckBox, QSpinBox,
    QScrollArea  # <-- Thêm mục này vào đây
)
from PyQt5.QtWidgets import QCheckBox
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt, QPropertyAnimation, pyqtProperty
from functools import wraps
import re
import uuid
import json, base64
from datetime import datetime
from nacl.signing import VerifyKey
from nacl.encoding import HexEncoder
from nacl.exceptions import BadSignatureError
### CÔNG CỤ
import sys
import numpy as np
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QDialog, 
    QVBoxLayout, QHBoxLayout, QTabWidget, QWidget, 
    QLabel, QSlider, QDoubleSpinBox, QGroupBox
)
from PyQt5.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from mpl_toolkits.mplot3d import Axes3D  # Cần cho 3D


def bt_dang18_p4_b3_c1_ds9(self):
    def fmt_dec(val):
        if val == int(val):
            return str(int(val))
        return str(round(val, 2)).replace('.', '{,}')
    
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        x0 = random.choice([6.4, 6.8, 7.2, 7.5])
        y0 = random.choice([9, 10, 11])
    
        m2_1 = random.randint(4, 6)
        m2_2 = random.randint(7, 10)
        v1 = 10 + m2_1
        v2 = 10 + m2_2
    
        tien1 = round(10 * x0 + m2_1 * y0, 1)
        tien2 = round(10 * x0 + m2_2 * y0, 1)
    
        # Nội dung câu hỏi
        noidungcauhoi = ('''Giá nước sạch sinh hoạt của một hộ gia đình được tính theo mức: $10\\text{ m}^3$ đầu tiên tính theo giá $x$ (nghìn đồng/$\\text{m}^3$), từ trên $10\\text{ m}^3$ đến $20\\text{ m}^3$ tính theo giá $y$ (nghìn đồng/$\\text{m}^3$). Tháng $9$ gia đình dùng hết $%s\\text{ m}^3$ và phải trả $%s\\text{ nghìn đồng}$. Tháng $10$ gia đình dùng hết $%s\\text{ m}^3$ và phải trả $%s\\text{ nghìn đồng}$. Tính giá tiền $1\\text{ m}^3$ nước ở mỗi mức.'''
                         % (v1, fmt_dec(tien1), v2, fmt_dec(tien2)))
    
        # Nội dung lời giải
        loigiai = ('''\\begin{itemize}
                        \\item Điều kiện: $y > x > 0$.\\\\
                        Tháng $9$ gia đình dùng $10\\text{ m}^3$ ở mức $1$ và $%s\\text{ m}^3$ ở mức $2$, phải trả $%s\\text{ nghìn đồng}$ nên ta có phương trình:
                        $$10x + %sy = %s. \\quad (1)$$
                        Tháng $10$ gia đình dùng $10\\text{ m}^3$ ở mức $1$ và $%s\\text{ m}^3$ ở mức $2$, phải trả $%s\\text{ nghìn đồng}$ nên ta có phương trình:
                        $$10x + %sy = %s. \\quad (2)$$
                        Từ $(1)$ và $(2)$, ta có hệ phương trình:
                        $$\\begin{cases} 10x + %sy = %s \\\\ 10x + %sy = %s. \\end{cases}$$
                        \\item Trừ từng vế $(2)$ cho $(1)$, ta được:
                        $$%sy = %s \\Leftrightarrow y = %s.$$
                        Thay $y = %s$ vào $(1)$, ta được $10x = %s \\Leftrightarrow x = %s$.
                        \\item Các giá trị $x = %s$ và $y = %s$ thỏa mãn điều kiện của ẩn.\\\\
                        Vậy giá tiền $1\\text{ m}^3$ nước ở mức $1$ là $%s\\text{ nghìn đồng}$ ($%s\\text{ đồng}$) và ở mức $2$ là $%s\\text{ nghìn đồng}$ ($%s\\text{ đồng}$).
                    \\end{itemize}'''
                   % (m2_1, fmt_dec(tien1), m2_1, fmt_dec(tien1),
                      m2_2, fmt_dec(tien2), m2_2, fmt_dec(tien2),
                      m2_1, fmt_dec(tien1), m2_2, fmt_dec(tien2),
                      m2_2 - m2_1, fmt_dec(round(tien2 - tien1, 1)), fmt_dec(y0),
                      fmt_dec(y0), fmt_dec(round(tien1 - m2_1 * y0, 1)), fmt_dec(x0),
                      fmt_dec(x0), fmt_dec(y0),
                      fmt_dec(x0), int(x0 * 1000), fmt_dec(y0), int(y0 * 1000)))
    
    # Xuất câu hỏi với đáp án và lời giải
    content = ('\\begin{minipage}{\\textwidth} \n' '\\begin{ex}\n'+ str(noidungcauhoi)+ '\\loigiai{ \n' +str(loigiai)+'}\n' '\\end{ex}\n \\end{minipage} \n\n')
    

    return content
