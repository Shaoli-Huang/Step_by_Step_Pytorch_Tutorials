# Pytorch_Tutorials






## Set Up Enviroment and Install Required Packages

1. Install [`miniconda`](http://conda.pydata.org/miniconda.html)
2. Create and activate a conda enviroment  

    ```
    conda create -n pytorch_env
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
    Verify the pytorch tensorboard
    `python tensorboard_test_script.py`
    Run `tensorboard --logdir=runs`  and type http://localhost:6006/ in your browser to access the Tensorboard
    
5. Install PyTorchViz

    ```
    pip install torchviz
    ```

6. Install Jupyter and Jupyter conda extension

    ```
    pip install jupyter
    conda install nb_conda
    ```

    Run `source activate pytorch_env && jupyter notebook` to activate conda enviroment and assess the Jupyter notebook



    




