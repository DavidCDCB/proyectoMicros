#include <xc.h>
#define _XTAL_FREQ 4000000 //Frecuencia del micro
#include <string.h>

//RA0=E=RC3
//RA1=RS=RC2

void pulsote() {//produce el flanco de bajada    
    RC3 = 1;
    __delay_ms(5);
    RC3 = 0;    
}

void tirarEn4(int n,int rs) {
    PORTC = n;
    RC2=rs;
    pulsote();
    PORTC = n << 4;
    RC2=rs;
    pulsote();
}

// 4 ms luego 4 menos
//0010 1.
//0000 2.
void setLetra(char character,int i) {
    tirarEn4(128+i,0);
    tirarEn4(character,1);
    tirarEn4(15,0);
}

void setPalabra(char arr[]){
    for(int i=0;i<strlen(arr);i++){
        setLetra(arr[i],i);
    }
    
}

void limpiar(){
    for(int i=15;i>=0;i--){
        setLetra(" ",i);
    }
}

void conf() {
    TRISA = 0;
    ADCON1 = 7;
    TRISC = 0; //C COMO SALIDA 
    tirarEn4(32,0);
}

void main(void) {
    conf();
    setPalabra("Esta joda sirve");
    limpiar();
    setPalabra("XD");
    while (1){}
}
