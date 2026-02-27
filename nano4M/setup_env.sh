conda create -n nanofm python=3.10 -y
source activate nanofm
pip install --upgrade pip
pip install -e .
pip install git+https://github.com/NVIDIA/Cosmos-Tokenizer.git --no-dependencies
python -m ipykernel install --user --name nanofm --display-name "nano4M kernel (nanofm)"