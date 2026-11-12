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


def bt_dang5_p4_b3_c1_ds9(self):
    def fmt_dec(val):
        return str(round(val, 2)).replace('.', '{,}')
    
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        n10 = random.randint(20, 30)
        n9 = random.randint(35, 45)
        n7 = random.randint(10, 18)
        x0 = random.randint(8, 16)
        y0 = 100 - (n10 + n9 + n7 + x0)
    
        tong_diem = 10*n10 + 9*n9 + 8*x0 + 7*n7 + 6*y0
        diem_tb = tong_diem / 100
        tong_xy = x0 + y0
    
        bang_latex = ('''\\begin{center}
    \\begin{tabular}{|l|c|c|c|c|c|}
    \\hline
    Điểm số của mỗi lần bắn & $10$ & $9$ & $8$ & $7$ & $6$ \\\\
    \\hline
    Số lần bắn & $%s$ & $%s$ & $*$ & $%s$ & $*$ \\\\
    \\hline
    \\end{tabular}
    \\end{center}''' % (n10, n9, n7))
    
        # Nội dung câu hỏi
        noidungcauhoi = ('''Điểm số trung bình của một vận động viên bắn súng sau $100\\text{ lần}$ bắn là $%s\\text{ điểm}$. Kết quả cụ thể được ghi trong bảng sau, trong đó có hai ô bị mờ không đọc được (đánh dấu $*$): %s Em hãy tìm lại các số bị mờ trong hai ô đó.'''
                         % (fmt_dec(diem_tb), bang_latex))
    
        # Nội dung lời giải
        loigiai = ('''\\begin{itemize}
                        \\item Gọi số lần bắn đạt điểm $8$ là $x$ và số lần bắn đạt điểm $6$ là $y$. Điều kiện: $x, y \\in \\mathbb{N}$.\\\\
                        Vì tổng số lần bắn là $100$ nên ta có phương trình:
                        $$%s + %s + x + %s + y = 100 \\Leftrightarrow x + y = %s. \\quad (1)$$
                        Điểm số trung bình sau $100$ lần bắn là $%s$ nên ta có phương trình:
                        $$\\dfrac{10\\cdot %s + 9\\cdot %s + 8x + 7\\cdot %s + 6y}{100} = %s \\Leftrightarrow %s + 8x + 6y = %s \\Leftrightarrow 8x + 6y = %s. \\quad (2)$$
                        Từ $(1)$ và $(2)$, ta có hệ phương trình:
                        $$\\begin{cases} x + y = %s \\\\ 8x + 6y = %s. \\end{cases}$$
                        \\item Giải hệ phương trình:\\\\
                        Nhân hai vế của $(1)$ với $6$ rồi trừ từng vế của $(2)$ cho phương trình mới nhận được, ta có:
                        $$2x = %s - %s = %s \\Leftrightarrow x = %s.$$
                        Thay $x = %s$ vào $(1)$, ta được $y = %s - %s = %s$.
                        \\item Các giá trị $x = %s$ và $y = %s$ thỏa mãn điều kiện của ẩn.\\\\
                        Vậy số lần bắn đạt điểm $8$ là $%s$ lần và số lần bắn đạt điểm $6$ là $%s$ lần.
                    \\end{itemize}'''
                   % (n10, n9, n7, tong_xy,
                      fmt_dec(diem_tb), n10, n9, n7, fmt_dec(diem_tb),
                      10*n10 + 9*n9 + 7*n7, tong_diem, 8*x0 + 6*y0,
                      tong_xy, 8*x0 + 6*y0,
                      8*x0 + 6*y0, 6*tong_xy, 2*x0, x0,
                      x0, tong_xy, x0, y0,
                      x0, y0, x0, y0))
    
    # Xuất câu hỏi với đáp án và lời giải
    content = ('\\begin{minipage}{\\textwidth} \n' '\\begin{ex}\n'+ str(noidungcauhoi)+ '\\loigiai{ \n' +str(loigiai)+'}\n' '\\end{ex}\n \\end{minipage} \n\n')
    

    return content
