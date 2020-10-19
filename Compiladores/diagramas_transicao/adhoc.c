#include <stdio.h>
#include <string.h>

#define SIZE 50
int main() {
    int estado = 0,i,k=0;
    char cadeia[SIZE],c;

    printf("Digite a cadeia de caracteres: ");
    gets(cadeia);

    c = cadeia[0];

    if(c == 'b'){
        c = cadeia[++k];
        
        while(c == 'b'){
            c = cadeia[++k];
        }
        
        if(c == 'a'){
            estado = 1;
            c = cadeia[++k];

            if(c == 'b' && cadeia[++k] == '\0'){
                estado = 2;
                printf("Cadeia aceita");
            }else{
                printf("Cadeia rejeitada");
            }
        }else{
            printf("Cadeia rejeitada");
        }
    }

    return 0;
}