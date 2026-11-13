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


def bt_Dang14_p2_b2_c3_ds9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        c = randint(1, 4)
        c2 = c**2
        c3 = c**3
        k = randint(1, 5)
        m_chinhphuong = randint(4, 12)
        x0 = m_chinhphuong**2
        val_P_x0 = m_chinhphuong - k

        noidungcauhoi = ('''Cho biểu thức $P = \dfrac{x\sqrt{x} + %s}{x - %s\sqrt{x} + %s} - %s$ với $x \ge 0$. Xét tính đúng sai của các mệnh đề sau:'''
                         % (latex(c3), latex(c), latex(c2), latex(c + k)))

        nb_da_1_d = '\\True Với $x \ge 0$, ta có thể viết $x\sqrt{x} + %s = (\sqrt{x})^3 + %s^3$' % (latex(c3), latex(c))
        nb_da_1_s = 'Với $x \ge 0$, ta có thể viết $x\sqrt{x} + %s = (\sqrt{x})^2 + %s^2$' % (latex(c3), latex(c))
        list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
        loigiai_nb_1 = ('''Vì $x \ge 0$ nên $x = (\sqrt{x})^2$, suy ra $x\sqrt{x} + %s = (\sqrt{x})^3 + %s^3$.'''
                        % (latex(c3), latex(c)))

        th_da_1_d = '\\True Phân tích thành nhân tử, ta được $x\sqrt{x} + %s = (\sqrt{x} + %s)(x - %s\sqrt{x} + %s)$' % (latex(c3), latex(c), latex(c), latex(c2))
        th_da_1_s = 'Phân tích thành nhân tử, ta được $x\sqrt{x} + %s = (\sqrt{x} + %s)(x + %s\sqrt{x} + %s)$' % (latex(c3), latex(c), latex(c), latex(c2))
        list_th_da_1 = [th_da_1_d, th_da_1_s]
        loigiai_th_1 = ('''Áp dụng hằng đẳng thức tổng hai lập phương: $(\sqrt{x})^3 + %s^3 = (\sqrt{x} + %s)(x - %s\sqrt{x} + %s)$.'''
                        % (latex(c), latex(c), latex(c), latex(c2)))

        vd_da_1_d = '\\True Với $x \ge 0$, kết quả rút gọn của biểu thức $P$ là $\sqrt{x} - %s$' % (latex(k))
        vd_da_1_s = 'Với $x \ge 0$, kết quả rút gọn của biểu thức $P$ là $\sqrt{x} + %s$' % (latex(c))
        list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
        loigiai_vd_1 = ('''Ta có $x - %s\sqrt{x} + %s = \left(\sqrt{x} - \dfrac{%s}{2}\right)^2 + \dfrac{%s}{4} > 0$, nên $P = (\sqrt{x} + %s) - %s = \sqrt{x} - %s$.'''
                        % (latex(c), latex(c2), latex(c), latex(3 * c2), latex(c), latex(c + k), latex(k)))

        vdc_da_1_d = '\\True Giá trị của biểu thức $P$ tại $x = %s$ bằng $%s$' % (latex(x0), latex(val_P_x0))
        vdc_da_1_s = 'Giá trị của biểu thức $P$ tại $x = %s$ bằng $%s$' % (latex(x0), latex(val_P_x0 + c))
        list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
        loigiai_vdc_1 = ('''Tại $x = %s$ (thỏa mãn $x \ge 0$), ta có $P = \sqrt{%s} - %s = %s - %s = %s$.'''
                         % (latex(x0), latex(x0), latex(k), latex(m_chinhphuong), latex(k), latex(val_P_x0)))

        def count_true_answers(answers):
            return sum('\\True' in ans for ans in answers)

        while True:
            nb_da_1 = random.choice(list_nb_da_1)
            th_da_1 = random.choice(list_th_da_1)
            vd_da_1 = random.choice(list_vd_da_1)
            vdc_da_1 = random.choice(list_vdc_da_1)
            answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
            if 1 <= count_true_answers(answers) <= 3:
                break

        list_nb_1, list_nb_2 = [nb_da_1], [loigiai_nb_1]
        list_th_1, list_th_2 = [th_da_1], [loigiai_th_1]
        list_vd_1, list_vd_2 = [vd_da_1], [loigiai_vd_1]
        list_vdc_1, list_vdc_2 = [vdc_da_1], [loigiai_vdc_1]

        combined_nb = list(zip(list_nb_1, list_nb_2))
        combined_th = list(zip(list_th_1, list_th_2))
        combined_vd = list(zip(list_vd_1, list_vd_2))
        combined_vdc = list(zip(list_vdc_1, list_vdc_2))

        random.shuffle(combined_nb)
        random.shuffle(combined_th)
        random.shuffle(combined_vd)
        random.shuffle(combined_vdc)

        shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
        shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
        shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
        shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

    # Xuất câu hỏi
    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
               '\\choiceTFn \n'
               '{' + str(shuffled_answers_nb[0]) + '}\n'
               '{' + str(shuffled_answers_th[0]) + '}\n'
               '{' + str(shuffled_answers_vd[0]) + '}\n'
               '{' + str(shuffled_answers_vdc[0]) + '}\n'
               '\\loigiai{ \n'
               '\\begin{enumEX}[a)]{1} \n'
               '\\item ' + str(shuffled_solutions_nb[0]) + '\n'
               '\\item ' + str(shuffled_solutions_th[0]) + '\n'
               '\\item ' + str(shuffled_solutions_vd[0]) + '\n'
               '\\item ' + str(shuffled_solutions_vdc[0]) + '\n'
               '\\end{enumEX}} \n'
               '\\end{ex}\n \\end{minipage}\n\n')

    return content
