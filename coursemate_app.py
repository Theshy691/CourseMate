import tkinter as tk
from tkinter import ttk

class CourseMateApp:
    def __init__(self, root):
        self.root = root
        self.root.title("CourseMate")
        self.root.geometry("1200x800")

        self.course = {}
        self.current_view = None

        self._setup_styles()
        self._setup_layout()
        self._create_widgets()
    
    def _setup_styles(self):
        pass
    def _setup_layout(self):
        pass
    def _create_widgets(self):
        self._create_header()
        self._create_sidebar()
    
    def _create_header(self):
        pass
    def _create_sidebar(self):
        pass
