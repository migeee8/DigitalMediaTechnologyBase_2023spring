import wave
import numpy as np
import matplotlib.pyplot as plt

# 宽带
with wave.open("./data/audio.wav", "rb") as wavfile:
    framerate = wavfile.getframerate() # 采样率
    framesize = 32 # 帧长，必须为2^n，n取小（如32，画出的图为宽带频谱图），n取大（如2048，画出的图为窄带频谱图）
    NFFT = framesize # 计算离散傅里叶变换的点数，NFFT必须与时域的点数framsize相等，即不补零的FFT
    overlapSize = 1.0 / 2 * framesize # 设置帧与帧重叠部分采样点数，overlapSize约为每帧点数的1/3~1/2
    overlapSize = int(round(overlapSize)) # 取整
    # 读取音频数据
    nframes = wavfile.getnframes()
    waveData = np.frombuffer(wavfile.readframes(nframes), dtype=np.short)
    # 绘制频谱图
    plt.specgram(waveData, NFFT=NFFT, Fs=framerate, window=np.hanning(M=framesize), noverlap=overlapSize)
    plt.title("Wide Band Spectrum")
    plt.ylabel('Frequency')
    plt.xlabel('Time')
    plt.ylim(0, 6000)
    plt.show()

#窄带
with wave.open("./data/audio.wav", "rb") as wavfile:
    framerate = wavfile.getframerate() # 采样率
    framesize = 2048 # 帧长，必须为2^n，n取小（如32，画出的图为宽带频谱图），n取大（如2048，画出的图为窄带频谱图）
    framelength = framesize / framerate
    NFFT = framesize # 计算离散傅里叶变换的点数，NFFT必须与时域的点数framsize相等，即不补零的FFT
    overlapSize = 1.0 / 2 * framesize # 设置帧与帧重叠部分采样点数，overlapSize约为每帧点数的1/3~1/2
    overlapSize = int(round(overlapSize)) # 取整
    # 读取音频数据
    nframes = wavfile.getnframes()
    waveData = np.frombuffer(wavfile.readframes(nframes), dtype=np.short)
    # 绘制频谱图
    plt.specgram(waveData, NFFT=NFFT, Fs=framerate, window=np.hanning(M=framesize), noverlap=overlapSize)
    plt.title("Narrow Band Spectrum")
    plt.ylabel('Frequency')
    plt.xlabel('Time')
    plt.ylim(0, 6000)
    plt.show()