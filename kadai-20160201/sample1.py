#!/usr/bin/python
import mcpi.minecraft as minecraft
import mcpi.block as block

mc = minecraft.Minecraft.create("133.45.242.221")
pos = mc.player.getPos()

#mc.postToChat("sample1")

for i in range(0, 10):
    for j in range(0, 10):
        for k in range(0, 10):
            if i > 0 and i < 9 and k > 0 and k < 9:
                mc.setBlock(0 + i, 0 + j, 0 + k, block.AIR.id)
            elif i == 0 and k == 3 and (j == 0 or j == 1):
                mc.setBlock(0 + i, 0 + j, 0 + k, block.AIR.id)
            else:
                mc.setBlock(0 + i, 0 + j, 0 + k, block.STONE.id)
