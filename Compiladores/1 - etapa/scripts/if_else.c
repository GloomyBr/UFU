#include <stdio.h>

int main(){
    int i = 0;
    int j = 2;

    if (i > 0) {
        j = 1 - i;
    } else if(i == 0) {
        i = j + 2;
    }
}