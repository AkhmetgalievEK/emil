import tkinter as tk
import math
root=tk.Tk()
canvas=tk.Canvas(root)


delta = 0
up = True
right = True 


def right_hand_forefinger_move():

    global delta, up
    if delta < 15 and up:
        delta += 1
        canvas.move('right_forefinger', 0, 1)
    elif delta > 0 and (not up):
        delta += -1
        canvas.move('right_forefinger', 0, -1)
    if delta == 15:
        up = False
    elif delta == 0:
        up = True

    canvas.after(15, right_hand_forefinger_move)


def left_hand_forefinger_move():

    global delta, right
    if delta < 15 and right:
        delta += 1
        canvas.move('left_forefinger', 1, 0)
    elif delta > 0 and (not right):
        delta += -1
        canvas.move('left_forefinger', -1, 0)
    if delta == 15:
        right = False
    elif delta == 0:
        right = True

    canvas.after(15, left_hand_forefinger_move)


#####################################################################
canvas["width"] = 1200
canvas["height"] = 600
canvas.create_polygon(2.0, 438.0, 59.0, 
		407.0, 60.0, 543.0, 1141.0, 
		543.0, 1141.0, 348.0, 1197.0, 
		349.0, 1201.0, 354.0, 1200.0,    #нижняя рамка
		597.0, 2.0, 600.0, 1.0, 438.0, 
		7.0, 445.0,fill = "#dac783",
		width=1.0,outline = "#dfd28e"
)

canvas.create_polygon(2.0, 223.0, 29.0, 210.0, 
		61.0, 194.0, 62.0, 59.0, 1144.0, 
		61.0, 1144.0, 170.0, 1199.0, 168.0,  #верхняя рамка
		1199.0, 2.0, 0.0, 1.0, 0.0, 221.0, 
		13.0, 209.0,fill = "#dac783",
		width=1.0,outline = "#dfd28e"
)



canvas.create_line(155.0, 156.0, 155.0,
		 155.0,fill = "#d2e6ab",width=1.0)

canvas.create_polygon(2.0, 433.0, 47.0, 411.0, 
		71.0, 397.0, 92.0, 383.0, 115.0, 
		368.0, 136.0, 346.0, 158.0, 322.0, 
		181.0, 299.0, 203.0, 279.0, 225.0, 
		269.0, 240.0, 265.0, 232.0, 240.0, 
		231.0, 218.0, 236.0, 191.0, 251.0,  # левая часть левой руки
		174.0, 273.0, 162.0, 307.0, 152.0, 
		234.0, 141.0, 223.0, 141.0, 80.0, 
		191.0, 48.0, 201.0, 1.0, 224.0, 
		2.0, 433.0, 13.0, 417.0,fill = "#e3a983",
		width=1.0,outline = "#cd885f", tags = ('leftarm')
)
canvas.create_polygon(317.0, 262.0, 308.0, 276.0, 
		311.0, 297.0, 316.0, 307.0, 331.0, 
		313.0, 352.0, 317.0, 372.0, 327.0, 
		387.0, 337.0, 407.0, 351.0, 423.0, 
		364.0, 439.0, 375.0, 456.0, 381.0, 
		467.0, 379.0, 469.0, 365.0, 468.0,   #большой палец левой руки
		354.0, 465.0, 342.0, 455.0, 332.0, 
		437.0, 318.0, 419.0, 306.0, 403.0, 
		292.0, 390.0, 278.0, 383.0, 267.0, 
		373.0, 259.0, 347.0, 249.0, 328.0, 
		254.0, 315.0, 265.0, 315.0, 265.0,
		fill = "#e3a983", width=1.0, 
		outline = "#cd885f", tags = ('leftarm')
)
canvas.create_polygon(455.0, 199.0, 438.0, 198.0, 
		423.0, 210.0, 420.0, 223.0, 419.0, 
		235.0, 417.0, 248.0, 432.0, 253.0, 
		447.0, 253.0, 460.0, 253.0, 476.0, 
		257.0, 492.0, 262.0, 508.0, 262.0, 
		513.0, 262.0, 536.0, 285.0, 541.0, 
		293.0, 552.0, 303.0, 555.0, 312.0,    #указательный палец левой руки
		567.0, 324.0, 576.0, 330.0, 589.0, 
		331.0, 602.0, 325.0, 593.0, 312.0, 
		579.0, 287.0, 554.0, 253.0, 529.0, 
		230.0, 497.0, 215.0, 463.0, 203.0, 
		454.0, 199.0, 454.0, 199.0, 
		fill = "#e3a983", width=1.0, 
		outline = "#cd885f",tags = ('left_forefinger')
)
canvas.create_polygon(308.0, 154.0, 267.0, 164.0, 
		244.0, 182.0, 232.0, 200.0, 233.0, 
		237.0, 239.0, 261.0, 245.0, 267.0, 
		260.0, 289.0, 272.0, 299.0, 285.0, 
		306.0, 297.0, 309.0, 315.0, 308.0, 
		310.0, 287.0, 312.0, 268.0, 327.0, 
		256.0, 343.0, 252.0, 359.0, 254.0, 
		377.0, 260.0, 388.0, 271.0, 385.0, 
		261.0, 408.0, 253.0, 417.0, 247.0,    #ладонь левой руки
		419.0, 229.0, 422.0, 213.0, 437.0, 
		200.0, 446.0, 196.0, 458.0, 198.0, 
		443.0, 182.0, 428.0, 174.0, 400.0, 
		169.0, 359.0, 166.0, 344.0, 164.0, 
		307.0, 153.0, 307.0, 153.0, 
		fill = "#e3a983",width=1.0, 
		outline = "#cd885f", tags = ('leftarm')
)
canvas.create_polygon(412.0, 253.0, 443.0, 278.0, 
		459.0, 298.0, 473.0, 315.0, 483.0, 
		321.0, 496.0, 348.0, 499.0, 356.0, 
		500.0, 370.0, 504.0, 382.0, 521.0, 
		387.0, 526.0, 387.0, 523.0, 370.0, 
		518.0, 343.0, 509.0, 328.0, 500.0, # безымянный палец левой руки
		312.0, 497.0, 295.0, 494.0, 276.0, 
		494.0, 262.0, 471.0, 257.0, 456.0, 
		253.0, 430.0, 256.0, 414.0, 250.0, 
		416.0, 256.0, fill = "#e3a983",
		width=1.0, outline = "#cd885f", 
		tags = ('leftarm')
)

