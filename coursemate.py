import tkinter as tk
from tkinter import ttk
import json
from datetime import datetime
from pathlib import Path

class CourseMateApp:
    #Part 1: Initialization
    def __init__(self, root):
        self.root = root
        self.root.title("CourseMate - think smarter, learn deeper, and solve problems better.")
        self.root.geometry("1100x700")

        #Data: Store everything here
        self.courses = {}
        self.tasks = []
        self.completed_tasks = []

        #Load data: Get saved data from file
        self.data_file = Path("coursemate_data.json")
        self._load_data()

        #Create UI: Build interface
        self._setup_styles()
        self._create_layout()
        self._create_sidebar()

        #Start: Show dashboard first
        self.show_dashboard()
    
    #Part 2: Data Storage (JSON)
    def _load_data(self):
        pass
    def _save_data(self):
        pass

    #Part 3: UI Setup
    def _setup_styles(self):
        pass
    def _create_layout(self):
        pass
    def _create_sidebar(self):
        pass

    #Part 4:Course Management
    def add_course(self):
        pass
    def delete_course(self, name):
        pass
    def view_course(self, course_name):
        pass
    def _display_note_card_in_frame(self, parent_frame, course_name, note_index, note):
        pass
    def delete_note(self, course_name, note_index):
        pass
    def view_full_note(self, note):
        pass
    def show_task_history(self):
        pass
    def _restore_task_and_refresh(self, index):
        pass
    def _delete_completed_from_dashboard(self, index):
        pass

    #Part 5: Task Management
    def add_task(self):
        pass
    def delete_task(self, indeX):
        pass
    def restore_task(self, index):
        pass
    def permanently_delete_task(self, index):
        pass

    #Part 6: Views
    def _clear_content(self):
        pass
    def show_dashboard(self):
        pass
    def show_freeform(self):
        pass
    def show_technical(self):
        pass
    def show_nontechnical(self):
        pass

    #Part 7: Template
    def open_template(self, template_key):
        pass

if __name__ == "__main__":
    root = tk.Tk()
    app = CourseMateApp(root)
    root.mainloop()