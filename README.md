# Llama2-on-CPU

## User Interface :
![Screenshot 2024-04-05 140320](https://github.com/HarshalGidh/Llama2-on-CPU/assets/126465410/4ad0e91e-3d7b-4a18-af7c-e6ba150b13fa)


# How to run?

### Steps 1:

clone the repository

```bash
git clone https://github.com/
```

### Steps 2:

Create a virtual environment

```bash
conda create -n cpullama python=3.8 -y
```

```bash
conda activate cpullama
```

```bash
pip install -r requirements.txt
```

```bash
python app.py
```


### Download the quantize model from the link provided in model folder & keep the model in the model directory:

```ini
## Download the Llama 2 Model:

llama-2-7b-chat.ggmlv3.q4_0.bin


## From the following link:
https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML/tree/main
```

## Output by the Model :
![Screenshot 2024-04-05 140601](https://github.com/HarshalGidh/Llama2-on-CPU/assets/126465410/61c1d3c1-2ab6-4845-9640-2a598c712aeb)
