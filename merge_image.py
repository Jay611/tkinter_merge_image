from tkinter import *
from tkinter import filedialog
from PIL import Image
import tkinter.messagebox as msgbox
import tkinter.ttk as ttk
import os

root = Tk()
root.title('Merge images')

# Add file
def add_file():
    files = filedialog.askopenfilenames(title='Select image files', \
        filetypes=(('PNG file', '*.png'), ('All file', '*.*')), \
        initialdir='C:/')

    for file in files:
        list_file.insert(END, file)
    
# Remove file
def remove_file():
    for idx in reversed(list_file.curselection()):
        list_file.delete(idx)

# Save location (folder)
def browser_dest_path():
    folder_selected = filedialog.askdirectory()
    if not folder_selected:
        return
    txt_dest_path.delete(0, END)
    txt_dest_path.insert(0, folder_selected)

# Merge images
def merge_images():
    
    try:
        # Width
        img_width = cmb_width.get()
        if img_width == 'Original':
            img_width = -1
        else:
            img_width = int(img_width)
            
        # Gap
        img_gap = cmb_gap.get()
        if img_gap == 'Narrow':
            img_gap = 30
        elif img_gap == 'Normal':
            img_gap = 60
        elif img_gap == 'Wide':
            img_gap = 90
        else:
            img_gap = 0
            
        # Format
        img_format = cmb_format.get().lower()
        
        ############################################################
        
        
        images = [Image.open(img) for img in list_file.get(0, END)]
        # size -> size[0]: width, size[1]: height
        
        image_sizes = []    #[(width1, height1), (width2, height2), ...]
        if img_width > -1:
            image_sizes = [(int(img_width), int(img_width * x.size[1] / x.size[0])) for x in images]
        else:
            image_sizes = [(x.size[0], x.size[1]) for x in images]
        
        widths, heights = zip(*image_sizes)
        
        # Max width, total height
        max_width, total_height = max(widths), sum(heights)
        
        # Base image
        # Apply gap
        if img_gap > 0:
            total_height += (img_gap * (len(images) - 1))
            
        result_img = Image.new('RGB', (max_width, total_height), (255, 255, 255))
        y_offset = 0
        
        # Paste images
        for idx, img in enumerate(images):
            if img_width > -1:
                img = img.resize(image_sizes[idx])
            
            result_img.paste(img, (0, y_offset))
            y_offset += (img.size[1] + img_gap) # Apply gap
            
            progress = (idx + 1) / len(images) * 100
            p_var.set(progress)
            progress_bar.update()
            
        file_name = 'result_img.' + img_format
        dest_path = os.path.join(txt_dest_path.get(), file_name)
        result_img.save(dest_path)
        msgbox.showinfo('Info', 'Merge completed')
    except Exception as err:
        msgbox.showerror('Error', err)


# Start
def start():
    if list_file.size() == 0:
        msgbox.showwarning('Warning', 'Select images')
        return
    
    if len(txt_dest_path.get()) == 0:
        msgbox.showwarning('Warning', 'Select destination path')
        return

    merge_images()

# File frame
file_frame = Frame(root)
file_frame.pack(fill='x', padx=5, pady=5)

btn_add_file = Button(file_frame, width=12, padx=5, pady=5, text='Add File', command=add_file)
btn_add_file.pack(side='left')

btn_remove_file = Button(file_frame, width=12, padx=5, pady=5, text='Remove File', command=remove_file)
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

btn_dest_path = Button(path_frame, text='Browse', width=10, command=browser_dest_path)
btn_dest_path.pack(side='right', padx=5, pady=5)

# Option frame
option_frame = LabelFrame(root, text='Option')
option_frame.pack(padx=5, pady=5, ipady=5)

# 1. Width option
lbl_width = Label(option_frame, text='Width', width=8)
lbl_width.pack(side='left')

opt_width = ['Original', '1024', '800', '640']
cmb_width = ttk.Combobox(option_frame, state='readonly', value=opt_width, width=10)
cmb_width.current(0)
cmb_width.pack(side='left')

# 2. Gap option
lbl_gap = Label(option_frame, text='Gap', width=8)
lbl_gap.pack(side='left', padx=5, pady=5)

opt_gap = ['None', 'Narrow', 'Normal', 'Wide']
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

btn_start = Button(exec_frame, padx=5, pady=5, text='Start', width=12, command=start)
btn_start.pack(side='right', padx=5, pady=5)


root.resizable(False, False)
root.mainloop()
