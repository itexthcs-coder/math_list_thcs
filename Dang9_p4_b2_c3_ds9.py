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


def bt_Dang9_p4_b2_c3_ds9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        m = randint(2, 4)
        n = random.choice([5, 6, 7])
        u = random.choice([5, 7, 10])
        v = random.choice([2, 3])
        val_M = (m**2 - n) - (u - v)

        hieu_uv = u - v
        hieu_mn = m**2 - n

        # Nội dung câu hỏi
        noidungcauhoi = ('''Thực hiện các yêu cầu sau:\\
                         a) Tính giá trị biểu thức $M = (%s + \sqrt{%s})(%s - \sqrt{%s}) - (\sqrt{%s} + \sqrt{%s})(\sqrt{%s} - \sqrt{%s})$.\\
                         b) Rút gọn biểu thức $N = (a + \sqrt{b})(a - \sqrt{b}) + (\sqrt{a} + \sqrt{b})(\sqrt{a} - \sqrt{b})$ với $a \ge 0, b \ge 0$.\\
                         c) Trục căn thức ở mẫu của biểu thức $P = \dfrac{%s}{\sqrt{%s} - \sqrt{%s}} - \dfrac{%s}{%s + \sqrt{%s}}$.'''
                         % (latex(m), latex(n), latex(m), latex(n), latex(u), latex(v), latex(u), latex(v),
                            latex(hieu_uv), latex(u), latex(v), latex(abs(hieu_mn)), latex(m), latex(n)))

        # Nội dung lời giải
        loigiai = ('''\\begin{enumEX}[a)]{1}
                      \item Áp dụng hằng đẳng thức hiệu hai bình phương, ta có:
                      $$M = \left[%s^2 - (\sqrt{%s})^2\right] - \left[(\sqrt{%s})^2 - (\sqrt{%s})^2\right] = (%s - %s) - (%s - %s) = %s.$$
                      \item Với $a \ge 0, b \ge 0$, ta có:
                      $$N = (a^2 - b) + (a - b) = a^2 + a - 2b.$$
                      \item Nhân cả tử và mẫu mỗi phân thức với biểu thức liên hợp của mẫu (lưu ý $%s^2 - %s = %s$):
                      $$P = \dfrac{%s(\sqrt{%s} + \sqrt{%s})}{%s - %s} - \dfrac{%s(%s - \sqrt{%s})}{%s^2 - %s} = (\sqrt{%s} + \sqrt{%s}) + (%s - \sqrt{%s}).$$
                      \\end{enumEX}'''
                   % (latex(m), latex(n), latex(u), latex(v), latex(m**2), latex(n), latex(u), latex(v), latex(val_M),
                      latex(m), latex(n), latex(hieu_mn),
                      latex(hieu_uv), latex(u), latex(v), latex(u), latex(v),
                      latex(abs(hieu_mn)), latex(m), latex(n), latex(m), latex(n),
                      latex(u), latex(v), latex(m), latex(n)))

    # Xuất câu hỏi
    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) + '\\loigiai{ \n' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')

    return content
