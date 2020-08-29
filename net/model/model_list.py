from .model import *

match_list = {
    "CNN": CNN,
    "MultiLSTM": MultiLSTM,
    "CNNSeq": CNNSeq,
    "MultiLSTMSeq": MultiLSTMSeq,
    "Article": Article,
    "LSTM": LSTM,
    "ArtFact": NNFactArt,
    "ArtFactSeq": NNFactArtSeq,
    "Pipeline": Pipeline,
    "HLSTMSeq": HLSTMSeq
}


def get_model(model_name, config, usegpu):
    try:
        net = match_list[model_name](config, usegpu)
        return net
    except:
       print("No such a model")

