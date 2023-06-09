# ASR Punctuation and Capitalisation Restoration
The code for fine-tuning Google T5 for punctuation and capitalisation restoration for the dataset of old newspapers (https://www.kaggle.com/datasets/alvations/old-newspapers).
There is the code for data extraction phase as well as the pre-processinng phase and post-processing pahse and the final figures we created from the results. 
Due to the size of the models and the dataset those are ommited, the dataset can be found and downloaded from the link above and the model plus the results folder can be obtain from running the code. The process for recreating our result is: 

1) Download newpapers (https://www.kaggle.com/datasets/alvations/old-newspapers), extract zip, create a folder names articles and run dataset_extract.
2) Run pre_process. 
3) Create needed folders with the lanaguges and the model used.
4) Run T5.
5) Run postprocess.
6) Run compute_wer.
7) Run results_figures_extraction.
