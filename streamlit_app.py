import streamlit as st

import tkinter as tk
import random

# Funzione per generare la risposta del chatbot in base alla temperatura
def get_chatbot_response(temp):
    responses = [
        "Ciao! Come posso aiutarti?",
        "Oggi è una giornata fantastica!",
        "Che bella domanda! Fammi pensare...",
        "Sì, lo so, un sacco di cose!",
        "Wow, la temperatura è alta, lascia che ti dica una curiosità interessante!",
        "Ho tanti segreti da condividere! Hai mai sentito parlare di un dragone che vola sopra le montagne?"
    ]
    if temp > 30:
        return random.choice(responses)
    elif temp > 20:
        return "Sembra che il tempo sia perfetto per una passeggiata!"
    elif temp > 10:
        return "Un po' fresco oggi, ma comunque piacevole."
    else:
        return "Oggi è decisamente freddo, meglio stare al caldo!"

# Funzione per aggiornare la temperatura
def update_temperature():
    temp = int(temperature_slider.get())
    temperature_label.config(text=f"Temperatura: {temp}°C")
    chatbot_response = get_chatbot_response(temp)
    chatbot_text.config(state=tk.NORMAL)
    chatbot_text.delete(1.0, tk.END)  # Cancella la risposta precedente
    chatbot_text.insert(tk.END, chatbot_response)  # Inserisce la nuova risposta
    chatbot_text.config(state=tk.DISABLED)

# Creazione della finestra principale
root = tk.Tk()
root.title("Chatbot con Misuratore di Temperatura")
root.geometry("600x400")

# Frame per il chatbot
chatbot_frame = tk.Frame(root)
chatbot_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

# Area di testo per il chatbot
chatbot_text = tk.Text(chatbot_frame, wrap=tk.WORD, height=10, width=50, state=tk.DISABLED)
chatbot_text.pack(padx=10, pady=10)

# Barra laterale sinistra per il misuratore di temperatura
sidebar_frame = tk.Frame(root, width=150, bg="lightgray")
sidebar_frame.pack(side=tk.LEFT, fill=tk.Y)

# Etichetta della temperatura
temperature_label = tk.Label(sidebar_frame, text="Temperatura: 20°C", bg="lightgray", font=("Arial", 14))
temperature_label.pack(padx=10, pady=10)

# Slider per la temperatura
temperature_slider = tk.Scale(sidebar_frame, from_=0, to_=40, orient=tk.HORIZONTAL, command=lambda x: update_temperature())
temperature_slider.set(20)
temperature_slider.pack(padx=10, pady=10)

# Bottone per aggiornare la risposta del chatbot
update_button = tk.Button(sidebar_frame, text="Aggiorna Chatbot", command=update_temperature)
update_button.pack(padx=10, pady=10)

# Avvio dell'applicazione
root.mainloop()
