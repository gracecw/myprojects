## AI Novel Writer - Char-rnn text generator
Implemented a character-level Recurrent Neural Network in PyTorch to generate novel paragraphs, training on English and Chinese novels (Pride and Prejudice and 笑傲江湖） 
- Pride and Prejudice - still in training (2 layer GRU, dropout 0.2, hidden layer size 512, lr 0.005, temperature 0.8)
- Xiaoao/Xiaoao2 - trained on Chinese Novel 笑傲江湖 with 2 layer LSTM, hiddeen layer 512, lr 0.005. Current loss ~ 1.6
- Comparison on hyperparameter tuning (GRU vs LSTM, dropout, lr, temperature) to follow
