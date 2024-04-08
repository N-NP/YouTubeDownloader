import customtkinter as ctk
from tkinter import ttk
from pytube import YouTube
import os

#criando função do download
def download_video ():
    url = entry_url.get()
    resolution = resolution_var.get()

    progress_label.pack(pady=10)
    progress_bar.pack(pady=10)
    status_label.pack(pady=10)

    try:
        yt = YouTube(url, on_progress_callback = on_progress)
        stream = yt.streams.filter(res=resolution).first()
        #Download do video em um pasta expecifica
        os.path.join("downloads", f"{yt.title}.mp4")
        stream.download(output_path="downloads")
        status_label.configure(text="")
        status_label.configure(text="Concluido!", text_color="white", fg_color="green")

    except Exception as e:
        status_label.configure(text=f"Error {str(e)}", text_color="white", fg_color="red")

#Criando o processo da barra de progresso
def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_completed = bytes_downloaded / total_size * 100

    progress_label.configure(text=str(int(percentage_completed)) + "%")
    progress_label.update()

    progress_bar.set(float(percentage_completed / 100))

def combobox_callback(resolution_var):
    status_label.pack_forget()
    
    if resolution_var == "1080p":
        status_label.configure(text="Nesta qualidade é somente video.", text_color="white", fg_color="red")
        status_label.pack(pady=10)

#criar a janela raiz
root = ctk.CTk()
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

#Titulo da Janela
root.title("Youtube Downloader  by. Birula")

#set o largura e altura maxima da janela
root.geometry("720x380")
root.minsize(720, 380)
root.maxsize(720, 380)

#Criar um frame para receber o conteudo
content_frame = ctk.CTkFrame(root)
content_frame.pack(fill=ctk.BOTH, expand=True, padx=10, pady=10)

#criar label e a entrada da url
url_label = ctk.CTkLabel(content_frame, text="Insira o link do video para download")
entry_url = ctk.CTkEntry(content_frame, width=500, height=40)
url_label.pack(pady=10)
entry_url.pack(pady=10)

#Criar Botão de Download
download_button = ctk.CTkButton(content_frame, text="Download", command= download_video)
download_button.pack(pady=10)

#criar a combo box da resolução que vai ser downloaded
resolutions = ["1080p", "720p", "360p"]
resolution_var = ctk.StringVar()
#resolution_combobox = ttk.Combobox(content_frame, values= resolutions, textvariable=resolution_var)
resolution_combobox = ctk.CTkComboBox(content_frame, values= resolutions,command=combobox_callback, variable=resolution_var)
resolution_combobox.pack(pady=10)
resolution_combobox.set("")

#criar a label de progresso do download
progress_label = ctk.CTkLabel(content_frame, text="0%")

progress_bar = ctk.CTkProgressBar(content_frame, width=400)
progress_bar.set(0)

#criar a barra de status
status_label = ctk.CTkLabel(content_frame, text="")

#para iniciar a janela
root.mainloop()