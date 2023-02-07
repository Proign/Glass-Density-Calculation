from tkinter import *
from tkinter import ttk

window = Tk()
window.resizable(width=False, height=False)
window.geometry('720x650')  
window.title("Glass Density Calculation")

#Top frame
top_frame = Frame(window, width= 720, height = 275)
top_frame.propagate(0)
top_frame.pack(side=TOP, padx = 2)

# define columns
columns = ('element', 'content')

tree = ttk.Treeview(top_frame, columns=columns, show='headings')

# define headings
tree.heading('element', text='Chemical element')
tree.column('element', anchor=CENTER)
tree.heading('content', text='The percentage of the element in the composition')
tree.column('content', anchor=CENTER)

tree.pack(side = TOP, pady = 10, fill=X)

def clear_treeview():
    result_label.config(text = '* * *')

    for item in tree.get_children():
        tree.delete(item)
        global current_element
        current_element = []
        global current_element_percent
        current_element_percent = []

clear_button = Button(top_frame, text="Clear", command = clear_treeview)  
clear_button.pack(side = TOP, fill=X, padx = 10)

#Middle frame
middle_frame = Frame(window, width= 720, height = 210)
middle_frame.propagate(0)
middle_frame.pack(side=TOP, pady = 5, padx = 2)

#Middle label frame
middle_label_frame = LabelFrame(middle_frame, text="Add chemical element", padx=10, pady=10)
middle_label_frame.pack(fill="both", expand="yes")

method_label = Label(middle_label_frame, text = "Select the glass density calculation method")
method_label.pack(side=TOP, anchor = W)

winkelmann_schott_elements = [u'P\u2082O\u2085', u'SiO\u2082', u'B\u2082O\u2083',  
u'Al\u2082O\u2083', 'BaO', 'ZnO', 'PbO', u'Na\u2082O', u'K\u2082O', 'MgO', 'CaO']
winkelmann_schott_odds = [2.55, 2.30, 1.90, 4.10, 7.10, 5.00, 9.60, 2.60, 2.80, 3.80, 3.30]

tillotson_elements = [u'Al\u2082O\u2083', u'B\u2082O\u2083', 'BaO', 'CaO', u'Li\u2082O', 
'MgO', u'SiO\u2082', 'ZnO']
tillotson_odds = [2.75, 2.20, 7.00, 4.10, 3.70, 4.00, 2.30, 5.90]

belie_elements = [u'Al\u2082O\u2083', u'B\u2082O\u2083', 'BaO', 'CaO', u'K\u2082O', 
'MgO', u'Na\u2082O', 'PbO', u'Sb\u2082O\u2083', u'SiO\u2082']
belie_odds = [2.75, 2.90, 7.20, 4.30, 3.20, 3.60, 3.20, 10.30, 3.0, 2.20]

english_terner_elements = [u'Al\u2082O\u2083', 'CaO', 'MgO', 
u'Na\u2082O', u'SiO\u2082', 'ZnO']
english_terner_odds = [2.75, 5.00, 3.38, 3.47, 2.20, 7.50]

stuckert_elements = [u'Al\u2082O\u2083', u'B\u2082O\u2083', 'BaO', 'CaO', u'K\u2082O', u'Li\u2082O',
'MgO', 'MnO', u'Na\u2082O', u'P\u2082O\u2085', 'PbO', u'Sb\u2082O\u2083', u'SiO\u2082', 'ZnO']
stuckert_odds = [2.75, 2.90, 7.20, 4.30, 3.20, 3.70, 3.50, 4.65, 3.25, 2.55, 10.00, 3.00, 2.25, 5.90]

knapp_elements =  [u'Al\u2082O\u2083', 'BaO', 'BeO', 'CaO', u'K\u2082O',
'MgO', u'Na\u2082O', 'PbO', u'SiO\u2082', u'TiO\u2082', 'ZnO', u'ZrO\u2082']
knapp_odds = [0.02530, 0.04344, 0.02924, 0.03495, 0.02657, 0.02942, 0.02890, 0.04538, 0.02284, 0.03713, 0.04140, 0.04113]

huggins_elements = [u'Al\u2082O\u2083', u'B\u2082O\u2083 [BO\u2083]', u'B\u2082O\u2083 [BO\u2084]', 'BaO', 'BeO',
u'Bi\u2082O\u2083', 'CaO', 'CdO', u'Fe\u2082O\u2083', u'K\u2082O', u'Li\u2082O', 'MgO', u'Na\u2082O', 'PbO',
u'Rb\u2082O', u'SiO\u2082', 'SrO', u'Ta\u2082O\u2085', u'TiO\u2082', u'Tl\u2082O', 'ZnO', u'ZrO\u2082']

