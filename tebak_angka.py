import random

def play():
    secret_number = random.randint(1, 100)
    attempts = 0
    print("===  TEBAK ANGKA BY ANGEL ===")
    print("Aku memikirkan angka antara 1 sampai 100.")

    while True:
        guess = int(input("Tebakanmu: "))
        attempts += 1
        
        if guess < secret_number:
            print("Terlalu rendah! Coba lagi.")
        elif guess > secret_number:
            print("Terlalu tinggi! Coba lagi.")
        else:
            print(f" HEBAT! Kamu berhasil menebak angka {secret_number} dalam {attempts} kali percobaan.")
            break

if __name__ == "__main__":
    play()
