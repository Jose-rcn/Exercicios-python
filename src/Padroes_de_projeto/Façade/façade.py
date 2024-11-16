# Subsistema do Home Theater
class Projector:
    def on(self):
        print("Projetor ligado.")
    
    def off(self):
        print("Projetor desligado.")
    
    def set_input(self, input_source):
        print(f"Projetor configurado para a fonte de entrada: {input_source}.")

class SoundSystem:
    def on(self):
        print("Sistema de som ligado.")
    
    def off(self):
        print("Sistema de som desligado.")
    
    def set_volume(self, volume):
        print(f"Volume do sistema de som ajustado para {volume}.")

class MediaPlayer:
    def on(self):
        print("Player de mídia ligado.")
    
    def off(self):
        print("Player de mídia desligado.")
    
    def play(self, movie):
        print(f"Reproduzindo o filme: {movie}")

# Classe Facade
class HomeTheaterFacade:
    def __init__(self):
        self.projector = Projector()
        self.sound_system = SoundSystem()
        self.media_player = MediaPlayer()
    
    def start_movie(self, movie):
        print("\nIniciando o sistema de home theater...\n")
        self.projector.on()
        self.projector.set_input("HDMI")
        self.sound_system.on()
        self.sound_system.set_volume(30)
        self.media_player.on()
        self.media_player.play(movie)
        print("\nFilme iniciado com sucesso!\n")
    
    def end_movie(self):
        print("\nDesligando o sistema de home theater...\n")
        self.media_player.off()
        self.sound_system.off()
        self.projector.off()
        print("Sistema de home theater desligado.")

# Uso do Facade
home_theater = HomeTheaterFacade()
home_theater.start_movie("Inception")
home_theater.end_movie()