huggins_r_odds = [2.9429, 4.3079, 4.3079, 0.65206, 3.9970, 0.6438, 1.7832, 0.7786, 1.8785, 1.06171, 
3.3470, 2.4800, 1.6131, 0.44801, 0.53487, 3.3300, 0.96497, 1.5318, 2.5032, 0.23542, 1.2288, 1.6231]

huggins_v270_odds = [0.4620, 0.7910, 0.5900, 0.1420, 0.3480, 0.1050, 0.2850, 0.1380, 0.2820, 0.3900, 
0.4520, 0.3970, 0.3730, 0.1060, 0.2660, 0.4063, 0.2000, 0.1640, 0.3190, 0.1220, 0.2050, 0.2220]

huggins_v345_odds = [0.4180, 0.7270, 0.5260, 0.1320, 0.2890, 0.9580, 0.2590, 0.1260, 0.2550, 0.3740, 
0.4020, 0.3600, 0.3490, 0.0955, 0.2580, 0.4281, 0.1850, 0.1470, 0.2820, 0.1180, 0.1870, 0.1980]

huggins_v400_odds = [0.3730, 0.6610, 0.4600, 0.1220, 0.2270, 0.8580, 0.2310, 0.1140, 0.2250, 0.3570, 
0.3500, 0.3220, 0.3240, 0.0926, 0.2500, 0.4409, 0.1710, 0.1300, 0.2430, 0.1150, 0.1680, 0.1730]

huggins_v435_odds = [0.2940, 0.5460, 0.3450, 0.1040, 0.1200, 0.6870, 0.1840, 0.0935, 0.1760, 0.3290, 
0.2610, 0.2560, 0.2810, 0.0807, 0.2350, 0.4542, 0.1450, 0.0997, 0.1760, 0.1080, 0.1350, 0.1300]

demkina_elements = [u'Al\u2082O\u2083', u'As\u2082O\u2083', u'B\u2082O\u2083 [BO\u2084]', u'B\u2082O\u2083 [BO\u2083]', 'BaO',
'CaO', u'K\u2082O', 'MgO', u'Na\u2082O', 'PbO - I', 'PbO - II', 'PbO - III', u'Sb\u2082O\u2083', u'SiO\u2082 - I', 
u'SiO\u2082 - II', 'ZnO',]

demkina_p_odds = [2.50, 3.30, 2.95, 1.85, 8.10, 3.70, 2.95, 2.90, 3.05, 11.70, 10.20, 10.20, 5.60, 2.27, 2.20, 6.80]
demkina_s_odds = [59, 107, 43, 70, 213, 86, 94, 140, 62, 343, 223, 223, 154, 60, 60, 223]

gillar_dubrul_elements = [u'Al\u2082O\u2083', 'BaO', 'BeO', 'CaO - I', 'CaO - II', u'K\u2082O', 'MgO', u'Na\u2082O', 
'PbO', u'SiO\u2082', u'TiO\u2082', 'ZnO', u'ZrO\u2082']

gillar_dubrul_a_odds = [0.390, 0.100, 0.195, 0.175, 0.200, 0.333, 0.250, 0.286, 0.092, 0.454, 0.150, 0.160, 0.150]
gillar_dubrul_b_odds = [0, 0.001, 0.009, 0.002, 0.004, 0, 0.004, 0, 0, 0, 0.007, 0, 0.0025]

appen_elements = [u'Al\u2082O\u2083', u'B\u2082O\u2083', 'BaO', 'BeO', 'CaO', 'CdO', u'K\u2082O', 
u'Li\u2082O', 'MgO', u'Na\u2082O', 'PbO', u'SiO\u2082', 'SrO', u'TiO\u2082', 'ZnO']

appen_elements_weight = [101.96, 69.6182, 153.33, 25.01158, 56.0774, 128.4112, 94.2, 29.88, 
40.3044, 61.9789, 223.2, 60.08, 103.62, 79.866, 81.38]

appen_v_odds = [40.4, 38.0, 22.0, 7.8, 14.4, 18.2, 34.1, 11.0, 12.5, 20.2, 23.5, 27.25, 18.0, 20.5, 14.5]

