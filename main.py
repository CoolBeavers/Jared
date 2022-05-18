import sounddevice as sd
import time

import torch as torch

model_id = 'ru_v3'
sample_rate = 48000
speaker = 'aidar'

device = torch.device('cpu')
text = "Добро пожаловать, Вадим!"
