class Cliente:
    """Classe per rappresentare un cliente."""
    def __init__(self, nome, cognome, email, telefono):
        self.nome = nome
        self.cognome = cognome
        self.email = email
        self.telefono = telefono

    def __str__(self):
        return f"{self.nome} {self.cognome} - Email: {self.email}, Telefono: {self.telefono}"

class GestioneClienti:
    """Classe per gestire le operazioni sui clienti."""
    def __init__(self):
        self.clienti = []

    def aggiungi_cliente(self):
        """Aggiunge un nuovo cliente alla lista."""
        nome = input("Inserisci il nome del cliente: ")
        cognome = input("Inserisci il cognome del cliente: ")
        email = input("Inserisci l'email del cliente: ")
        telefono = input("Inserisci il numero di telefono del cliente: ")
        
        cliente = Cliente(nome, cognome, email, telefono)
        self.clienti.append(cliente)
        print("Cliente aggiunto con successo!")

    def visualizza_clienti(self):
        """Mostra tutti i clienti nella lista."""
        if not self.clienti:
            print("Nessun cliente trovato.")
            return

        print("\n--- Lista Clienti ---")
        for i, cliente in enumerate(self.clienti, start=1):
            print(f"{i}. {cliente}")

    def modifica_cliente(self):
        """Modifica le informazioni di un cliente esistente."""
        self.visualizza_clienti()
        if not self.clienti:
            return

        indice = int(input("Inserisci il numero del cliente da modificare: ")) - 1
        if 0 <= indice < len(self.clienti):
            cliente = self.clienti[indice]
            print("\nModifica le informazioni (lascia vuoto per mantenere il valore attuale):")
            cliente.nome = input(f"Nome ({cliente.nome}): ") or cliente.nome
            cliente.cognome = input(f"Cognome ({cliente.cognome}): ") or cliente.cognome
            cliente.email = input(f"Email ({cliente.email}): ") or cliente.email
            cliente.telefono = input(f"Telefono ({cliente.telefono}): ") or cliente.telefono
            print("Informazioni del cliente aggiornate con successo!")
        else:
            print("Cliente non trovato.")

    def elimina_cliente(self):
        """Elimina un cliente dalla lista."""
        self.visualizza_clienti()
        if not self.clienti:
            return

        indice = int(input("Inserisci il numero del cliente da eliminare: ")) - 1
        if 0 <= indice < len(self.clienti):
            self.clienti.pop(indice)
            print("Cliente eliminato con successo!")
        else:
            print("Cliente non trovato.")

    def menu(self):
        """Menu principale del programma."""
        while True:
            print("\nGestione Clienti")
            print("1. Aggiungi Cliente")
            print("2. Visualizza Clienti")
            print("3. Modifica Cliente")
            print("4. Elimina Cliente")
            print("5. Esci")

            scelta = input("Scegli un'opzione: ")

            if scelta == "1":
                self.aggiungi_cliente()
            elif scelta == "2":
                self.visualizza_clienti()
            elif scelta == "3":
                self.modifica_cliente()
            elif scelta == "4":
                self.elimina_cliente()
            elif scelta == "5":
                print("Uscita dal programma.")
                break
            else:
                print("Opzione non valida, riprova.")

# Avvio del programma
gestione_clienti = GestioneClienti()
gestione_clienti.menu()
