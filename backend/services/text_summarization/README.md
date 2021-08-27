# Text Summarization Using T5
Performing abstractive text summarization task using T5, and serving it via REST API.

- More about T5(text-to-text-transfer-transformer) can be found [here](https://huggingface.co/transformers/model_doc/t5.html)
- T5 paper can be found [here](https://github.com/R-aryan/Text-Summarization-Using-T5/blob/develop/msc/t5_paper.pdf)
- End to End NLP  abstractive text summarization Problem.
- The Kaggle dataset can be found Here [Click Here](https://www.kaggle.com/sunnysai12345/news-summary)
- My kaggle Notebook can be found [here](https://www.kaggle.com/raryan/t5-abstractive-text-summarization)


## Steps to Run the Project:
- What is [**Virtual Environment in python ?**](https://www.geeksforgeeks.org/python-virtual-environment/)
- [Create virtual environment in python](https://www.geeksforgeeks.org/creating-python-virtual-environment-windows-linux/)
- [Create virtual environment Anaconda](https://www.geeksforgeeks.org/set-up-virtual-environment-for-python-using-anaconda/)
- create a virtual environment and install [requirements.txt](https://github.com/R-aryan/Text-Summarization-Using-T5/blob/develop/requirements.txt)


### For Training/Fine-Tuning
- After Setting up the environment go to **backend/services/text_summarization/application/ai/training/** and run **main.py** and the training will start.
- After training is complete the weights of the model will be saved in weights directory, and this weights can be used for inference.



