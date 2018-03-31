

#include "stm32f0xx.h"
#include "time.h"
#include "stm32f0xx_misc.h"



int main(void)
{
	RCC ->AHBENR |= (1<<19);	  //Enable GPIO PORT C clock

	GPIOC ->MODER |= (1<< 16);	 //enable PortC pin8 as digital output
    GPIOC ->MODER |= (1<<18);	//enable PORTC9 as digital output


    while(1)
    {
    	for (unsigned int i =0; i < 1000000;i++);
    	GPIOC -> ODR |= (1<<8);		//SET to HI
    	GPIOC -> ODR &= ~(1<<9);		//SET to LO
    	for (int i =0; i < 1000000;i++);		//delay
    	GPIOC -> ODR &= ~(1<<8);		//SET to HI
    	GPIOC -> ODR |= (1<<9);		//SET to LO
    }
}

