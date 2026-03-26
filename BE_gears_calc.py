from tkinter import *
from tkinter import ttk


# ==========================================================================================
# КЛАССЫ
# Категории
class Cat:

    def __init__(self, outer_win, num):
        self.num = num
        self.name = f"Категория {self.num + 1}"
        self.type = "Обычное"

        self.frame = ttk.Frame(outer_win, borderwidth = 1, width = 300,
                               height = 170, relief = SOLID, padding = 4)

        self.numname_label = ttk.Label(self.frame, text = f"C{self.num} | {self.name}", width = 200)

        self.del_btn = ttk.Button(self.frame, text = "del", command = lambda: delete_cat(self.frame, self.num))

        self.name_label = ttk.Label(self.frame, text = f"Название категории:")

        self.name_entry = ttk.Entry(self.frame)
        self.name_entry.insert(0, self.name)

        self.type_text = ttk.Label(self.frame, text = f"\nТип снаряжения:")

        self.type_entry = ttk.Combobox(self.frame, state="readonly")
        self.type_entry["values"] = ("Обычное", "Боевое (сетовое)", "Персональное", "Командное")
        self.type_entry.current(0)
        self.type_entry.bind("<MouseWheel>", block_mousewheel)

        self.dev_type_label = ttk.Label(self.frame, text = f"Выбран тип: {self.type}")

        self.numname_label.pack(anchor=NW)
        self.del_btn.pack(anchor=NE)
        self.name_label.pack(anchor=NW)
        self.name_entry.pack(anchor=NW)
        self.type_text.pack(anchor=NW)
        self.type_entry.pack(anchor=NW)
        self.dev_type_label.pack(anchor=NW)
        self.frame.pack(anchor=NW, expand = False, padx=5, pady=5)
        self.frame.pack_propagate(False)

    def update(self, num):
        self.num = num
        self.name = self.name_entry.get()
        self.type = self.type_entry.get()
        self.numname_label["text"] = f"C{num} | {self.name}"
        self.del_btn["command"] = lambda: delete_cat(self.frame, self.num)
        self.dev_type_label["text"] = f"Выбран тип: {self.type}"

    def cat_redraw(self):
        self.numname_label.pack_forget()
        self.del_btn.pack_forget()
        self.name_label.pack_forget()
        self.name_entry.pack_forget()
        self.type_text.pack_forget()
        self.type_entry.pack_forget()
        self.dev_type_label.pack_forget()
        self.frame.pack_forget()

        self.numname_label.pack(anchor=NW)
        self.del_btn.pack(anchor=NE)
        self.name_label.pack(anchor=NW)
        self.name_entry.pack(anchor=NW)
        self.type_text.pack(anchor=NW)
        self.type_entry.pack(anchor=NW)
        self.dev_type_label.pack(anchor=NW)
        self.frame.pack(anchor=NW, expand = False, padx=5, pady=5)
        self.frame.pack_propagate(False)


