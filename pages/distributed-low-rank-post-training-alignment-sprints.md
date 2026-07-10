# Distributed Low-Rank Post-Training Alignment Sprints (LoRA Tuning)

Fine-tunes foundation architectures over enterprise datasets using distributed FSDP and LoRA.

## Diagram
```mermaid
graph LR
    F[Foundation Model] -->|LoRA & FSDP| T[Tuned Architecture]
```

[Back to README](../README.md)