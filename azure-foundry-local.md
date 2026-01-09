/ [Home](index.md)

## Azure Foundry Local

### Setup

```
brew tap microsoft/foundrylocal
brew install foundrylocal


# verify
foundry --version
0.8.117

foundry model run qwen2.5-0.5b

foundry --help
```

```
foundry --help

Description:
  Foundry Local CLI: Run AI models on your device.

  🚀 Getting started:

     1. To view available models: foundry model list
     2. To run a model: foundry model run <model>

     EXAMPLES:
         foundry model run phi-3-mini-4k

Usage:
  foundry [command] [options]

Options:
  -?, -h, --help  Show help and usage information
  --version       Show version information
  --license       Display foundry license information

Commands:
  model    Discover, run and manage models
  cache    Manage the local cache
  service  Manage the local model inference service
```

```
foundry model list
🟢 Service is Started on http://127.0.0.1:57497/, PID 11818!
Alias                          Device     Task           File Size    License      Model ID
-----------------------------------------------------------------------------------------------
phi-4                          GPU        chat           8.37 GB      MIT          Phi-4-generic-gpu:1
                               CPU        chat           10.16 GB     MIT          Phi-4-generic-cpu:1
----------------------------------------------------------------------------------------------------------
phi-3.5-mini                   GPU        chat           2.16 GB      MIT          Phi-3.5-mini-instruct-generic-gpu:1
                               CPU        chat           2.53 GB      MIT          Phi-3.5-mini-instruct-generic-cpu:1
--------------------------------------------------------------------------------------------------------------------------
phi-3-mini-128k                GPU        chat           2.13 GB      MIT          Phi-3-mini-128k-instruct-generic-gpu:1
                               CPU        chat           2.54 GB      MIT          Phi-3-mini-128k-instruct-generic-cpu:2
-----------------------------------------------------------------------------------------------------------------------------
phi-3-mini-4k                  GPU        chat           2.13 GB      MIT          Phi-3-mini-4k-instruct-generic-gpu:1
                               CPU        chat           2.53 GB      MIT          Phi-3-mini-4k-instruct-generic-cpu:2
---------------------------------------------------------------------------------------------------------------------------
mistral-7b-v0.2                GPU        chat           4.07 GB      apache-2.0   mistralai-Mistral-7B-Instruct-v0-2-generic-gpu:1
                               CPU        chat           4.07 GB      apache-2.0   mistralai-Mistral-7B-Instruct-v0-2-generic-cpu:2
---------------------------------------------------------------------------------------------------------------------------------------
deepseek-r1-14b                GPU        chat           10.27 GB     MIT          deepseek-r1-distill-qwen-14b-generic-gpu:3
                               CPU        chat           11.51 GB     MIT          deepseek-r1-distill-qwen-14b-generic-cpu:3
---------------------------------------------------------------------------------------------------------------------------------
deepseek-r1-7b                 GPU        chat           5.58 GB      MIT          deepseek-r1-distill-qwen-7b-generic-gpu:3
                               CPU        chat           6.43 GB      MIT          deepseek-r1-distill-qwen-7b-generic-cpu:3
--------------------------------------------------------------------------------------------------------------------------------
qwen2.5-coder-0.5b             GPU        chat, tools    0.52 GB      apache-2.0   qwen2.5-coder-0.5b-instruct-generic-gpu:4
                               CPU        chat, tools    0.80 GB      apache-2.0   qwen2.5-coder-0.5b-instruct-generic-cpu:4
--------------------------------------------------------------------------------------------------------------------------------
phi-4-mini-reasoning           GPU        chat           3.15 GB      MIT          Phi-4-mini-reasoning-generic-gpu:3
                               CPU        chat           4.52 GB      MIT          Phi-4-mini-reasoning-generic-cpu:3
-------------------------------------------------------------------------------------------------------------------------
qwen2.5-0.5b                   GPU        chat, tools    0.68 GB      apache-2.0   qwen2.5-0.5b-instruct-generic-gpu:4
                               CPU        chat, tools    0.80 GB      apache-2.0   qwen2.5-0.5b-instruct-generic-cpu:4
--------------------------------------------------------------------------------------------------------------------------
qwen2.5-1.5b                   GPU        chat, tools    1.51 GB      apache-2.0   qwen2.5-1.5b-instruct-generic-gpu:4
                               CPU        chat, tools    1.78 GB      apache-2.0   qwen2.5-1.5b-instruct-generic-cpu:4
--------------------------------------------------------------------------------------------------------------------------
qwen2.5-coder-1.5b             GPU        chat, tools    1.25 GB      apache-2.0   qwen2.5-coder-1.5b-instruct-generic-gpu:4
                               CPU        chat, tools    1.78 GB      apache-2.0   qwen2.5-coder-1.5b-instruct-generic-cpu:4
--------------------------------------------------------------------------------------------------------------------------------
phi-4-mini                     GPU        chat, tools    3.72 GB      MIT          Phi-4-mini-instruct-generic-gpu:5
                               CPU        chat, tools    4.80 GB      MIT          Phi-4-mini-instruct-generic-cpu:5
------------------------------------------------------------------------------------------------------------------------
qwen2.5-14b                    GPU        chat, tools    9.30 GB      apache-2.0   qwen2.5-14b-instruct-generic-gpu:4
                               CPU        chat, tools    11.06 GB     apache-2.0   qwen2.5-14b-instruct-generic-cpu:4
-------------------------------------------------------------------------------------------------------------------------
qwen2.5-coder-14b              GPU        chat, tools    8.79 GB      apache-2.0   qwen2.5-coder-14b-instruct-generic-gpu:4
                               CPU        chat, tools    11.06 GB     apache-2.0   qwen2.5-coder-14b-instruct-generic-cpu:4
-------------------------------------------------------------------------------------------------------------------------------
qwen2.5-coder-7b               GPU        chat, tools    4.73 GB      apache-2.0   qwen2.5-coder-7b-instruct-generic-gpu:4
                               CPU        chat, tools    6.16 GB      apache-2.0   qwen2.5-coder-7b-instruct-generic-cpu:4
------------------------------------------------------------------------------------------------------------------------------
qwen2.5-7b                     GPU        chat, tools    5.20 GB      apache-2.0   qwen2.5-7b-instruct-generic-gpu:4
                               CPU        chat, tools    6.16 GB      apache-2.0   qwen2.5-7b-instruct-generic-cpu:4
------------------------------------------------------------------------------------------------------------------------
gpt-oss-20b                    CPU        chat           12.26 GB     MIT          gpt-oss-20b-generic-cpu:1
```

### Ref:
- [Azure Foundry Local](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/reference/reference-cli?view=foundry-classic)