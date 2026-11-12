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


def bt_dang18_p4_b2_c2_ds9(self):
    # Dạng 18: Bài toán tính tiền nước sinh hoạt theo định mức bậc thang
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        g1, g2, g3 = 7000, 8500, 10500
        tien_20 = 10 * g1 + 10 * g2 # 155000
        vuot_20 = randint(6, 18)
        max_m3 = 20 + vuot_20
        ngan_sach = tien_20 + vuot_20 * g3
    
        def fmt_n(so):
            return f"{so:,}".replace(",", "\\,")
    
        # Nội dung câu hỏi
        noidungcauhoi = ('''Giá bán nước sạch sinh hoạt cho hộ gia đình tại một địa phương được quy định theo mức sử dụng trong tháng như sau:
                         \\begin{itemize}
                             \\item Mức 1: $10\\text{ m}^3$ đầu tiên giá $7\\,000\\text{ đồng/m}^3$.
                             \\item Mức 2: Từ trên $10\\text{ m}^3$ đến $20\\text{ m}^3$ giá $8\\,500\\text{ đồng/m}^3$.
                             \\item Mức 3: Trên $20\\text{ m}^3$ giá $10\\,500\\text{ đồng/m}^3$.
                         \\end{itemize}
                         Trong tháng 10, hóa đơn tiền nước của gia đình cô Mai (chưa tính thuế và phí bảo vệ môi trường) không vượt quá $%s$ đồng. Hỏi trong tháng 10, gia đình cô Mai đã sử dụng nhiều nhất bao nhiêu mét khối nước (biết lượng nước tiêu thụ là một số nguyên)?'''
                         % (fmt_n(ngan_sach)))
    
        # Nội dung lời giải
        loigiai = ('''Số tiền nước cho $20\\text{ m}^3$ đầu tiên (Mức 1 và Mức 2) là:
                   $$10 \\cdot 7\\,000 + 10 \\cdot 8\\,500 = 155\\,000 \\text{ (đồng)}.$$
                   Vì $%s > 155\\,000$ nên lượng nước sử dụng $x$ ($x \\in \\mathbb{N}^*$, tính theo $\\text{m}^3$) của gia đình cô Mai thuộc Mức 3 ($x > 20$). \\\\
                   Tổng số tiền nước phải trả là: $155\\,000 + 10\\,500(x - 20)$ (đồng). \\\\
                   Theo đề bài, ta có bất đẳng thức:
                   $$155\\,000 + 10\\,500(x - 20) \\le %s.$$
                   Cộng cả hai vế với $-155\\,000$ ta được:
                   $$10\\,500(x - 20) \\le %s.$$
                   Nhân cả hai vế với số dương $\\dfrac{1}{10\\,500} > 0$ ta được:
                   $$x - 20 \\le %d.$$
                   Cộng cả hai vế với $20$ ta được:
                   $$x \\le %d.$$
                   Vậy trong tháng 10, gia đình cô Mai đã sử dụng nhiều nhất $%d\\text{ m}^3$ nước.'''
                   % (fmt_n(ngan_sach), fmt_n(ngan_sach), fmt_n(ngan_sach - tien_20), vuot_20, max_m3, max_m3))
    
    # Xuất câu hỏi
    content = ('\\begin{minipage}{\\textwidth} \n' '\\begin{ex}\n' + str(noidungcauhoi) + '\\loigiai{ \n' + str(loigiai) + '}\n' '\\end{ex}\n \\end{minipage} \n\n')
    

    return content
