# Encode/Decode Benchmark: Python vs Cython

This project benchmarks pure Python encode/decode functions against Cython-optimized versions.

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Build the Cython extension:
```bash
python setup.py build_ext --inplace
```

3. Run the benchmark:
```bash
python benchmark.py
```

## Files

- `common.py` - Pure Python implementation
- `fast_common.pyx` - Cython implementation
- `setup.py` - Build script for Cython extension
- `benchmark.py` - Benchmark script comparing both implementations

## Calls 
* The encode and decode functions are called:
* `4-7 times` per RPC call
* `160,000-490,000` times per second in high-traffic services
* In the critical path of EVERY gRPC operation
* Across ALL RPC types (unary, streaming, bidirectional)