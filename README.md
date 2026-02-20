# COM-304 Intelligent systems: communications & AI.
## Foundation models (FM) track. 

The goal of this project is to familiarize you with the essential building blocks that make up modern large language and multimodal models. 

To prepare you for this, we will distribute homeworks that teach you the basics of **[PyTorch](https://pytorch.org/)** and computing clusters like **[SCITAS](https://www.epfl.ch/research/facilities/scitas/)**, which will be used throughout this course. 

Throughout the course, you will get familiar with key concepts and models such as **[GPT](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf)**, **[MaskGIT](https://masked-generative-image-transformer.github.io/)**, **[4M](https://4m.epfl.ch/)**, **[Flow Matching](https://arxiv.org/abs/2210.02747)**, and **[Vision-Language Models (VLMs)](https://llava-vl.github.io)**, gaining a practical understanding of how modern multimodal foundation models are designed and trained.

The main part of the exercises will be about implementing `nano4M`, a minimal version of 4M, which will give you a practical understanding of how to design and train multimodal foundation models. In addition, you will implement a series of extensions of your choice on top of the `nano4M` codebase.

![4M Architecture](./assets/4M_architecture.png)

Following the `nano4M` exercise, there will be two advanced exercises, one on **Flow Matching** (`nanoFlowMatching`) and one on **Vision-Language Models** (`nanoVLM`).

To ensure you grasp these concepts, we have designed exercises in the provided Jupyter notebooks. These exercises will help you verify your understanding as you progress through the materials.

## Schedule

Each homework notebook will be released according to the schedule below. For most of the exercises, you will have **2 weeks** from the release date to complete and submit each notebook.

| Homework | Release Date | Deadline |
|---|---|---|
| PyTorch Tutorial + Cluster Setup | 20 Feb | 6 Mar |
| nanoGPT Notebook | 27 Feb | 13 Mar |
| nanoMaskGIT Notebook | 6 Mar | 20 Mar |
| 4M Tutorial | 13 Mar | 27 Mar |
| nano4M Notebook | 20 Mar | 13 Apr |
| nanoFlowMatching Notebook | 27 Mar | 17 Apr |
| nanoVLM Notebook | 2 Apr | 24 Apr |

## Notebooks
### 1. SCITAS & gnoto
We provide 2 types of compute platforms for the FM track. Using SCITAS is recommended for compute-demanding homeworks like homework 4 (4M Tutorial) & homework 5 (nano4M). For debugging, visualizations, and completing exercises that are not very compute-intensive (e.g., the PyTorch tutorial), we recommend using gnoto resources.
- Follow the provided instructions at [SCITAS tutorial](./SCITAS_Tutorial/scitas_tutorial.md) to set up your **SCITAS environment**. 
- To use GPU-powered Jupyter notebooks, follow the instructions provided at [gnoto tutorial](./gnoto_Tutorial/gnoto_tutorial.md).

### 2. Homework 1: PyTorch [Worth 5% of your overall grade]
[PyTorch](https://pytorch.org/) is an **open-source deep learning framework**, which provides a flexible and intuitive way to build deep learning models.

In the [PyTorch_Tutorial](./PyTorch_Tutorial/) folder, you will find three tutorials covering the **basic usage of PyTorch** and the corresponding exercises. 

If you are already familiar with PyTorch, you can proceed directly to the exercises.

### 3. Homework 2: nanoGPT [Worth 7.5% of your overall grade]
In this homework, you will implement the necessary building blocks to construct an **autoregressive Transformer**, like **[GPT](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf)**. Through this homework, you will gain experience with **causal attention**, **decoder-only Transformer** models, basic **tokenization**, **positional encodings**, and **autoregressive modelling** on text and images.

To get started, follow the instructions in the [nanoGPT notebook (coming soon)](TODO) to fill in the missing code, run the training loops, and evaluate the trained models.

### 4. Homework 3: nanoMaskGIT [Worth 10% of your overall grade]
In this homework, you will implement a **masked generative model** in the style of **[MaskGIT](https://masked-generative-image-transformer.github.io/)**. Along the way, you will learn about **bi-directional attention**, **encoder-only Transformer** models, basic **masking schemes**, and **masked modelling** on text and images.

You can find the exercises and detailed instructions in the [nanoMaskGIT notebook (coming soon)](TODO).

### 5. Homework 4: 4M Tutorial [Worth 7.5% of your overall grade]
You will explore the multimodal foundation model **[4M](https://4m.epfl.ch/)**. This hands-on experience will help you understand the model's key components and how to utilize its pipeline for generation and retrieval tasks.

Follow the instructions in the [4M_Tutorial (coming soon)](TODO) folder to learn more about the model, set up the required environment, and experiment with the provided Jupyter notebooks!

### 6. Homework 5: nano4M [Worth 20% of your overall grade]
You will implement a minimal version of 4M, which will give you a practical understanding of how to design and train multimodal foundation models.

See the [nano4M notebook (coming soon)](TODO) for the full set of exercises and instructions.

### 7. Advanced Homework 6: nanoFlowMatching [Worth 10% of your overall grade]
In this advanced homework, you will implement a minimal **[Flow Matching](https://arxiv.org/abs/2210.02747)** model. The exercise covers **continuous normalizing flows**, **vector field regression**, and how flow-based generative models can be used for high-quality image generation.

Check out the [nanoFlowMatching notebook (coming soon)](TODO) for the full set of exercises and instructions.

### 8. Advanced Homework 7: nanoVLM [Worth 10% of your overall grade]
In this advanced homework, you will implement a minimal **[Vision-Language Models (VLMs)](https://llava-vl.github.io)**. You will learn how to combine **visual encoders** with **language models**, enabling multimodal understanding and reasoning across vision and language tasks.

You can find the exercises and detailed instructions in the [nanoVLM notebook (coming soon)](TODO).

## Project Guidelines
You can find more details and the project guidelines in the [project guidelines PDF](COM_304_Spring_2026_nano4M_Project_Guidelines.pdf) file.
