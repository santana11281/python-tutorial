ninja_belts = {
    "crystal":'red',
    'michael':'blue',
    'ambar':'black'
}
# print(ninja_belts['michael'])
# for ninja in ninja_belts:
#     print(f'the ninja is {ninja} and the ninja belt is {ninja_belts[ninja]}')


# ninjakeys = list(ninja_belts.keys())
# ninjavalues = list(ninja_belts.values())
#
# ninjacount = ninjavalues.count('blue')
# print(ninjacount)

for key, val in ninja_belts.items():
    print(' the key is ' + key + ' and the value is '+ val)
