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


def bt_dang9_p2_b3_c1_ds9(self):
    # Random bộ số đẹp cho đường kính d, thời gian ngược chiều t1, cùng chiều t2
    # C = d * pi; x0 + y0 = d / t1; x0 - y0 = d / t2
    cases = [
        (20, 4, 20, 3, 2),   # C=20pi, x+y=5pi, x-y=pi => x=3pi, y=2pi
        (30, 5, 30, 3.5, 2.5),
        (24, 4, 12, 4, 2),   # C=24pi, x+y=6pi, x-y=2pi => x=4pi, y=2pi
        (40, 5, 20, 5, 3)    # C=40pi, x+y=8pi, x-y=2pi => x=5pi, y=3pi
    ]
    # Chỉ lấy nghiệm nguyên cho sạch
    int_cases = [c for c in cases if c[3] == int(c[3])]
    d_tron, t_nguoc, t_cung, x_coef, y_coef = random.choice(int_cases)
    
    noidungcauhoi = ('''Hai vật chuyển động đều trên một đường tròn đường kính $%s\\text{ cm}$, xuất phát cùng một lúc, từ cùng một điểm. Nếu chuyển động ngược chiều thì cứ sau $%s\\text{ giây}$ chúng lại gặp nhau. Nếu chuyển động cùng chiều thì cứ sau $%s\\text{ giây}$ chúng lại gặp nhau. Gọi $x\\text{ (cm/s)}$ là vận tốc vật nhanh hơn và $y\\text{ (cm/s)}$ là vận tốc vật chậm hơn ($x > y > 0$).''' % (d_tron, t_nguoc, t_cung))
    
    ######################################################################## Nhận biết ############################################
    nb_da_1_d = '\\True Chu vi của đường tròn chuyển động là $C = %s\\pi\\text{ (cm)}$' % d_tron
    nb_da_1_s = 'Chu vi của đường tròn chuyển động là $C = %s\\pi\\text{ (cm)}$' % (2 * d_tron)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    
    loigiai_nb_1 = ('''Đường tròn có đường kính $d = %s\\text{ cm}$ nên chu vi là $C = \\pi d = %s\\pi\\text{ (cm)}$.''' % (d_tron, d_tron))
    list_nb_2 = [loigiai_nb_1]
    
    ######################################################################## Thông hiểu ############################################
    th_da_1_d = '\\True Khi chuyển động ngược chiều, sau $%s\\text{ giây}$ tổng quãng đường hai vật đi được bằng cả chu vi đường tròn nên $%s(x + y) = %s\\pi$' % (t_nguoc, t_nguoc, d_tron)
    th_da_1_s = 'Khi chuyển động ngược chiều, sau $%s\\text{ giây}$ tổng quãng đường hai vật đi được bằng nửa chu vi đường tròn nên $%s(x + y) = %s\\pi$' % (t_nguoc, t_nguoc, d_tron // 2)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    
    loigiai_th_1 = ('''Xuất phát cùng lúc từ một điểm và đi ngược chiều, hai vật gặp nhau khi tổng quãng đường hai vật đi được đúng bằng $1$ vòng đường tròn, tức là $%s(x + y) = %s\\pi$.''' % (t_nguoc, d_tron))
    list_th_2 = [loigiai_th_1]
    
    ######################################################################## Vận dụng ############################################
    vd_da_1_d = '\\True Khi chuyển động cùng chiều, sau $%s\\text{ giây}$ vật nhanh đi nhiều hơn vật chậm đúng $1$ vòng đường tròn nên $%s(x - y) = %s\\pi$' % (t_cung, t_cung, d_tron)
    vd_da_1_s = 'Khi chuyển động cùng chiều, sau $%s\\text{ giây}$ vật nhanh đi nhiều hơn vật chậm đúng $1$ vòng đường tròn nên $%s(y - x) = %s\\pi$' % (t_cung, t_cung, d_tron)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    
    loigiai_vd_1 = ('''Khi đi cùng chiều, vật nhanh hơn đuổi kịp vật chậm hơn khi quãng đường nó đi nhiều hơn vật chậm đúng $1$ chu vi đường tròn, nên $%s(x - y) = %s\\pi$ (vì $x > y$).''' % (t_cung, d_tron))
    list_vd_2 = [loigiai_vd_1]
    
    ######################################################################## Vận dụng cao ############################################
    vdc_da_1_d = '\\True Vận tốc của hai vật lần lượt là $%s\\pi\\text{ cm/s}$ và $%s\\pi\\text{ cm/s}$' % (x_coef, y_coef)
    vdc_da_1_s = 'Vận tốc của hai vật lần lượt là $%s\\pi\\text{ cm/s}$ và $%s\\pi\\text{ cm/s}$' % (x_coef + 1, y_coef - 1 if y_coef > 1 else 1)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    
    loigiai_vdc_1 = ('''Ta có hệ phương trình $\\begin{cases} x + y = %s\\pi \\\\ x - y = %s\\pi. \\end{cases}$ Cộng từng vế hai phương trình, ta được $x = %s\\pi$ và $y = %s\\pi$ (thỏa mãn).''' % (x_coef + y_coef, x_coef - y_coef, x_coef, y_coef))
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
    
    content = ('\\begin{minipage}{\\textwidth} \n' '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n' '\\choiceTFn \n' '{'+str(shuffled_answers_nb[0])+'}\n' '{'+str(shuffled_answers_th[0])+'}\n' '{'+str(shuffled_answers_vd[0])+'}\n' '{'+str(shuffled_answers_vdc[0])+'}\n' '\\loigiai{ \n' '\\begin{enumEX}[a)]{1} \n' '\\item '+str(shuffled_solutions_nb[0])+'\n' '\\item '+str(shuffled_solutions_th[0])+'\n' '\\item '+str(shuffled_solutions_vd[0])+'\n' '\\item '+str(shuffled_solutions_vdc[0])+'\n' '\\end{enumEX}} \n' '\\end{ex}\n \\end{minipage}\n\n')

    return content
