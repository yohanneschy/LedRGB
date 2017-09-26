//yohannes CHy
//11020

int NilaiMerah;   
int NilaiHijau;
int NilaiBiru;
const int led1 = 9;   //merah
const int led2 = 10; //hijau
const int led3 = 11; //biru
byte RXBuf[3];


void setup() {                
  // initialize the digital pin as an output.
  pinMode(led1, OUTPUT);
  pinMode(led2, OUTPUT);
  pinMode(led3, OUTPUT);  
  Serial.begin(9600);   //open serial port
 }
 
 void Nyala_led(int NilaiMerah, int NilaiHijau, int NilaiBiru){
   analogWrite(led1, ~NilaiMerah); //  R
   analogWrite(led2, ~NilaiHijau); //  B
   analogWrite(led3, ~NilaiBiru); //  G
    }
    
void loop(){
  Nyala_led(NilaiMerah,NilaiHijau,NilaiBiru);
  if (Serial.available()){
   int nBytes = Serial.readBytes(RXBuf,sizeof(RXBuf));
   if (nBytes>=3){
    NilaiMerah = int(RXBuf[0]);
    NilaiHijau = int(RXBuf[1]);
    NilaiBiru  = int(RXBuf[2]);
    }
 }
}



