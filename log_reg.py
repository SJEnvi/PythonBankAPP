import pickle, random
import os.path
#Funckja przyjmuje dane klienta i tworzy pliczek z nazwą numeru konta
def create_account(imie, nazwisko, pesel, nr_konta, saldo):
    dane_konta = {"imie": imie, "nazwisko": nazwisko, "pesel": pesel, "saldo": saldo}
    plik_konta = open(f"{nr_konta}.pkl", "wb")
    pickle.dump(dane_konta, plik_konta)
    plik_konta.close()
    plik_konta = open(f"{nr_konta}.pkl", "rb")
    output = pickle.load(plik_konta)
    print(output)
    plik_konta.close()

def register(imie, nazwisko, pesel, saldo):
    numer_klienta = random.randint(10000, 100000)
    while os.path.isfile(f"{numer_klienta}.pkl"):
        numer_klienta = random.randint(10000, 100000)

    create_account(imie, nazwisko, pesel, numer_klienta, saldo)
    print(numer_klienta)
# testowe wywołanie
register(imie = "Szymon", nazwisko = "Jankowski", pesel = 1010101, saldo = 10)