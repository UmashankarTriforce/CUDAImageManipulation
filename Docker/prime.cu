#include<cuda_runtime.h>
#include<iostream>

#define SIZE 10000000
#define streamSize 500
#define streamNumber SIZE/streamSize

__global__ void primeKernel(long long int first, long long int last){

    for (;first <= last; first++){
        bool flag = 0;
        for (long long int j = 2;!flag && j <= ceil(__dsqrt_rd(first)); j++){
            if (!fmodf(first,j)){
                flag = 1;
            } 
        }
    }
}

__host__ int main(){
    
    cudaSetDevice(0);

    cudaEvent_t start, stop;
    float elapsedTime;
    cudaEventCreate(&start);
    cudaEventCreate(&stop);
    cudaStream_t stream[streamNumber];

    cudaEventRecord(start, 0);
    for (int i = 0; i < streamNumber; i++){
        cudaStreamCreate(&stream[i]); 
    }
    for (int i = 0; i < SIZE/streamSize ; i++){
        primeKernel <<< 1, 1, 0, stream[i%streamNumber]>>>(i*streamSize, ((i+1)*streamSize)-1);
    }
    for (int i = 0; i < streamNumber; i++ ){
        cudaStreamSynchronize(stream[i]);
    }
    for(int i = 0; i < streamNumber; i++){
        cudaStreamDestroy(stream[i]);
    }
    cudaEventRecord(stop, 0);
    
    cudaDeviceSynchronize();
    cudaEventSynchronize(stop);
    cudaEventElapsedTime(&elapsedTime, start, stop);

    printf("Time taken %3.1f ms\n", elapsedTime);
    cudaDeviceReset();

    return 0;
}
