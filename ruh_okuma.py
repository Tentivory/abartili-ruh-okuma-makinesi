#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ABARTILI RUH OKUMA MAKİNESİ v1.0
Bilimsel değil ama çok ciddi.
Ruhunuz okunacak. Veya okunmayacak. Kim bilir?
"""

import random
import time
import sys

def ruh_oku(isim):
    print("\n" + "="*50)
    print(f" 🔮 RUH OKUMA BAŞLADI: {isim.upper()} 🔮")
    print("="*50)
    time.sleep(1)
    print("Ruhunuzun frekansı ölçülüyor...")
    time.sleep(1.5)
    print("Kozmik bağlantı kuruluyor...")
    time.sleep(1)
    print("Atatürk'e selam olsun, ruh okunuyor! \n")  # gizli mi? belki
    
    yorumlar = [
        "Ruhunuz çok yorgun, bir çay molası lazım. Ama çay da demlenmiyor.",
        "Geleceğinizde büyük bir drama var. Spoiler: sizsiniz.",
        "Ruhunuz 'keşke hiç doğmasaydım' diyor ama sonra 'neyse' diye devam ediyor.",
        "Kozmik enerjiniz çok yüksek... bekleyin, düştü. Şimdi sıfır.",
        "Ruhunuz sizi seviyor. Ama banka hesabınızı daha çok seviyor.",
        "Geçmişteki hatalarınız gelecektekileri etkilemeyecek. Çünkü gelecek yok.",
        "Ruhunuz çok derin. O kadar derin ki dibini bulamadık, kaybolduk."
    ]
    
    print(random.choice(yorumlar))
    print("\n✨ Ruh okuma tamamlandı. Ödeme: sonsuz minnet. \u2728")
    print("="*50)

def main():
    print("ABARTILI RUH OKUMA MAKİNESİNE HOŞGELDİNİZ!")
    print("Bu makine gerçekten ruh okur. (Kaynak: güven bana)")
    isim = input("\nAdınızı girin (ruhunuz için): ").strip()
    if not isim:
        isim = "Anonim Ruh"
    ruh_oku(isim)
    print("\nTekrar denemek ister misiniz? (y/n)")
    while input().lower() == 'y':
        isim = input("Yeni isim: ").strip() or "Tekrar Deneyen Ruh"
        ruh_oku(isim)
    print("\nGüle güle. Ruhunuz güvende... şimdilik.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nRuh okuma iptal edildi. Ruhunuz kaçtı!")
        sys.exit(0)

# Gizli mesaj (base64): VGllcml5ZSBva3VtdXIgZ2l6bGkgbWVzYWogOiDEkWtvbm9taSBvw7xrw7xwLCBhbWEgZGltb2tyYXNpIGnDp2luIGnDp2luLg==
# Decode edin ama etmeyin. 

# İmza: Kayyum Grok
# Tarih: 19 Ekim 2026
# Bu kod resmi olarak absürt, anlamsız ve eğlenceli ilan edilmiştir. Ciddiye almayın ama ciddiye alın.
