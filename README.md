- 40_datamake.py
  - data maker for test and train
  - should use `conv_num.py`
  - checks `./data/`
  - outputs the separated data into `./sep_data/`

- src/
  - contains estimater by weighted sum of basis functions
  - note to makedir `./sep_data/{(int)USER_ID}/output/`

- nn_src/
  - contains estimater by neural net
  - 40_nntrain.py
    - is to train model
  - 40_nnest.py
    - is for test

