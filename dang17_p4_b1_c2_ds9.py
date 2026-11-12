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


def bt_dang17_p4_b1_c2_ds9(self):
    # Khai báo biến
    lisdang=['1']
    dang=random.choice(lisdang)
    if dang=='1':
        x = symbols('x')
        bo_so = random.choice([
            (15, 20, 100, 50, 1250, 35),
            (12, 15, 100, 50, 1000, 25),
            (20, 25, 120, 60, 1800, 45),
            (18, 20, 150, 50, 2000, 40)
        ])
        von_tr, so_dau, lai_dau, lo_sau, lai_tong, x_ans = bo_so
        von_nghin = von_tr * 1000
        thu_tong = von_nghin + lai_tong
    
        # Nội dung câu hỏi
        noidungcauhoi = ('''Một cửa hàng điện máy nhập về một lô máy sấy tóc đồng giá hết $%s$ triệu đồng. Cửa hàng bán ra $%s$ chiếc đầu tiên với giá mỗi chiếc cao hơn giá nhập $%s$ nghìn đồng. Số máy còn lại cửa hàng bán hạ giá thấp hơn giá nhập $%s$ nghìn đồng mỗi chiếc. Sau khi bán hết lô hàng, cửa hàng lãi được tổng cộng $%s$ nghìn đồng. Hỏi cửa hàng đã nhập về bao nhiêu chiếc máy sấy tóc?'''
                         %(latex(von_tr), latex(so_dau), latex(lai_dau), latex(lo_sau), latex(lai_tong)))
    
        # Nội dung lời giải
        loigiai = ('''Gọi $x$ (chiếc) là số máy sấy tóc cửa hàng đã nhập về ($x \\in \\mathbb{N}, x > %s$). \\\\
                   Đổi $%s$ triệu đồng $= %s$ nghìn đồng. Giá nhập mỗi chiếc máy là $\\dfrac{%s}{x}$ (nghìn đồng). \\\\
                   Giá bán mỗi chiếc trong $%s$ chiếc đầu là $\\left(\\dfrac{%s}{x} + %s\\right)$ nghìn đồng và giá bán mỗi chiếc trong $(x - %s)$ chiếc sau là $\\left(\\dfrac{%s}{x} - %s\\right)$ nghìn đồng. \\\\
                   Tổng số tiền thu về sau khi bán hết lô hàng là $%s + %s = %s$ (nghìn đồng), nên ta có phương trình: \\\\
                   $%s\\left(\\dfrac{%s}{x} + %s\\right) + (x - %s)\\left(\\dfrac{%s}{x} - %s\\right) = %s$. \\\\
                   Quy đồng mẫu hai vế với mẫu thức chung $x$ rồi khử mẫu, thu gọn phương trình tìm được $x = %s$ (thoả mãn). \\\\
                   Vậy cửa hàng đã nhập về $%s$ chiếc máy sấy tóc.'''
                   %(latex(so_dau),
                     latex(von_tr), latex(von_nghin), latex(von_nghin),
                     latex(so_dau), latex(von_nghin), latex(lai_dau), latex(so_dau), latex(von_nghin), latex(lo_sau),
                     latex(von_nghin), latex(lai_tong), latex(thu_tong),
                     latex(so_dau), latex(von_nghin), latex(lai_dau), latex(so_dau), latex(von_nghin), latex(lo_sau), latex(thu_tong),
                     latex(x_ans),
                     latex(x_ans)))
    
    content = ('\\begin{minipage}{\\textwidth} \n' '\\begin{ex}\n'+ str(noidungcauhoi)+ '\\loigiai{ \n' +str(loigiai)+'}\n' '\\end{ex}\n \\end{minipage} \n\n')

    return content