def change_element_values(event):
    clear_treeview()
    element_box.set('')
    percent_entry.delete(0, 'end')

    element_box['state'] = 'normal'
    percent_entry['state'] = 'normal'
    
    if method_box.get() == "Winkelmann and Schott method":
        element_box['values'] = winkelmann_schott_elements

    elif method_box.get() == "Tillotson method":
        element_box['values'] = tillotson_elements

    elif method_box.get() == "Bellier Method":
        element_box['values'] = belie_elements

    elif method_box.get() == "English and Turner method":
        element_box['values'] = english_terner_elements

    elif method_box.get() == "Stuckert method":
        element_box['values'] = stuckert_elements

    elif method_box.get() == "Knapp method":
        element_box['values'] = knapp_elements

    elif method_box.get() == "Method M.L. Huggins":
        element_box['values'] = huggins_elements

    elif method_box.get() == "L.I. Demkin's method":
        element_box['values'] = demkina_elements

    elif method_box.get() == "Gillar and Dubrul's method":
        element_box['values'] = gillar_dubrul_elements

    elif method_box.get() == "A.A. Appen's method":
        element_box['values'] = appen_elements

method_box = ttk.Combobox(middle_label_frame, width = 30, values=["Winkelmann and Schott method", "Tillotson method", 
"Bellier Method", "English and Turner method", "Stuckert method", "Knapp method", "Method M.L. Huggins", "L.I. Demkin's method",
"Gillar and Dubrul's method", "A.A. Appen's method"])
method_box.bind("<<ComboboxSelected>>", change_element_values)
method_box.pack(side=TOP, anchor = W)

element_label = Label(middle_label_frame, text = "Choose a chemical element")
element_label.pack(side=TOP, anchor = W)

element_box = ttk.Combobox(middle_label_frame, width = 30, values=None, state='disabled')
element_box.pack(side=TOP, anchor = W)

percent_label = Label(middle_label_frame, text = "Enter the content of the selected element in the glass as a percentage")
percent_label.pack(side=TOP, anchor = W)

percent_entry = Entry(middle_label_frame, width=33, state='disabled')
percent_entry.pack(side=TOP, anchor = W)

current_element = []
current_element_percent = []

def add_element():
    element = element_box.get()
    percent = percent_entry.get()
    if element != "" and percent != "" and element != "You must select a method":
        current_element.append(element)
        current_element_percent.append(percent)

        tree.insert("", END, values=[element, percent])
        element_box.set('')
        percent_entry.delete(0, 'end')

confirm_button = Button(middle_label_frame, text="Add chemical element", command = add_element)  
confirm_button.pack(side=TOP, fill=X, pady = 10, anchor = W)

#Bottom frame
bottom_frame = Frame(window, width= 720, height = 130)
bottom_frame.propagate(0)
bottom_frame.pack(side=TOP, padx = 2)

bottom_label_frame = LabelFrame(bottom_frame, text="Calculation of glass density by its chemical composition", padx=10, pady=10)
bottom_label_frame.pack(fill="both", expand="yes")

result_label = Label(bottom_label_frame, text = "* * *")
result_label.pack(side = TOP, pady = 10)

