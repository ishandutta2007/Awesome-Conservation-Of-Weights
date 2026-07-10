import re

def process_readme():
    with open('README.md', 'r', encoding='utf-8') as f:
        content = f.read()

    # Define the replacements for each section
    
    # Section 1
    s1_old = """*   **The Initialization Variance Conservation Era (Xavier / He Foundations, 2010–2015)**
    *   *Concept:* The core foundational baseline of parameter scale management. Xavier Glorot (2010) and Kaiming He (2015) formalized initialization as a mathematical variance conservation task. They proved that to prevent gradient explosion at step zero, the weights of a layer must be initialized using specialized statistical distributions whose variance scales inversely proportional to layer thickness ($\\text{fan}_{\\text{in}}$).
    *   *Limitation:* Confined strictly to the initialization gate. As soon as the first optimization backpropagation pass updates the model, the weights drift unconstrained, causing the early variance conservation boundaries to dissolve completely.
*   **The Parameter Magnitude-Direction Decoupling Era (Weight Normalization, 2016–2019)**
    *   *Concept:* Ported conservation constraints directly into the active optimization loop. Popularized by Tim Salimans and Diederik Kingma, **Weight Normalization (2016)** reparameterized each weight vector $w$ into two completely independent, learnable components: a scalar magnitude parameter ($g$) and a normalized directional vector ($v$).
    *   *Significance:* By explicitly separating length from orientation ($w = g \\cdot \\frac{v}{\\|v\\|_2}$), the network guarantees that the directional vector preserves a constant unit norm throughout training, stabilizing gradient propagation and accelerating backpropagation convergence velocities.
*   **The Continuous Isometric Optimization Era (Orthogonal Weight Initializers & Regularizers)**
    *   *Concept:* Advanced conservation into perfect geometric isometry. Instead of normalizing isolated vectors, it forces the entire multi-dimensional weight matrix to behave as an **Orthogonal Matrix** ($W^T W = I$). 
    *   *Significance:* This mathematical restriction enforces absolute **Euclidean Length Conservation**. As an activation vector passes through an orthogonal weight matrix, its physical length and spatial angles are preserved completely without any attenuation or expansion, flatlining vanishing/exploding loops across deep recurrent and generative structures.
*   **The Scale-Invariant Deep Transformer Era (~2022–Present)**
    *   *Concept:* The current modern state-of-the-art foundation infrastructure standard driving multi-billion parameter foundation architectures (such as Llama 3 and DeepSeek-V3) [INDEX: 15, 22]. When scaling models to hundreds of layers, gradient tracking suffers heavily from cumulative variance inflation along parallel residual addition highways [INDEX: 1].
    *   *Significance:* Modern frameworks deploy **DeepNorm / Fixed-Update conservation protocols**. The weights of terminal residual blocks are downscaled by an explicit factor bound to total layer depth ($1/\\sqrt{2L}$), ensuring gradient trajectories remain scale-invariant over trillions of tokens [INDEX: 1, 22]."""

    s1_new = """| Era / Concept | Description | Year First Used | Paper Link |
| --- | --- | --- | --- |
| **[The Initialization Variance Conservation Era](pages/initialization-variance-conservation-era.md)** | **Concept:** Foundational baseline of parameter scale management...<br>**Limitation:** Confined strictly to the initialization gate. | 2010 | [Glorot & Bengio (2010)](https://proceedings.mlr.press/v9/glorot10a/glorot10a.pdf) |
| **[The Parameter Magnitude-Direction Decoupling Era](pages/parameter-magnitude-direction-decoupling-era.md)** | **Concept:** Ported conservation constraints directly into the active optimization loop...<br>**Significance:** Stabilizes gradient propagation. | 2016 | [Salimans & Kingma (2016)](https://arxiv.org/abs/1602.07868) |
| **[The Continuous Isometric Optimization Era](pages/continuous-isometric-optimization-era.md)** | **Concept:** Advanced conservation into perfect geometric isometry...<br>**Significance:** Enforces absolute Euclidean Length Conservation. | 2013 | [Saxe et al. (2013)](https://arxiv.org/abs/1312.6120) |
| **[The Scale-Invariant Deep Transformer Era](pages/scale-invariant-deep-transformer-era.md)** | **Concept:** Modern state-of-the-art foundation infrastructure...<br>**Significance:** Modern frameworks deploy DeepNorm conservation protocols. | 2022 | [Wang et al. (2022)](https://arxiv.org/abs/2203.00555) |"""

    s2_old = """- ### A. Weight Normalization (Vector-Scale Decoupling)
	*   **Mechanism:** Reparameterizes the weight vectors of a layer by dividing the direction tensor by its Euclidean $L_2$ norm, using a separate scalar variable ($g$) to track magnitude:
	    $$w = g \\frac{v}{\\|v\\|_2}$$
	*   **Pros:** Slashes the computational overhead of traditional Batch Normalization layers [INDEX: 16], optimal for recurrent, reinforcement learning, and low-latency generative models.

- ### B. Orthogonal Layer Transformations (Isometric Matching)
	*   **Mechanism:** Restricts the weight matrix elements to be strictly orthogonal. During backpropagation, the gradients are projected onto the Stiefel Manifold using Cayley transforms or explicit Riemannian optimization algorithms, forcing the singular values of the matrix to remain locked at absolute unit scale ($1.0$).
	*   **Pros:** Guarantees perfect energy conservation across the hidden layer nodes.

- ### C. Weight Standardization (WS Regularizers)
	*   **Mechanism:** Popularized by Google's Big Transfer (BiT) framework. It re-centers and scales the active convolutional kernel parameters to ensure a constant zero mean and unit variance layout before executing linear algebra transformations:
	    $$\\hat{W}_{i,j} = \\frac{W_{i,j} - \\mu_{W_i}}{\\sigma_{W_i}}$$

- ### D. Scaled Weight Standardization (AGC / NFNet Pipelines)
	*   **Mechanism:** The operational core of Normalization-Free Networks. It maps weight standardization parameters concurrently with **Adaptive Gradient Clipping (AGC)**, capping the gradient step length relative to the existing weight magnitude to prevent parameter explosion."""

    s2_new = """| Variant | Mechanism & Pros | Year First Used | Paper Link |
| --- | --- | --- | --- |
| **[A. Weight Normalization (Vector-Scale Decoupling)](pages/weight-normalization.md)** | **Mechanism:** Reparameterizes the weight vectors by dividing the direction tensor by its Euclidean norm...<br>**Pros:** Slashes computational overhead. | 2016 | [Salimans & Kingma (2016)](https://arxiv.org/abs/1602.07868) |
| **[B. Orthogonal Layer Transformations (Isometric Matching)](pages/orthogonal-layer-transformations.md)** | **Mechanism:** Restricts the weight matrix elements to be strictly orthogonal...<br>**Pros:** Guarantees perfect energy conservation. | 2013 | [Saxe et al. (2013)](https://arxiv.org/abs/1312.6120) |
| **[C. Weight Standardization (WS Regularizers)](pages/weight-standardization.md)** | **Mechanism:** Re-centers and scales the active convolutional kernel parameters to ensure a constant zero mean and unit variance. | 2019 | [Qiao et al. (2019)](https://arxiv.org/abs/1903.10520) |
| **[D. Scaled Weight Standardization (AGC / NFNet Pipelines)](pages/scaled-weight-standardization.md)** | **Mechanism:** Maps weight standardization parameters concurrently with Adaptive Gradient Clipping (AGC). | 2021 | [Brock et al. (2021)](https://arxiv.org/abs/2102.06171) |"""

    s3_old = """*   **Frobenius Norm Estimators ($\\|\\cdot\\|_F$)**
    *   *The Math:* Maps out multidimensional tensor weights. The initialization and clipping scripts track the aggregate Frobenius norm of a layer's parameters ($\\|W\\|_F = \\sqrt{\\sum \\sum |w_{ij}|^2}$) at each epoch milestone to verify scale preservation.
*   **The $\\beta$-Variance Caching Gate**
    *   *Profile:* Memory bus load balancing. In standard foundation transformer sweeps, the analytical variance values ($\\beta$) are calculated once and cached as a single scalar, executing the division in a single step across distributed data-parallel hardware nodes [INDEX: 22]."""

    s3_new = """| Concept | Description | Year First Used | Paper Link |
| --- | --- | --- | --- |
| **[Frobenius Norm Estimators](pages/frobenius-norm-estimators.md)** | **The Math:** Maps out multidimensional tensor weights to verify scale preservation. | 1980s | [Standard Math](#) |
| **[The Beta-Variance Caching Gate](pages/beta-variance-caching-gate.md)** | **Profile:** Memory bus load balancing for calculating and caching variance values. | 2022 | [Zhao et al. (2023) / FSDP](#) |"""

    s4_old = """- ### The Stiefel Manifold Optimization Complexity Wall
	*   **The Problem:** Enforcing continuous, hard orthogonal weight matrices requires calculating matrix inversions or Singular Value Decompositions (SVD) at every backpropagation step. For high-dimensional hidden layers (e.g., $d_{\\text{model}} > 8,192$), this introduces an intolerable $O(N^3)$ computational time complexity, slowing down training clusters.
	*   **Mitigation:** Bypassing exact manifold projections by deploying **Soft Orthogonality Regularization**, adding a lightweight penalty term directly to the objective loss function ($\\mathcal{L}_{\\text{reg}} = \\lambda \\|W^T W - I\\|_F^2$) to softly encourage weight conservation without hardware stalls.

- ### The Low-Precision Underflow Gradient Saturation Crisis
	*   **The Problem:** When executing deep parameter downscaling ($1/\\sqrt{2L}$) inside models that train under low-precision 16-bit floats (FP16 or BF16) [INDEX: 11], the heavily compressed weights of early transformer blocks can experience **Underflow Errors**, zeroing out initialization elements completely.
	*   **Mitigation:** Maintaining a strict **FP32 Master Weight Optimizer configuration (AdamW integration)** [INDEX: 11]. While model forward and backward passes execute in fast, low-bit 16-bit matrices, the system caches and updates a copy of the master parameters in full 32-bit floating-point registers to protect low-bit learning increments safely."""

    s4_new = """| Challenge | Problem & Mitigation | Year First Used | Paper Link |
| --- | --- | --- | --- |
| **[The Stiefel Manifold Optimization Complexity Wall](pages/stiefel-manifold-optimization-complexity-wall.md)** | **The Problem:** Intolerable computational time complexity from SVD.<br>**Mitigation:** Soft Orthogonality Regularization. | 2017 | [Bansal et al. (2018)](https://arxiv.org/abs/1811.00973) |
| **[The Low-Precision Underflow Gradient Saturation Crisis](pages/low-precision-underflow-gradient-saturation-crisis.md)** | **The Problem:** Underflow errors in low-precision FP16/BF16 training.<br>**Mitigation:** FP32 Master Weight Optimizer configuration. | 2017 | [Micikevicius et al. (2017)](https://arxiv.org/abs/1710.03740) |"""

    s5_old = """*   **Pre-Training Trillion-Token Foundational LLM Suites (DeepSpeed/FSDP Supercomputing)**
    *   *Application:* Serves as the critical baseline safety gate stabilizing large-scale foundational transformers (e.g., Llama 3, DeepSeek-V3) [INDEX: 15, 22]. DeepNorm weight conservation and scale-invariant multipliers ensure that multi-million dollar training budgets running across thousands of cluster nodes converge stably over tens of trillions of tokens without experiencing optimization divergence [INDEX: 15, 22].
*   **High-Volume Low-Latency Cloud Generative Diffusion Simulation (Sora Class)**
    *   *Application:* Optimizes generative image and video platforms (such as FLUX.1 or Stable Diffusion). Continuous weight normalization and scale preservation allow deep text-image cross-attention blocks to balance broad macro-geometric composition learning with microscopic high-frequency image texture generation stably over long epoch profiles.
*   **Distributed Low-Rank Post-Training Alignment Sprints (LoRA Tuning)**
    *   *Application:* Fine-tunes foundation architectures over domain-specific enterprise datasets (such as private corporate legal or healthcare portfolios) [INDEX: 11, 16]. Distributed FSDP configurations shard low-rank adapter gradients and utilize weight scale conservation to simulate large, stable optimization batch boundaries on commodity edge server nodes smoothly [INDEX: 16, 22]."""

    s5_new = """| Application Area | Application Details | Year First Used | Paper Link |
| --- | --- | --- | --- |
| **[Pre-Training Trillion-Token Foundational LLM Suites](pages/pre-training-trillion-token-foundational-llm-suites.md)** | **Application:** Stabilizes large-scale foundational transformers across supercomputing clusters. | 2022 | [Wang et al. (2022)](https://arxiv.org/abs/2203.00555) |
| **[High-Volume Low-Latency Cloud Generative Diffusion Simulation](pages/high-volume-low-latency-cloud-generative-diffusion-simulation.md)** | **Application:** Optimizes generative image and video platforms balancing macro-geometry with micro-textures. | 2020 | [Ho et al. (2020)](https://arxiv.org/abs/2006.11239) |
| **[Distributed Low-Rank Post-Training Alignment Sprints](pages/distributed-low-rank-post-training-alignment-sprints.md)** | **Application:** Fine-tunes architectures using FSDP configurations and LoRA. | 2021 | [Hu et al. (2021)](https://arxiv.org/abs/2106.09685) |"""

    content = content.replace(s1_old, s1_new)
    content = content.replace(s2_old, s2_new)
    content = content.replace(s3_old, s3_new)
    content = content.replace(s4_old, s4_new)
    content = content.replace(s5_old, s5_new)

    with open('README.md', 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == '__main__':
    process_readme()