# ==========================================================================================
# Класс для блоков
class Block:

    def __init__(self, outer_win, cat_num, num, type):
        global copies_data
        self.cat_num = cat_num
        self.num = num
        self.type = type
        self.name = f"Снаряжение {self.num + 1}"
        self.rang = "Обычное"
        self.copies = 0
        match self.type:
            case "Обычное":
                self.max_copies = copies_data[0][self.rang]
            case "Боевое (сетовое)":
                self.max_copies = copies_data[1][self.rang]
            case "Персональное":
                self.max_copies = copies_data[2][self.rang]
            case "Командное":
                self.max_copies = copies_data[2][self.rang]

        self.frame = ttk.Frame(outer_win, borderwidth = 1, width = 300,
                               height = 240, relief = SOLID, padding = 4)

        self.numname_label = ttk.Label(self.frame, text = f"C{cat_num} B{num} | {self.name}")

        self.del_btn = ttk.Button(self.frame, text = "del", command = lambda: delete_block(self.frame, self.cat_num, self.num))

        self.name_label = ttk.Label(self.frame, text = f"Название снаряжения:")

        self.name_entry = ttk.Entry(self.frame)
        self.name_entry.insert(0, self.name)

        self.rang_text = ttk.Label(self.frame, text = f"\nРанг прокачки:")

        self.rang_entry = ttk.Combobox(self.frame, state="readonly")
        self.rang_entry["values"] = ("Обычное", "Редкое", "Эпическое", "Легендарное", "Мифическое", "Высшее", "Ультимативное", "Небесное", "Звёздное", "Бессмертное", "Божественное")
        self.rang_entry.current(0)
        self.rang_entry.bind("<MouseWheel>", block_mousewheel)
        self.dev_rang_label = ttk.Label(self.frame, text = f"Выбран ранг: {self.rang}")

        self.copies_text = ttk.Label(self.frame, text = f"\nКол-во копий:")
        self.copies_entry = ttk.Entry(self.frame)
        self.copies_entry.insert(0, self.copies)
        self.dev_copies_label = ttk.Label(self.frame, text = f"Копии: {self.copies} / {self.max_copies}")


        self.numname_label.pack(anchor=NW)
        self.del_btn.pack(anchor=NE)
        self.name_label.pack(anchor=NW)
        self.name_entry.pack(anchor=NW)

        self.rang_text.pack(anchor=NW)
        self.rang_entry.pack(anchor=NW)
        self.dev_rang_label.pack(anchor=NW)

        self.copies_text.pack(anchor=NW)
        self.copies_entry.pack(anchor=NW)
        self.dev_copies_label.pack(anchor=NW)

        self.frame.pack(anchor=NW, expand = False, padx=35, pady=5)
        self.frame.pack_propagate(False)

    def update(self, cat_num = 999, num = 999, type = 999):
        if cat_num != 999:
            self.cat_num = cat_num
        if num != 999:
            self.num = num
        if type != 999:
            self.type = type
        self.name = self.name_entry.get()
        self.rang = self.rang_entry.get()
        self.copies = self.copies_entry.get()
        match self.type:
            case "Обычное":
                self.max_copies = copies_data[0][self.rang]
            case "Боевое (сетовое)":
                self.max_copies = copies_data[1][self.rang]
            case "Персональное":
                self.max_copies = copies_data[2][self.rang]
            case "Командное":
                self.max_copies = copies_data[2][self.rang]

        self.numname_label["text"] = f"C{self.cat_num} B{self.num} | {self.name}"
        self.del_btn["command"] = lambda: delete_block(self.frame, self.cat_num, self.num)
        self.dev_rang_label["text"] = f"Выбран ранг: {self.rang}"
        self.dev_copies_label["text"] = f"Копии: {self.copies} / {self.max_copies}"

    def block_redraw(self):
        self.numname_label.pack_forget()
        self.del_btn.pack_forget()
        self.name_label.pack_forget()
        self.name_entry.pack_forget()

        self.rang_text.pack_forget()
        self.rang_entry.pack_forget()
        self.dev_rang_label.pack_forget()

        self.copies_text.pack_forget()
        self.copies_entry.pack_forget()
        self.dev_copies_label.pack_forget()

        self.frame.pack_forget()


        self.numname_label.pack(anchor=NW)
        self.del_btn.pack(anchor=NE)
        self.name_label.pack(anchor=NW)
        self.name_entry.pack(anchor=NW)

        self.rang_text.pack(anchor=NW)
        self.rang_entry.pack(anchor=NW)
        self.dev_rang_label.pack(anchor=NW)

        self.copies_text.pack(anchor=NW)
        self.copies_entry.pack(anchor=NW)
        self.dev_copies_label.pack(anchor=NW)

        self.frame.pack(anchor=NW, expand = False, padx=35, pady=5)
        self.frame.pack_propagate(False)


# ==========================================================================================
# Класс - Кнопка нового блока
class BtnNewBlock:

    # Инициализация
    def __init__(self, outer_win, cat_num):
        self.cat_num = cat_num
        self.outer_win = outer_win

        self.btn = ttk.Button(self.outer_win,
                              text = "+ Новый блок",
                              command = lambda: create_block(self.outer_win, cat_num))
        self.btn.pack(anchor = NW, padx = 35)

    def update(self, cat_num):
        self.cat_num = cat_num

    # Перерисовать кнопку
    def btn_redraw(self):
        self.btn.pack_forget()
        self.btn = ttk.Button(self.outer_win,
                              text = "+ Новый блок",
                              command = lambda: create_block(self.outer_win, self.cat_num))
        self.btn.pack(anchor = NW, padx = 35)

    def btn_del(self):
        self.btn.pack_forget()


