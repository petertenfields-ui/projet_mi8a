#READS MICROPHONE AUDIO
import sounddevice as sd
def open_microphone(sample_rate=44100, block_size = 2048,device = None):
    return sd.InputStream(sample_rate = sample_rate,
                          block_size = block_size,
                          device = device
                          )