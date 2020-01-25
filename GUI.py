import tkinter as tk
from tkinter import ttk
import requests
from PIL import Image, ImageTk
from tkinter.font import Font
import requests
import json
import time 
import functions

HEIGHT = 720
WIDTH = 1280
	
def update_time(event = None): # Update time continusouly on GUI #Problem with indentation
	t = f.get_local_time()
	time_label['text'] = t
	time_label.after(500, update_time)	
	
def update_BTC():
	p = f.get_price(f.price_list, 0)
	price_label_BTC['text'] = f"${p} USD"
	price_label_BTC.after(10000, update_BTC) #When the time is low, GUI will not load [1000 = 1 sec]
	return p

def update_ETH():
	p = f.get_price(f.price_list, 1)
	price_label_ETH['text'] = f"${p} USD"
	price_label_ETH.after(10000, update_ETH)
	return p
	
def update_LTC():
	p = f.get_price(f.price_list, 2)
	price_label_LTC['text'] = f"${p} USD"
	price_label_LTC.after(10000, update_LTC)
	return p

def update_XLM():
	p = f.get_price(f.price_list, 3)
	price_label_XLM['text'] = f"${p} USD"
	price_label_XLM.after(10000, update_XLM)
	return p

def update_24hr_BTC():
	p_24hr = f.get_last24hr_price('BTC')
	s = str(p_24hr)
	if (s.find("-", 0) == -1):
		p24_BTC_label.config(fg = '#1aff1a')
		p24_BTC_label['text'] = f"Last 24hr: +{p_24hr}%"
	else:
		p24_BTC_label.config(fg = '#cc0000')
		p24_BTC_label['text'] = f"Last 24hr: {p_24hr}%"
	p24_BTC_label.after(300000, update_24hr_BTC)	#5-minute updates due to API limit

def update_24hr_ETH():
	p_24hr = f.get_last24hr_price('ETH')
	s = str(p_24hr)
	if (s.find("-", 0) == -1):
		p24_ETH_label.config(fg = '#1aff1a')
		p24_ETH_label['text'] = f"Last 24hr: +{p_24hr}%"
	else:
		p24_ETH_label.config(fg = '#cc0000')
		p24_ETH_label['text'] = f"Last 24hr: {p_24hr}%"
	p24_ETH_label.after(300000, update_24hr_ETH)

def update_24hr_LTC():
	p_24hr = f.get_last24hr_price('LTC')
	s = str(p_24hr)
	if (s.find("-", 0) == -1):
		p24_LTC_label.config(fg = '#1aff1a')
		p24_LTC_label['text'] = f"Last 24hr: +{p_24hr}%"
	else:
		p24_LTC_label.config(fg = '#cc0000')
		p24_LTC_label['text'] = f"Last 24hr: {p_24hr}%"
	p24_LTC_label.after(300000, update_24hr_LTC)

def update_24hr_XLM():
	p_24hr = f.get_last24hr_price('XLM')
	s = str(p_24hr)
	if (s.find("-", 0) == -1):
		p24_XLM_label.config(fg = '#1aff1a')
		p24_XLM_label['text'] = f"Last 24hr: +{p_24hr}%"
	else:
		p24_XLM_label.config(fg = '#cc0000')
		p24_XLM_label['text'] = f"Last 24hr: {p_24hr}%"
	p24_XLM_label.after(300000, update_24hr_XLM)
# ---------------------------------------------------------------------------------
	
f = functions.functions() #Create object to access list of methods
root = tk.Tk() # Create Gui
root.title("CryptoTracker")

# ----Set Height of the window-----
canvas = tk.Canvas(root, height = HEIGHT, width = WIDTH)
canvas.pack()

# ----Main Frame (Background Light Blue)------
frame = tk.Frame(root, bg = '#0080ff')
frame.place(relwidth = 1, relheight = 1)

# -----Import Time------
timefont = Font(family = "Open Sans", size = 14)
time_label = tk.Label(root, font = timefont, bg ='#0080ff', fg = '#f2f2f2')
time_label.place(relx = 0.01, rely = 0.02)
update_time()

