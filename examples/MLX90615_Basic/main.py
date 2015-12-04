################################################################################
# MLX90615
#
# Created: 2015-12-04 21:34:56.758233
#
################################################################################

import streams
from melexis.mlx90615 import mlx90615

streams.serial()

# create a MLX90615 instance passing the I2C peripheral it is connected to
mlx = mlx90615.MLX90615(I2C0)

# start the MLX90615
mlx.start()

while True:
    # read data!
    print("Object Temperature is:",mlx.temperature())
    print("Ambient Temperature is:",mlx.ambient())
    print("Raw Infrared value is:",mlx.raw())
    print("-"*30)
    sleep(1000)


