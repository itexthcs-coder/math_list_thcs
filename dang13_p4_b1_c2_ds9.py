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


def bt_dang13_p4_b1_c2_ds9(self):
    # Khai báo biến
    lisdang=['1']
    dang=random.choice(lisdang)
    if dang=='1':
        x = symbols('x')
        bo_so = random.choice([
            (12, 8, 4, 48, Rational(24, 5), 3, 4, Rational(3, 4)),
            (15, 10, 6, 0, 6, 4, 5, Rational(23, 30)),
            (10, 15, 6, 0, 6, 3, 6, Rational(7, 10)),
            (12, 24, 8, 0, 8, 4, 8, Rational(2, 3))
        ])
        t1, t2, gio_chung, phut_chung, t_chung_phan, t_v1, t_v2, phan_be = bo_so
        tg_chung_text = f"{gio_chung}\\text{{ giờ }} {phut_chung}\\text{{ phút}}" if phut_chung > 0 else f"{gio_chung}\\text{{ giờ}}"
    
        # Nội dung câu hỏi
        noidungcauhoi = ('''Hai vòi nước cùng chảy vào một bể không có nước thì sau $%s$ đầy bể. Nếu mở vòi thứ nhất chảy trong $%s\\text{ giờ}$ rồi khoá lại, sau đó mở tiếp vòi thứ hai chảy trong $%s\\text{ giờ}$ thì được $%s$ bể. Hỏi nếu chảy một mình thì mỗi vòi chảy đầy bể trong bao lâu?'''
                         %(tg_chung_text, latex(t_v1), latex(t_v2), latex(phan_be)))
    
        # Nội dung lời giải
        loigiai = ('''Đổi $%s = %s\\text{ giờ}$. Gọi $x$ (giờ) là thời gian vòi thứ nhất chảy một mình đầy bể ($x > %s$). \\\\
                   Trong $1\\text{ giờ}$, vòi thứ nhất chảy được $\\dfrac{1}{x}$ bể, cả hai vòi cùng chảy được $\\dfrac{1}{%s} = %s$ bể, nên vòi thứ hai chảy một mình được $\\left(%s - \\dfrac{1}{x}\\right)$ bể. \\\\
                   Vì mở vòi thứ nhất chảy trong $%s\\text{ giờ}$ rồi mở tiếp vòi thứ hai chảy trong $%s\\text{ giờ}$ thì được $%s$ bể nên ta có phương trình: \\\\
                   $\\dfrac{%s}{x} + %s\\left(%s - \\dfrac{1}{x}\\right) = %s$. \\\\
                   Quy đồng mẫu hai vế và khử mẫu, giải phương trình tìm được $x = %s$ (thoả mãn). \\\\
                   Trong $1\\text{ giờ}$, vòi thứ hai chảy được $%s - \\dfrac{1}{%s} = \\dfrac{1}{%s}$ bể, suy ra thời gian vòi thứ hai chảy một mình đầy bể là $%s\\text{ giờ}$. \\\\
                   Vậy nếu chảy một mình, vòi thứ nhất chảy đầy bể trong $%s\\text{ giờ}$ và vòi thứ hai chảy đầy bể trong $%s\\text{ giờ}$.'''
                   %(tg_chung_text, latex(t_chung_phan), latex(t_chung_phan),
                     latex(t_chung_phan), latex(Rational(1, t_chung_phan)), latex(Rational(1, t_chung_phan)),
                     latex(t_v1), latex(t_v2), latex(phan_be),
                     latex(t_v1), latex(t_v2), latex(Rational(1, t_chung_phan)), latex(phan_be),
                     latex(t1),
                     latex(Rational(1, t_chung_phan)), latex(t1), latex(t2), latex(t2),
                     latex(t1), latex(t2)))
    
    content = ('\\begin{minipage}{\\textwidth} \n' '\\begin{ex}\n'+ str(noidungcauhoi)+ '\\loigiai{ \n' +str(loigiai)+'}\n' '\\end{ex}\n \\end{minipage} \n\n')

    return content
