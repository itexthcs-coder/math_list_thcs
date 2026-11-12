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


def bt_dang13_p4_b3_c1_ds9(self):
    def fmt_dec(val):
        if val == int(val):
            return str(int(val))
        return str(round(val, 3)).replace('.', '{,}')
    
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        cases = [
            (500, 6, 7.5, 300, 200),
            (600, 5.5, 7, 400, 200),
            (800, 6, 8, 500, 300),
            (400, 5, 6.5, 200, 200)
        ]
        tong_von, r1, r2, x0, y0 = random.choice(cases)
        tong_lai = round(x0 * r1 / 100 + y0 * r2 / 100, 1)
    
        # Nội dung câu hỏi
        noidungcauhoi = ('''Bác Hùng chia số tiền $%s\\text{ triệu đồng}$ thành hai khoản để gửi tiết kiệm tại hai ngân hàng A và B với kì hạn $1\\text{ năm}$. Lãi suất tại ngân hàng A là $%s\\%%/\\text{năm}$, tại ngân hàng B là $%s\\%%/\\text{năm}$. Sau $1\\text{ năm}$, tổng số tiền lãi bác Hùng nhận được từ cả hai ngân hàng là $%s\\text{ triệu đồng}$. Hỏi bác Hùng đã gửi bao nhiêu tiền vào mỗi ngân hàng?'''
                         % (tong_von, fmt_dec(r1), fmt_dec(r2), fmt_dec(tong_lai)))
    
        # Nội dung lời giải
        loigiai = ('''\\begin{itemize}
                        \\item Gọi $x$ (triệu đồng) và $y$ (triệu đồng) lần lượt là số tiền bác Hùng gửi vào ngân hàng A và ngân hàng B. Điều kiện: $x > 0$ và $y > 0$.\\\\
                        Tổng số tiền gửi ở hai ngân hàng là $%s\\text{ triệu đồng}$ nên ta có phương trình:
                        $$x + y = %s. \\quad (1)$$
                        Sau $1\\text{ năm}$, tiền lãi nhận được từ ngân hàng A là $%sx$ (triệu đồng) và từ ngân hàng B là $%sy$ (triệu đồng). Tổng số tiền lãi là $%s\\text{ triệu đồng}$ nên ta có phương trình:
                        $$%sx + %sy = %s. \\quad (2)$$
                        Từ $(1)$ và $(2)$, ta có hệ phương trình:
                        $$\\begin{cases} x + y = %s \\\\ %sx + %sy = %s. \\end{cases}$$
                        \\item Giải hệ phương trình trên bằng phương pháp thế, ta tìm được $x = %s$ và $y = %s$.
                        \\item Các giá trị $x = %s$ và $y = %s$ thỏa mãn điều kiện của ẩn.\\\\
                        Vậy bác Hùng đã gửi $%s\\text{ triệu đồng}$ vào ngân hàng A và $%s\\text{ triệu đồng}$ vào ngân hàng B.
                    \\end{itemize}'''
                   % (tong_von, tong_von,
                      fmt_dec(r1/100), fmt_dec(r2/100), fmt_dec(tong_lai),
                      fmt_dec(r1/100), fmt_dec(r2/100), fmt_dec(tong_lai),
                      tong_von, fmt_dec(r1/100), fmt_dec(r2/100), fmt_dec(tong_lai),
                      x0, y0, x0, y0, x0, y0))
    
    # Xuất câu hỏi với đáp án và lời giải
    content = ('\\begin{minipage}{\\textwidth} \n' '\\begin{ex}\n'+ str(noidungcauhoi)+ '\\loigiai{ \n' +str(loigiai)+'}\n' '\\end{ex}\n \\end{minipage} \n\n')
    

    return content
