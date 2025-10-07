# Encode/Decode Benchmark: Python vs Cython

This project benchmarks pure Python encode/decode functions against Cython-optimized versions.

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


## Output
```shell
asheshvidyut@asheshvidyut:~/bench-encode-decode$ python benchmark.py
Running benchmarks with 100,000 iterations...

============================================================
ENCODING BENCHMARKS (str -> bytes)
============================================================
Python encode:  0.0200 seconds
Cython encode:  0.0092 seconds
Speedup:        2.18x

============================================================
DECODING BENCHMARKS (bytes -> str)
============================================================
Python decode:  0.0202 seconds
Cython decode:  0.0068 seconds
Speedup:        2.98x

============================================================
ENCODING BENCHMARKS (bytes -> bytes, pass-through)
============================================================
Python encode:  0.0096 seconds
Cython encode:  0.0038 seconds
Speedup:        2.55x

============================================================
DECODING BENCHMARKS (str -> str, pass-through)
============================================================
Python decode:  0.0119 seconds
Cython decode:  0.0038 seconds
Speedup:        3.09x

============================================================
asheshvidyut@asheshvidyut:~/bench-encode-decode$
```