canvas.create_polygon(495.0, 263.0, 497.0, 297.0, 
		509.0, 325.0, 519.0, 341.0, 522.0, 
		363.0, 531.0, 379.0, 546.0, 385.0, 
		558.0, 384.0, 546.0, 357.0, 545.0,   # средний палец левой руки
		342.0, 536.0, 291.0, 513.0, 265.0, 
		497.0, 264.0, 497.0, 264.0,
		fill = "#e3a983", width=1.0, 
		outline = "#cd885f", tags = ('leftarm')
)


canvas.create_polygon(392.0, 274.0, 410.0, 277.0, 
		416.0, 295.0, 417.0, 301.0, 447.0, 
		323.0, 458.0, 333.0, 454.0, 292.0, 
		440.0, 276.0, 411.0, 254.0, 388.0,  # мизинец левой руки, верхняя часть
		262.0, 390.0, 275.0, 409.0, 278.0, 
		410.0, 278.0, fill = "#e3a983", 
		width=1.0, outline = "#cd885f",
		tags = ('leftarm')
)



canvas.create_polygon(413.0, 359.0, 406.0, 380.0, 
		419.0, 394.0, 428.0, 390.0, 436.0, 
		375.0, 413.0, 360.0, 415.0, 361.0,   # мизинец левой руки, нижняя часть
		fill = "#e3a983", width=1.0, 
		outline = "#cd885f", tags = ('leftarm')
)

