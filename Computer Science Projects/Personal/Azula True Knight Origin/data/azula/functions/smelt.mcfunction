setblock ~ 0 ~ chest replace
item replace block ~ 0 ~ container.0 from entity @s weapon.mainhand
item modify entity @s weapon.mainhand azula:consume
item modify block ~ 0 ~ container.0 azula:limit
item modify block ~ 0 ~ container.0 azula:smelt
summon item ~ ~ ~ {Tags:["item_init"],Item:{id:"minecraft:acacia_boat",Count:1b}}
data modify entity @e[tag=item_init,limit=1] Item set from block ~ 0 ~ Items[0]
tag @e remove item_init
setblock ~ 0 ~ bedrock replace