# -----Update BTC Price-----
pricefont_BTC = Font(family = "Open Sans", size = 22)
price_label_BTC = tk.Label(frame, font = pricefont_BTC, bg ='#0080ff', fg = '#f2f2f2')
price_label_BTC.place(relx = 0.35, rely = 0.55)
BTC_price = update_BTC() 

pricefont_secondary = Font(family = "Open Sans", size = 18, slant = "italic")
# ------24hr ago price of BTC-----
p24_BTC_label = tk.Label(frame, font = pricefont_secondary, bg = '#0080ff', fg = '#f2f2f2')
p24_BTC_label.place(relx = 0.35, rely = 0.6)
update_24hr_BTC()

# -----Update ETH Price-----
price_label_ETH = tk.Label(frame, font = pricefont_secondary, bg ='#0080ff', fg = '#f2f2f2')
price_label_ETH.place(relx = 0.75, rely = 0.25)
ETH_price = update_ETH() 
# ------24hr ago price of ETH-----
p24_ETH_label = tk.Label(frame, font = pricefont_secondary, bg = '#0080ff', fg = '#f2f2f2')
p24_ETH_label.place(relx = 0.75, rely = 0.3)
update_24hr_ETH()

# -----Update LTC Price-----
price_label_LTC = tk.Label(frame, font = pricefont_secondary, bg ='#0080ff', fg = '#f2f2f2')
price_label_LTC.place(relx = 0.75, rely = 0.52)
LTC_price = update_LTC()
# ------24hr ago price of LTC-----
p24_LTC_label = tk.Label(frame, font = pricefont_secondary, bg = '#0080ff', fg = '#f2f2f2')
p24_LTC_label.place(relx = 0.75, rely = 0.57)
update_24hr_LTC()

# -----Update XLM Price-----
price_label_XLM = tk.Label(frame, font = pricefont_secondary, bg ='#0080ff', fg = '#f2f2f2')
price_label_XLM.place(relx = 0.75, rely = 0.8)
XLM_price = update_XLM()
# ------24hr ago price of XLM-----
p24_XLM_label = tk.Label(frame, font = pricefont_secondary, bg = '#0080ff', fg = '#f2f2f2')
p24_XLM_label.place(relx = 0.75, rely = 0.85)
update_24hr_XLM()


# ----Set crypto image--------------------------------------------------------------------

	# ---Bitcoin---#
im1_BTC = Image.open("bitcoin.png")
im2_BTC = im1_BTC.resize((150, 150), Image.ANTIALIAS)
BTC_image = ImageTk.PhotoImage(im2_BTC)
crypto_label_BTC = tk.Label(frame, image = BTC_image, borderwidth = 0)
crypto_label_BTC.place(relx = 0.22, rely = 0.41)

	# ---Ethereum---#
im1_ETH = Image.open("ETH.png")
im2_ETH = im1_ETH.resize((100, 162), Image.ANTIALIAS)
ETH_image = ImageTk.PhotoImage(im2_ETH)
crypto_label_ETH = tk.Label(frame, image = ETH_image, borderwidth = 0)
crypto_label_ETH.place(relx = 0.65, rely = 0.12)

	# ---Litecoin---#
im1_LTC = Image.open("LTC.png")
im2_LTC = im1_LTC.resize((100, 100), Image.ANTIALIAS)
LTC_image = ImageTk.PhotoImage(im2_LTC)
crypto_label_LTC = tk.Label(frame, image = LTC_image, borderwidth = 0)
crypto_label_LTC.place(relx = 0.65, rely = 0.45)
	
	#---Stellar Lumens---#
im1_XLM = Image.open("XLM.png")
im2_XLM = im1_XLM.resize((100, 100), Image.ANTIALIAS)
XLM_image = ImageTk.PhotoImage(im2_XLM)
crypto_label_XLM = tk.Label(frame, image = XLM_image, borderwidth = 0)
crypto_label_XLM.place(relx = 0.65, rely = 0.7)