canvas.create_polygon(1198.0, 173.0, 1134.0, 
		172.0, 1074.0, 182.0, 1043.0, 
		193.0, 1003.0, 197.0, 967.0, 
		208.0, 978.0, 218.0, 981.0, 
		234.0, 969.0, 251.0, 977.0, 
		274.0, 985.0, 296.0, 999.0, 
		322.0, 1014.0, 339.0, 1030.0,     #Правая часть правой руки
		333.0, 1040.0, 329.0, 1064.0, 
		330.0, 1090.0, 336.0, 1125.0, 
		344.0, 1157.0, 346.0, 1198.0, 
		346.0, 1198.0, 174.0, 1189.0, 
		186.0, fill = "#e3a983", 
		width=1.0, outline = "#cd885f", 
		tags = ('rightarm')
)
canvas.create_polygon(784.0, 263.0, 745.0, 261.0, 
		714.0, 261.0, 670.0, 274.0, 619.0, 
		292.0, 622.0, 303.0, 628.0, 312.0, 
		649.0, 315.0, 671.0, 312.0, 705.0, 
		305.0, 730.0, 304.0, 756.0, 306.0, 
# Указательный палец правой руки без соединения с рукой
		776.0, 308.0, 778.0, 307.0, 775.0, 
		296.0, 772.0, 283.0, 782.0, 261.0, 
		782.0, 261.0, fill = "#e3a983", 
		width=1.0, outline = "#cd885f",
		tags = ('right_forefinger')
)
canvas.create_polygon(872.0, 276.0, 849.0, 292.0, 
		839.0, 309.0, 820.0, 322.0, 793.0, 
		336.0, 771.0, 349.0, 746.0, 365.0, 
		744.0, 378.0, 750.0, 391.0, 757.0, 
		396.0, 774.0, 397.0, 797.0, 393.0, 
		812.0, 385.0, 828.0, 370.0, 844.0, #большой палец правой руки
		360.0, 860.0, 350.0, 886.0, 350.0, 
		917.0, 351.0, 945.0, 350.0, 965.0, 
		335.0, 977.0, 318.0, 980.0, 303.0, 
		978.0, 277.0, 971.0, 260.0, 963.0, 
		252.0, 936.0, 255.0, 908.0, 262.0, 
		876.0, 276.0, 867.0, 280.0, 858.0, 
		286.0, 858.0, 286.0, fill = "#e3a983",
		width=1.0,outline = "#cd885f", 
		tags = ('rightarm', 'finger1')
)
canvas.create_polygon(823.0, 255.0, 798.0, 256.0, 
		779.0, 263.0, 731.0, 260.0, 709.0, 
		261.0, 617.0, 292.0, 625.0, 310.0, 
		650.0, 318.0, 708.0, 306.0, 731.0, 
#Указательный палец правой руки соединенный с рукой
		305.0, 756.0, 307.0, 778.0, 308.0, 
		782.0, 315.0, 814.0, 312.0, 828.0, 
		304.0, 823.0, 258.0, 822.0, 255.0,
		fill = "#e3a983", width=1.0, 
		outline = "#cd885f", tags = ('rightarm')
)
canvas.create_polygon(970.0, 210.0, 930.0, 210.0, 
		909.0, 218.0, 890.0, 222.0, 823.0, 
		253.0, 827.0, 296.0, 829.0, 308.0, 
		785.0, 317.0, 794.0, 325.0, 786.0, 
		338.0, 824.0, 320.0, 840.0, 310.0,    #верхняя часть правой руки
		851.0, 289.0, 874.0, 276.0, 905.0, 
		265.0, 932.0, 255.0, 961.0, 251.0, 
		970.0, 249.0, 982.0, 235.0, 977.0, 
		218.0, 970.0, 211.0, 956.0, 225.0,
		fill = "#e3a983", width=1.0, 
		outline = "#cd885f", tags = ('rightarm')
)
canvas.create_polygon(864.0, 392.0, 859.0, 407.0, 
		851.0, 423.0, 851.0, 441.0, 852.0, 
		457.0, 858.0, 470.0, 869.0, 474.0, 
		882.0, 470.0, 888.0, 459.0, 889.0, 
		446.0, 889.0, 433.0, 892.0, 423.0,   #мизинец правой руки
		896.0, 406.0, 899.0, 402.0, 888.0, 
		395.0, 867.0, 389.0, 864.0, 389.0,
		fill = "#e3a983", width=1.0,
		outline = "#cd885f", tags = ('rightarm')
)
canvas.create_polygon(765.0, 397.0, 758.0, 432.0, 
		762.0, 456.0, 769.0, 484.0, 774.0, 
		488.0, 787.0, 484.0, 795.0, 478.0, 
		793.0, 440.0, 796.0, 418.0, 799.0, 
		402.0, 805.0, 391.0, 813.0, 387.0,   #средний палец правой руки, нижняя часть
		798.0, 393.0, 779.0, 397.0, 767.0, 
		398.0, 767.0, 398.0, fill = "#e3a983",
		width=1.0, outline = "#cd885f",
		tags = ('rightarm')
)
canvas.create_polygon(844.0, 366.0, 833.0, 369.0, 
		825.0, 376.0, 812.0, 388.0, 802.0, 
		397.0, 797.0, 412.0, 794.0, 436.0, 
		794.0, 452.0, 795.0, 472.0, 795.0, 
		482.0, 802.0, 484.0, 813.0, 483.0, 
		821.0, 473.0, 825.0, 459.0, 824.0,    #безымянный палец правой руки
		447.0, 829.0, 438.0, 835.0, 428.0, 
		836.0, 417.0, 842.0, 408.0, 853.0, 
		396.0, 859.0, 387.0, 853.0, 373.0, 
		842.0, 366.0, 840.0, 375.0,
		fill = "#e3a983", width=1.0,
		outline = "#cd885f", tags = ('rightarm')
)
canvas.create_polygon(980.0, 284.0, 979.0, 320.0, 
		953.0, 345.0, 933.0, 351.0, 898.0, 
		350.0, 864.0, 351.0, 849.0, 358.0, 
		844.0, 362.0, 852.0, 374.0, 860.0, 
		387.0, 872.0, 388.0, 888.0, 394.0, 
		900.0, 402.0, 916.0, 402.0, 933.0,  #нижняя часть ладони правой руки
		398.0, 947.0, 391.0, 963.0, 381.0, 
		978.0, 370.0, 1014.0, 340.0, 1000.0, 
		325.0, 994.0, 315.0, 980.0, 284.0, 
		980.0, 284.0, fill = "#e3a983", 
		width=1.0, outline = "#cd885f",
		tags = ('rightarm')
)


canvas.grid(sticky="nwes")


right_hand_forefinger_move()
left_hand_forefinger_move()


root.mainloop()

