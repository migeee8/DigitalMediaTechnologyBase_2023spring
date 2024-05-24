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


#语音信号段时能量
def calEnergy(wave_data):
    energy = [] #数组存储每一帧的能量值
    sum = 0
    frameSize = 256
    #每256个采样点为一帧，能量取帧内所有值的平方和
    for i in range(len(wave_data)):
        sum = sum + (wave_data[i] * wave_data[i])
        if (i+1) % frameSize == 0:
            energy.append(sum)
            sum=0 #清零
        elif i == len(wave_data) - 1 : #音频数据末端处理
            energy.append(sum)
    return energy

energy = calEnergy(waveData[:,0])
time2 = np.arange(0,len(energy))*(nframes/len(energy)/framerate)

plt.plot(time2, energy)
plt.ylabel("short energy")
plt.xlabel("time(seconds)")
plt.show()


#语音信号短时过零率
def ZeroCR(wave_data,frameSize,overlap):
    wlen = len(wave_data)
    step = frameSize - overlap
    frameNum = math.ceil(wlen/step)
    zcr = np.zeros((frameNum,1))
    for i in range(frameNum):
        curFrame = wave_data[np.arange(i*step,min(i*step+frameSize,wlen))]
        curFrame = curFrame - np.mean(curFrame)
        zcr[i] = sum(curFrame[0:-1]*curFrame[1::]<=0)
    return zcr

frameSize = 256
overLap = 0
zcr = ZeroCR(waveData[:,0],frameSize,overLap)
time3 = np.arange(0, len(zcr)) * (nframes/len(zcr) / framerate)
plt.plot(time3, zcr)
plt.ylabel("ZCR")
plt.xlabel("time (seconds)")
plt.show()