# -------Graphs Button & Font--------------------------------------------------------------------
# buttonfont = Font(family = "Open Sans", size = 20, slant = "italic")
# graph_button = tk.Button(frame, text = "Graphs", font = buttonfont, bg = '#0080ff', fg = '#f2f2f2',
# 		activebackground = '#005c99', activeforeground = '#f2f2f2', justify = "center", 
# 		highlightthickness = 0, bd = 0)
# graph_button.place(relx = 0.02, rely = 0.9) # this was 45 and 650 for abs x and y

# -----Crypto Name Label-------------------------------------------------------------------

	# ---Bitcoin---#
headerfont_BTC = Font(family = "News Gothic", size = 52)
label_BTC = tk.Label(frame, text = "Bitcoin", font = headerfont_BTC, bg = '#0080ff', fg = '#f2f2f2', 
		bd = 1)
label_BTC.place(relx = 0.35, rely = 0.44)

headerfont_secondary = Font(family = "Open Sans", size = 28, slant = "italic")

	# ---Ethereum---#
label_ETH = tk.Label(frame, text = "Ethereum", font = headerfont_secondary, bg = '#0080ff', fg = '#f2f2f2', 
		bd = 1)
label_ETH.place(relx = 0.75, rely = 0.18)

	# ---Litecoin---#
label_LTC = tk.Label(frame, text = "Litecoin", font = headerfont_secondary, bg = '#0080ff', fg = '#f2f2f2', 
		bd = 1)
label_LTC.place(relx = 0.75, rely = 0.45)

	# ---Stellar Lumens---#
label_XLM = tk.Label(frame, text = "Stellar \n Lumens", font = headerfont_secondary, bg = '#0080ff', fg = '#f2f2f2', 
		bd = 1)
label_XLM.place(relx = 0.75, rely = 0.67)

# -----Your amount Entry-----#		# Need to empty entry upon click
font_entry = Font(family = "Open Sans", size = 18, slant = "italic")
entryText = tk.StringVar()
amount = tk.Entry(frame, textvariable = entryText, font = font_entry, width = 20)
entryText.set("Enter amount")
amount.place(relx = 0.25, rely = 0.652)
amount.bind('<Return>', lambda x: f.get_conversion(amount.get(), combo_box1.get(), combo_box2.get(), entryText)) #Can hit enter to submit textbox
amount.bind('<Button-1>', lambda x: amount.delete(0, 100))

# -----ComboBox Currency Selection-----#
combo_box_text1 = tk.StringVar()
combo_box_text1.set("BTC")
combo_box1 = ttk.Combobox(root, width = 5, textvariable = combo_box_text1, values = ["BTC", "ETH", "LTC", "XLM",
			"XRP", "BCH"], state = "readonly")
combo_box1.place(relx = .45, rely = .71)

combo_box_text2 = tk.StringVar()
combo_box_text2.set("USD")
combo_box2 = ttk.Combobox(root, width = 5, textvariable = combo_box_text2, values = ["USD", "EUR", "GBP", "JPY"], state = "readonly")
combo_box2.place(relx = .52, rely = .71)

to = Font(family = "Open Sans", size = 14, slant = "italic")
label_to = tk.Label(frame, text = "to", font = to, bg = '#0080ff', fg = '#f2f2f2', 
		bd = 1)
label_to.place(relx = 0.497, rely = 0.7055)

# -----Calculate Button-----#
calc_font = Font(family = "Open Sans", size = 16, slant = "italic")
calc_button = tk.Button(frame, text = "Calculate", font = calc_font, bg = '#0080ff',
		fg = '#f2f2f2', activebackground = '#005c99', activeforeground = '#f2f2f2', 
		justify = "center", highlightthickness = 0, bd = 1, relief = "raised",
		command = lambda: f.get_conversion(amount.get(), combo_box1.get(), combo_box2.get(), entryText), 
		padx = 1, pady = 1)
calc_button.place(relx = 0.465, rely = 0.65) 


root.mainloop()