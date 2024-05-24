import wave
import matplotlib.pyplot as plt
import numpy as np
import os
import math

#读取本地音频
f = wave.open("./data/audio.wav",'rb')
#获取音频参数
params = f.getparams() 
nchannel,sampwidth,framerate,nframes = params [:4]
print(nchannel,sampwidth,framerate,nframes)
#2 2 44100 6140484

#读取多通道音频
strData = f.readframes(nframes)
waveData = np.frombuffer(strData,dtype=np.int16).reshape(-1,nchannel)

# 归一化
waveData = waveData.astype(np.float32)
max_sample = np.max(np.abs(waveData))
waveData /= max_sample

# 创建一个0~nframe单位时间为1frame的数组
time = np.arange(0,nframes)*(1.0/framerate)


# 绘图(单通道)
plt.plot(time, waveData[:, 1])
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.title("Single Channel Wave Data")
plt.legend()
plt.show()

# 绘图(多通道)
plt.figure()
plt.subplot(3,1,1) 
plt.plot(time,waveData[:,0]) 
plt.xlabel("Time(s)") 
plt.ylabel("Amplitude") 
plt.title("Ch-1 wavedata") 
plt.subplot(3,1,3) 
plt.plot(time,waveData[:,1]) 
plt.xlabel("Time(s)") 
plt.ylabel("Amplitude") 
plt.title("Ch-2 wavedata") 
plt.show()
