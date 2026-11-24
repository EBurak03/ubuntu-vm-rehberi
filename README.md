# VMware Ubuntu 20.04 Geliştirme Ortamı (ROS Noetic & Gazebo 11)

Bu depo; VMware üzerinde çalışan **Ubuntu 20.04 LTS (Focal)** sanal makinesinin kurulum dosyalarını, hazır imaj bağlantılarını, yüklü sistem/ROS/Python paket listelerini ve `catkin_ws` çalışma alanı yapılandırmasını içerir.

---

## 1. Ön Gereksinim: VMware Workstation Kurulumu

Sanal makineyi çalıştırabilmek için bilgisayarınızda **VMware Workstation Pro / Player** kurulu olmalıdır (kişisel kullanım için ücretsizdir):

1. **İndirme:** [VMware Kurulum Klasörünü Aç (Google Drive)](https://drive.google.com/drive/folders/1GrJUJuae8ebKat6Tl69tlN2IRF5aPr8M?usp=sharing) bağlantısından **`VMware-Workstation-Full-25H2-24995812.exe`** dosyasını indirin.
2. **Kurulum:** İndirdiğiniz `.exe` dosyasına çift tıklayın; kurulum sihirbazında **Next → Next → Install** adımlarını izleyerek kurulumu tamamlayın ve istenirse bilgisayarınızı yeniden başlatın.

---

## 2. Seçenek A: Hazır Sanal Makine İmajını İndir (Kurulumsuz)

Sıfırdan kurulum adımlarıyla uğraşmadan tüm paketlerin, depo anahtarlarının ve `catkin_ws` çalışma ortamının hazır olduğu sanal makineyi doğrudan indirebilirsiniz.

| Paket Formatı | Google Drive İndirme Bağlantısı | Uyumlu Programlar | Nasıl Çalıştırılır? |
| :--- | :--- | :--- | :--- |
| **Evrensel İmaj (`.ova`)** | [UBUNTU ama ova Klasörünü Aç](https://drive.google.com/drive/folders/1aqVtQD4IpLpWMVB0WZM79LHmjMahRcwg?usp=sharing) | VMware Player, VMware Pro, VirtualBox | İnen `.ova` dosyasına çift tıklayın (veya programda **File > Open / Import** seçin) ve **Import** butonuna basın. |
| **VMware Klasörü (`.zip`)** | [UBUNTU ama zip Klasörünü Aç](https://drive.google.com/drive/folders/1jj5whzaO3t8m82DYW6JDQkDBN73Sl2Eg?usp=sharing) | VMware Player, VMware Pro | `.zip` dosyasını klasöre çıkartın, VMware'de **Open a Virtual Machine** ile `.vmx` dosyasını seçin. |

### Sanal Makine Giriş Bilgileri ve Önemli Notlar
- **Ubuntu Kullanıcı Adı:** `emir`
- **Ubuntu Şifresi:** `[UBUNTU_SIFRENIZ]`
- **Önerilen Sistem:** En az 8 GB fiziksel RAM (sanal makine için 4–8 GB) ve 60 GB boş disk alanı
- **İlk Açılış Uyarısı:** `.zip` sürümünü ilk kez başlatırken ekrana *"This virtual machine might have been moved or copied"* uyarısı gelirse mutlaka **"I Copied It"** butonuna tıklayın.

---

## 3. Seçenek B: Temiz Ubuntu Üzerine Otomatik Kurulum (`setup.sh`)

Hazır imaj indirmek yerine kendi kurduğunuz temiz **Ubuntu 20.04 Desktop** sisteminin üzerine aynı paketleri, ROS/Gazebo depo anahtarlarını ve `catkin_ws` çalışma alanını tek komutla kurmak için terminali (`Ctrl + Alt + T`) açıp şu komutları çalıştırın:

    sudo apt update && sudo apt install -y open-vm-tools-desktop git
    git clone https://github.com/EBurak03/ubuntu-vm-rehberi.git
    cd ubuntu-vm-rehberi
    ./setup.sh

---

## 4. Yüklü Ana Bileşenler ve Yapılandırma
- **İşletim Sistemi & Ağ:** Ubuntu 20.04 Desktop (64-bit), NAT ağ bağdaştırıcısı
- **Robotik & Simülasyon:** ROS Noetic Desktop Full, Gazebo 11, TurtleBot3 paketleri, hazır `catkin_ws` çalışma alanı
- **Gömülü Sistem & Derleyiciler:** `gcc-arm-none-eabi`, `esptool`, `cmake`, `gdb-multiarch`, `clang`
- **Editör & Kütüphaneler:** Visual Studio Code (Snap), Mono, OpenCV (C++ ve Python), Eigen3
