import time
from common import encode, decode
from fast_common import encode_cython, decode_cython


def benchmark_encode(func, data, iterations=100000):
    """Benchmark encoding function"""
    start = time.perf_counter()
    for _ in range(iterations):
        func(data)
    end = time.perf_counter()
    return end - start


def benchmark_decode(func, data, iterations=100000):
    """Benchmark decoding function"""
    start = time.perf_counter()
    for _ in range(iterations):
        func(data)
    end = time.perf_counter()
    return end - start


def main():
    # Test data
    test_string = "Hello, World! This is a test string for benchmarking."
    test_bytes = test_string.encode("utf-8")
    
    iterations = 100000
    
    print(f"Running benchmarks with {iterations:,} iterations...\n")
    
    # Benchmark encoding
    print("=" * 60)
    print("ENCODING BENCHMARKS (str -> bytes)")
    print("=" * 60)
    
    py_encode_time = benchmark_encode(encode, test_string, iterations)
    print(f"Python encode:  {py_encode_time:.4f} seconds")
    
    cy_encode_time = benchmark_encode(encode_cython, test_string, iterations)
    print(f"Cython encode:  {cy_encode_time:.4f} seconds")
    
    speedup = py_encode_time / cy_encode_time
    print(f"Speedup:        {speedup:.2f}x")
    
    # Benchmark decoding
    print("\n" + "=" * 60)
    print("DECODING BENCHMARKS (bytes -> str)")
    print("=" * 60)
    
    py_decode_time = benchmark_decode(decode, test_bytes, iterations)
    print(f"Python decode:  {py_decode_time:.4f} seconds")
    
    cy_decode_time = benchmark_decode(decode_cython, test_bytes, iterations)
    print(f"Cython decode:  {cy_decode_time:.4f} seconds")
    
    speedup = py_decode_time / cy_decode_time
    print(f"Speedup:        {speedup:.2f}x")
    
    # Test with bytes input for encode (should return as-is)
    print("\n" + "=" * 60)
    print("ENCODING BENCHMARKS (bytes -> bytes, pass-through)")
    print("=" * 60)
    
    py_encode_bytes_time = benchmark_encode(encode, test_bytes, iterations)
    print(f"Python encode:  {py_encode_bytes_time:.4f} seconds")
    
    cy_encode_bytes_time = benchmark_encode(encode_cython, test_bytes, iterations)
    print(f"Cython encode:  {cy_encode_bytes_time:.4f} seconds")
    
    speedup = py_encode_bytes_time / cy_encode_bytes_time
    print(f"Speedup:        {speedup:.2f}x")
    
    # Test with str input for decode (should return as-is)
    print("\n" + "=" * 60)
    print("DECODING BENCHMARKS (str -> str, pass-through)")
    print("=" * 60)
    
    py_decode_str_time = benchmark_decode(decode, test_string, iterations)
    print(f"Python decode:  {py_decode_str_time:.4f} seconds")
    
    cy_decode_str_time = benchmark_decode(decode_cython, test_string, iterations)
    print(f"Cython decode:  {cy_decode_str_time:.4f} seconds")
    
    speedup = py_decode_str_time / cy_decode_str_time
    print(f"Speedup:        {speedup:.2f}x")
    
    print("\n" + "=" * 60)


if __name__ == "__main__":
    main()

