# The Parameter Magnitude-Direction Decoupling Era

Ported conservation constraints directly into the active optimization loop by reparameterizing each weight vector.

## Diagram
```mermaid
graph LR
    W[Weight Vector] -->|Decouple| G[Magnitude g]
    W -->|Decouple| V[Direction v]
```

[Back to README](../README.md)