class Table:

    def __init__(self, outer_win, cat_num):
        global cats, blocks, copies_data, copies_data_sum
        self.cat_num = cat_num
        self.cat_name = cats[cat_num].name
        match cats[cat_num].type:
            case "Обычное":
                self.type = 0
            case "Боевое (сетовое)":
                self.type = 1
            case "Персональное":
                self.type = 2
            case "Командное":
                self.type = 2

        self.frame = ttk.Frame(outer_win, borderwidth = 1, width = 808,
                               height = 55 + len(blocks[cat_num]) * 20, relief = SOLID, padding = 4)

        self.catname_label = ttk.Label(self.frame, text = f"{self.cat_name} | Тип: {cats[cat_num].type} | Всего копий: ")

        self.columns = ("name", "now", "max", "total")
        self.tree = ttk.Treeview(self.frame, columns = self.columns, show = "headings", height = 30)

        self.tree.heading("name", text = "Название")
        self.tree.heading("now", text = "Сейчас")
        self.tree.heading("max", text = "Макс.")
        self.tree.heading("total", text = "Всего")
        self.tree.column(f"#1", stretch=NO, width=200)
        self.tree.column(f"#2", stretch=NO, width=200)
        self.tree.column(f"#3", stretch=NO, width=200)
        self.tree.column(f"#4", stretch=NO, width=200)

        self.data = []
        self.cat_total_copies = 0
        for i in range(len(blocks[cat_num])):
            match blocks[cat_num][i].rang:
                case "Обычное":
                    self.rang = 0
                case "Редкое":
                    self.rang = 1
                case "Эпическое":
                    self.rang = 2
                case "Легендарное":
                    self.rang = 3
                case "Мифическое":
                    self.rang = 4
                case "Высшее":
                    self.rang = 5
                case "Ультимативное":
                    self.rang = 6
                case "Небесное":
                    self.rang = 7
                case "Звёздное":
                    self.rang = 8
                case "Бессмертное":
                    self.rang = 9
                case "Божественное":
                    self.rang = 10
            self.total_copies = copies_data_sum[self.type][self.rang] + int(blocks[cat_num][i].copies)
            self.total_percent = round((self.total_copies / copies_data_sum[self.type][10]) * 100, 2)
            for j in range(10, -1, -1):
                if self.total_copies >= copies_data_sum[self.type][j]:
                    self.k = j
                    break
            
            self.data.append((blocks[cat_num][i].name,
                              f"{blocks[cat_num][i].rang} | Копии: {blocks[cat_num][i].copies} / {blocks[cat_num][i].max_copies}",
                              f"{list(copies_data[self.type].keys())[self.k]} | Копии: {self.total_copies - copies_data_sum[self.type][self.k]} / {list(copies_data[self.type].values())[self.k]}",
                              f"{self.total_copies} / {copies_data_sum[self.type][10]} | {self.total_percent}%"))
            self.cat_total_copies += self.total_copies
        self.cat_total_percent = round((self.cat_total_copies / (copies_data_sum[self.type][10] * len(blocks[cat_num]))) * 100, 2)
        self.catname_label["text"] = f"{self.cat_name} | Тип: {cats[cat_num].type} | Всего копий: {self.cat_total_copies} / {copies_data_sum[self.type][10] * len(blocks[cat_num])} ({self.cat_total_percent}%)"

        for rows in self.data:
            self.tree.insert("", END, values = rows)

        self.catname_label.pack(anchor = NW)
        self.tree.pack(anchor = NW, expand = True)
        self.frame.pack(anchor = NW, expand = True, padx=5, pady=5)
        self.frame.pack_propagate(False)

    def table_redraw(self):
        self.catname_label.pack_forget()
        self.tree.pack_forget()
        self.frame.pack_forget()

        self.catname_label.pack(anchor=NW)
        self.tree.pack(anchor = NW, expand = True)
        self.frame.pack(anchor=NW, expand = True, padx=5, pady=5)
        self.frame.pack_propagate(False)

    


# ==========================================================================================
# ФУНКЦИИ
def create_cat(outer_win):
    global cats, new_cat_btn, new_block_btn
    cat_num = len(cats)

    cats.append(Cat(outer_win, cat_num))

    blocks.append([])
    blocks[cat_num].append(Block(outer_win, cat_num, len(blocks[cat_num]), "Обычное"))

    new_block_btn.append(BtnNewBlock(second_frame, cat_num))

    redraw()
    dev()

def delete_cat(frame, num):
    global cats, blocks, new_block_btn

    while len(blocks[num]) != 0:
        delete_block(blocks[num][0].frame, num, 0)
    del blocks[num]
    for i in range(len(blocks)):
        for j in range(len(blocks[i])):
            blocks[i][j].update(cat_num = i, num = j)

    new_block_btn[num].btn_del()
    del new_block_btn[num]
    for i in range(len(new_block_btn)):
        new_block_btn[i].update(i)

    frame.pack_forget()
    del cats[num]
    for j in range(len(cats)):
        cats[j].update(j)

    redraw()
    dev()

