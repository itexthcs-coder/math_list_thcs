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


def bt_dang14_p4_b1_c2_ds9(self):
    # Khai báo biến
    lisdang=['1']
    dang=random.choice(lisdang)
    if dang=='1':
        x = symbols('x')
        bo_so = random.choice([
            (80, 72, 4, 15, Rational(1, 4), 36),
            (60, 48, 3, 12, Rational(1, 5), 27),
            (96, 80, 4, 20, Rational(1, 3), 28),
            (50, 44, 3, 15, Rational(1, 4), 25)
        ])
        s_xuoi, s_nguoc, v_nuoc, phut_it, gio_it, v_cano = bo_so
    
        # Nội dung câu hỏi
        noidungcauhoi = ('''Một ca nô xuôi dòng trên một khúc sông từ bến $A$ đến bến $B$ dài $%s\\text{ km}$, sau đó lại ngược dòng đến địa điểm $C$ cách bến $B$ một khoảng $%s\\text{ km}$. Thời gian ca nô xuôi dòng ít hơn thời gian ngược dòng là $%s\\text{ phút}$. Tính vận tốc riêng của ca nô, biết vận tốc của dòng nước là $%s\\text{ km/h}$.'''
                         %(latex(s_xuoi), latex(s_nguoc), latex(phut_it), latex(v_nuoc)))
    
        # Nội dung lời giải
        loigiai = ('''Đổi $%s\\text{ phút} = %s\\text{ giờ}$. Gọi $x\\text{ (km/h)}$ là vận tốc riêng của ca nô ($x > %s$). \\\\
                   Vận tốc của ca nô khi xuôi dòng là $(x + %s)\\text{ km/h}$ và khi ngược dòng là $(x - %s)\\text{ km/h}$. \\\\
                   Thời gian ca nô đi xuôi dòng là $\\dfrac{%s}{x + %s}$ (giờ) và thời gian đi ngược dòng là $\\dfrac{%s}{x - %s}$ (giờ). \\\\
                   Vì thời gian xuôi dòng ít hơn thời gian ngược dòng là $%s\\text{ giờ}$ nên ta có phương trình: \\\\
                   $\\dfrac{%s}{x - %s} - \\dfrac{%s}{x + %s} = %s$. \\\\
                   Quy đồng mẫu hai vế với mẫu thức chung $%s(x - %s)(x + %s)$ rồi khử mẫu, đưa về phương trình tích tìm được nghiệm dương $x = %s$ (thoả mãn $x > %s$). \\\\
                   Vậy vận tốc riêng của ca nô là $%s\\text{ km/h}$.'''
                   %(latex(phut_it), latex(gio_it), latex(v_nuoc),
                     latex(v_nuoc), latex(v_nuoc),
                     latex(s_xuoi), latex(v_nuoc), latex(s_nguoc), latex(v_nuoc),
                     latex(gio_it),
                     latex(s_nguoc), latex(v_nuoc), latex(s_xuoi), latex(v_nuoc), latex(gio_it),
                     latex(gio_it.q), latex(v_nuoc), latex(v_nuoc), latex(v_cano), latex(v_nuoc),
                     latex(v_cano)))
    
    content = ('\\begin{minipage}{\\textwidth} \n' '\\begin{ex}\n'+ str(noidungcauhoi)+ '\\loigiai{ \n' +str(loigiai)+'}\n' '\\end{ex}\n \\end{minipage} \n\n')

    return content
