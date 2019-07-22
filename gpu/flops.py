
from pycuda import gpuarray
import numpy as np
from skcuda import cublas
from time import time

m = 1000
n = 2000
k = 2000


def compute_gflops(precision='S'):


    if precision=='S':
        float_type = 'float32'
    elif precision=='D':
        float_type = 'float64'
    else:
        return -1
        
        
    A = np.random.randn(m, k).astype(float_type)
    B = np.random.randn(k, n).astype(float_type)
    C = np.random.randn(m, n).astype(float_type)

    A_cm = A.T.copy()
    B_cm = B.T.copy()
    C_cm = C.T.copy()

    A_gpu = gpuarray.to_gpu(A_cm)
    B_gpu = gpuarray.to_gpu(B_cm)
    C_gpu = gpuarray.to_gpu(C_cm)

    alpha = np.random.randn()
    beta = np.random.randn()

    transa = cublas._CUBLAS_OP['N']
    transb = cublas._CUBLAS_OP['N']

    lda = m
    ldb = k
    ldc = m

    t = time()
    handle = cublas.cublasCreate()


    exec('cublas.cublas%sgemm(handle, transa, transb, m, n, k, alpha, A_gpu.gpudata, lda, \
                        B_gpu.gpudata, ldb, beta, C_gpu.gpudata, ldc)' % precision)

    cublas.cublasDestroy(handle)
    t = time() - t

    gflops = 2*m*n*(k+1)*(10**-9) / t 

    return gflops

def work():
    result = []
    result.append(compute_gflops('S'))
    result.append(compute_gflops('D'))
    return result
