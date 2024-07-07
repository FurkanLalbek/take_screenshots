## Take_Screenshot

This Python script allows users to capture screenshots from a specific window at a defined frame rate. The screenshots can be saved to a specified directory. The script uses various libraries, such as `pyautogui`, `dxcam`, `cv2` (OpenCV), and `keyboard` to accomplish its task. The configuration can be saved and loaded from a JSON file.

### Prerequisites

Ensure you have Python installed on your system. You can download it from [Python's official website](https://www.python.org/downloads/).

You will need the following Python packages:
- `pyautogui`
- `dxcam`
- `opencv-python`
- `keyboard`
- `pywin32` (for `win32gui`)

Install them using pip:

```sh
pip install pyautogui dxcam opencv-python keyboard pywin32
```

### Usage

1. **Clone the Repository**
   ```sh
   git clone https://github.com/FurkanLalbek/Take_Screenshot.git
   cd Take_Screenshot
   ```

2. **Run the Script**
   ```sh
   python take_screenshot.py
   ```

### Configuration

When you first run the script, it will ask for user inputs to set the target frame rate, the number of screenshots to take, whether to save the screenshots, and which window to capture. These settings can be saved and loaded from a JSON configuration file (`config.json`).

### Options

1. **FPS (Frames Per Second)**
   Set the number of frames per second to capture.

2. **Number of Screenshots**
   Specify the number of screenshots to capture. If set to `0`, the script will capture screenshots indefinitely until stopped by pressing `ESC` or `q`.

3. **Save Screenshots**
   Decide whether to save the screenshots. If `yes`, the screenshots will be saved in the specified directory.

4. **Select Window**
   Choose the window to capture from the list of visible windows.

### Functions

- **`list_visible_windows`**: Lists all visible windows.
- **`select_window`**: Prompts the user to select a window from the list of visible windows.
- **`initialize_camera`**: Initializes the camera and sets the region of the window to capture.
- **`capture_screenshots`**: Continuously captures screenshots at the specified frame rate.
- **`stop_program`**: Checks if the `ESC` or `q` key is pressed to stop the program.
- **`save_config`**: Saves the configuration to a JSON file.
- **`load_config`**: Loads the configuration from a JSON file.
- **`get_user_input`**: Prompts the user to input settings.

### Example

When you run the script, it will display the following options:

```sh
https://github.com/FurkanLalbek
1. Window Name 1
2. Window Name 2

Hangi uygulamayı seçmek istersiniz? (Sayı giriniz): 
```

After selecting the window, you will be prompted to enter the FPS, the number of screenshots to take, and whether to save the screenshots.

### Exiting the Program

To stop the program, press `ESC` or `q`.

### Notes

- Ensure the selected window is active to capture the screenshots. The script will wait if the window is not active.
- The screenshots will be saved in the `screenshots` directory by default.

### Author

Furkan Lalbek - [GitHub](https://github.com/FurkanLalbek)

### License

This project is licensed under the MIT License.

---

TR - Türkçe

Take_Screenshot Python betiği, belirli bir pencereden tanımlanan kare hızında ekran görüntüleri yakalamak için kullanıcılara imkan tanır. Ekran görüntüleri belirli bir dizine kaydedilebilir. Betik, görevini gerçekleştirmek için pyautogui, dxcam, cv2 (OpenCV) ve keyboard gibi çeşitli kütüphaneleri kullanır. Konfigürasyon JSON dosyasından kaydedilip yüklenebilir.

### Gereksinimler
Sisteminizde Python yüklü olduğundan emin olun. Python'un resmi web sitesinden indirebilirsiniz.

Aşağıdaki Python paketlerine ihtiyacınız olacak:
- pyautogui
- dxcam
- opencv-python
- keyboard
- pywin32 (win32gui için) 

Bu paketleri pip kullanarak yükleyin:

```sh
pip install pyautogui dxcam opencv-python keyboard pywin32
```

### Kullanım
### Depoyu Klonlayın

```sh
git clone https://github.com/FurkanLalbek/Take_Screenshot.git
cd Take_Screenshot
```

### Betiği Çalıştırın

```sh
python take_screenshot.py
```

### Konfigürasyon
Betik ilk çalıştırıldığında, hedef kare hızını, alınacak ekran görüntüsü sayısını, ekran görüntülerinin kaydedilip kaydedilmeyeceğini ve hangi pencerenin yakalanacağını ayarlamak için kullanıcı girdileri isteyecektir. Bu ayarlar JSON konfigürasyon dosyasına (config.json) kaydedilip yüklenebilir.

#### Seçenekler
- **FPS (Saniyedeki Kare Sayısı):** Yakalanacak saniyedeki kare sayısını ayarlayın.
- **Ekran Görüntüsü Sayısı:** Yakalanacak ekran görüntüsü sayısını belirtin. 0 olarak ayarlanırsa, betik ESC veya q tuşuna basılarak durdurulana kadar ekran görüntüsü yakalar.
- **Ekran Görüntülerini Kaydet:** Ekran görüntülerinin kaydedilip kaydedilmeyeceğine karar verin. Evet ise, ekran görüntüleri belirtilen dizine kaydedilecektir.
- **Pencere Seçimi:** Görünen pencerelerin listesinden yakalanacak pencereyi seçin.

#### Fonksiyonlar
- **list_visible_windows:** Tüm görünen pencereleri listeler.
- **select_window:** Kullanıcıdan görünen pencereler listesinden bir pencere seçmesini ister.
- **initialize_camera:** Kamerayı başlatır ve yakalanacak pencere bölgesini ayarlar.
- **capture_screenshots:** Belirtilen kare hızında sürekli olarak ekran görüntüleri yakalar.
- **stop_program:** Programı durdurmak için ESC veya q tuşuna basıldığını kontrol eder.
- **save_config:** Konfigürasyonu bir JSON dosyasına kaydeder.
- **load_config:** Konfigürasyonu bir JSON dosyasından yükler.
- **get_user_input:** Kullanıcıdan ayarları girmesini ister.

#### Örnek
Betik çalıştırıldığında aşağıdaki seçenekler görüntülenecektir:

```sh
1. Pencere Adı 1
2. Pencere Adı 2

Hangi uygulamayı seçmek istersiniz? (Sayı giriniz): 
```

Pencere seçtikten sonra, FPS, alınacak ekran görüntüsü sayısı ve ekran görüntülerinin kaydedilip kaydedilmeyeceği sorulacaktır.

### Programdan Çıkma
Programı durdurmak için ESC veya q tuşuna basın.

### Notlar
- Seçilen pencerenin aktif olduğundan emin olun. Pencere aktif değilse betik bekleyecektir.
- Ekran görüntüleri varsayılan olarak screenshots dizinine kaydedilecektir.

### Yazar
Furkan Lalbek - [GitHub](https://github.com/FurkanLalbek)

### Lisans
Bu proje MIT Lisansı altında lisanslanmıştır.
