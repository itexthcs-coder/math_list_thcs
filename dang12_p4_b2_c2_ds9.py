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


def bt_dang12_p4_b2_c2_ds9(self):
    # Dạng 12: Bài toán tính điểm thi tuyển sinh vào lớp 10 THPT
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        diem_chuan = random.choice([37.5, 38.0, 38.5, 39.0, 40.0])
        van = random.choice([7.25, 7.5, 7.75, 8.0])
        anh = random.choice([8.0, 8.25, 8.5, 8.75])
        tong_2_mon = round(2 * van + anh, 2)
        con_thieu = round(diem_chuan - tong_2_mon, 2)
        toan_min = round(con_thieu / 2, 3)
    
        def fmt(val):
            s = f"{val:g}"
            return s.replace('.', ',')
    
        # Nội dung câu hỏi
        noidungcauhoi = ('''Trong kì thi tuyển sinh vào lớp 10 THPT, điểm xét tuyển là tổng điểm của 3 môn: Toán (hệ số 2), Ngữ văn (hệ số 2) và Tiếng Anh (hệ số 1). Năm trước, điểm chuẩn trúng tuyển vào trường THPT A là $%s$ điểm. Bạn Nam đã thi xong hai môn Ngữ văn và Tiếng Anh với số điểm lần lượt là $%s$ điểm và $%s$ điểm. Hỏi ở môn Toán, bạn Nam cần đạt ít nhất bao nhiêu điểm để có tổng điểm xét tuyển không thấp hơn điểm chuẩn năm trước?'''
                         % (fmt(diem_chuan), fmt(van), fmt(anh)))
    
        # Nội dung lời giải
        loigiai = ('''Gọi $x$ ($0 \\le x \\le 10$) là điểm môn Toán của bạn Nam. \\\\
                   Tổng điểm xét tuyển của bạn Nam là: $2x + 2 \\cdot %s + %s = 2x + %s$. \\\\
                   Để tổng điểm xét tuyển không thấp hơn $%s$ điểm, ta có bất đẳng thức:
                   $$2x + %s \\ge %s.$$
                   Cộng cả hai vế với $-%s$ ta được:
                   $$2x \\ge %s.$$
                   Nhân cả hai vế với số dương $\\dfrac{1}{2} > 0$ ta được:
                   $$x \\ge %s.$$
                   Vậy bạn Nam cần đạt ít nhất $%s$ điểm môn Toán để có tổng điểm xét tuyển không thấp hơn điểm chuẩn năm trước.'''
                   % (fmt(van), fmt(anh), fmt(tong_2_mon), fmt(diem_chuan),
                      fmt(tong_2_mon), fmt(diem_chuan), fmt(tong_2_mon), fmt(con_thieu), fmt(toan_min), fmt(toan_min)))
    
    # Xuất câu hỏi
    content = ('\\begin{minipage}{\\textwidth} \n' '\\begin{ex}\n' + str(noidungcauhoi) + '\\loigiai{ \n' + str(loigiai) + '}\n' '\\end{ex}\n \\end{minipage} \n\n')
    


    return content
