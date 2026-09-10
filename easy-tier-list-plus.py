import customtkinter
import tkinter
import tkinter.font
from tkinter import colorchooser
from PIL import Image, ImageTk, ImageGrab
from CTkMenuBar import *
from tkinter import filedialog
from CTkMessagebox import *
from tkinterdnd2 import TkinterDnD, DND_ALL
import os
from urllib.request import urlopen
import io
import json
import shutil
import random
import sys
import base64
import tempfile
import atexit
import time

platform = sys.platform
if platform.startswith("win"):
    try:
        import pywinstyles
    except ImportError:
        pywinstyles = None
else:
    pywinstyles = None

customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("blue")
customtkinter.set_widget_scaling(1.0)
customtkinter.set_window_scaling(1.0)
customtkinter.deactivate_automatic_dpi_awareness()


T = {
    "en": {
        "title": "Easy-Tier-List-Plus",
        "file": "File", "add_cat": "Add Category", "add_content": "Add Content",
        "settings": "Settings",
        "open": "Open", "save": "Save",
        "save_json": "JSON (no images)", "save_json_img": "JSON + images",
        "save_tierlist": "Tierlist (.tierlist)", "save_png": "Screenshot (image)",
        "font": "Font", "theme": "Theme", "img_size_global": "Image size (global)",
        "fullscreen": "Fullscreen", "language": "Language", "about": "About",
        "russian": "Русский", "english": "English",
        "ok": "OK", "cancel": "Cancel", "yes": "Yes", "no": "No",
        "error": "Error", "done": "Done!", "duplicate": "Duplicate",
        "dup_img": "This image is already added.",
        "no_assets": "No assets", "no_assets_msg": "Images folder is missing!",
        "invalid": "Invalid file", "invalid_msg": "This file is not compatible!",
        "img_size": "Image size", "orig_size": "Original size",
        "size_px": "Size (px):", "caption": "Caption",
        "enter_caption": "Enter caption (can be empty):",
        "enter_caption2": "Enter caption:", "url": "URL",
        "paste_url": "Paste URL", "text": "Text", "enter_text": "Enter text:",
        "no_clipboard": "No image in clipboard.",
        "no_recognize": "Failed to recognize image.",
        "load_err": "Failed to load image.",
        "add_images": "Add images", "add_url": "Add by URL",
        "add_text": "Add text", "paste_clip": "Paste from clipboard",
        "import": "IMPORT", "cat_name": "Category name", "color": "Color",
        "add_cat_title": "Add Category", "edit_cat_title": "Edit Category",
        "choose_cat_color": "Choose category color",
        "del_cat": "Delete category", "clear": "Clear list",
        "move_up": "Move up", "move_down": "Move down",
        "config": "Configure", "del_q": "Delete?",
        "del_cat_q": "Delete this category?\n(Irreversible)", "saved_json": "Saved to JSON:\n",
        "saved_tierlist": "Tierlist saved:\n", "saved_png": "Screenshot saved:\n",
        "exit": "Exit", "exit_q": "Do you want to close the program?",
        "edit_caption": "Edit caption", "enter_new_caption": "Enter new caption:",
        "view_img": "View image", "set_size": "Set size...",
        "edit_text": "Edit text", "enter_new_text": "Enter new text:",
        "delete": "Delete", "cant_open": "Failed to open image.",
        "view": "View", "close": "Close",
        "global_size": "Global image size", "current_size": "Current size: ",
        "font_size": "Font and size", "size": "Size",
        "bold": "Bold", "italic": "Italic", "underline": "Underline",
        "color_scheme": "Color scheme", "cat_color": "Category color",
        "main_bg": "Main background", "txt_color": "Text color",
        "choose_cat_bg": "Choose category background color",
        "choose_main_bg": "Choose main background color",
        "choose_txt": "Choose text color", "no_caption": "(no caption)",
        "original": "original", "tierlist": "TIERLIST",
        "exporting": "Exporting...",
        "about_text": (
            "Easy-Tier-List-Plus\n"
            "Original author: Akash Bora\n"
            "Mod author: mreliseyyt\n"
            "Version: 1.0\n"
            "License: MIT\n\n"
            "MOD FEATURES:\n"
            "• Image captions\n"
            "• Double-click to view image in full size\n"
            "• Individual image size (original / custom px)\n"
            "• Paste image from clipboard\n"
            "• Save entire tierlist as .tierlist (Base64 embedded)\n"
            "• Horizontal scroll inside every category\n"
            "• Drag & Drop items between categories\n"
            "• Delete items via right-click or Del key\n"
            "• Export full tierlist (all categories) to PNG\n"
            "• Global image size slider\n"
            "• Custom font (family, size, bold, italic, underline)\n"
            "• Custom color scheme (categories / background / text)\n"
            "• Two languages: English / Русский"
        ),
    },
    "ru": {
        "title": "Easy-Tier-List-Plus",
        "file": "Файл", "add_cat": "Добавить категорию", "add_content": "Добавить контент",
        "settings": "Настройки",
        "open": "Открыть", "save": "Сохранить",
        "save_json": "JSON (без изображений)", "save_json_img": "JSON + изображения",
        "save_tierlist": "Тирлист (.tierlist)", "save_png": "Скриншот (изображение)",
        "font": "Шрифт", "theme": "Тема", "img_size_global": "Размер изображений (глобальный)",
        "fullscreen": "Полный экран", "language": "Язык", "about": "О программе",
        "russian": "Русский", "english": "English",
        "ok": "ОК", "cancel": "Отмена", "yes": "Да", "no": "Нет",
        "error": "Ошибка", "done": "Готово!", "duplicate": "Дубликат",
        "dup_img": "Это изображение уже добавлено.",
        "no_assets": "Нет ресурсов", "no_assets_msg": "Папка с изображениями отсутствует!",
        "invalid": "Неверный файл", "invalid_msg": "Этот файл не совместим!",
        "img_size": "Размер изображения", "orig_size": "Оригинальный размер",
        "size_px": "Размер (пикселей):", "caption": "Подпись",
        "enter_caption": "Введите подпись (можно оставить пустым):",
        "enter_caption2": "Введите подпись:", "url": "Ссылка",
        "paste_url": "Вставьте ссылку", "text": "Текст", "enter_text": "Введите текст:",
        "no_clipboard": "В буфере нет изображения.",
        "no_recognize": "Не удалось распознать изображение.",
        "load_err": "Не удалось загрузить изображение.",
        "add_images": "Добавить изображения", "add_url": "Добавить по ссылке",
        "add_text": "Добавить текст", "paste_clip": "Вставить из буфера",
        "import": "ИМПОРТ", "cat_name": "Название категории", "color": "Цвет",
        "add_cat_title": "Добавить категорию", "edit_cat_title": "Редактировать категорию",
        "choose_cat_color": "Выберите цвет категории",
        "del_cat": "Удалить категорию", "clear": "Очистить список",
        "move_up": "Переместить вверх", "move_down": "Переместить вниз",
        "config": "Настроить", "del_q": "Удаление?",
        "del_cat_q": "Удалить категорию?\n(Процесс необратим)", "saved_json": "Данные сохранены в JSON:\n",
        "saved_tierlist": "Тирлист сохранён:\n", "saved_png": "Скриншот сохранён:\n",
        "exit": "Выход", "exit_q": "Вы хотите закрыть программу?",
        "edit_caption": "Редактировать подпись", "enter_new_caption": "Введите новую подпись:",
        "view_img": "Просмотреть изображение", "set_size": "Установить размер...",
        "edit_text": "Редактировать текст", "enter_new_text": "Введите новый текст:",
        "delete": "Удалить", "cant_open": "Не удалось открыть изображение.",
        "view": "Просмотр", "close": "Закрыть",
        "global_size": "Глобальный размер изображений", "current_size": "Текущий размер: ",
        "font_size": "Шрифт и размер", "size": "Размер",
        "bold": "Жирный", "italic": "Курсив", "underline": "Подчёркнутый",
        "color_scheme": "Цветовая схема", "cat_color": "Цвет категорий",
        "main_bg": "Основной фон", "txt_color": "Цвет текста",
        "choose_cat_bg": "Выберите цвет фона категорий",
        "choose_main_bg": "Выберите цвет основного фона",
        "choose_txt": "Выберите цвет текста", "no_caption": "(без подписи)",
        "original": "оригинал", "tierlist": "ТИРЛИСТ",
        "exporting": "Экспорт...",
        "about_text": (
            "Easy-Tier-List-Plus\n"
            "Автор оригинала: Akash Bora\n"
            "Автор мода: mreliseyyt\n"
            "Версия: 1.0\n"
            "Лицензия: MIT\n\n"
            "ВОЗМОЖНОСТИ МОДА:\n"
            "• Подписи к изображениям\n"
            "• Просмотр изображения в полном размере (двойной клик)\n"
            "• Индивидуальный размер каждого изображения (оригинал / свой в px)\n"
            "• Вставка изображения из буфера обмена\n"
            "• Сохранение тирлиста в один .tierlist (Base64 внутри)\n"
            "• Горизонтальная прокрутка внутри каждой категории\n"
            "• Перетаскивание элементов между категориями (Drag & Drop)\n"
            "• Удаление элементов правым кликом или клавишей Del\n"
            "• Экспорт ВСЕГО тирлиста (все категории) в PNG\n"
            "• Ползунок глобального размера изображений\n"
            "• Настройка шрифта (семейство, размер, жирный, курсив, подчёркнутый)\n"
            "• Настройка цветовой схемы (категории / фон / текст)\n"
            "• Два языка: English / Русский"
        ),
    },
}


