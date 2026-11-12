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


def bt_dang16_p4_b2_c1_ds9(self):
    # Khai báo biến
    def fmt_tp(val):
        return str(val).replace('.', ',')
    
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        x0 = random.choice([300, 400, 500])
        y0 = random.choice([400, 500, 600])
        while x0 == y0:
            y0 = random.choice([400, 500, 600])
    
        p1 = 15
        p2 = 20
        tong_t1 = x0 + y0
        tong_t2 = (x0 * (100 + p1) + y0 * (100 + p2)) // 100
    
        hs1_tp = fmt_tp((100 + p1) / 100)
        hs2_tp = fmt_tp((100 + p2) / 100)
    
        # Nội dung câu hỏi
        noidungcauhoi = ('''Trong tháng Giêng, hai tổ sản xuất của một nhà máy làm được tổng cộng $%s\\text{ sản phẩm}$. Sang tháng Hai, do cải tiến kĩ thuật nên tổ I vượt mức $%s\\%%$ và tổ II vượt mức $%s\\%%$ so với tháng Giêng, vì vậy cả hai tổ đã sản xuất được $%s\\text{ sản phẩm}$. Hỏi trong tháng Giêng, mỗi tổ sản xuất được bao nhiêu sản phẩm?'''
                         % (latex(tong_t1), latex(p1), latex(p2), latex(tong_t2)))
    
        # Nội dung lời giải
        loigiai = ('''Gọi $x$ (sản phẩm) và $y$ (sản phẩm) lần lượt là số sản phẩm tổ I và tổ II sản xuất được trong tháng Giêng ($x, y \\in \\mathbb{N}^*$). \\\\
                   Trong tháng Giêng hai tổ làm được $%s$ sản phẩm nên ta có phương trình: $x + y = %s$. \\\\
                   Sang tháng Hai, tổ I vượt mức $%s\\%%$ nên làm được $%sx$ (sản phẩm), tổ II vượt mức $%s\\%%$ nên làm được $%sy$ (sản phẩm), nên ta có phương trình: $%sx + %sy = %s$. \\\\
                   Ta có hệ phương trình $\\begin{cases} x + y = %s \\\\ %sx + %sy = %s \\end{cases}$. \\\\
                   Giải hệ phương trình trên, ta tìm được $x = %s$ và $y = %s$ (thỏa mãn điều kiện). \\\\
                   Vậy trong tháng Giêng, tổ I sản xuất được $%s\\text{ sản phẩm}$ và tổ II sản xuất được $%s\\text{ sản phẩm}$.'''
                   % (latex(tong_t1), latex(tong_t1),
                      latex(p1), hs1_tp, latex(p2), hs2_tp, hs1_tp, hs2_tp, latex(tong_t2),
                      latex(tong_t1), hs1_tp, hs2_tp, latex(tong_t2),
                      latex(x0), latex(y0),
                      latex(x0), latex(y0)))
    
    # Xuất câu hỏi
    content = ('\\begin{minipage}{\\textwidth} \n' '\\begin{ex}\n' + str(noidungcauhoi) + '\\loigiai{ \n' + str(loigiai) + '}\n' '\\end{ex}\n \\end{minipage} \n\n')

    return content