def create_block(outer_win, cat_num):
    global cats, blocks, new_block_btn
    blocks.append([])
    blocks[cat_num].append(Block(outer_win, cat_num, len(blocks[cat_num]), cats[cat_num].type))
    redraw()
    dev()

def delete_block(frame, cat_num, num):
    global blocks
    del blocks[cat_num][num]
    for j in range(0, len(blocks[cat_num])):
        blocks[cat_num][j].update(num = j)
    frame.pack_forget()
    redraw()
    dev()

def generate_table():
    global cats, tables, second_frame

    while len(tables) != 0:
        tables[0].frame.pack_forget()
        del tables[0]
    
    for i in range(len(cats)):
        tables.append(Table(second_frame, i))

    redraw()
    dev()

def redraw():
    global cats, blocks, tables, new_cat_btn, new_block_btn, interlude_text, redraw_btn

    for i in range(4):
        interlude_text[i].pack_forget()
        if i == 2:
            interlude_text[i].pack(anchor = NW, fill = X)
        else:
            interlude_text[i].pack(anchor = NW)

    for i in range(len(cats)):
        cats[i].update(i)
        cats[i].cat_redraw()
        for j in range(len(blocks[i])):
            blocks[i][j].update(type = cats[i].type)
            blocks[i][j].block_redraw()
        new_block_btn[i].btn_redraw()
    new_cat_btn.pack_forget()
    new_cat_btn.pack(anchor=NW)

    interlude_text[4].pack_forget()
    interlude_text[4].pack(anchor = NW)
    redraw_btn.pack_forget()
    redraw_btn.pack(anchor = NW)
    for i in range(5, 8):
        interlude_text[i].pack_forget()
        if i == 6:
            interlude_text[i].pack(anchor = NW, fill = X)
        else:
            interlude_text[i].pack(anchor = NW)
    generate_btn.pack_forget()
    generate_btn.pack(anchor = NW)
    for i in range(len(tables)):
        tables[i].table_redraw()
    for i in range(8, 11):
        interlude_text[i].pack_forget()
        if i == 9:
            interlude_text[i].pack(anchor = NW, fill = X)
        else:
            interlude_text[i].pack(anchor = NW)

def block_mousewheel(event):
    return "break"

def dev():
    print("================================")
    for i in range(len(cats)):
        print(f"Cat {i}\nBlocks ", end="")
        for j in range(len(blocks[i])):
            print(j, end=" ")
        print()
    print(f"Tables ", end="")
    for i in range(len(tables)):
        print(i, end=" ")
    print()


# ==========================================================================================
# MAIN
root = Tk()
root.title("BE - Калькулятор снаряжения")
root.state('zoomed')

main_frame = ttk.Frame(root)
main_frame.pack(fill=BOTH, expand=1)

# canvas
my_canvas = Canvas(main_frame)
my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

# scrollbar
my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
my_scrollbar.pack(side=RIGHT, fill=Y)

# configure the canvas
my_canvas.configure(yscrollcommand=my_scrollbar.set)

second_frame = ttk.Frame(my_canvas, padding = 10)
canvas_window = my_canvas.create_window((0, 0), window=second_frame, anchor="nw")

def update_scrollregion(event):
    my_canvas.configure(scrollregion=my_canvas.bbox("all"))

second_frame.bind("<Configure>", update_scrollregion)

def on_canvas_resize(event):
    my_canvas.itemconfig(canvas_window, width=event.width)

my_canvas.bind("<Configure>", on_canvas_resize)

def on_mouse_wheel(event):
    # Windows / macOS
    my_canvas.yview_scroll(int(-event.delta / 120), "units")

def on_mouse_wheel_linux(event):
    # Linux: event.num == 4 (вверх), 5 (вниз)
    if event.num == 4:
        my_canvas.yview_scroll(-1, "units")
    elif event.num == 5:
        my_canvas.yview_scroll(1, "units")

# Привязываем события к корневому окну (работает везде)
root.bind_all("<MouseWheel>", on_mouse_wheel)          # Windows, macOS
root.bind_all("<Button-4>", on_mouse_wheel_linux)      # Linux (вверх)
root.bind_all("<Button-5>", on_mouse_wheel_linux)      # Linux (вниз)


cats = []
blocks = [[]]
tables = []
new_cat_btn = ttk.Button(second_frame, text="+ Новая категория", command = lambda: create_cat(second_frame))
new_block_btn = []
redraw_btn = ttk.Button(second_frame, text="Обновление", command = redraw)
generate_btn = ttk.Button(second_frame, text="Сгенерировать отчёт", command = generate_table)

