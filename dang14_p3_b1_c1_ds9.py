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


def bt_dang14_p3_b1_c1_ds9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        # Thời gian người thứ nhất làm một mình là t1, người thứ hai làm một mình là t2
        # Cả hai người cùng làm mất t ngày: 1/t = 1/t1 + 1/t2 => t = (t1 * t2) / (t1 + t2)
        # => 1/t2 = 1/t - 1/t1 = (t1 - t) / (t * t1) => t2 = (t * t1) / (t1 - t)
        
        # Chọn t và t1 sao cho t2 nguyên dương (t1 > t)
        # t1 = t + d, t2 = t * (t + d) / d = t + t^2 / d => d là ước của t^2
        t = randint(6, 18)
        uoc_cua_t2 = [d for d in range(1, t**2 + 1) if (t**2) % d == 0 and d > 1]
        d = random.choice(uoc_cua_t2)
        
        t1 = t + d
        t2 = t + (t**2) // d
        
        # Phân số phần công việc làm trong 1 ngày
        ps_chung = Rational(1, t)
        ps_nguoi1 = Rational(1, t1)
        ps_nguoi2 = ps_chung - ps_nguoi1  # = Rational(1, t2)
        
        # Kết quả cần tìm: thời gian người thứ hai làm một mình hoàn thành bức tường
        kq = t2
        kq_str = str(kq)
    
        # Nội dung câu hỏi
        noidungcauhoi = ('''Hai người thợ cùng xây một bức tường thì sau %s ngày sẽ xong. Nếu người thứ nhất làm một mình thì phải mất %s ngày mới xong. Hỏi nếu người thứ hai làm một mình thì sẽ mất bao nhiêu ngày để hoàn thành?'''
                         %(str(t),
                           str(t1)
                         ))
    
        # Nội dung lời giải
        loigiai = ('''Coi toàn bộ công việc xây bức tường là $1$ đơn vị. \\\\
    Trong $1$ ngày, cả hai người thợ cùng làm được số phần bức tường là: \\\\
    $1 : %s = %s$ (bức tường). \\\\
    Trong $1$ ngày, người thợ thứ nhất làm một mình được số phần bức tường là: \\\\
    $1 : %s = %s$ (bức tường). \\\\
    Trong $1$ ngày, người thợ thứ hai làm một mình được số phần bức tường là: \\\\
    $%s - %s = %s$ (bức tường). \\\\
    Nếu người thứ hai làm một mình thì hoàn thành bức tường trong số ngày là: \\\\
    $1 : %s = %s$ (ngày). \\\\
    Vậy người thứ hai làm một mình thì mất $%s$ ngày để hoàn thành.'''
                   %(str(t), latex(ps_chung),
                     str(t1), latex(ps_nguoi1),
                     latex(ps_chung), latex(ps_nguoi1), latex(ps_nguoi2),
                     latex(ps_nguoi2), str(kq_str),
                     str(kq_str)
                   ))
    
        # Đáp án
        dapan = '\\shortans[0]{$%s$}\n'%(str(kq_str))
    
    # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + str(dapan) +
               '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n' +
               '\\end{minipage} \n\n')
    return content
