import torch

class default:
    #default values
    MODEL_DEF = "medium"
    VIDEO_LANGUAGE_DEF = "english"
    SUBS_LANGUAGE_DEF = "english"
    DEVICE_DEF = "cuda:0" if torch.cuda.is_available() else "cpu"

DEFAULT = default()