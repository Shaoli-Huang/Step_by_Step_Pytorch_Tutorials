# Pytorch_Tutorials






## Set Up Enviroment and Install Required Packages

1. Install [`miniconda`](http://conda.pydata.org/miniconda.html)
2. Create and activate a conda enviroment  

    ```
    conda create -n pytorch_env && source activate pytorch_env
    ```
3. Install Pytorch and verify installation success

    ```
    conda install pytorch torchvision -c pytorch
    python -c 'import torch; print(torch.rand(2,3));print(torch.cuda.is_available())'
    ```

4. Install tensorboard and pytorch tensorboard utils

    ```
    pip install tensorboard
    pip install tb-nightly
    pip install -r requirements.txt
    ```
    
5. Install PyTorchViz

    ```
    pip install torchviz
    ```



    




