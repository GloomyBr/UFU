#include <stdio.h>
#include <string.h>

#define SIZE 50

int main(){
    int estado = 0,i,k=0;
    char cadeia[SIZE],c;

    printf("Digite a cadeia de caracteres: ");
    gets(cadeia);
    
    while(estado == 0 || estado == 1){
        c = cadeia[k++];

        if(estado == 0){  

            if(c == 'a'){
                estado = 1;
            }else if(c == 'b'){
                estado = 0;
            }else{
                printf("Cadeia rejeitada");
                break;
            }
        }else if(estado == 1){
            if(c == 'b'){
                estado = 2;
            }else{
                printf("Cadeia rejeitada");
                break;
            }
        }
    }

    if(estado == 2){
        printf("Cadeia aceita");
    }

    return 0;
}