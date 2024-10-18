'''
Created on Oct 18, 2024

Basic uPython driver for the blinkencap

@author: Pat Deegan
@copyright: Copyright (C) 2024 Pat Deegan, https://psychogenic.com
'''
import machine 
import time
PIDX_NRST = 19
PIDX_CLK = 20
PIDX_INC = 21
PIDX_ENA = 22

_BlinkenDriver_Singleton = None 
class BlinkenDriver:
    def __init__(self):
        self.pin_nrst = machine.Pin(PIDX_NRST, machine.Pin.OUT)
        self.pin_clk = machine.Pin(PIDX_CLK, machine.Pin.OUT)
        self.pin_ena = machine.Pin(PIDX_ENA, machine.Pin.OUT)
        self.pin_inc = machine.Pin(PIDX_INC, machine.Pin.OUT)
        
        for p in [self.pin_nrst, self.pin_clk, self.pin_ena, self.pin_inc]:
            p.value(0)

    def select_project(self, idx:int):
        print(f"selecting project {idx}")
        self.pin_nrst.value(0)
        self.pin_ena.value(0)
        self.pin_inc.value(0)
        time.sleep_ms(2)
        
        self.pin_nrst.value(1)
        time.sleep_ms(2)
        
        # send the number of pulses required
        for _c in range(idx):
            self.pin_inc.value(1)
            time.sleep_ms(1)
            self.pin_inc.value(0)
            time.sleep_ms(1)
            
        self.pin_ena.value(1)
    
    def clock_once(self):
        self.pin_clk.value(0)
        time.sleep_ms(1)
        self.pin_clk.value(1)
        time.sleep_ms(1)
        self.pin_clk.value(0)
        
def getDriver():
    global _BlinkenDriver_Singleton
    if _BlinkenDriver_Singleton is None:
        _BlinkenDriver_Singleton = BlinkenDriver()
    
    return _BlinkenDriver_Singleton 


def run(proj_idx:int=1, num_clocks:int=30, delayms:int=500):
    drv = getDriver()
    drv.select_project(proj_idx)
    for _c in range(num_clocks):
        drv.clock_once()
        time.sleep_ms(delayms)
        
        
    
    
    
