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


def bt_dang10_p4_b1_c1_ds9(self):
    # Khai báo biến
    lisdang=['1']
    dang=random.choice(lisdang)
    if dang=='1':
        while True:
            x_val = randint(6, 12) / 10.0
            y_val = randint(6, 12) / 10.0
            tong_trc = x_val + y_val
            giam_A = random.choice([10, 15, 20])
            tang_B = random.choice([10, 15, 20])
            tien_A = x_val * (1 - giam_A / 100)
            tien_B = y_val * (1 + tang_B / 100)
            tong_sau = tien_A + tien_B
            if len(str(tong_sau)) <= 5: 
                break
                
        tt_s = str(round(tong_trc, 2)).replace('.', ',') if tong_trc != int(tong_trc) else str(int(tong_trc))
        ts_s = str(round(tong_sau, 2)).replace('.', ',') if tong_sau != int(tong_sau) else str(int(tong_sau))
        
        noidungcauhoi = ('''Hai gia đình A và B tháng trước trả tổng cộng $%s$ triệu đồng tiền điện sinh hoạt. Tháng này gia đình A thực hiện tiết kiệm nên giảm được $%s\\%%$ lượng điện tiêu thụ, trong khi gia đình B có thêm người nên lượng điện dùng tăng $%s\\%%$. Do đó, tổng tiền điện tháng này của cả hai nhà là $%s$ triệu đồng. (Giả sử giá điện không đổi). Hỏi tháng trước mỗi gia đình phải trả bao nhiêu tiền điện?''' % (tt_s, giam_A, tang_B, ts_s))
        
        loigiai = ('''Gọi số tiền điện tháng trước của gia đình A và B lần lượt là $x$ và $y$ (triệu đồng) ($0 < x, y < %s$).\\\\
    Vì tháng trước hai nhà trả tổng cộng $%s$ triệu đồng nên ta có phương trình: $x + y = %s$ (1).\\\\
    Số tiền điện tháng này của gia đình A giảm $%s\\%%$ nên phải trả: $(100\\%% - %s\\%%)x = %s x$ (triệu đồng).\\\\
    Số tiền điện tháng này của gia đình B tăng $%s\\%%$ nên phải trả: $(100\\%% + %s\\%%)y = %s y$ (triệu đồng).\\\\
    Tổng số tiền điện tháng này là $%s$ triệu đồng nên ta có phương trình: $%s x + %s y = %s$ (2).\\\\
    Từ (1) và (2) ta có hệ phương trình:\\\\
    $\\begin{cases} x + y = %s \\\\ %s x + %s y = %s \\end{cases}$\\\\
    Giải hệ phương trình, ta được $x = %s$, $y = %s$ (thỏa mãn).\\\\
    Vậy tháng trước nhà A trả $%s$ triệu đồng, nhà B trả $%s$ triệu đồng.''' % (tt_s, tt_s, tt_s, giam_A, giam_A, str((100-giam_A)/100).replace('.', ','), tang_B, tang_B, str((100+tang_B)/100).replace('.', ','), ts_s, str((100-giam_A)/100).replace('.', ','), str((100+tang_B)/100).replace('.', ','), ts_s, tt_s, str((100-giam_A)/100).replace('.', ','), str((100+tang_B)/100).replace('.', ','), ts_s, str(x_val).replace('.', ','), str(y_val).replace('.', ','), str(x_val).replace('.', ','), str(y_val).replace('.', ',')))
    
    # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
    content = ('\\begin{minipage}{\\textwidth} \\n'
               '\\begin{ex}\\n'+
               str(noidungcauhoi)+
               '\\loigiai{ \\n' +str(loigiai)+'}\\n'
               '\\end{ex}\\n'
               '\\end{minipage} \\n\\n')
    return content
