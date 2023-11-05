#include <stdio.h>
#include <stdlib.h>

int main() {
    // Crie um ponteiro que aponta para uma variável inteira
    int *ponteiro;

    // Aloque memória para armazenar oito dados inteiros
    ponteiro = (int *)malloc(8 * sizeof(int));
    if (ponteiro == NULL) {
        printf("Falha na alocação de memória\n");
        return 1;
    }

    // Realoque memória para um tamanho que armazene doze dados inteiros
    ponteiro = (int *)realloc(ponteiro, 12 * sizeof(int));
    if (ponteiro == NULL) {
        printf("Falha na realocação de memória\n");
        return 1;
    }

    // Libere o espaço alocado
    free(ponteiro);

    return 0;
}
