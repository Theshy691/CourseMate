import tkinter as tk
from tkinter import ttk 


class CourseMateApp:
    """
    Main application class for CourseMate.
    
    WHY USE A CLASS?
    1. ORGANIZATION: Groups related code together (all UI, data, methods in one place)
    2. STATE MANAGEMENT: Can store data (courses, notes) that persists across functions
    3. REUSABILITY: Easy to create multiple instances or extend functionality
    4. MAINTAINABILITY: Easier to find and fix bugs, add features
    5. SCALABILITY: As your app grows, classes keep it organized
    """
    
    def __init__(self, root):
        """
        Constructor: Runs when you create the app
        Sets up the initial state and creates the UI
        """
        self.root = root
        self.root.title("CourseMate")
        self.root.geometry("1200x800")
        
        # Instance variables (data that belongs to this app instance)
        self.courses = {}  # Store course data
        self.current_view = None  # Track which view is showing
        
        # Build the UI in organized steps
        self._setup_styles()
        self._setup_layout()
        self._create_widgets()
    
    def _setup_styles(self):
        """
        Separate method for styling - keeps code organized
        The underscore (_) prefix means "private method" - internal use only
        """
        self.style = ttk.Style()
        self.style.theme_use('clam')
        
        # Frame styles
        self.style.configure('Sidebar.TFrame', background='#2c3e50')
        self.style.configure('TFrame', background='#f5f5f5')
        self.style.configure('Card.TFrame', background='white', relief='solid', borderwidth=1)
        
        # Button styles
        self.style.configure('Sidebar.TButton', 
                            background='#34495e', 
                            foreground='white',
                            borderwidth=0, 
                            font=('Helvetica', 10))
        self.style.map('Sidebar.TButton', 
                      background=[('active', '#546a7e')])
    
    def _setup_layout(self):
        """
        Create the main layout structure
        Separating layout from widgets makes code cleaner
        """
        # Header frame
        self.header_frame = ttk.Frame(self.root, height=60, style='Sidebar.TFrame')
        self.header_frame.pack(fill='x', side='top')
        self.header_frame.pack_propagate(False)
        
        # Sidebar frame
        self.sidebar_frame = ttk.Frame(self.root, width=240, style='Sidebar.TFrame')
        self.sidebar_frame.pack(fill='y', side='left')
        self.sidebar_frame.pack_propagate(False)
        
        # Main content frame
        self.main_content = ttk.Frame(self.root, style='TFrame')
        self.main_content.pack(fill='both', side='right', expand=True)
    
    def _create_widgets(self):
        """
        Create all the UI widgets
        Organized into logical sections
        """
        self._create_header()
        self._create_sidebar()
    
    def _create_header(self):
        """Create header widgets"""
        header_title = ttk.Label(
            self.header_frame, 
            text="CourseMate: A Smart Note-Taking & Study Aid For Students",
            font=('Helvetica', 16, 'bold'), 
            foreground='white',
            background='#2c3e50'
        )
        header_title.pack(pady=15, padx=20, side='left')
    
    def _create_sidebar(self):
        """
        Create sidebar navigation
        Each button gets a command that links to a method
        """
        # Navigation section
        ttk.Label(
            self.sidebar_frame, 
            text="NAVIGATION",
            font=('Helvetica', 9, 'bold'), 
            foreground='#95a5a6',
            background='#2c3e50'
        ).pack(pady=(20, 10), padx=20, anchor='w')
        
        # My Courses button - now it can actually do something!
        mycourse_button = ttk.Button(
            self.sidebar_frame, 
            text="My Courses", 
            style='Sidebar.TButton',
            command=self.show_my_courses  # Links to method below
        )
        mycourse_button.pack(fill='x', pady=3, padx=15)
        
        # Separator
        ttk.Separator(self.sidebar_frame, orient='horizontal').pack(
            fill='x', pady=15, padx=15
        )
        
        # General Education Templates section
        ttk.Label(
            self.sidebar_frame, 
            text="TEMPLATES FOR\nGENERAL EDUCATION COURSES",
            font=('Helvetica', 9, 'bold'), 
            foreground='#95a5a6',
            background='#2c3e50'
        ).pack(pady=10, padx=20, anchor='w')
        
        # Template buttons
        templates_general = [
            ("Cornell Notes", self.open_cornell),
            ("Main Idea & Supporting Details", self.open_main_idea),
            ("Frayer Model", self.open_frayer_model)
        ]
        
        for text, command in templates_general:
            btn = ttk.Button(
                self.sidebar_frame, 
                text=text, 
                style='Sidebar.TButton',
                command=command
            )
            btn.pack(fill='x', pady=3, padx=15)
        
        # Separator
        ttk.Separator(self.sidebar_frame, orient='horizontal').pack(
            fill='x', pady=15, padx=15
        )
        
        # Technical Templates section
        ttk.Label(
            self.sidebar_frame, 
            text="TEMPLATES FOR\nTECHNICAL COURSES",
            font=('Helvetica', 9, 'bold'), 
            foreground='#95a5a6',
            background='#2c3e50'
        ).pack(pady=10, padx=20, anchor='w')
        
        # Technical template buttons
        templates_technical = [
            ("Polya's 4 Steps", self.open_polya),
            ("KWLH", self.open_kwlh),
            ("5W1H", self.open_5w1h)
        ]
        
        for text, command in templates_technical:
            btn = ttk.Button(
                self.sidebar_frame, 
                text=text, 
                style='Sidebar.TButton',
                command=command
            )
            btn.pack(fill='x', pady=3, padx=15)
    
    # ============================================
    # BUTTON COMMAND METHODS
    # These run when buttons are clicked
    # ============================================
    
    def show_my_courses(self):
        """Show the My Courses view"""
        print("My Courses clicked!")
        # Clear main content
        for widget in self.main_content.winfo_children():
            widget.destroy()
        
        # Create course view
        ttk.Label(
            self.main_content, 
            text="My Courses",
            font=('Helvetica', 24, 'bold')
        ).pack(padx=30, pady=20, anchor='nw')
        
        ttk.Label(
            self.main_content,
            text="Your courses will appear here.",
            font=('Helvetica', 12)
        ).pack(padx=30, pady=10, anchor='nw')
    
    def open_cornell(self):
        """Open Cornell Notes template"""
        print("Cornell Notes clicked!")
        self._show_template_view("Cornell Notes")
    
    def open_main_idea(self):
        """Open Main Idea template"""
        print("Main Idea clicked!")
        self._show_template_view("Main Idea & Supporting Details")
    
    def open_frayer_model(self):
        """Open Frayer Model template"""
        print("Frayer Model clicked!")
        self._show_template_view("Frayer Model")
    
    def open_polya(self):
        """Open Polya's 4 Steps template"""
        print("Polya's 4 Steps clicked!")
        self._show_template_view("Polya's 4 Steps")
    
    def open_kwlh(self):
        """Open KWLH template"""
        print("KWLH clicked!")
        self._show_template_view("KWLH")
    
    def open_5w1h(self):
        """Open 5W1H template"""
        print("5W1H clicked!")
        self._show_template_view("5W1H")
    
    def _show_template_view(self, template_name):
        """
        Helper method to display any template
        This avoids code duplication
        """
        # Clear main content
        for widget in self.main_content.winfo_children():
            widget.destroy()
        
        # Show template
        ttk.Label(
            self.main_content, 
            text=f"{template_name} Template",
            font=('Helvetica', 24, 'bold')
        ).pack(padx=30, pady=20, anchor='nw')
        
        ttk.Label(
            self.main_content,
            text=f"This is where the {template_name} form will appear.",
            font=('Helvetica', 12)
        ).pack(padx=30, pady=10, anchor='nw')


# ============================================
# COMPARISON: Without Class vs With Class
# ============================================

"""
WITHOUT CLASS (Your original approach):
- All code in one file at the top level
- Hard to organize as it grows
- Variables are global (can cause bugs)
- Can't easily create multiple instances
- Difficult to add features later

WITH CLASS (This approach):
- Organized into logical methods
- Data is contained (self.courses, self.current_view)
- Easy to add new methods/features
- Can create multiple app instances if needed
- Professional, maintainable code structure
- Other developers can understand it easily

WHEN YOUR APP GROWS:
- Add new templates: Just add a method like open_new_template()
- Save data: Add self.courses = {...} and save methods
- Add views: Create _show_dashboard(), _show_statistics(), etc.
- Everything stays organized!
"""


# ============================================
# MAIN ENTRY POINT
# ============================================

if __name__ == "__main__":
    # Create the main window
    root = tk.Tk()
    
    # Create the app (this runs __init__)
    app = CourseMateApp(root)
    
    # Start the event loop
    root.mainloop()