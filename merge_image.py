from tkinter import *
import tkinter.ttk as ttk

root = Tk()
root.title('Merge images')

# File frame
file_frame = Frame(root)
file_frame.pack(fill='x', padx=5, pady=5)

btn_add_file = Button(file_frame, width=12, padx=5, pady=5, text='Add File')
btn_add_file.pack(side='left')

btn_remove_file = Button(file_frame, width=12, padx=5, pady=5, text='Remove File')
btn_remove_file.pack(side='right')

# List frame
list_frame = Frame(root)
list_frame.pack(fill='both', padx=5, pady=5)

scrollbar = Scrollbar(list_frame)
scrollbar.pack(side='right', fill='y')

list_file = Listbox(list_frame, selectmode='extended', height=15, yscrollcommand=scrollbar.set)
list_file.pack(side='left', fill='both', expand=True)
scrollbar.config(command=list_file.yview)

# Save location frame
path_frame = LabelFrame(root, text='Save Location')
path_frame.pack(fill='x', padx=5, pady=5, ipady=5)

txt_dest_path = Entry(path_frame)
txt_dest_path.pack(side='left', fill='x', expand=True, padx=5, pady=5, ipady=4)

btn_dest_path = Button(path_frame, text='Browse', width=10)
btn_dest_path.pack(side='right', padx=5, pady=5)

# Option frame
option_frame = LabelFrame(root, text='Option')
option_frame.pack(padx=5, pady=5, ipady=5)

# 1. Width option
lbl_width = Label(option_frame, text='Width', width=8)
lbl_width.pack(side='left')

opt_width = ['Original', '1024', '800', '600']
cmb_width = ttk.Combobox(option_frame, state='readonly', value=opt_width, width=10)
cmb_width.current(0)
cmb_width.pack(side='left')

# 2. Gap option
lbl_gap = Label(option_frame, text='Gap', width=8)
lbl_gap.pack(side='left', padx=5, pady=5)

opt_gap = ['None', 'Narrow', 'Normal', 'wide']
cmb_gap = ttk.Combobox(option_frame, state='readonly', value=opt_gap, width=10)
cmb_gap.current(0)
cmb_gap.pack(side='left', padx=5, pady=5)

# 3. Format option
lbl_format = Label(option_frame, text='Format', width=8)
lbl_format.pack(side='left', padx=5, pady=5)

opt_format = ['PNG', 'JPG', 'BMP']
cmb_format = ttk.Combobox(option_frame, state='readonly', value=opt_format, width=10)
cmb_format.current(0)
cmb_format.pack(side='left', padx=5, pady=5)

# Progress frame
progress_frame = LabelFrame(root, text='Progress')
progress_frame.pack(fill='x', padx=5, pady=5, ipady=5)

p_var = DoubleVar()
progress_bar = ttk.Progressbar(progress_frame, maximum=100, variable=p_var)
progress_bar.pack(fill='x', padx=5, pady=5)

# Execute frame
exec_frame = Frame(root)
exec_frame.pack(fill='x', padx=5, pady=5)

btn_close = Button(exec_frame, padx=5, pady=5, text='Close', width=12, command=root.quit)
btn_close.pack(side='right', padx=5, pady=5)

btn_start = Button(exec_frame, padx=5, pady=5, text='Start', width=12)
btn_start.pack(side='right', padx=5, pady=5)


root.resizable(False, False)
root.mainloop()
