#!/usr/bin/env python
#coding=utf-8

# @Author:  Accagain
# @Date:    2019/03/27 14:37
# @File:    torch_examples.py

# @Content: study torch basic operations

import numpy as np
import torch
from torch import nn
from torch.nn import CrossEntropyLoss
import torch.nn.functional as F


def test_BiLSTM(x, x_mask):
    # batch_size = 2, seq_length = 6, hidden = 3
    lstm = nn.LSTM(input_size=4, hidden_size=2, num_layers=1, bidirectional=True)

    # sequence_output = np.array([[[0.1, 0.2, 0.1],
    #                              [0.4, 0.5, 0.6],
    #                              [0.1, 0.1, 0.1],
    #                              [0.2, 0.2, 0.2],
    #                              [0.3, 0.1, 0.2],
    #                              [0.4, 0.1, 0.3]], [[0, 0.1, 0.1],
    #                                                 [0.2, 0.3, 0.6],
    #                                                 [0.3, 0.2, 0.1],
    #                                                 [0.1, 0.1, 0.2],
    #                                                 [0.2, 0.2, 0.3],
    #                                                 [0.2, 0.3, 0.4]]])
    # x = torch.from_numpy(sequence_output)
    # x = x.type(torch.float32)
    # x_mask = torch.from_numpy(np.array([[1, 1, 1, 1, 0 ,0], [1, 1, 1, 1, 1, 0]]))
    x_lengths = x_mask.eq(1).sum(1)
    _, idx_sort = torch.sort(x_lengths, dim=0, descending=True) #
    _, idx_unsort = torch.sort(idx_sort, dim=0)
    x = x.index_select(0, idx_sort)
    x_lengths = x_lengths[idx_sort]
    x_packed = nn.utils.rnn.pack_padded_sequence(x, x_lengths, batch_first=True)
    y_packed, _ = lstm(x_packed)
    y_unpacked, _ = nn.utils.rnn.pad_packed_sequence(y_packed, batch_first=True)
    y_unpacked = y_unpacked.index_select(0, idx_unsort)

    if y_unpacked.size(1) != x_mask.size(1):
        padding = torch.zeros(y_unpacked.size(0), x_mask.size(1) - y_unpacked.size(1), y_unpacked.size(2)).type(
            y_unpacked.type())
        y_unpacked = torch.cat((y_unpacked, padding), dim=1)
    #return y_unpacked
    #print(idx_sort, idx_unsort, x_lengths, x_packed, y_packed, y_unpacked)
    return y_unpacked

def test_conv_and_pool():
    qa_outputs = nn.Linear(4, 2)
    na_linear = nn.Linear(6, 1)
    sequence_output = np.array([[[0.1, 0.2, 0.1, 0.2],
                                 [0.4, 0.5, 0.6, 0.3],
                                 [0.1, 0.1, 0.1, 0.1],
                                 [0.2, 0.2, 0.2, 0.1],
                                 [0.3, 0.1, 0.2, 0.2],
                                 [0.4, 0.1, 0.3, 0.4]], [[0, 0.1, 0.1, 0.2],
                                                    [0.2, 0.3, 0.6, 0.3],
                                                    [0.3, 0.2, 0.1, 0.1],
                                                    [0.1, 0.1, 0.2, 0.4],
                                                    [0.2, 0.2, 0.3, 0.1],
                                                    [0.2, 0.3, 0.4, 0.2]]])
    sequence_output = torch.from_numpy(sequence_output)
    sequence_output = sequence_output.type(torch.float32) # [batch_size, sequence_len, hidden_size]
    mask = torch.from_numpy(np.array([[1, 1, 1, 1, 0, 0], [1, 1, 1, 1, 1, 0]])) # [batch_size, seqence]
    pooled_output = torch.from_numpy(np.array([[0.1, 0.3, 0.2, 0.4], [0.4, 0.5, 0.6, 0.3]])).type(torch.float32)

    sequence_output1 = test_BiLSTM(sequence_output, mask)
    logits = qa_outputs(sequence_output1)
    start_logits, end_logits = logits.split(1, dim=-1)
    start_logits = start_logits.squeeze(-1)

    def _conv_and_pool(x):
        x = x.unsqueeze(1)
        conv = nn.Conv2d(in_channels=1, out_channels=2, kernel_size=(3, 4), padding=(1, 0))
        x = conv.forward(x)
        x = x.squeeze(3)
        # print(x)
        x = F.max_pool1d(x, x.size(2)).squeeze(2)
        return x

    sequence_output2 = test_BiLSTM(sequence_output, mask)
    na_logits = na_linear(torch.cat((pooled_output, _conv_and_pool(sequence_output2)), dim=1))


    print(start_logits, na_logits)



if __name__ == '__main__':
    #test_BiLSTM()
    test_conv_and_pool()