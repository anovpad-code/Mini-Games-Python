import random

def game():
    options = ["batu", "gunting", "kertas"]
    print("=== SUIT JEPANG v1.0 === ")
    
    user = input("Pilih (batu/gunting/kertas): ").lower()
    comp = random.choice(options)
    
    print(f"Komputer memilih: {comp}")
    
    if user == comp:
        print("Hasil: SERI!")
    elif (user == "batu" and comp == "gunting") or \
         (user == "gunting" and comp == "kertas") or \
         (user == "kertas" and comp == "batu"):
        print("Hasil: KAMU MENANG! ")
    else:
        print("Hasil: KAMU KALAH!")

game()
