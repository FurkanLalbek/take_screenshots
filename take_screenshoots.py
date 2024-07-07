import pyautogui
import time
import cv2
import keyboard
import dxcam
import win32gui
import os
import json
import random

class Take_Screenshot:
    def __init__(self):
        self.visible_windows = []
        self.selected_window = None
        self.window = None
        self.region = None
        self.camera = None
        self.target_fps = 2
        self.count = 0
        self.save_dir = "screenshots"
        self.config_file = "config.json"
        self.i = 1
        self.save = True

    def list_visible_windows(self):
        def winEnumHandler(hwnd, ctx):
            if win32gui.IsWindowVisible(hwnd):
                name = win32gui.GetWindowText(hwnd)
                if name:
                    self.visible_windows.append(win32gui.GetWindowText(hwnd))
        win32gui.EnumWindows(winEnumHandler, None)
    
    def select_window(self):
        while True:
            try:
                max_len = max(map(len, self.visible_windows)) + 5
                for idx, window_name in enumerate(self.visible_windows, start=1):
                    print(f"{idx}. {window_name.ljust(max_len)}", end="")
                    if idx % 2 == 0:
                        print()
                print("\n")
                selection = int(input("Hangi uygulamayı seçmek istersiniz? (Sayı giriniz): "))
                self.selected_window = self.visible_windows[selection - 1]
                break
            except (ValueError, IndexError):
                print("Lütfen geçerli bir değer giriniz.")
    
    def initialize_camera(self):
        self.camera = dxcam.create()
        while True:
            self.window = pyautogui.getWindowsWithTitle(self.selected_window)
            if self.window and self.window[0].isActive:
                try:
                    self.window = self.window[0]
                    print(f"{self.selected_window} penceresi aktif, kamera başlatılıyor...", end="\r")
                    left = max(self.window.left, 0)
                    top = max(self.window.top, 0)
                    right = min(self.window.left + self.window.width, pyautogui.size().width)
                    bottom = min(self.window.top + self.window.height, pyautogui.size().height)
                    self.region = (left, top, right, bottom)
                    self.camera.start(target_fps=self.target_fps, region=self.region)
                    break
                except Exception as e:
                    print("Seçilen pencere aktif değil, tekrar deneniyor... " + " " * 100, end="\r")
                    time.sleep(random.uniform(0.1, 0.5))
            else:
                print("Seçilen pencere aktif değil, bekleniyor... " + " " * 100, end="\r")
                time.sleep(random.uniform(0.1, 0.5))
    
    def capture_screenshots(self):
        if self.save:
            os.makedirs(self.save_dir, exist_ok=True)
        while True:
            self.window = pyautogui.getWindowsWithTitle(self.selected_window)
            if self.window and self.window[0].isActive:
                print(f"{self.selected_window} penceresi aktif, ekran görüntüsü alınıyor...", end="\r")
                screenshot = self.camera.get_latest_frame()
                screenshot = cv2.cvtColor(screenshot, cv2.COLOR_BGR2RGB)
                
                if self.save:
                    cv2.imwrite(f"{self.save_dir}/{self.i}.png", screenshot)

                if self.stop_program():
                    break
                if self.count and self.i == self.count:
                    print(f"{self.count} adet ekran görüntüsü alındı.")
                    break
                self.i += 1
            else:
                if self.stop_program():
                    break
                print("Seçilen pencere aktif değil, bekleniyor... " + " " * 100, end="\r")  # Boşluklar eklenerek önceki mesajın üzerine yazılır
                time.sleep(random.uniform(0.1, 0.5)) 

    def stop_program(self):
        if keyboard.is_pressed("esc") or keyboard.is_pressed("q"):
            print("ESC veya q tuşuna basıldı, çıkılıyor." + " " * 100)
            return True
    
    def save_config(self):
        with open(self.config_file, "w") as f:
            json.dump({"target_fps": self.target_fps,
                       "count": self.count,
                       "save_dir": self.save_dir,
                       "selected_window": self.selected_window},
                      f, indent=4)
    
    def load_config(self):
        with open(self.config_file, "r") as f:
            config = json.load(f)
            self.target_fps = config["target_fps"]
            self.count = config["count"]
            self.save_dir = config["save_dir"]
            self.selected_window = config["selected_window"]
    
    def get_user_input(self):
        def get_int_input(prompt):
            while True:
                try:
                    return int(input(prompt))
                except ValueError:
                    print("Lütfen geçerli bir sayı giriniz.")

        def get_bool_input(prompt):
            while True:
                response = input(prompt).strip().lower()
                if response == 'e':
                    return True
                elif response == 'h':
                    return False
                else:
                    print("Lütfen 'e' veya 'h' giriniz.")

        self.target_fps = get_int_input("FPS değeri giriniz: ")
        self.count = get_int_input("Kaç adet ekran görüntüsü almak istersiniz? 0 = Sonsuz: ")
        self.save = get_bool_input("Ekran görüntülerini kaydetmek istiyor musunuz? (e/h): ")
        self.select_window()
    
    def run(self):
        self.list_visible_windows()
        if os.path.exists(self.config_file):
            if input("Kaydedilen ayarları yüklemek istiyor musunuz? (e/h): ").lower() == "e":
                self.load_config()
                if self.selected_window not in self.visible_windows:
                    print("Kaydedilen pencere adı bulunamadı. Lütfen tekrar seçiniz.")
                    time.sleep(1)
                    self.select_window()
                    if input("Yeni ayarları kaydetmek istiyor musunuz? (e/h): ").lower() == "e":
                        self.save_config()
            else:
                self.get_user_input()
                if input("Kaydedilen ayarları güncellemek istiyor musunuz? (e/h): ").lower() == "e":
                    self.save_config()
        else:
            self.get_user_input()
            if input("Ayarları kaydetmek istiyor musunuz? (e/h): ").lower() == "e":
                self.save_config()

        self.initialize_camera()
        self.capture_screenshots()
    
if __name__ == "__main__":
    print("https://github.com/FurkanLalbek")
    Take_Screenshot().run()
