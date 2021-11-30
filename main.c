/**
  @Summary
 This simple code is demonstrating the X2Cscope functionalities.

  @Description
    This source file provides main entry point for system initialization and application code development.
    Generation Information :
        Product Revision  :  PIC24 / dsPIC33 / PIC32MM MCUs - 1.169.0
        Device            :  dsPIC33CK256MP508
    The generated drivers are tested against the following:
        Compiler          :  XC16 v1.70
        MPLAB 	          :  MPLAB X v5.50
*/

/**
  Section: Included Files
*/
#include "mcc_generated_files/system.h"
#include "mcc_generated_files/pin_manager.h"
#include "mcc_generated_files/tmr1.h"
#include "mcc_generated_files/X2Cscope/X2Cscope.h"
#include <stdbool.h>
#include <stdint.h>
#include <math.h>
#define PI (3.14)
/**
 Section: Global Variables
 */

volatile bool btnState;
volatile bool led1Control = false;
volatile bool led2State;

uint16_t sawTooth;
uint8_t speed = 1; // slope speed of the sawtooth
int16_t gain = 100; // amplitude of the generated sawtooth
    
typedef struct _MY_STRUCT_T
{ 
    float sinus;
    double rad;
}MY_STRUCT_t;

MY_STRUCT_t myStruct;

/**
 * Generate sawtooth and sine wave. Then do sample point for X2Cscope.
 */
void myTMR_1ms_callback(void)
{  
    sawTooth += speed;          // Generate sawtooth
    if(sawTooth >= (360 * 2) )     // up-to multiple of 360
    {   
        sawTooth = 0;
        IO_LED2_Toggle();       //Toggle LED to Signal of sawtooth overflow (hearthbeat)
    }
    // Generate sinus from the sawtooth signal
    myStruct.rad = ((double) sawTooth) * PI / 360.0;
    myStruct.sinus = gain * sin(myStruct.rad);
    
    // This is the sample point of the scope
    // The period of execution interval of this function must be synced with the X2CScope settings
    X2CScope_Update();
}

/*
                         Main application
 */
int main(void)
{
    // initialize the device
    SYSTEM_Initialize();
    TMR1_SetInterruptHandler(myTMR_1ms_callback); //1ms period timer interrupt
    
    while (1)
    {
        // Add this line manually to the idle loop or low priority task
        X2CScope_Communicate();
        
        //Handle LED1
        if(led1Control)
        {
            IO_LED1_SetHigh();
        }
        else
        {
            IO_LED1_SetLow();
        }
        //Read SW1 state
        btnState = IO_SW1_GetValue();
        //Read back LED2 state
        led2State = IO_LED2_GetValue();
    }
    return 1; 
}


/**
 End of File
*/

