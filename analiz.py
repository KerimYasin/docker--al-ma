# islem.py
import os

print("Docker konteyneri içinden selamlar! Analiz başlıyor...")

try:
    with open('/workspace/karakterler.txt', 'r', encoding='utf-8') as f:
        icerik = f.read()

    # Noktalama işaretlerini temizle ve küçük harfe çevir
    temiz_icerik = icerik.lower().replace('.', '').replace(',', '')
    kelimeler = temiz_icerik.split()
    
    # Kelime sayımı
    frekans = {}
    for k in kelimeler:
        frekans[k] = frekans.get(k, 0) + 1

    # Sonucu yeni bir dosyaya yazdır
    cikis_yolu = '/workspace/analiz_sonucu.txt'
    with open(cikis_yolu, 'w', encoding='utf-8') as f:
        f.write("Kelime Frekans Analizi\n")
        f.write("-" * 22 + "\n")
        for kelime, sayi in sorted(frekans.items(), key=lambda x: x[1], reverse=True):
            f.write(f"{kelime}: {sayi}\n")

    print(f"İşlem başarılı! Sonuçlar '{cikis_yolu}' dosyasına kaydedildi.")

except Exception as e:
    print(f"Bir hata oluştu: {e}")