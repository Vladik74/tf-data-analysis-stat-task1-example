import pandas as pd
import numpy as np


chat_id = 773978697 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    mu = -27+np.exp(1)
    var = (np.exp(2)-54)*mu**2
    a = 10/(x.mean()**2)
    return a
