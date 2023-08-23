import os
import shutil
import time
import sys
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = r"C:\Users\Leandro Miranda\Downloads"
to_dir = r"C:\Users\Leandro Miranda\Downloads\imagens2"

dir_tree = {
    "Image_files": ['.jpg', '.jpeg', '.png', '.gif', '.jfif'],
    "Video_files": ['.mpg', '.mp2', '.mpeg', '.mpv', '.mp4', '.m4p', '.m4v', '.avi', '.mov'],
    "Document_files": ['.pdf', '.txt'],
    "Setup_files": ['.exe', '.cmd']
}
# Classe Gerenciadora de Eventos.

class FileMovementHandler(FileSystemEventHandler):
    def on_created(self, event):
        print(event)
        print(event.src_path) 
    def on_deleted(self, event):
        print(f"Opa, alguém excluiu uma pasta {event.src_path}")
    def on_modified(self, event):
        print("Olá {event.src_path} foi modificada")
    def on_moved(self, event):
        print("Olá, a {event.src_path} foi movida")
# Inicialize a classa para escutar a movimentação dos arquivos
event_handler = FileMovementHandler()

# Inicialize o observador
observer = Observer()

# Agendar a observação
observer.schedule(event_handler, from_dir, recursive=True)

observer.start()

try:
    while True:
        time.sleep(2)
        print("executando. . .")
except KeyboardInterrupt:
    print("interrompido")
    observer.stop()



