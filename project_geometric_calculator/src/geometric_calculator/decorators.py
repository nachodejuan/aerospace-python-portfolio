"""
Performance tracking decorators for geometric calculations.

Provides timing and logging utilities for method performance analysis.
Author: Nacho de Juan
Date: 04/09/2025
"""

import functools
import time
from typing import Callable, Any


def timer(func: Callable) -> Callable:
    """
    Decorator to measure and log function execution time.
    
    Args:
        func: Function to be timed
    
    Returns:
        Wrapped function with performance tracking
    """
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        
        print(f"[PERFORMANCE] {func.__name__} executed in {end_time - start_time:.6f} seconds")
        return result
    
    return wrapper