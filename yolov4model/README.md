## yolov4 custom training for camparing the faces of the employees 
the trained weights are avliable at [weights for yolov4](https://drive.google.com/file/d/1-80De2OXeJby9ne6d2gCP_lfB3FrU4UM/view?usp=sharing) these are avaliable only of dowell members.

#### training
the traing part is avaliable [here](https://github.com/LL05-AI-Dowell/R05.003.conversion-to-csv-and-extracting-frames.Dowell/blob/Branch-1/yolov4model/training/training_the_model.ipynb)

### to run the script
install requirments.txt
pip install -r requirments.txt


download the weights from the above link
keep them in the same folder from where you are running the script [main.py](https://github.com/LL05-AI-Dowell/R05.003.conversion-to-csv-and-extracting-frames.Dowell/blob/Branch-1/yolov4model/main.py)

keep the [obj.names](https://github.com/LL05-AI-Dowell/R05.003.conversion-to-csv-and-extracting-frames.Dowell/blob/Branch-1/yolov4model/obj.names) file in the same directory

and [yolov4_custom.cfg](https://github.com/LL05-AI-Dowell/R05.003.conversion-to-csv-and-extracting-frames.Dowell/blob/Branch-1/yolov4model/yolov4-custom.cfg)

#### after that run the script using 
python3 main.py


###  The results are here

<p align="center">
  <img src="https://raw.githubusercontent.com/LL05-AI-Dowell/R05.003.conversion-to-csv-and-extracting-frames.Dowell/Branch-1/yolov4model/training/chart.png" align="center" alt="Result Chart" width="480" height="260">
</p>
<h1 align="center"><b><i>Performance of the model</i></b></h1>

### Testing of the model
<p align="center">
  <img src="https://raw.githubusercontent.com/LL05-AI-Dowell/R05.003.conversion-to-csv-and-extracting-frames.Dowell/Branch-1/yolov4model/training/Screenshot%20from%202021-03-20%2022-50-12.png" align="center" alt="Test" width="480" height="260">
</p>
<h1 align="center"><b><i>Prediction of our model</i></b></h1>



