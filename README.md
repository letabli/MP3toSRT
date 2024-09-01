### Install Required Libraries
First, you need to install the Whisper model and any other dependencies:

```shell
pip install git+https://github.com/openai/whisper.git
pip install torch
pip install tqdm
```

### 호환성 관리
* GPU 하드웨어에 맞는 CUDA 드라이버를 설치할 필요
* GTX 1660 Ti는 CUDA SDK 11.2를 설치
* CUDA 11.2에 맞게 torch 버전을 설치해야 한다. 안 그러면 프로그램이 GPU를 활용하지 못하고 CPU를 활용하면서 굉장히 느리게 돌아간다.

```shell
pip uninstall torch torchvision torchaudio
pip install torch==1.12.0+cu113 torchvision torchaudio -f https://download.pytorch.org/whl/torch_stable.html
```
