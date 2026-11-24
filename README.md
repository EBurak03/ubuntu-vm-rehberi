# VMware Ubuntu 20.04 Geliştirme Ortamı (ROS Noetic & Gazebo 11)

Bu depo; VMware üzerinde çalışan **Ubuntu 20.04 LTS (Focal)** sanal makinesinin hazır imaj indirme bağlantılarını, kurulum adımlarını, yüklü sistem/ROS/Python paket listelerini ve `catkin_ws` çalışma alanı yapılandırmasını içerir.

---

## Seçenek 1: Hazır Sanal Makine İmajını İndir (Kurulumsuz)

Sıfırdan kurulum adımlarıyla uğraşmadan tüm paketlerin, depo anahtarlarının ve çalışma ortamının hazır olduğu sanal makineyi doğrudan indirebilirsiniz.

> **Not:** İndireceğiniz paketlerin içinde Ubuntu 20.04 ve yüklü tüm programlar/ayarlar mevcuttur; ancak sanallaştırma programının kendisi dahil değildir. Başlamadan önce bilgisayarınızda **VMware Workstation 17 Player** (veya `.ova` için **VirtualBox**) kurulu olmalıdır.

| Paket Formatı | Google Drive İndirme Bağlantısı | Uyumlu Programlar | Nasıl Çalıştırılır? |
| :--- | :--- | :--- | :--- |
| **Evrensel İmaj (`.ova`)** | [UBUNTU ama ova Klasörünü Aç](https://drive.google.com/drive/folders/1aqVtQD4IpLpWMVB0WZM79LHmjMahRcwg?usp=sharing) | VMware Player, VMware Pro, VirtualBox | İndirdiğiniz `.ova` dosyasına çift tıklayın (veya programda **File > Open / Import** seçin) ve **Import** butonuna basın. |
| **VMware Klasörü (`.zip`)** | [UBUNTU ama zip Klasörünü Aç](https://drive.google.com/drive/folders/1jj5whzaO3t8m82DYW6JDQkDBN73Sl2Eg?usp=sharing) | VMware Player, VMware Pro | `.zip` dosyasını klasöre çıkartın, VMware'de **Open a Virtual Machine** ile `.vmx` dosyasını seçin. |

### Sanal Makine Giriş Bilgileri ve Önerilen Ayarlar
- **Ubuntu Kullanıcı Adı:** `emir`
- **Ubuntu Şifresi:** `[UBUNTU_SIFRENIZ]`
- **Önerilen Sistem:** En az 8 GB fiziksel RAM (sanal makine için 4–8 GB) ve 60 GB boş disk alanı
- **İlk Açılış Uyarısı:** `.zip` sürümünü ilk kez başlatırken ekrana *"This virtual machine might have been moved or copied"* uyarısı gelirse mutlaka **"I Copied It"** butonuna tıklayın.

---

## Seçenek 2: Temiz Ubuntu Üzerine Otomatik Kurulum (`setup.sh`)

Hazır imaj indirmek yerine kendi kurduğunuz temiz **Ubuntu 20.04 Desktop** sisteminin üzerine aynı paketleri, ROS/Gazebo depo anahtarlarını ve `catkin_ws` çalışma alanını tek komutla kurmak için:

1. Ubuntu kurulumunu tamamladıktan sonra terminali açın (`Ctrl + Alt + T`).
2. Ekran çözünürlüğü, kopyala-yapıştır desteği ve Git için gerekli araçları kurun:

       sudo apt update && sudo apt install -y open-vm-tools-desktop git

3. Bu depoyu bilgisayarınıza indirin ve otomatik kurulumu başlatın:

       git clone https://github.com/EBurak03/ubuntu-vm-rehberi.git
       cd ubuntu-vm-rehberi
       ./setup.sh

---

## Yüklü Ana Bileşenler ve Yapılandırma
- **İşletim Sistemi & Ağ:** Ubuntu 20.04 Desktop (64-bit), NAT ağ bağdaştırıcısı
- **Robotik & Simülasyon:** ROS Noetic Desktop Full, Gazebo 11, TurtleBot3 paketleri, hazır `catkin_ws` çalışma alanı
- **Gömülü Sistem & Derleyiciler:** `gcc-arm-none-eabi`, `esptool`, `cmake`, `gdb-multiarch`, `clang`
- **Editör & Kütüphaneler:** Visual Studio Code (Snap), Mono, OpenCV (C++ ve Python), Eigen3
