# fmt: off
from pathlib import Path

import torch.nn as nn

from torch_uncertainty import cli_main
from torch_uncertainty.baselines.packed import PackedResNet
from torch_uncertainty.datamodules import CIFAR100DataModule
from torch_uncertainty.optimization_procedures import optim_cifar100_resnet18

# fmt: on

if __name__ == "__main__":
    root = Path(__file__).parent.absolute().parents[1]
    cli_main(
        PackedResNet,
        CIFAR100DataModule,
        nn.CrossEntropyLoss,
        optim_cifar100_resnet18,
        root,
        "packed",
    )