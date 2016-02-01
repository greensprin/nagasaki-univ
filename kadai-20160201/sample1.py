#!/usr/bin/python
import mcpi.minecraft as minecraft
import mcpi.block as block

mc = minecraft.Minecraft.create("133.45.242.221")
pos = mc.player.getPos()

def clear():
    for i in range(0, 30):
        for j in range(0, 10):
            for k in range(0, 40):
                if j == 0:
                    mc.setBlock(-15 + i, -1 + j, -10 + k, block.STONE.id)
                mc.setBlock(-1 + i, 0 + j, -1 + k, block.AIR.id)

def wall():
    for i in range(0, 10):
        for j in range(0, 5):
            for k in range(0, 15):
                if i > 0 and i < 9 and k > 0 and k < 14:
                    mc.setBlock(0 + i, 0 + j, 0 + k, block.AIR.id)
                elif i == 0 and (k == 1 or k == 2 or k == 13 or k == 12) and (j == 0 or j == 1):
                    mc.setBlock(0 + i, 0 + j, 0 + k, block.AIR.id)
                else:
                    mc.setBlock(0 + i, 0 + j, 0 + k, block.WOOL.id)

def roof():
    for i in range(0, 12):
        for j in range(0, 17):
            mc.setBlock(-1 + i, 5, -1 + j, block.DIRT.id)

def set_torch():
    for i in range(0, 8):
        for j in range(0, 13):
            if (i == 0 and j == 0) or (i == 0 and j == 12) or (i == 7 and j == 0) or (i == 7 and j == 12):
                mc.setBlock(1 + i, 0,1 + j, block.TORCH.id)

def set_mado():
    for i in range(0, 10):
        for j in range(0, 5):
            for k in range(0, 15):
                if ( ((i == 0 or i == 9) and (k == 5 or k == 6) and (j == 2 or j == 1))
                     or ((i == 0 or i == 9) and (k == 9 or k == 10) and (j == 2 or j == 1)) ):
                    mc.setBlock(0 + i, 0 + j, 0 + k, block.GLASS.id)

def desk():
    mc.setBlock(4, 0, 2, block.WOOD.id)
    mc.setBlock(5, 0, 2, block.WOOD.id)
    for i in range(0, 4):
        mc.setBlock(2, 0, 5 + i * 2, block.WOOD.id)
        mc.setBlock(3, 0, 5 + i * 2, block.WOOD.id)
        mc.setBlock(6, 0, 5 + i * 2, block.WOOD.id)
        mc.setBlock(7, 0, 5 + i * 2, block.WOOD.id)

clear()
wall()
roof()
set_torch()
set_mado()
desk();

mc.setBlock(-1, 2, 1, block.STONE_SLAB.id)
mc.setBlock(-1, 2, 2, block.STONE_SLAB.id)
mc.setBlock(-1, 2, 12, block.STONE_SLAB.id)
mc.setBlock(-1, 2, 13, block.STONE_SLAB.id)