def pick_color(title, initial=None):
    result = colorchooser.askcolor(color=initial, title=title)
    if result and result[1]:
        return result[1]
    return None


def image_is_black(img, threshold=10):
    try:
        small = img.convert("RGB").resize((40, 40))
        data = small.tobytes()
        if not data:
            return True
        avg = sum(data) / len(data)
        return avg < threshold
    except:
        return False


class CTk(customtkinter.CTk, TkinterDnD.DnDWrapper):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.TkdndVersion = TkinterDnD._require(self)


class App(CTk):
    def __init__(self):
        super().__init__()
        self.geometry("1000x800")

        self.temp_dir = tempfile.mkdtemp(prefix="tierlist_temp_")
        atexit.register(self.cleanup_temp)

        self.thumb_size = 100
        self.category_height = 140

        self.lang = "en"

        self.drag_active = False
        self.drag_pending = False
        self.drag_item = None
        self.drag_clone = None
        self.drag_widget = None
        self.drag_start_x = 0
        self.drag_start_y = 0

        self.protocol("WM_DELETE_WINDOW", self.ask_leave)

        self.bind("<B1-Motion>", self.on_drag_motion, add="+")
        self.bind("<ButtonRelease-1>", self.on_drag_release, add="+")

        self.frame_color = self._apply_appearance_mode(
            customtkinter.ThemeManager.theme["CTkFrame"]["top_fg_color"])
        self.frame_color2 = self._apply_appearance_mode(
            customtkinter.ThemeManager.theme["CTkFrame"]["fg_color"])
        self.theme_colors = {"bg": self.frame_color2, "fg": self.frame_color, "txt": "black"}

        self.font_data = {"family": "default", "size": 15, "weight": 0, "slant": 0, "underline": 0}
        self.global_font = customtkinter.CTkFont()

        self.blocks = {
            "S": {"fg": "#fe7e7e", "content": []},
            "A": {"fg": "#ffbf7f", "content": []},
            "B": {"fg": "#ffdf7f", "content": []},
            "C": {"fg": "#ffff7f", "content": []},
            "D": {"fg": "#bfff7f", "content": []},
            "E": {"fg": "#7fff7f", "content": []},
            "ALL": {"content": []}
        }

        self.frame_data = []
        self.menu_bar = None

        self.create_menu()

        self.main_scroll = customtkinter.CTkScrollableFrame(self, fg_color=self.frame_color2)
        self.main_scroll.pack(padx=10, pady=10, fill="both", expand=True)

        self.bg_frame = customtkinter.CTkFrame(self.main_scroll, fg_color=self.frame_color2)
        self.bg_frame.pack(fill="both", expand=True)

        for i in self.blocks:
            if i != "ALL":
                self.make_category(i, self.blocks[i]["fg"])

        self.update_global_font()

        self.content_frame = customtkinter.CTkScrollableFrame(
            self.main_scroll, height=150, orientation="horizontal",
            label_text=self.t("tierlist"), fg_color=self.frame_color2)
        self.content_frame.pack(fill="x", pady=(5, 0))
        self.blocks["ALL"]["frame"] = self.content_frame
        self.blocks["ALL"]["scroll"] = self.content_frame

        self.drop_target_register(DND_ALL)
        self.dnd_bind("<<Drop>>", self.dropped_content)

        self.fullscreen = False

        self.bind("<Escape>", lambda e: self.disable_fullscreen())
        self.bind("<F11>", lambda e: self.toggle_fullscreen())
        self.bind("<n>", lambda e: self.new_category())
        self.bind("<f>", lambda e: self.adjust_font())
        self.bind("<Control-s>", lambda e: self.save_template())
        self.bind("<Control-o>", lambda e: self.open_template())
        self.bind("<t>", lambda e: self.adjust_theme())
        self.bind("<space>", lambda e: self.edit_content())

        self.title(self.t("title"))

    def t(self, key):
        return T.get(self.lang, T["en"]).get(key, key)

    def create_menu(self):
        has_scroll = hasattr(self, "main_scroll") and self.main_scroll is not None
        if has_scroll:
            try:
                self.main_scroll.pack_forget()
            except:
                pass

        if self.menu_bar is not None:
            try:
                self.menu_bar.destroy()
            except:
                pass
            self.menu_bar = None

        menu = CTkMenuBar(self)
        self.menu_bar = menu

        btn_file = menu.add_cascade(self.t("file"))
        menu.add_cascade(self.t("add_cat"), command=lambda: self.new_category())
        menu.add_cascade(self.t("add_content"), command=lambda: self.edit_content())
        btn_settings = menu.add_cascade(self.t("settings"))

        dd_file = CustomDropdownMenu(widget=btn_file, corner_radius=4, width=200)
        dd_file.add_option(option=self.t("open"), command=lambda: self.open_template())
        sub_save = dd_file.add_submenu(self.t("save"))
        sub_save.add_option(option=self.t("save_json"), command=lambda: self.save_template())
        sub_save.add_option(option=self.t("save_json_img"), command=lambda: self.save_template(copy=True))
        sub_save.add_option(option=self.t("save_tierlist"), command=lambda: self.save_tierlist())
        sub_save.add_option(option=self.t("save_png"), command=lambda: self.export_image())

        dd_set = CustomDropdownMenu(widget=btn_settings, corner_radius=4, width=220)
        dd_set.add_option(option=self.t("font"), command=lambda: self.adjust_font())
        dd_set.add_option(option=self.t("theme"), command=lambda: self.adjust_theme())
        dd_set.add_option(option=self.t("img_size_global"), command=lambda: self.adjust_thumb_size())
        dd_set.add_option(option=self.t("fullscreen"), command=lambda: self.toggle_fullscreen())
        sub_lang = dd_set.add_submenu(self.t("language"))
        sub_lang.add_option(option=self.t("english"), command=lambda: self.set_language("en"))
        sub_lang.add_option(option=self.t("russian"), command=lambda: self.set_language("ru"))
        dd_set.add_option(option=self.t("about"), command=lambda: self.show_about())

        if has_scroll:
            self.main_scroll.pack(padx=10, pady=10, fill="both", expand=True)

    def set_language(self, lang):
        if lang not in T:
            return
        self.lang = lang
        self.title(self.t("title"))
        try:
            self.content_frame.configure(label_text=self.t("tierlist"))
        except:
            pass
        self.create_menu()

    def cleanup_temp(self):
        try:
            shutil.rmtree(self.temp_dir)
        except:
            pass

    def is_text_item(self, item):
        return isinstance(item, dict) and item.get("type") == "text"

    def is_image_item(self, item):
        return isinstance(item, dict) and item.get("type") == "image"

    def open_template(self, saved_data=False):
        if not saved_data:
            saved_data = {}
            for i in self.blocks:
                saved_data[i] = self.blocks[i]

            open_json = filedialog.askopenfilename(
                filetypes=[("Tierlist", "*.tierlist"), ("JSON", "*.json"), ("All files", "*.*")])
            if open_json:
                try:
                    with open(open_json, encoding='utf-8') as f:
                        data = json.load(f)
                except Exception as e:
                    CTkMessagebox(self, title=self.t("error"), message=str(e), icon="cancel")
                    return
                if "images_base64" in data:
                    self.load_tierlist_data(data, open_json)
                    return
                else:
                    self.blocks = data
            else:
                return
        else:
            self.blocks = saved_data

        self._load_json_data(open_json if 'open_json' in locals() else None)

    def _load_json_data(self, file_path):
        if "lang" in self.blocks:
            self.lang = self.blocks["lang"]
            del self.blocks["lang"]
            self.title(self.t("title"))
            self.create_menu()
            try:
                self.content_frame.configure(label_text=self.t("tierlist"))
            except:
                pass

        for cat in self.blocks:
            if cat != "ALL" and "content" in self.blocks[cat]:
                new_content = []
                for item in self.blocks[cat]["content"]:
                    if isinstance(item, str):
                        if item.startswith("TEXT:"):
                            new_content.append({"type": "text", "text": item[5:]})
                        else:
                            new_content.append({"type": "image", "path": item, "caption": "",
                                                "custom_size": None, "use_original": False})
                    else:
                        new_content.append(item)
                self.blocks[cat]["content"] = new_content

        asset_folder = None
        if "DATAPATH" in self.blocks:
            asset_folder = os.path.join(os.path.dirname(file_path), self.blocks["DATAPATH"])
            del self.blocks["DATAPATH"]
            if not os.path.exists(asset_folder):
                CTkMessagebox(self, title=self.t("no_assets"), message=self.t("no_assets_msg"), icon="cancel")

        self.font_data = {"family": "default", "size": 15, "weight": 0, "slant": 0, "underline": 0}
        if "font" in self.blocks:
            self.font_data = self.blocks["font"]
            del self.blocks["font"]
        self.update_global_font()

        self.frame_color = self._apply_appearance_mode(
            customtkinter.ThemeManager.theme["CTkFrame"]["top_fg_color"])
        self.theme_colors = {"bg": self.frame_color2, "fg": self.frame_color, "txt": "black"}
        if "theme" in self.blocks:
            self.theme_colors = self.blocks["theme"]
            del self.blocks["theme"]

        for i in self.frame_data:
            i.destroy()
        self.frame_data = []

        try:
            for i in self.blocks:
                if i != "ALL":
                    self.make_category(i, self.blocks[i]["fg"])

            for child in self.content_frame.winfo_children():
                child.destroy()

            for cat_name, cat_data in self.blocks.items():
                if cat_name == "ALL":
                    continue
                scroll = self.blocks[cat_name].get("scroll")
                if scroll is None:
                    continue
                new_list = []
                for item in cat_data["content"]:
                    if self.is_text_item(item):
                        new_list.append(item)
                        self.new_content(item, frame=scroll, add_to_data=False)
                    elif self.is_image_item(item):
                        path = item.get("path", "")
                        if asset_folder and not os.path.isabs(path):
                            path = os.path.join(asset_folder, path)
                        item["path"] = path
                        new_list.append(item)
                        self.new_content(item, frame=scroll, add_to_data=False)
                self.blocks[cat_name]["content"] = new_list

            self.update_colors()
            self.content_frame.configure(
                label_text=os.path.basename(file_path).split(".")[0] if file_path else self.t("tierlist"))
        except Exception:
            self.blocks = {"ALL": {"content": []}}
            CTkMessagebox(self, title=self.t("invalid"), message=self.t("invalid_msg"), icon="cancel")

    def load_tierlist_data(self, data, file_path):
        image_map = {}
        if "images_base64" in data:
            for filename, b64_str in data["images_base64"].items():
                try:
                    img_data = base64.b64decode(b64_str)
                    temp_path = os.path.join(self.temp_dir, filename)
                    with open(temp_path, "wb") as f:
                        f.write(img_data)
                    image_map[filename] = temp_path
                except:
                    pass
            del data["images_base64"]

        for cat_name, cat_data in data.items():
            if cat_name in ("font", "theme", "lang"):
                continue
            if "content" not in cat_data:
                continue
            new_content = []
            for item in cat_data["content"]:
                if isinstance(item, str):
                    if item.startswith("TEXT:"):
                        new_content.append({"type": "text", "text": item[5:]})
                    else:
                        p = image_map.get(item, item)
                        new_content.append({"type": "image", "path": p, "caption": "",
                                            "custom_size": None, "use_original": False})
                elif isinstance(item, dict):
                    if self.is_image_item(item) and item.get("path") in image_map:
                        item["path"] = image_map[item["path"]]
                    if "custom_size" not in item:
                        item["custom_size"] = None
                    if "use_original" not in item:
                        item["use_original"] = False
                    new_content.append(item)
            cat_data["content"] = new_content

        self.blocks = data
        self._load_json_data(file_path)

    def save_template(self, copy=False):
        template_data = {}
        for i in self.blocks:
            if i == "ALL":
                template_data[i] = {"content": self.blocks[i]["content"]}
            else:
                template_data[i] = {"fg": self.blocks[i]["fg"], "content": self.blocks[i]["content"]}

        template_data["font"] = self.font_data
        template_data["theme"] = self.theme_colors
        template_data["lang"] = self.lang

        save_file = filedialog.asksaveasfilename(initialfile="", defaultextension=".json",
                                                 filetypes=[("JSON", "*.json"), ("All files", "*.*")])
        if not save_file:
            return

        if copy:
            dest_folder = os.path.join(os.path.dirname(save_file),
                                       f"{os.path.basename(save_file).split('.')[0]}_assets")
            if not os.path.exists(dest_folder):
                os.mkdir(dest_folder)
            for i in template_data:
                if i in ("font", "theme", "lang"):
                    continue
                new_list = []
                for item in template_data[i]["content"]:
                    if self.is_text_item(item):
                        new_list.append(item)
                    elif self.is_image_item(item):
                        path = item.get("path", "")
                        if os.path.exists(path):
                            dest_path = os.path.join(dest_folder, os.path.basename(path))
                            if not os.path.exists(dest_path):
                                shutil.copy(path, dest_path)
                            item_copy = item.copy()
                            item_copy["path"] = os.path.basename(path)
                            new_list.append(item_copy)
                        else:
                            new_list.append(item)
                template_data[i]["content"] = new_list
            template_data["DATAPATH"] = os.path.basename(dest_folder)

        with open(save_file, "w", encoding='utf-8') as f:
            json.dump(template_data, f, ensure_ascii=False, indent=2)

        self.content_frame.configure(label_text=os.path.basename(save_file).split(".")[0])
        CTkMessagebox(self, title=self.t("done"),
                      message=f"{self.t('saved_json')}{save_file}", icon="check")

    def save_tierlist(self):
        image_items = []
        for cat in self.blocks:
            for item in self.blocks[cat]["content"]:
                if self.is_image_item(item):
                    image_items.append(item)

        images_b64 = {}
        mapping = {}
        for item in image_items:
            path = item.get("path", "")
            if path in mapping:
                continue
            try:
                if os.path.exists(path):
                    with open(path, "rb") as f:
                        raw = f.read()
                    fname = os.path.basename(path)
                else:
                    with urlopen(path) as response:
                        raw = response.read()
                    fname = f"url_{abs(hash(path))}.png"
                images_b64[fname] = base64.b64encode(raw).decode('utf-8')
                mapping[path] = fname
            except:
                pass

        template_data = {}
        for i in self.blocks:
            if i == "ALL":
                template_data[i] = {"content": []}
            else:
                template_data[i] = {"fg": self.blocks[i]["fg"], "content": []}
            for item in self.blocks[i]["content"]:
                if self.is_text_item(item):
                    template_data[i]["content"].append(item)
                elif self.is_image_item(item):
                    ic = item.copy()
                    if item.get("path") in mapping:
                        ic["path"] = mapping[item["path"]]
                    template_data[i]["content"].append(ic)

        template_data["font"] = self.font_data
        template_data["theme"] = self.theme_colors
        template_data["lang"] = self.lang
        template_data["images_base64"] = images_b64

        save_file = filedialog.asksaveasfilename(initialfile="", defaultextension=".tierlist",
                                                 filetypes=[("Tierlist", "*.tierlist"), ("All files", "*.*")])
        if not save_file:
            return

        with open(save_file, "w", encoding='utf-8') as f:
            json.dump(template_data, f, ensure_ascii=False, indent=2)

        self.content_frame.configure(label_text=os.path.basename(save_file).split(".")[0])
        CTkMessagebox(self, title=self.t("done"),
                      message=f"{self.t('saved_tierlist')}{save_file}", icon="check")

    def export_image(self):
        save_file = filedialog.asksaveasfilename(
            initialfile="tierlist",
            defaultextension=".png",
            filetypes=[("PNG", "*.png"), ("JPG", "*.jpg"), ("All files", "*.*")]
        )
        if not save_file:
            return
        self.after(500, lambda: self._capture_full(save_file))

    def _capture_full(self, save_file):
        old_geom = self.geometry()
        old_x = self.winfo_x()
        old_y = self.winfo_y()
        try:
            self.update_idletasks()
            self.update()

            self.deiconify()
            self.lift()
            self.focus_force()
            self.attributes("-topmost", True)

            needed = 0
            for f in self.frame_data:
                needed += f.winfo_reqheight() + 6
            needed += self.content_frame.winfo_reqheight() + 30
            needed += 100

            screen_w = self.winfo_screenwidth()
            screen_h = self.winfo_screenheight()

            new_h = min(needed, screen_h - 60)
            new_w = min(1000, screen_w - 40)

            self.geometry(f"{new_w}x{new_h}+{old_x}+{old_y}")

            for _ in range(12):
                self.update_idletasks()
                self.update()
                time.sleep(0.05)

            try:
                self.main_scroll._parent_canvas.yview_moveto(0)
            except:
                pass
            for _ in range(6):
                self.update_idletasks()
                self.update()
                time.sleep(0.03)

            x1 = self.bg_frame.winfo_rootx()
            y1 = self.bg_frame.winfo_rooty()
            w = self.bg_frame.winfo_width()
            h = self.bg_frame.winfo_height()
            x2 = x1 + w
            y2 = y1 + h

            img = None
            try:
                img = ImageGrab.grab(bbox=(x1, y1, x2, y2), all_screens=True)
            except TypeError:
                img = ImageGrab.grab(bbox=(x1, y1, x2, y2))

            if img is None or image_is_black(img):
                full = None
                try:
                    full = ImageGrab.grab(all_screens=True)
                except TypeError:
                    full = ImageGrab.grab()
                if full is not None:
                    img = full.crop((x1, y1, x2, y2))

            self.attributes("-topmost", False)
            self.geometry(old_geom)
            self.update_idletasks()
            self.update()

            if img is None:
                raise Exception("ImageGrab returned None")

            img.save(save_file)
            CTkMessagebox(self, title=self.t("done"),
                          message=f"{self.t('saved_png')}{save_file}", icon="check")
        except Exception as e:
            try:
                self.attributes("-topmost", False)
                self.geometry(old_geom)
            except:
                pass
            CTkMessagebox(self, title=self.t("error"), message=str(e), icon="cancel")

    def edit_content(self):
        content = []

        def remove(item, frame):
            if item in content:
                content.remove(item)
            frame.destroy()

        def ask_image_size():
            dialog = customtkinter.CTkToplevel(self)
            dialog.title(self.t("img_size"))
            dialog.geometry("350x200")
            dialog.transient(self)
            dialog.grab_set()

            use_original = tkinter.BooleanVar(value=False)
            custom_size = tkinter.IntVar(value=100)

            frame_size = customtkinter.CTkFrame(dialog, fg_color="transparent")
            frame_size.pack(pady=5)
            customtkinter.CTkLabel(frame_size, text=self.t("size_px")).pack(side="left", padx=5)
            size_entry = customtkinter.CTkEntry(frame_size, width=80, textvariable=custom_size)
            size_entry.pack(side="left")

            chk = customtkinter.CTkCheckBox(dialog, text=self.t("orig_size"), variable=use_original,
                                            command=lambda: size_entry.configure(
                                                state="disabled" if use_original.get() else "normal"))
            chk.pack(pady=10)

            result = {"use_original": False, "size": 100}

            def confirm():
                result["use_original"] = use_original.get()
                if not use_original.get():
                    try:
                        val = int(custom_size.get())
                        if val < 10:
                            val = 10
                        result["size"] = val
                    except:
                        result["size"] = 100
                dialog.destroy()

            customtkinter.CTkButton(dialog, text=self.t("ok"), command=confirm).pack(pady=10)

            dialog.wait_window()
            return result

        def add_image(open_files=None):
            if open_files is None:
                open_files = filedialog.askopenfilenames(
                    filetypes=[("Images", ["*.png", "*.jpg", "*.jpeg"]), ("All files", "*.*")])
            if open_files:
                for file in open_files:
                    try:
                        Image.open(file)
                    except:
                        continue
                    for i in self.blocks:
                        for it in self.blocks[i]["content"]:
                            if self.is_image_item(it) and it.get("path") == file:
                                CTkMessagebox(self, title=self.t("duplicate"),
                                              message=self.t("dup_img"), icon="warning")
                                return

                    size_result = ask_image_size()
                    if size_result is None:
                        return

                    caption_dialog = customtkinter.CTkInputDialog(
                        text=self.t("enter_caption"), title=self.t("caption"))
                    caption = caption_dialog.get_input() or ""

                    item_dict = {
                        "type": "image",
                        "path": file,
                        "caption": caption,
                        "use_original": size_result["use_original"],
                        "custom_size": size_result["size"] if not size_result["use_original"] else None
                    }
                    content.append(item_dict)

                    base = customtkinter.CTkFrame(scroll_frame, fg_color="transparent")
                    base.pack(pady=(0, 5), fill="x", expand=True)

                    delete_button = customtkinter.CTkButton(base, width=30, text="✕", fg_color="transparent",
                                                            border_width=1,
                                                            command=lambda it=item_dict, fr=base: remove(it, fr))
                    delete_button.pack(side="left", padx=(0, 5))

                    preview_img = customtkinter.CTkImage(Image.open(file), size=(60, 60))
                    label = customtkinter.CTkLabel(base, image=preview_img, text=None)
                    label.pack(side="left", padx=5)
                    size_text = self.t("original") if size_result["use_original"] else f"{size_result['size']}px"
                    cap_label = customtkinter.CTkLabel(
                        base, text=f"{caption if caption else self.t('no_caption')} ({size_text})", wraplength=150)
                    cap_label.pack(side="left", fill="x", expand=True, padx=5)

        def add_url():
            get_url = customtkinter.CTkInputDialog(text=self.t("paste_url"), title=self.t("url"))
            url = get_url.get_input()
            if url:
                try:
                    file = urlopen(url)
                    raw_data = file.read()
                    file.close()
                    image = Image.open(io.BytesIO(raw_data))
                except:
                    CTkMessagebox(self, title=self.t("error"), message=self.t("load_err"), icon="warning")
                    return

                for i in self.blocks:
                    for it in self.blocks[i]["content"]:
                        if self.is_image_item(it) and it.get("path") == url:
                            CTkMessagebox(self, title=self.t("duplicate"),
                                          message=self.t("dup_img"), icon="warning")
                            return

                size_result = ask_image_size()
                if size_result is None:
                    return

                caption_dialog = customtkinter.CTkInputDialog(
                    text=self.t("enter_caption2"), title=self.t("caption"))
                caption = caption_dialog.get_input() or ""

                item_dict = {
                    "type": "image",
                    "path": url,
                    "caption": caption,
                    "use_original": size_result["use_original"],
                    "custom_size": size_result["size"] if not size_result["use_original"] else None
                }
                content.append(item_dict)

                base = customtkinter.CTkFrame(scroll_frame, fg_color="transparent")
                base.pack(pady=(0, 5), fill="x", expand=True)

                delete_button = customtkinter.CTkButton(base, width=30, text="✕", fg_color="transparent",
                                                        border_width=1,
                                                        command=lambda it=item_dict, fr=base: remove(it, fr))
                delete_button.pack(side="left", padx=(0, 5))

                preview_img = customtkinter.CTkImage(image, size=(60, 60))
                label = customtkinter.CTkLabel(base, image=preview_img, text=None)
                label.pack(side="left", padx=5)
                size_text = self.t("original") if size_result["use_original"] else f"{size_result['size']}px"
                cap_label = customtkinter.CTkLabel(
                    base, text=f"{caption if caption else self.t('no_caption')} ({size_text})", wraplength=150)
                cap_label.pack(side="left", fill="x", expand=True, padx=5)

        def add_text():
            input_dialog = customtkinter.CTkInputDialog(text=self.t("enter_text"), title=self.t("text"))
            text = input_dialog.get_input()
            if text and text.strip():
                item_dict = {"type": "text", "text": text.strip()}
                content.append(item_dict)
                base = customtkinter.CTkFrame(scroll_frame, fg_color="transparent")
                base.pack(pady=(0, 5), fill="x", expand=True)

                delete_button = customtkinter.CTkButton(base, width=30, text="✕", fg_color="transparent",
                                                        border_width=1,
                                                        command=lambda it=item_dict, fr=base: remove(it, fr))
                delete_button.pack(side="left", padx=(0, 5))

                label = customtkinter.CTkLabel(base, text=text.strip(), font=self.global_font, wraplength=200)
                label.pack(side="left", fill="x", expand=True, padx=5)

        def add_from_clipboard():
            try:
                img = ImageGrab.grabclipboard()
                if img is None:
                    CTkMessagebox(self, title=self.t("error"), message=self.t("no_clipboard"), icon="warning")
                    return
                if isinstance(img, list):
                    for path in img:
                        if os.path.isfile(path):
                            add_image([path])
                    return
                if isinstance(img, Image.Image):
                    temp_filename = f"clipboard_{random.randint(1000, 9999)}.png"
                    temp_path = os.path.join(self.temp_dir, temp_filename)
                    img.save(temp_path, "PNG")
                    for i in self.blocks:
                        for it in self.blocks[i]["content"]:
                            if self.is_image_item(it) and it.get("path") == temp_path:
                                CTkMessagebox(self, title=self.t("duplicate"),
                                              message=self.t("dup_img"), icon="warning")
                                return
                    size_result = ask_image_size()
                    if size_result is None:
                        return
                    caption_dialog = customtkinter.CTkInputDialog(
                        text=self.t("enter_caption2"), title=self.t("caption"))
                    caption = caption_dialog.get_input() or ""
                    item_dict = {
                        "type": "image",
                        "path": temp_path,
                        "caption": caption,
                        "use_original": size_result["use_original"],
                        "custom_size": size_result["size"] if not size_result["use_original"] else None
                    }
                    content.append(item_dict)

                    base = customtkinter.CTkFrame(scroll_frame, fg_color="transparent")
                    base.pack(pady=(0, 5), fill="x", expand=True)

                    delete_button = customtkinter.CTkButton(base, width=30, text="✕", fg_color="transparent",
                                                            border_width=1,
                                                            command=lambda it=item_dict, fr=base: remove(it, fr))
                    delete_button.pack(side="left", padx=(0, 5))

                    preview_img = customtkinter.CTkImage(img, size=(60, 60))
                    label = customtkinter.CTkLabel(base, image=preview_img, text=None)
                    label.pack(side="left", padx=5)
                    size_text = self.t("original") if size_result["use_original"] else f"{size_result['size']}px"
                    cap_label = customtkinter.CTkLabel(
                        base, text=f"{caption if caption else self.t('no_caption')} ({size_text})", wraplength=150)
                    cap_label.pack(side="left", fill="x", expand=True, padx=5)
                else:
                    CTkMessagebox(self, title=self.t("error"), message=self.t("no_recognize"), icon="warning")
            except Exception as e:
                CTkMessagebox(self, title=self.t("error"), message=f"{self.t('error')}: {str(e)}", icon="warning")

        def save():
            for item in content:
                self.new_content(item, add_to_data=True)
            toplevel.destroy()

        toplevel = customtkinter.CTkToplevel(self)
        toplevel.resizable(False, False)
        toplevel.transient(self)
        toplevel.title(self.t("add_content"))

        frame = customtkinter.CTkFrame(toplevel, fg_color="transparent")
        frame.pack(pady=5, padx=5)

        customtkinter.CTkButton(frame, text=self.t("add_images"),
                                command=add_image).pack(padx=5, fill="x", side="left")
        customtkinter.CTkButton(frame, text=self.t("add_url"),
                                command=add_url).pack(padx=(0, 5), fill="x", side="right")
        customtkinter.CTkButton(frame, text=self.t("add_text"),
                                command=add_text).pack(padx=(0, 5), fill="x", side="right")
        customtkinter.CTkButton(frame, text=self.t("paste_clip"),
                                command=add_from_clipboard).pack(padx=(0, 5), fill="x", side="right")

        scroll_frame = customtkinter.CTkScrollableFrame(toplevel)
        scroll_frame.pack(expand=True, fill="both")

        customtkinter.CTkButton(toplevel, text=self.t("import"),
                                command=save).pack(padx=10, fill="x", pady=5)

        spawn_x = int(self.winfo_width() * .5 + self.winfo_x() - .5 * 300 + 7)
        spawn_y = int(self.winfo_height() * .5 + self.winfo_y() - .5 * toplevel.winfo_height() + 20)
        toplevel.geometry(f"+{spawn_x}+{spawn_y}")
        toplevel.grab_set()

    def new_category(self, frame=None):
        def add_category():
            if (len(entry_.get()) > 0) and entry_.get() != "ALL":
                if not frame:
                    self.blocks[entry_.get()] = {"fg": color.cget("fg_color"), "content": []}
                    self.make_category(entry_.get(), color.cget("fg_color"))
                else:
                    old_name = None
                    for cat, data in self.blocks.items():
                        if data.get("frame") == frame:
                            old_name = cat
                            break
                    if old_name:
                        self.blocks[old_name]["fg"] = color.cget("fg_color")
                        new_name = entry_.get()
                        if new_name != old_name:
                            self.blocks[new_name] = self.blocks.pop(old_name)
                            for child in frame.winfo_children():
                                if isinstance(child, customtkinter.CTkButton):
                                    child.configure(text=new_name)
                                    break
                        for child in frame.winfo_children():
                            if isinstance(child, customtkinter.CTkButton):
                                child.configure(fg_color=color.cget("fg_color"))
                                break
                toplevel.destroy()
            else:
                entry_.configure(placeholder_text_color="#fe7e7e", text_color="#fe7e7e")

                def reset_color():
                    try:
                        if entry_.winfo_exists():
                            entry_.configure(text_color=["black", "white"])
                    except:
                        pass
                self.after(1000, reset_color)

        def change_color():
            new_color = pick_color(self.t("choose_cat_color"), color.cget("fg_color"))
            if new_color:
                color.configure(fg_color=new_color)

        toplevel = customtkinter.CTkToplevel(self)
        toplevel.resizable(False, False)
        toplevel.transient(self)
        toplevel.title(self.t("add_cat_title") if not frame else self.t("edit_cat_title"))

        entry_ = customtkinter.CTkEntry(toplevel, placeholder_text=self.t("cat_name"), width=300)
        entry_.pack(fill="x", padx=5, pady=10)

        random_color = "#" + ''.join(random.choice('ABCDEF0123456789') for i in range(6))
        color = customtkinter.CTkButton(toplevel, text=self.t("color"), hover=False, border_width=2,
                                        fg_color=random_color, command=change_color)
        color.pack(fill="x", padx=5, pady=(0, 10))

        ok = customtkinter.CTkButton(toplevel, text=self.t("ok"), command=add_category)
        ok.pack(fill="x", padx=5, pady=(0, 10))

        spawn_x = int(self.winfo_width() * .5 + self.winfo_x() - .5 * 300 + 7)
        spawn_y = int(self.winfo_height() * .5 + self.winfo_y() - .5 * toplevel.winfo_height() + 20)
        toplevel.geometry(f"+{spawn_x}+{spawn_y}")

        if frame:
            for cat, data in self.blocks.items():
                if data.get("frame") == frame:
                    entry_.insert(0, cat)
                    color.configure(fg_color=data.get("fg", random_color))
                    break

        toplevel.grab_set()

    def make_category(self, text, color):
        outer_frame = customtkinter.CTkFrame(self.bg_frame, fg_color=self.frame_color,
                                             height=self.category_height)
        outer_frame.pack(fill="x", pady=3, padx=0)
        outer_frame.pack_propagate(False)

        button = customtkinter.CTkButton(outer_frame, width=80, text_color="black", font=self.global_font,
                                         text=text, fg_color=color, hover=False)
        button.pack(fill="y", side="left", padx=(5, 5))

        scroll_frame = customtkinter.CTkScrollableFrame(outer_frame, orientation="horizontal",
                                                        fg_color=self.frame_color)
        scroll_frame.pack(side="left", fill="both", expand=True, padx=(0, 5), pady=5)

        self.blocks[text]["frame"] = outer_frame
        self.blocks[text]["scroll"] = scroll_frame
        self.frame_data.append(outer_frame)

        menu = tkinter.Menu(button, tearoff=False, background=self.frame_color, fg='white', borderwidth=0, bd=0)
        menu.add_command(label=self.t("del_cat"),
                         command=lambda f=outer_frame: self.clear_list(f, delete=True))
        menu.add_command(label=self.t("clear"), command=lambda f=outer_frame: self.clear_list(f))
        menu.add_command(label=self.t("move_up"), command=lambda f=outer_frame: self.move(f, "up"))
        menu.add_command(label=self.t("move_down"), command=lambda f=outer_frame: self.move(f, "down"))
        menu.add_command(label=self.t("config"), command=lambda f=outer_frame: self.new_category(f))

        button.bind("<Button-3>", lambda event, m=menu: self.do_popup(event, m))
        button.bind("<Button-2>", lambda event, m=menu: self.do_popup(event, m))

        return outer_frame

    def clear_list(self, outer_frame, delete=False):
        if delete:
            if len(outer_frame.winfo_children()) > 1:
                ask = CTkMessagebox(self, title=self.t("del_q"), message=self.t("del_cat_q"),
                                    option_1=self.t("no"), option_2=self.t("yes"), icon="question")
                if ask.get() != self.t("yes"):
                    return

        target_cat = None
        for cat in self.blocks:
            if self.blocks[cat].get("frame") == outer_frame:
                target_cat = cat
                break
        if target_cat is None:
            return

        content = self.blocks[target_cat]["content"]
        self.blocks[target_cat]["content"] = []

        for item in content:
            self.new_content(item, frame=self.content_frame, add_to_data=True)

        scroll = self.blocks[target_cat].get("scroll")
        if scroll:
            for child in scroll.winfo_children():
                child.destroy()

        if delete:
            del self.blocks[target_cat]
            self.frame_data.remove(outer_frame)
            outer_frame.destroy()

    def move(self, outer_frame, direction):
        idx = self.frame_data.index(outer_frame)
        if direction == "up" and idx > 0:
            self.frame_data.insert(idx - 1, self.frame_data.pop(idx))
        elif direction == "down" and idx < len(self.frame_data) - 1:
            self.frame_data.insert(idx + 1, self.frame_data.pop(idx))
        else:
            return
        for f in self.frame_data:
            f.pack_forget()
            f.pack(fill="x", pady=3, padx=0)

    def _click_item(self, event, widget, clone, item):
        try:
            widget.focus_set()
        except:
            pass
        self.start_drag(event, widget, clone, item)

    def start_drag(self, event, widget, clone, item):
        self.drag_pending = True
        self.drag_active = False
        self.drag_item = item
        self.drag_clone = clone
        self.drag_widget = widget
        self.drag_start_x = event.x_root
        self.drag_start_y = event.y_root

    def on_drag_motion(self, event):
        if not self.drag_pending:
            return
        if not self.drag_active:
            dx = abs(event.x_root - self.drag_start_x)
            dy = abs(event.y_root - self.drag_start_y)
            if dx < 5 and dy < 5:
                return
            self.drag_active = True
            x = event.x_root - self.winfo_rootx() - 40
            y = event.y_root - self.winfo_rooty() - 40
            try:
                self.drag_clone.place(x=x, y=y)
                self.drag_clone.lift()
            except:
                pass

        if self.drag_clone is None:
            return
        x = event.x_root - self.winfo_rootx() - 40
        y = event.y_root - self.winfo_rooty() - 40
        try:
            self.drag_clone.place(x=x, y=y)
        except:
            pass

        for i in self.frame_data:
            i.configure(border_width=0)
        mouse_root_y = event.y_root
        for i in self.frame_data:
            top = i.winfo_rooty()
            bottom = top + i.winfo_height()
            if top <= mouse_root_y <= bottom:
                i.configure(border_width=2)
                break

    def on_drag_release(self, event):
        was_active = self.drag_active
        self.drag_pending = False
        self.drag_active = False

        if not was_active:
            self.drag_item = None
            self.drag_clone = None
            self.drag_widget = None
            return

        try:
            self.drag_clone.place_forget()
        except:
            pass
        for i in self.frame_data:
            i.configure(border_width=0)

        item = self.drag_item
        if item is None:
            self.drag_item = None
            self.drag_clone = None
            self.drag_widget = None
            return

        target_frame = None
        mouse_root_y = event.y_root
        for i in self.frame_data:
            top = i.winfo_rooty()
            bottom = top + i.winfo_height()
            if top <= mouse_root_y <= bottom:
                target_frame = i
                break

        target_cat = None
        if target_frame is None:
            target_cat = "ALL"
        else:
            for cat in self.blocks:
                if self.blocks[cat].get("frame") == target_frame:
                    target_cat = cat
                    break
            if target_cat is None:
                target_cat = "ALL"

        current_cat = None
        for cat in self.blocks:
            if item in self.blocks[cat]["content"]:
                current_cat = cat
                break
        if current_cat is None or current_cat == target_cat:
            self.drag_item = None
            self.drag_clone = None
            self.drag_widget = None
            return

        self.blocks[current_cat]["content"].remove(item)
        self.blocks[target_cat]["content"].append(item)

        self.refresh_all_items()

        self.drag_item = None
        self.drag_clone = None
        self.drag_widget = None

    def adjust_thumb_size(self):
        def set_size(val):
            self.thumb_size = int(val)
            self.refresh_all_items()

        toplevel = customtkinter.CTkToplevel(self)
        toplevel.title(self.t("global_size"))
        toplevel.geometry("300x150")
        toplevel.transient(self)
        toplevel.grab_set()

        slider = customtkinter.CTkSlider(toplevel, from_=50, to=250, number_of_steps=40, command=set_size)
        slider.pack(pady=20, padx=20)
        slider.set(self.thumb_size)

        label = customtkinter.CTkLabel(toplevel,
                                       text=f"{self.t('current_size')}{self.thumb_size} px")
        label.pack()

        customtkinter.CTkButton(toplevel, text=self.t("ok"),
                                command=toplevel.destroy).pack(pady=10)

    def refresh_all_items(self):
        all_data = {}
        for cat in self.blocks:
            all_data[cat] = self.blocks[cat]["content"]

        for cat in self.blocks:
            if cat != "ALL":
                scroll = self.blocks[cat].get("scroll")
                if scroll:
                    for child in scroll.winfo_children():
                        child.destroy()
            else:
                for child in self.content_frame.winfo_children():
                    child.destroy()

        for cat in all_data:
            if cat == "ALL":
                frame = self.content_frame
            else:
                frame = self.blocks[cat].get("scroll")
                if frame is None:
                    continue
            for item in all_data[cat]:
                self.new_content(item, frame=frame, add_to_data=False)

    def new_content(self, item, frame=None, add_to_data=True):
        if frame is None:
            frame = self.content_frame

        target_cat = None
        for cat in self.blocks:
            if self.blocks[cat].get("scroll") == frame:
                target_cat = cat
                break
        if target_cat is None:
            target_cat = "ALL"

        if add_to_data:
            if item not in self.blocks[target_cat]["content"]:
                self.blocks[target_cat]["content"].append(item)

        if self.is_text_item(item):
            text = item.get("text", "")
            label = customtkinter.CTkLabel(frame, text=text, font=self.global_font,
                                           width=self.thumb_size, height=60,
                                           wraplength=self.thumb_size, justify="center")
            label.pack(side="left", fill="y", padx=5, pady=5)
            label.data = item
            clone = customtkinter.CTkLabel(self, text=text, font=self.global_font,
                                           width=self.thumb_size, height=60,
                                           wraplength=self.thumb_size, justify="center")

            label.bind("<ButtonPress-1>",
                       lambda e, w=label, c=clone, it=item: self._click_item(e, w, c, it))
            label.bind("<Button-3>", lambda e, it=item: self.show_item_menu(e, it))
            label.bind("<Button-2>", lambda e, it=item: self.show_item_menu(e, it))
            label.bind("<Delete>", lambda e, w=label, it=item, c=clone: self.delete_item(w, it, c))
        else:
            path = item.get("path", "")
            caption = item.get("caption", "")
            use_original = item.get("use_original", False)
            custom_size = item.get("custom_size", None)

            if use_original:
                try:
                    if os.path.exists(path):
                        with Image.open(path) as img:
                            orig_w, orig_h = img.size
                    else:
                        with urlopen(path) as response:
                            img = Image.open(io.BytesIO(response.read()))
                            orig_w, orig_h = img.size
                    display_size = (orig_w, orig_h)
                except:
                    display_size = (self.thumb_size, self.thumb_size)
            elif custom_size:
                display_size = (custom_size, custom_size)
            else:
                display_size = (self.thumb_size, self.thumb_size)

            try:
                if os.path.exists(path):
                    pil_img = Image.open(path)
                    pil_img.thumbnail(display_size, Image.Resampling.LANCZOS)
                    img = customtkinter.CTkImage(pil_img, size=pil_img.size)
                else:
                    file = urlopen(path)
                    raw_data = file.read()
                    file.close()
                    pil_img = Image.open(io.BytesIO(raw_data))
                    pil_img.thumbnail(display_size, Image.Resampling.LANCZOS)
                    img = customtkinter.CTkImage(pil_img, size=pil_img.size)
            except:
                return

            container = customtkinter.CTkFrame(frame, fg_color="transparent")
            container.pack(side="left", fill="y", padx=5, pady=5)

            img_label = customtkinter.CTkLabel(container, image=img, text=None)
            img_label.pack()
            img_label.data = item
            img_label.bind("<Double-Button-1>", lambda e, it=item: self.view_image(it))

            cap_text = caption if caption else ""
            cap_label = customtkinter.CTkLabel(container, text=cap_text, font=self.global_font,
                                               wraplength=self.thumb_size, justify="center")
            cap_label.pack()

            container.data = item
            img_label.data = item
            cap_label.data = item

            clone = customtkinter.CTkLabel(self, image=img, text=None,
                                           width=display_size[0], height=display_size[1])

            for w in (container, img_label, cap_label):
                w.bind("<ButtonPress-1>",
                       lambda e, ww=container, c=clone, it=item: self._click_item(e, ww, c, it))
                w.bind("<Button-3>", lambda e, it=item: self.show_item_menu(e, it))
                w.bind("<Button-2>", lambda e, it=item: self.show_item_menu(e, it))
                w.bind("<Delete>",
                       lambda e, ww=container, it=item, c=clone: self.delete_item(ww, it, c))

        if platform.startswith("win") and pywinstyles is not None:
            try:
                pywinstyles.set_opacity(clone, 0.6)
            except:
                pass

    def view_image(self, item):
        if not self.is_image_item(item):
            return
        path = item.get("path", "")
        try:
            if os.path.exists(path):
                img = Image.open(path)
            else:
                file = urlopen(path)
                raw_data = file.read()
                file.close()
                img = Image.open(io.BytesIO(raw_data))
        except:
            CTkMessagebox(self, title=self.t("error"), message=self.t("cant_open"), icon="warning")
            return

        view_win = customtkinter.CTkToplevel(self)
        view_win.title(self.t("view"))
        max_w, max_h = 800, 600
        img_w, img_h = img.size
        scale = min(max_w / img_w, max_h / img_h, 1.0)
        new_w = int(img_w * scale)
        new_h = int(img_h * scale)
        view_win.geometry(f"{new_w + 40}x{new_h + 60}")

        photo = ImageTk.PhotoImage(img.resize((new_w, new_h), Image.Resampling.LANCZOS))
        label = tkinter.Label(view_win, image=photo)
        label.image = photo
        label.pack(padx=10, pady=10)

        caption = item.get("caption", "")
        if caption:
            cap_label = tkinter.Label(view_win, text=caption, font=("Arial", 12))
            cap_label.pack()

        customtkinter.CTkButton(view_win, text=self.t("close"),
                                command=view_win.destroy).pack(pady=5)

    def show_item_menu(self, event, item):
        menu = tkinter.Menu(self, tearoff=0)
        if self.is_image_item(item):
            menu.add_command(label=self.t("edit_caption"),
                             command=lambda: self.edit_caption(item))
            menu.add_command(label=self.t("view_img"),
                             command=lambda: self.view_image(item))
            menu.add_command(label=self.t("set_size"),
                             command=lambda: self.set_item_size(item))
        elif self.is_text_item(item):
            menu.add_command(label=self.t("edit_text"),
                             command=lambda: self.edit_text_item(item))
        menu.add_separator()
        menu.add_command(label=self.t("delete"), command=lambda: self.delete_item_by_data(item))
        menu.post(event.x_root, event.y_root)

    def edit_caption(self, item):
        if not self.is_image_item(item):
            return
        new_cap = customtkinter.CTkInputDialog(text=self.t("enter_new_caption"),
                                               title=self.t("edit_caption"))
        new_text = new_cap.get_input()
        if new_text is not None:
            item["caption"] = new_text.strip()
            self.refresh_all_items()

    def set_item_size(self, item):
        if not self.is_image_item(item):
            return
        dialog = customtkinter.CTkToplevel(self)
        dialog.title(self.t("img_size"))
        dialog.geometry("350x200")
        dialog.transient(self)
        dialog.grab_set()

        use_original = tkinter.BooleanVar(value=item.get("use_original", False))
        custom_size = tkinter.IntVar(value=item.get("custom_size", 100) if not use_original.get() else 100)

        frame_size = customtkinter.CTkFrame(dialog, fg_color="transparent")
        frame_size.pack(pady=5)
        customtkinter.CTkLabel(frame_size, text=self.t("size_px")).pack(side="left", padx=5)
        size_entry = customtkinter.CTkEntry(frame_size, width=80, textvariable=custom_size)
        size_entry.pack(side="left")
        if use_original.get():
            size_entry.configure(state="disabled")

        chk = customtkinter.CTkCheckBox(dialog, text=self.t("orig_size"), variable=use_original,
                                        command=lambda: size_entry.configure(
                                            state="disabled" if use_original.get() else "normal"))
        chk.pack(pady=10)

        def confirm():
            item["use_original"] = use_original.get()
            if not use_original.get():
                try:
                    val = int(custom_size.get())
                    if val < 10:
                        val = 10
                    item["custom_size"] = val
                except:
                    item["custom_size"] = 100
            else:
                item["custom_size"] = None
            dialog.destroy()
            self.refresh_all_items()

        customtkinter.CTkButton(dialog, text=self.t("ok"), command=confirm).pack(pady=10)

    def edit_text_item(self, item):
        if not self.is_text_item(item):
            return
        new_text = customtkinter.CTkInputDialog(text=self.t("enter_new_text"),
                                                title=self.t("edit_text"))
        txt = new_text.get_input()
        if txt is not None:
            item["text"] = txt.strip()
            self.refresh_all_items()

    def delete_item_by_data(self, item):
        for cat in self.blocks:
            if item in self.blocks[cat]["content"]:
                self.blocks[cat]["content"].remove(item)
        self.refresh_all_items()

    def delete_item(self, widget, item, clone):
        for cat in self.blocks:
            if item in self.blocks[cat]["content"]:
                self.blocks[cat]["content"].remove(item)
                break
        try:
            widget.destroy()
        except:
            pass
        try:
            clone.destroy()
        except:
            pass

    def dropped_content(self, event):
        dropped_file = event.data.split("{")
        files = []
        for i in dropped_file:
            i = i.replace("{", "").replace("} ", "").replace("}", "")
            if os.path.isfile(i):
                files.append(i)
        for i in files:
            item = {"type": "image", "path": i, "caption": "",
                    "use_original": False, "custom_size": None}
            self.new_content(item, add_to_data=True)

    def ask_leave(self):
        res = CTkMessagebox(self, title=self.t("exit"), message=self.t("exit_q"),
                            option_1=self.t("cancel"), option_2=self.t("no"),
                            option_3=self.t("yes"), icon="question")
        if res.get() == self.t("yes"):
            self.destroy()

    def toggle_fullscreen(self):
        if not self.fullscreen:
            self.wm_attributes("-fullscreen", 1)
            self.fullscreen = True
        else:
            self.wm_attributes("-fullscreen", 0)
            self.fullscreen = False
        self.resizable(True, True)

    def disable_fullscreen(self):
        if self.fullscreen:
            self.wm_attributes("-fullscreen", 0)
            self.fullscreen = False
            self.resizable(True, True)

    def update_global_font(self):
        if self.font_data["family"] != "default":
            self.global_font.configure(family=self.font_data["family"])
        else:
            self.global_font.configure(family=customtkinter.ThemeManager.theme["CTkFont"]["family"])
        self.global_font.configure(size=self.font_data["size"])
        self.global_font.configure(underline=1 if self.font_data["underline"] else 0)
        self.global_font.configure(slant="italic" if self.font_data["slant"] else "roman")
        self.global_font.configure(weight="bold" if self.font_data["weight"] else "normal")

    def adjust_font(self):
        def change_size(val):
            self.global_font.configure(size=int(val))

        def change_font_family(val):
            if val == "default":
                self.global_font.configure(family=customtkinter.ThemeManager.theme["CTkFont"]["family"])
            else:
                self.global_font.configure(family=val)

        def toggle_bold():
            self.global_font.configure(weight="bold" if bold_box.get() else "normal")

        def toggle_slant():
            self.global_font.configure(slant="italic" if italic_box.get() else "roman")

        def toggle_underline():
            self.global_font.configure(underline=1 if underline_box.get() else 0)

        def save():
            self.font_data["weight"] = 1 if bold_box.get() else 0
            self.font_data["slant"] = 1 if italic_box.get() else 0
            self.font_data["underline"] = 1 if underline_box.get() else 0
            if font_box.get() != "default":
                self.font_data["family"] = font_box.get()
            self.font_data["size"] = int(size_slider.get())
            toplevel.destroy()

        toplevel = customtkinter.CTkToplevel(self)
        toplevel.resizable(False, False)
        toplevel.transient(self)
        toplevel.protocol("WM_DELETE_WINDOW", save)
        toplevel.title(self.t("font_size"))

        customtkinter.CTkLabel(toplevel, text=self.t("font")).pack(anchor="w", padx=12)
        font_values = ["default"] + list(tkinter.font.families())
        font_box = customtkinter.CTkComboBox(toplevel, width=200, values=font_values,
                                             command=change_font_family)
        font_box.pack(expand=True, fill="x", padx=10, pady=5)
        font_box.set(self.font_data["family"])

        customtkinter.CTkLabel(toplevel, text=self.t("size")).pack(anchor="w", padx=12)
        size_slider = customtkinter.CTkSlider(toplevel, from_=10, to=35, number_of_steps=10,
                                              command=change_size)
        size_slider.pack(expand=True, fill="x", padx=8)
        size_slider.set(self.font_data["size"])

        frame = customtkinter.CTkFrame(toplevel, fg_color="transparent")
        frame.pack(pady=10, padx=(15, 0))

        bold_box = customtkinter.CTkCheckBox(frame, text=self.t("bold"), command=toggle_bold)
        bold_box.pack(side="left")
        if self.font_data["weight"]:
            bold_box.select()

        italic_box = customtkinter.CTkCheckBox(frame, text=self.t("italic"), command=toggle_slant)
        italic_box.pack(side="left")
        if self.font_data["slant"]:
            italic_box.select()

        underline_box = customtkinter.CTkCheckBox(frame, text=self.t("underline"),
                                                  command=toggle_underline)
        underline_box.pack(side="left")
        if self.font_data["underline"]:
            underline_box.select()

        ok = customtkinter.CTkButton(toplevel, text=self.t("ok"), command=save)
        ok.pack(expand=True, fill="x", side="bottom", padx=10, pady=(0, 10))

        spawn_x = int(self.winfo_width() * .5 + self.winfo_x() - .5 * 300 + 7)
        spawn_y = int(self.winfo_height() * .5 + self.winfo_y() - .5 * toplevel.winfo_height() + 20)
        toplevel.geometry(f"+{spawn_x}+{spawn_y}")
        toplevel.grab_set()

    def update_colors(self):
        for i in self.frame_data:
            i.configure(fg_color=self.theme_colors["fg"])
            for j in i.winfo_children():
                if type(j) is tkinter.Label:
                    j.configure(bg=self.theme_colors["fg"])
                elif type(j) is customtkinter.CTkButton:
                    j.configure(text_color=self.theme_colors["txt"])
        self.bg_frame.configure(fg_color=self.theme_colors["bg"])

    def adjust_theme(self):
        def change_fg():
            new_color = pick_color(self.t("choose_cat_bg"), self.theme_colors["fg"])
            if not new_color:
                new_color = self._apply_appearance_mode(
                    customtkinter.ThemeManager.theme["CTkFrame"]["top_fg_color"])
            self.theme_colors["fg"] = new_color
            self.frame_color = new_color
            bt1.configure(fg_color=new_color)
            self.update_colors()

        def change_bg():
            new_color = pick_color(self.t("choose_main_bg"), self.theme_colors["bg"])
            if not new_color:
                new_color = self.frame_color2
            self.theme_colors["bg"] = new_color
            bt2.configure(fg_color=new_color)
            self.update_colors()

        def change_txt():
            new_color = pick_color(self.t("choose_txt"), self.theme_colors["txt"])
            if not new_color:
                new_color = "black"
            self.theme_colors["txt"] = new_color
            bt3.configure(fg_color=new_color)
            self.update_colors()

        toplevel = customtkinter.CTkToplevel(self)
        toplevel.resizable(False, False)
        toplevel.transient(self)
        toplevel.title(self.t("color_scheme"))

        frame1 = customtkinter.CTkFrame(toplevel, fg_color="transparent")
        frame1.pack(expand=True, fill="x", padx=10, pady=5)
        customtkinter.CTkLabel(frame1, width=100, anchor="w",
                               text=self.t("cat_color")).pack(side="left", padx=(0, 10))
        bt1 = customtkinter.CTkButton(frame1, text="", hover=False,
                                      fg_color=self.theme_colors["fg"],
                                      width=30, border_width=2, command=change_fg)
        bt1.pack(side="right")

        frame2 = customtkinter.CTkFrame(toplevel, fg_color="transparent")
        frame2.pack(expand=True, fill="x", padx=10, pady=5)
        customtkinter.CTkLabel(frame2, text=self.t("main_bg")).pack(side="left", padx=(0, 10))
        bt2 = customtkinter.CTkButton(frame2, text="", hover=False,
                                      fg_color=self.theme_colors["bg"],
                                      width=30, border_width=2, command=change_bg)
        bt2.pack(side="right")

        frame3 = customtkinter.CTkFrame(toplevel, fg_color="transparent")
        frame3.pack(expand=True, fill="x", padx=10, pady=5)
        customtkinter.CTkLabel(frame3, text=self.t("txt_color")).pack(side="left", padx=(0, 10))
        bt3 = customtkinter.CTkButton(frame3, text="", hover=False,
                                      fg_color=self.theme_colors["txt"],
                                      width=30, border_width=2, command=change_txt)
        bt3.pack(side="right")

        spawn_x = int(self.winfo_width() * .5 + self.winfo_x() - .5 * 300 + 7)
        spawn_y = int(self.winfo_height() * .5 + self.winfo_y() - .5 * toplevel.winfo_height() + 20)
        toplevel.geometry(f"+{spawn_x}+{spawn_y}")
        toplevel.grab_set()

    def show_about(self):
        CTkMessagebox(self, title=self.t("about"), message=self.t("about_text"))

    def do_popup(self, event, menu):
        menu.tk_popup(event.x_root + 6, event.y_root + 5)


if __name__ == "__main__":
    root = App()
    root.mainloop()
