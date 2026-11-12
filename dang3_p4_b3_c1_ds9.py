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


def bt_dang3_p4_b3_c1_ds9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        t_chung = random.choice([12, 15, 18, 24, 30])
        x0 = (5 * t_chung) // 3
        y0 = (3 * x0) // 2
    
        # Nội dung câu hỏi
        noidungcauhoi = ('''Hai đội công nhân cùng làm một đoạn đường trong $%s\\text{ ngày}$ thì xong. Mỗi ngày, đội I làm được nhiều gấp rưỡi đội II. Hỏi nếu làm một mình thì mỗi đội làm xong đoạn đường đó trong bao lâu? (Giả sử năng suất của mỗi đội là không đổi).'''
                         % (t_chung))
    
        # Nội dung lời giải
        loigiai = ('''\\begin{itemize}
                        \\item Gọi $x$ là số ngày để đội I hoàn thành công việc nếu làm một mình; $y$ là số ngày để đội II hoàn thành công việc nếu làm một mình. Điều kiện: $x > 0$ và $y > 0$.\\\\
                        Mỗi ngày đội I làm được $\\dfrac{1}{x}$ (công việc) và đội II làm được $\\dfrac{1}{y}$ (công việc).\\\\
                        Mỗi ngày đội I làm được nhiều gấp rưỡi đội II nên ta có phương trình:
                        $$\\dfrac{1}{x} = 1{,}5 \\cdot \\dfrac{1}{y} \\quad \\text{hay} \\quad \\dfrac{1}{x} = \\dfrac{3}{2} \\cdot \\dfrac{1}{y}. \\quad (1)$$
                        Hai đội làm chung trong $%s\\text{ ngày}$ thì xong công việc nên mỗi ngày, hai đội làm chung được $\\dfrac{1}{%s}$ (công việc). Ta có phương trình:
                        $$\\dfrac{1}{x} + \\dfrac{1}{y} = \\dfrac{1}{%s}. \\quad (2)$$
                        Từ $(1)$ và $(2)$, ta có hệ phương trình:
                        $$\\begin{cases} \\dfrac{1}{x} = \\dfrac{3}{2} \\cdot \\dfrac{1}{y} \\\\ \\dfrac{1}{x} + \\dfrac{1}{y} = \\dfrac{1}{%s}. \\end{cases}$$
                        \\item Đặt $u = \\dfrac{1}{x}$ và $v = \\dfrac{1}{y}$, ta có hệ phương trình bậc nhất hai ẩn mới là $u$ và $v$:
                        $$\\begin{cases} u = \\dfrac{3}{2}v \\\\ u + v = \\dfrac{1}{%s}. \\end{cases}$$
                        Thế $u = \\dfrac{3}{2}v$ vào phương trình thứ hai, ta được $\\dfrac{3}{2}v + v = \\dfrac{1}{%s}$ hay $\\dfrac{5}{2}v = \\dfrac{1}{%s}$, suy ra $v = \\dfrac{1}{%s}$.\\\\
                        Do đó $u = \\dfrac{3}{2} \\cdot \\dfrac{1}{%s} = \\dfrac{1}{%s}$.\\\\
                        Từ đó, ta có $u = \\dfrac{1}{x} = \\dfrac{1}{%s} \\Rightarrow x = %s$ và $v = \\dfrac{1}{y} = \\dfrac{1}{%s} \\Rightarrow y = %s$.
                        \\item Các giá trị tìm được của $x$ và $y$ thỏa mãn điều kiện của ẩn.\\\\
                        Vậy nếu làm một mình thì đội I làm xong đoạn đường đó trong $%s\\text{ ngày}$, còn đội II làm xong trong $%s\\text{ ngày}$.
                    \\end{itemize}'''
                   % (t_chung, t_chung, t_chung, t_chung,
                      t_chung, t_chung, t_chung, y0,
                      y0, x0,
                      x0, x0, y0, y0,
                      x0, y0))
    
    # Xuất câu hỏi với đáp án và lời giải
    content = ('\\begin{minipage}{\\textwidth} \n' '\\begin{ex}\n'+ str(noidungcauhoi)+ '\\loigiai{ \n' +str(loigiai)+'}\n' '\\end{ex}\n \\end{minipage} \n\n')


    return content
