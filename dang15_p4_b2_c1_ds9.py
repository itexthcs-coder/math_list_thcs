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


def bt_dang15_p4_b2_c1_ds9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        bo_so = random.choice([
            (60, 15, 12, 4, 14),   # 1/60 + 1/15 = 1/12; 4/60 + 14/15 = 1
            (30, 15, 10, 6, 12),   # 1/30 + 1/15 = 1/10; 6/30 + 12/15 = 1
            (24, 12, 8, 6, 9)      # 1/24 + 1/12 = 1/8; 6/24 + 9/12 = 1
        ])
        T1, T2, T_chung, t1_rieng, t2_rieng = bo_so
    
        # Nội dung câu hỏi
        noidungcauhoi = ('''Hai đội công nhân cùng làm một công trình trong $%s\\text{ ngày}$ thì hoàn thành. Nếu đội I làm một mình trong $%s\\text{ ngày}$ rồi nghỉ, sau đó đội II làm tiếp một mình trong $%s\\text{ ngày}$ thì mới hoàn thành xong công trình. Hỏi nếu làm một mình thì mỗi đội phải mất bao nhiêu ngày để hoàn thành công trình đó?'''
                         % (latex(T_chung), latex(t1_rieng), latex(t2_rieng)))
    
        # Nội dung lời giải
        loigiai = ('''Gọi $x$ (công trình/ngày) và $y$ (công trình/ngày) lần lượt là phần công trình đội I và đội II làm được trong $1\\text{ ngày}$ ($x, y > 0$). \\\\
                   Vì hai đội làm chung trong $%s\\text{ ngày}$ thì hoàn thành toàn bộ công trình nên trong $1\\text{ ngày}$ cả hai đội làm được $%s$ công trình, ta có phương trình: $x + y = %s$. \\\\
                   Đội I làm trong $%s\\text{ ngày}$ và đội II làm tiếp trong $%s\\text{ ngày}$ thì xong công trình nên ta có phương trình: $%sx + %sy = 1$. \\\\
                   Ta có hệ phương trình $\\begin{cases} x + y = %s \\\\ %sx + %sy = 1 \\end{cases}$. \\\\
                   Giải hệ phương trình trên, ta tìm được $x = %s$ và $y = %s$ (thỏa mãn điều kiện). \\\\
                   Vậy nếu làm một mình thì đội I hoàn thành công trình trong $1 : %s = %s\\text{ (ngày)}$ và đội II hoàn thành công trình trong $1 : %s = %s\\text{ (ngày)}$.'''
                   % (latex(T_chung), latex(Rational(1, T_chung)), latex(Rational(1, T_chung)),
                      latex(t1_rieng), latex(t2_rieng), latex(t1_rieng), latex(t2_rieng),
                      latex(Rational(1, T_chung)), latex(t1_rieng), latex(t2_rieng),
                      latex(Rational(1, T1)), latex(Rational(1, T2)),
                      latex(Rational(1, T1)), latex(T1),
                      latex(Rational(1, T2)), latex(T2)))
    
    # Xuất câu hỏi
    content = ('\\begin{minipage}{\\textwidth} \n' '\\begin{ex}\n' + str(noidungcauhoi) + '\\loigiai{ \n' + str(loigiai) + '}\n' '\\end{ex}\n \\end{minipage} \n\n')

    return content