copies_data = [0] * 3
copies_data[0] = {"Обычное": 4, "Редкое": 8, "Эпическое": 18, "Легендарное": 50,
                  "Мифическое": 140, "Высшее": 240, "Ультимативное": 350,
                  "Небесное": 470, "Звёздное": 590, "Бессмертное": 790, "Божественное": 0}
copies_data[1] = {"Обычное": 2, "Редкое": 9, "Эпическое": 19, "Легендарное": 40,
                  "Мифическое": 95, "Высшее": 150, "Ультимативное": 210,
                  "Небесное": 285, "Звёздное": 370, "Бессмертное": 470, "Божественное": 0}
copies_data[2] = {"Обычное": 2, "Редкое": 5, "Эпическое": 10, "Легендарное": 20,
                  "Мифическое": 30, "Высшее": 40, "Ультимативное": 45,
                  "Небесное": 50, "Звёздное": 55, "Бессмертное": 60, "Божественное": 0}
copies_data_sum = [0] * 3
copies_data_sum[0] = (0, 4, 12, 30, 80, 220, 460, 810, 1280, 1870, 2660)
copies_data_sum[1] = (0, 2, 11, 30, 70, 165, 315, 525, 810, 1180, 1650)
copies_data_sum[2] = (0, 2, 7, 17, 37, 67, 107, 152, 202, 257, 317)

interlude_text = [0] * 11
interlude_text[0] = ttk.Label(second_frame, text = "Калькулятор снаряжения", font = ("Arial", 21))
interlude_text[1] = ttk.Label(second_frame, text = "Программа для расчёта прокачки снаряжения в Bullet Echo. Перед работой ознакомьтесь с файлом README.txt\n", font = ("Arial", 10))
interlude_text[2] = ttk.Frame(second_frame, height = 2, borderwidth = 1, relief = SOLID)
interlude_text[3] = ttk.Label(second_frame, text = "\n1. Для ввода данных создайте несколько категорий. В каждой из них только один тип снаряжения (обычное / сетовое и т.д.)" + 
                                                   "\n2. Используйте категории для группирования (например, обычная снаряга 1-ый слот)" +
                                                   "\n3. Внутри категорий создайте блоки. Каждый блок это одно снаряжение. " +
                                                   "\n4. Вводите редкость и копии как они отображаются в игре.\n", font = ("Arial", 10))
interlude_text[4] = ttk.Label(second_frame, text = "\nЕсли данные не обновились, нажмите на кнопку.", font = ("Arial", 10))
interlude_text[5] = ttk.Label(second_frame, text = "\n", font = ("Arial", 5))
interlude_text[6] = ttk.Frame(second_frame, height = 2, borderwidth = 1, relief = SOLID)
interlude_text[7] = ttk.Label(second_frame, text = "\nДля итогового подсчёта прокачки используйте кнопку. Убедитесь, что данные обновлены и введены корректно.", font = ("Arial", 10))
interlude_text[8] = ttk.Label(second_frame, text = "\n", font = ("Arial", 5))
interlude_text[9] = ttk.Frame(second_frame, height = 2, borderwidth = 1, relief = SOLID)
interlude_text[10] = ttk.Label(second_frame, text = "\nВерсия приложения: v 1.0  –  Дата обновления: 26.03.2026" + 
                                                    "\nОфициальным источником является только репозиторий https://github.com/Detonator2103/BE-gears-calc. Следите за обновлениями." + 
                                                    "\n\nЭто фанатский проект, ZeptoLab не имеет отношения к разработке и распространению." +
                                                    "\nПо вопросам, репорту багов и предложениям обращайтесь к @Deto21 (телеграм, https://t.me/Deto21), либо используйте ветку issues в репозитории ГитХаба." + 
                                                    "\nПодробнее в файле README.txt", font = ("Arial", 8))


for i in range(4):
    if i == 2:
        interlude_text[i].pack(anchor = NW, fill = X)
    else:
        interlude_text[i].pack(anchor = NW)
new_cat_btn.pack(anchor=NW)
interlude_text[4].pack(anchor = NW)
redraw_btn.pack(anchor = NW)
for i in range(5, 8):
    if i == 6:
        interlude_text[i].pack(anchor = NW, fill = X)
    else:
        interlude_text[i].pack(anchor = NW)
generate_btn.pack(anchor = NW)
for i in range(8, 11):
    if i == 9:
        interlude_text[i].pack(anchor = NW, fill = X)
    else:
        interlude_text[i].pack(anchor = NW)

root.mainloop()