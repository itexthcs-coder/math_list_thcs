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


def bt_dang10_p4_b3_c1_ds9(self):
    def fmt_dec(val):
        if val == int(val):
            return str(int(val))
        return str(round(val, 2)).replace('.', '{,}')
    
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        x0 = random.choice([5, 10, 15])
        y0 = random.choice([i for i in [5, 10, 15, 20] if i != x0])
        tong_goc = x0 + y0
        tong_1 = round(1.1 * x0 + 1.08 * y0, 2)
        tong_2 = round(1.09 * tong_goc, 2)
    
        # Nội dung câu hỏi
        noidungcauhoi = ('''Một người mua hai loại hàng và phải trả tổng cộng là $%s\\text{ triệu đồng}$, kể cả thuế giá trị gia tăng (VAT) với mức $10\\%%$ đối với loại hàng thứ nhất và $8\\%%$ đối với loại hàng thứ hai. Nếu thuế VAT là $9\\%%$ đối với cả hai loại hàng thì người đó phải trả tổng cộng $%s\\text{ triệu đồng}$. Hỏi nếu không kể thuế VAT thì người đó phải trả bao nhiêu tiền cho mỗi loại hàng?'''
                         % (fmt_dec(tong_1), fmt_dec(tong_2)))
    
        # Nội dung lời giải
        loigiai = ('''\\begin{itemize}
                        \\item Gọi $x$ (triệu đồng) là số tiền phải trả cho loại hàng thứ nhất và $y$ (triệu đồng) là số tiền phải trả cho loại hàng thứ hai khi không kể thuế VAT. Điều kiện: $x > 0$ và $y > 0$.\\\\
                        Khi chịu thuế VAT $10\\%%$ cho loại hàng thứ nhất và $8\\%%$ cho loại hàng thứ hai, tổng số tiền phải trả là $%s\\text{ triệu đồng}$ nên ta có phương trình:
                        $$1{,}1x + 1{,}08y = %s. \\quad (1)$$
                        Nếu thuế VAT là $9\\%%$ đối với cả hai loại hàng thì tổng số tiền phải trả là $%s\\text{ triệu đồng}$ nên ta có phương trình:
                        $$1{,}09(x + y) = %s \\Leftrightarrow x + y = %s. \\quad (2)$$
                        Từ $(1)$ và $(2)$, ta có hệ phương trình:
                        $$\\begin{cases} 1{,}1x + 1{,}08y = %s \\\\ x + y = %s. \\end{cases}$$
                        \\item Giải hệ phương trình:\\\\
                        Từ $(2)$ rút $y = %s - x$ thế vào $(1)$, ta được:
                        $$1{,}1x + 1{,}08(%s - x) = %s \\Leftrightarrow 0{,}02x = %s \\Leftrightarrow x = %s.$$
                        Từ đó ta được $y = %s - %s = %s$.
                        \\item Các giá trị $x = %s$ và $y = %s$ thỏa mãn điều kiện của ẩn.\\\\
                        Vậy nếu không kể thuế VAT thì người đó phải trả $%s\\text{ triệu đồng}$ cho loại hàng thứ nhất và $%s\\text{ triệu đồng}$ cho loại hàng thứ hai.
                    \\end{itemize}'''
                   % (fmt_dec(tong_1), fmt_dec(tong_1),
                      fmt_dec(tong_2), fmt_dec(tong_2), tong_goc,
                      fmt_dec(tong_1), tong_goc,
                      tong_goc, tong_goc, fmt_dec(tong_1), fmt_dec(round(tong_1 - 1.08 * tong_goc, 2)), x0,
                      tong_goc, x0, y0,
                      x0, y0, x0, y0))
    
    # Xuất câu hỏi với đáp án và lời giải
    content = ('\\begin{minipage}{\\textwidth} \n' '\\begin{ex}\n'+ str(noidungcauhoi)+ '\\loigiai{ \n' +str(loigiai)+'}\n' '\\end{ex}\n \\end{minipage} \n\n')
    

    return content
