"""
.. module:: mlx90615

***************
MLX90615 Module
***************

This module implements Zerynth driver for the MLX90165 sensor (`datasheet <https://www.melexis.com/-/media/files/documents/datasheets/mlx90615-datasheet-melexis.pdf>`_)

The default communication protocol is I2C.

To use this module create a MLX90615 instance by passing the I2C peripheral name to which it is connected to.

Using the module is simple::

    from melexis.mlx90615 import mlx90615
    import streams

    streams.serial()

    mlx = mlx90615.MLX90615(I2C0)

    while True:
        print("Temperature:",mlx.temperature())
        sleep(1000)

        

    """

import i2c


class MLX90615(i2c.I2C):
    """
================
MLX90615 class
================

.. class:: MLX90615(drvname,clock=100000)

        Creates a MLX90615 instance using the MCU I2C circuitry *drvname* (one of I2C0, I2C1, ... check pinmap for details). 
        The created instance is configured and ready to communicate. 
        *clock* is configured by default in slow mode.
        
        MLX90615 inherits from i2c.I2C, therefore the method start() must be called to setup the I2C channel
        before any temperature can be read.

    """       
    def __init__(self,drvname,clock=100000):
        i2c.I2C.__init__(self,drvname,0x5b,clock)

    def temperature(self):
        """
.. method:: temperature()        

        Returns the object temperature in Celsius. The object temperature is the temperature of the object the mlx90615 is pointing towards.
        
        """
        t0 = self.write_read(0x27,3)
        t = (t0[0]+(t0[1]<<8))*0.02-273.15
        return t
    def ambient(self):
        """
.. method:: ambient()        

        Returns the ambient temperature in Celsius. The ambient temperature is the temperature inside the MLX90615 package.
        
        """
        ta = self.write_read(0x26,3)
        t = (ta[0]+(ta[1]<<8))*0.02-273.15
        return t
    def raw(self):
        """
.. method:: raw()        

        Returns the raw infrared readings (signed, 16 bits).
        
        """
        ta = self.write_read(0x25,3)
        t = (ta[0]+((ta[1]&0x7f)<<8))
        if ta[1]&0x7f:
            t=-t
        return t
