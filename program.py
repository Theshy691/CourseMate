import tkinter as tk
from tkinter import ttk 

#root
root = tk.Tk()
root.title("CourseMate: A Smart Note-Taking & Study Aid For Students")
root.geometry("1200x800")

#header frame
header_frame = ttk.Frame(root, height=60, style='Sidebar.TFrame')
header_frame.pack(fill='x', side='top')
header_frame.pack_propagate(False)

#sidebar frame
sidebar_frame = ttk.Frame(root, width=240, style='Sidebar.TFrame')
sidebar_frame.pack(fill='y', side='left')
sidebar_frame.pack_propagate(False)

#main content frame
main_content = ttk.Frame(root, style='TFrame')
main_content.pack(fill='both', side='right', expand=True)

#style of Sidebar.TFrame & TFrame
style = ttk.Style()
style.theme_use('clam')
style.configure('Sidebar.TFrame', background='#2c3e50')
style.configure('TFrame', background='#f5f5f5')
style.configure('Card.TFrame', background='white', relief='solid', borderwidht=1)

#widgets
header_title = ttk.Label(header_frame, text="CourseMate: A Smart Note-Taking & Study Aid For Students",
                         font=('Helvetica', 16, 'bold'), foreground='white',
                         background='#2c3e50')
header_title.pack(pady=15, padx=20, side='left')

ttk.Label(sidebar_frame, text="NAVIGATION",
          font=('Helvetica', 9, 'bold'), foreground='#95a5a6',
          background='#2c3e50').pack(pady=(20,10), padx=20, anchor='w')
mycourse_button = ttk.Button(sidebar_frame, text="My Courses", style='Sidebar.TButton')
mycourse_button.pack(fill='x', pady=3, padx=15)
ttk.Separator(sidebar_frame, orient='horizontal').pack(fill='x', pady=15, padx=15)
ttk.Label(sidebar_frame, text="TEMPLATES",
          font=('Helvetica', 9, 'bold'), foreground='#95a5a6',
          background='#2c3e50').pack(pady=(10), padx=20, anchor='w')
cornell_button = ttk.Button(sidebar_frame, text="Cornell Notes", style='Sidebar.TButton')
cornell_button.pack(fill='x', pady=3, padx=15)

main_idea_button = ttk.Button(sidebar_frame, text="Main Idea & Supporting Details", style='Sidebar.TButton')
main_idea_button.pack(fill='x', pady=3, padx=15)

frayer_model_button = ttk.Button(sidebar_frame, text="Frayer Model", style='Sidebar.TButton')
frayer_model_button.pack(fill='x', pady=3, padx=15)

Polyas_4_steps_button = ttk.Button(sidebar_frame, text="Polya's 4 Steps", style='Sidebar.TButton')
Polyas_4_steps_button.pack(fill='x', pady=3, padx=15)

five_w_1h_button = ttk.Button(sidebar_frame, text="5W1H", style='Sidebar.TButton')
five_w_1h_button.pack(fill='x', pady=3, padx=15)

kwlh_button = ttk.Button(sidebar_frame, text="KWLH", style='Sidebar.TButton')
kwlh_button.pack(fill='x', pady=3, padx=15)

root.mainloop() 