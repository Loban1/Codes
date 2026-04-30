#include <stdio.h>

long long int fibonacci(int i);
long long int vetor[100];

int main() 
{
    for(int i=1; i<=100; i++)
    {
        printf("Fibonacci Nº%d: %lld\n", i, fibonacci(i));
    }
    return (0);
}

long long int fibonacci(int i)
{
    if(i == 0 || i == 1) return 1;
    vetor[i] = fibonacci(i-1);
    return vetor[i]+vetor[i-1];
}
