# fast_common.pyx

cpdef bytes encode_cython(object s):
    """Encodes a string to bytes using UTF-8, returns bytes directly if passed bytes."""
    # The 'object' type allows Cython to handle str and bytes inputs.
    if isinstance(s, bytes):
        return <bytes>s
    else:
        # Assumes s is a str if not bytes.
        # This is a fast C-level call inside the Python interpreter.
        return s.encode("utf8")


cpdef str decode_cython(object b):
    """Decodes bytes to a string using UTF-8 with 'replace' error handling, returns str directly if passed str."""
    if isinstance(b, bytes):
        # This is a fast C-level call inside the Python interpreter.
        return (<bytes>b).decode("utf-8", "replace")
    return <str>b