def get_result():
    def fourth_formula_density(element_array, odds_array):
        sum = 0        
        current_odds = []
        for i in range(len(current_element)):
            for j in range(len(element_array)):
                if current_element[i] == element_array[j]:
                    current_odds.append(odds_array[j])

        for i in range(len(current_element_percent)):
            for j in range(len(current_odds)):
                if i==j:
                    sum += float(current_element_percent[i]) / current_odds[j]

        if sum != 0:
            density = 100 / sum
            result_label.config(text = 'The glass density is ' + str(round(density, 5)) + u' g/cm\u00B3')

    if method_box.get() == "Winkelmann and Schott method":
        fourth_formula_density(winkelmann_schott_elements, winkelmann_schott_odds)

    elif method_box.get() == "Tillotson method":
        fourth_formula_density(tillotson_elements, tillotson_odds)

    elif method_box.get() == "Bellier Method":
        fourth_formula_density(belie_elements, belie_odds)

    elif method_box.get() == "English and Turner method":
        fourth_formula_density(english_terner_elements, english_terner_odds)
        
    elif method_box.get() == "Stuckert method":
        fourth_formula_density(stuckert_elements, stuckert_odds)

    elif method_box.get() == "Knapp method":
        density = 0        
        current_odds = []
        for i in range(len(current_element)):
            for j in range(len(knapp_elements)):
                if current_element[i] == knapp_elements[j]:
                    current_odds.append(knapp_odds[j])

        for i in range(len(current_element_percent)):
            for j in range(len(current_odds)):
                if i==j:
                    density += float(current_element_percent[i]) * current_odds[j]

        result_label.config(text = 'The glass density is ' + str(round(density, 5)) + u' g/cm\u00B3')

    elif method_box.get() == "Method M.L. Huggins":
        L = 0
        sum = 0
        silica_percent = 0   
        current_odds = []

        for i in range(len(current_element)):
            if current_element[i] == u'SiO\u2082':
                silica_percent = float(current_element_percent[i])

        for i in range(len(current_element)):
            for j in range(len(huggins_elements)):
                if current_element[i] == huggins_elements[j]:
                    current_odds.append(huggins_r_odds[j] / 100)

        for i in range(len(current_element_percent)):
            for j in range(len(current_odds)):
                if i==j:
                    sum += float(current_element_percent[i]) * current_odds[j]

        L = silica_percent / (60.06 * sum)

        def huggins_density(array):
            sum = 0
            for i in range(len(current_element)):
                for j in range(len(huggins_elements)):
                    if current_element[i] == huggins_elements[j]:
                        sum += float(current_element_percent[i]) * array[j]

            density = 100 / sum
            result_label.config(text = 'The glass density is ' + str(round(density, 5)) + u' g/cm\u00B3')

        if L >= 0.270 and L < 0.345:
            huggins_density(huggins_v270_odds)

        elif L >= 0.345 and L < 0.400:
            huggins_density(huggins_v345_odds)     

        elif L >= 0.400 and L < 0.435:
            huggins_density(huggins_v400_odds)

        elif L >= 0.435 and L < 0.500:
            huggins_density(huggins_v435_odds)
    
    elif method_box.get() == "L.I. Demkin's method":

        sum_1 = 0
        sum_2 = 0
        current_s_odds = []
        current_p_odds = []
        for i in range(len(current_element)):
            for j in range(len(demkina_elements)):
                if current_element[i] == demkina_elements[j]:
                    current_p_odds.append(demkina_p_odds[j])
                    current_s_odds.append(demkina_s_odds[j])

        for i in range(len(current_element_percent)):
            sum_1 += (float(current_element_percent[i]) / current_s_odds[i]) * current_p_odds[i]
            sum_2 += float(current_element_percent[i]) / current_s_odds[i]

        density = sum_1 / sum_2

        result_label.config(text = 'The glass density is ' + str(round(density, 5)) + u' g/cm\u00B3')

    elif method_box.get() == "Gillar and Dubrul's method":

        sum_1 = 0
        sum_2 = 0
        current_a_odds = []
        current_b_odds = []
        for i in range(len(current_element)):
            for j in range(len(gillar_dubrul_elements)):
                if current_element[i] == gillar_dubrul_elements[j]:
                    current_a_odds.append(gillar_dubrul_a_odds[j])
                    current_b_odds.append(gillar_dubrul_b_odds[j])

        for i in range(len(current_element_percent)):
            sum_1 += float(current_element_percent[i])
            sum_2 += (current_a_odds[i] * float(current_element_percent[i])) + (current_b_odds[i] * float(current_element_percent[i]) * float(current_element_percent[i]))

        density = sum_1 / sum_2

        result_label.config(text = 'The glass density is ' + str(round(density, 5)) + u' g/cm\u00B3')

    elif method_box.get() == "A.A. Appen's method":

        sum = 0
        current_weight = []
        molar_mass = []
        current_odds = []
        for i in range(len(current_element)):
            for j in range(len(appen_elements)):
                if current_element[i] == appen_elements[j]:
                    current_weight.append(appen_elements_weight[j])
                    current_odds.append(appen_v_odds[j])

        for i in range(len(current_element_percent)):
            molar_mass.append(float(current_element_percent[i]) / current_weight[i])
        
        for i in range(len(molar_mass)):
            sum += molar_mass[i] * current_odds[i]

        density = 100 / sum

        result_label.config(text = 'The glass density is ' + str(round(density, 5)) + u' g/cm\u00B3')           

result_button = Button(bottom_label_frame, text="Calculate", command = get_result)  
result_button.pack(side = BOTTOM, fill=X, pady = 10)

window.mainloop()