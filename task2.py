import os

pages = [
    {
        "filename": "initialization-variance-conservation-era.md",
        "title": "The Initialization Variance Conservation Era",
        "content": "This era marks the foundational baseline of parameter scale management, pioneered by Xavier Glorot and Kaiming He.\n\n## Diagram\n```mermaid\ngraph TD\n    A[Input Layer] -->|Variance Scaling| B[Hidden Layer]\n    B --> C[Stable Initialization]\n```"
    },
    {
        "filename": "parameter-magnitude-direction-decoupling-era.md",
        "title": "The Parameter Magnitude-Direction Decoupling Era",
        "content": "Ported conservation constraints directly into the active optimization loop by reparameterizing each weight vector.\n\n## Diagram\n```mermaid\ngraph LR\n    W[Weight Vector] -->|Decouple| G[Magnitude g]\n    W -->|Decouple| V[Direction v]\n```"
    },
    {
        "filename": "continuous-isometric-optimization-era.md",
        "title": "The Continuous Isometric Optimization Era",
        "content": "Advanced conservation into perfect geometric isometry by forcing weight matrices to behave as Orthogonal Matrices.\n\n## Diagram\n```mermaid\ngraph TD\n    M[Weight Matrix] -->|Orthogonal Constraint| O[Orthogonal Matrix]\n    O -->|Maintains| E[Euclidean Length Conservation]\n```"
    },
    {
        "filename": "scale-invariant-deep-transformer-era.md",
        "title": "The Scale-Invariant Deep Transformer Era",
        "content": "The current state-of-the-art foundation infrastructure standard driving multi-billion parameter foundation architectures.\n\n## Diagram\n```mermaid\ngraph LR\n    L[Large Transformer Layers] -->|DeepNorm Protocol| S[Scale Invariant Gradient]\n```"
    },
    {
        "filename": "weight-normalization.md",
        "title": "Weight Normalization (Vector-Scale Decoupling)",
        "content": "Reparameterizes weight vectors by dividing the direction tensor by its Euclidean L2 norm.\n\n## Diagram\n```mermaid\ngraph TD\n    D[Direction Tensor] -->|Divide by L2 Norm| N[Normalized Vector]\n```"
    },
    {
        "filename": "orthogonal-layer-transformations.md",
        "title": "Orthogonal Layer Transformations (Isometric Matching)",
        "content": "Restricts the weight matrix elements to be strictly orthogonal for perfect energy conservation.\n\n## Diagram\n```mermaid\ngraph TD\n    W[Weight Matrix] -->|Stiefel Manifold Projection| O[Orthogonal Weight]\n```"
    },
    {
        "filename": "weight-standardization.md",
        "title": "Weight Standardization (WS Regularizers)",
        "content": "Re-centers and scales active convolutional kernel parameters to ensure constant zero mean and unit variance.\n\n## Diagram\n```mermaid\ngraph LR\n    K[Kernel Parameters] -->|Zero Mean & Unit Variance| S[Standardized Parameters]\n```"
    },
    {
        "filename": "scaled-weight-standardization.md",
        "title": "Scaled Weight Standardization (AGC / NFNet Pipelines)",
        "content": "Maps weight standardization parameters concurrently with Adaptive Gradient Clipping.\n\n## Diagram\n```mermaid\ngraph TD\n    W[Weight Standardization] --> A[Adaptive Gradient Clipping]\n    A --> N[Normalization-Free Networks]\n```"
    },
    {
        "filename": "frobenius-norm-estimators.md",
        "title": "Frobenius Norm Estimators",
        "content": "Tracks aggregate Frobenius norm of a layer's parameters to verify scale preservation.\n\n## Diagram\n```mermaid\ngraph TD\n    T[Tensor Weights] -->|Calculate Norm| F[Frobenius Norm]\n```"
    },
    {
        "filename": "beta-variance-caching-gate.md",
        "title": "The Beta-Variance Caching Gate",
        "content": "Memory bus load balancing for calculating and caching analytical variance values.\n\n## Diagram\n```mermaid\ngraph LR\n    B[Beta Variance] -->|Cache| S[Single Scalar]\n    S -->|Execute Division| D[Distributed Nodes]\n```"
    },
    {
        "filename": "stiefel-manifold-optimization-complexity-wall.md",
        "title": "The Stiefel Manifold Optimization Complexity Wall",
        "content": "Solves computational time complexity from exact manifold projections using Soft Orthogonality Regularization.\n\n## Diagram\n```mermaid\ngraph TD\n    O[Objective Loss] -->|Add Penalty Term| S[Soft Orthogonality]\n```"
    },
    {
        "filename": "low-precision-underflow-gradient-saturation-crisis.md",
        "title": "The Low-Precision Underflow Gradient Saturation Crisis",
        "content": "Mitigates underflow errors in low-precision training using an FP32 Master Weight Optimizer.\n\n## Diagram\n```mermaid\ngraph TD\n    F[FP16 Matrix] -->|Underflow Risk| M[FP32 Master Optimizer]\n```"
    },
    {
        "filename": "pre-training-trillion-token-foundational-llm-suites.md",
        "title": "Pre-Training Trillion-Token Foundational LLM Suites",
        "content": "DeepNorm weight conservation stabilizing multi-million dollar training budgets across supercomputing clusters.\n\n## Diagram\n```mermaid\ngraph LR\n    T[Trillion Tokens] -->|DeepNorm Conservation| S[Stable Convergence]\n```"
    },
    {
        "filename": "high-volume-low-latency-cloud-generative-diffusion-simulation.md",
        "title": "High-Volume Low-Latency Cloud Generative Diffusion Simulation",
        "content": "Optimizes generative image and video platforms balancing macro-geometry with microscopic textures.\n\n## Diagram\n```mermaid\ngraph TD\n    G[Generative Simulation] -->|Weight Scale Preservation| O[Optimized Generation]\n```"
    },
    {
        "filename": "distributed-low-rank-post-training-alignment-sprints.md",
        "title": "Distributed Low-Rank Post-Training Alignment Sprints (LoRA Tuning)",
        "content": "Fine-tunes foundation architectures over enterprise datasets using distributed FSDP and LoRA.\n\n## Diagram\n```mermaid\ngraph LR\n    F[Foundation Model] -->|LoRA & FSDP| T[Tuned Architecture]\n```"
    }
]

os.makedirs('pages', exist_ok=True)
for p in pages:
    with open(f"pages/{p['filename']}", "w", encoding="utf-8") as f:
        f.write(f"# {p['title']}\n\n{p['content']}\n\n[Back to README](../README.md)")
