import time
from plyer import notification

def show_notification(title, message):
    notification.notify(
        title=title,
        message=message,
        app_name="Beko Bildirim Uygulaması",
        timeout=10  # Bildirimin ekranda kalma süresi (saniye cinsinden)
    )

if __name__ == "__main__":
    try:
        while True:
            show_notification("BEKO", "BEKO IKC")
            time.sleep(3600)
    except KeyboardInterrupt:
        print("Uygulama kapatıldı.")