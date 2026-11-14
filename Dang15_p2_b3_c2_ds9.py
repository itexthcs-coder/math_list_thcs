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


def bt_Dang15_p2_b3_c2_ds9(self):
    so_cau = random.choice([25, 30, 40])
    diem_tang = random.choice([5, 10])
    diem_dung = random.choice([2, 3])
    diem_tru = 1
    he_so_x = diem_dung + diem_tru
    hang_so = diem_tang - so_cau * diem_tru
    diem_chuan = random.choice([50, 60, 65, 70])
    while (diem_chuan - hang_so) % he_so_x == 0:
        diem_chuan += 1

    cau_dung_min = math.ceil((diem_chuan - hang_so) / he_so_x)
    bt_diem = latex(he_so_x*x + hang_so)

    noidungcauhoi = ('''Trong một vòng sơ tuyển gồm $%s$ câu hỏi trắc nghiệm, mỗi thí sinh được tặng sẵn $%s$ điểm. Với mỗi câu trả lời đúng thí sinh được cộng $%s$ điểm, mỗi câu trả lời sai bị trừ $%s$ điểm (thí sinh bắt buộc trả lời hết cả $%s$ câu). Để lọt vào vòng phỏng vấn, thí sinh cần đạt tổng số điểm từ $%s$ điểm trở lên. Gọi $x$ ($x \\in \\mathbb{N}, x \\le %s$) là số câu thí sinh trả lời đúng. Xét tính đúng sai của các khẳng định sau:''' % (so_cau, diem_tang, diem_dung, diem_tru, so_cau, diem_chuan, so_cau))

    nb_da_1_d = '\\True Số câu thí sinh trả lời sai là $%s - x$ (câu)' % (so_cau)
    nb_da_1_s = 'Số câu thí sinh trả lời sai là $x - %s$ (câu)' % (so_cau)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = ('''Vì tổng số câu phải trả lời là $%s$ câu và có $x$ câu đúng nên số câu sai là $%s - x$ (câu).''' % (so_cau, so_cau))
    list_nb_2 = [loigiai_nb_1]

    th_da_1_d = '\\True Tổng số điểm thí sinh đạt được tính theo $x$ là $%s$ (điểm)' % (bt_diem)
    th_da_1_s = 'Tổng số điểm thí sinh đạt được tính theo $x$ là $%s$ (điểm)' % (latex(diem_dung*x + diem_tang))
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = ('''Tổng số điểm đạt được là $%s + %sx - %s(%s - x) = %s$ (điểm).''' % (diem_tang, diem_dung, diem_tru, so_cau, bt_diem))
    list_th_2 = [loigiai_th_1]

    vd_da_1_d = '\\True Bất phương trình để thí sinh được vào vòng phỏng vấn là $%s \\ge %s$' % (bt_diem, diem_chuan)
    vd_da_1_s = 'Bất phương trình để thí sinh được vào vòng phỏng vấn là $%s > %s$' % (bt_diem, diem_chuan)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = ('''Để đạt từ $%s$ điểm trở lên, ta phải có $%s \\ge %s$.''' % (diem_chuan, bt_diem, diem_chuan))
    list_vd_2 = [loigiai_vd_1]

    vdc_da_1_d = '\\True Thí sinh cần trả lời đúng ít nhất $%s$ câu hỏi mới được vào vòng phỏng vấn' % (cau_dung_min)
    vdc_da_1_s = 'Thí sinh cần trả lời đúng ít nhất $%s$ câu hỏi mới được vào vòng phỏng vấn' % (cau_dung_min - 1)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = ('''Ta có $%s \\ge %s \\Leftrightarrow x \\ge %.2f$. Vì $x \\in \\mathbb{N}$ nên thí sinh cần trả lời đúng ít nhất $%s$ câu.''' % (bt_diem, diem_chuan, (diem_chuan - hang_so)/he_so_x, cau_dung_min))
    list_vdc_2 = [loigiai_vdc_1]

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

    list_nb_1 = [nb_da_1]
    list_th_1 = [th_da_1]
    list_vd_1 = [vd_da_1]
    list_vdc_1 = [vdc_da_1]

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

    content = ('\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
        '\\choiceTFn \n'
        '{'+str(shuffled_answers_nb[0])+'}\n'
        '{'+str(shuffled_answers_th[0])+'}\n'
        '{'+str(shuffled_answers_vd[0])+'}\n'
        '{'+str(shuffled_answers_vdc[0])+'}\n'
        '\\loigiai{ \n'
        '\\begin{enumEX}[a)]{1} \n'
        '\\item '+str(shuffled_solutions_nb[0])+'\n'
        '\\item '+str(shuffled_solutions_th[0])+'\n'
        '\\item '+str(shuffled_solutions_vd[0])+'\n'
        '\\item '+str(shuffled_solutions_vdc[0])+'\n'
        '\\end{enumEX}} \n'
        '\\end{ex}\n \\end{minipage}\n\n')
    return content
