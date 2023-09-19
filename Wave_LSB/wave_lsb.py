import wave

secret = "" #Nhet Secret vao.

with wave.open("D:\Downloads\Glorious_Morning.wav", "rb") as song:
    n_channels = song.getnchannels()
    sample_width = song.getsampwidth()
    frame_rate = song.getframerate()
    n_frames = song.getnframes()
    compression_type = song.getcomptype()
    compression_name = song.getcompname()
    
    frames = bytearray(list(song.readframes(n_frames)))

#Padding with trash characters
secret = secret + int((len(frames) - (len(secret) * 8 * 8)) / 8) * '#'

#convert secret to binary list
secret_bits = list(map(int, ''.join([bin(ord(i)).lstrip('0b').rjust(8, '0') for i in secret])))

for i, bit in enumerate(secret_bits):
    frames[i] = frames[i] & 254 | bit
    #print(frames[i], end = '')

modified_frames = bytes(frames)

with wave.open("Embeded.wav", "wb") as f:
    f.setparams(song.getparams())
    f.writeframes(modified_frames)

song.close()
