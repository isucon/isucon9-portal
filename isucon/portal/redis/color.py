

colors = [
    "rgba(244,67,54,{alpha})",
    "rgba(233,30,99,{alpha})",
    "rgba(156,39,176,{alpha})",
    "rgba(103,58,183,{alpha})",
    "rgba(63,81,181,{alpha})",
    "rgba(33,150,243,{alpha})",
    "rgba(3,169,244,{alpha})",
    "rgba(0,188,212,{alpha})",
    "rgba(0,150,136,{alpha})",
    "rgba(76,175,80,{alpha})",
    "rgba(139,195,74,{alpha})",
    "rgba(205,220,57,{alpha})",
    "rgba(255,235,59,{alpha})",
    "rgba(255,193,7,{alpha})",
    "rgba(255,152,0,{alpha})",
    "rgba(255,87,34,{alpha})",
    "rgba(121,85,72,{alpha})",
    "rgba(158,158,158,{alpha})",
    "rgba(96,125,139,{alpha})",
    "rgba(239,83,80,{alpha})",
    "rgba(236,64,122,{alpha})",
    "rgba(171,71,188,{alpha})",
    "rgba(126,87,194,{alpha})",
    "rgba(92,107,192,{alpha})",
    "rgba(66,165,245,{alpha})",
    "rgba(41,182,246,{alpha})",
    "rgba(38,198,218,{alpha})",
    "rgba(38,166,154,{alpha})",
    "rgba(102,187,106,{alpha})",
    "rgba(156,204,101,{alpha})",
    "rgba(212,225,87,{alpha})",
    "rgba(255,238,88,{alpha})",
    "rgba(255,202,40,{alpha})",
    "rgba(255,167,38,{alpha})",
    "rgba(255,112,67,{alpha})",
    "rgba(141,110,99,{alpha})",
    "rgba(189,189,189,{alpha})",
    "rgba(120,144,156,{alpha})",
    "rgba(229,115,115,{alpha})",
    "rgba(240,98,146,{alpha})",
    "rgba(186,104,200,{alpha})",
    "rgba(149,117,205,{alpha})",
    "rgba(121,134,203,{alpha})",
    "rgba(100,181,246,{alpha})",
    "rgba(79,195,247,{alpha})",
    "rgba(77,208,225,{alpha})",
    "rgba(77,182,172,{alpha})",
    "rgba(129,199,132,{alpha})",
    "rgba(174,213,129,{alpha})",
    "rgba(220,231,117,{alpha})",
    "rgba(255,241,118,{alpha})",
    "rgba(255,213,79,{alpha})",
    "rgba(255,183,77,{alpha})",
    "rgba(255,138,101,{alpha})",
    "rgba(161,136,127,{alpha})",
    "rgba(224,224,224,{alpha})",
    "rgba(144,164,174,{alpha})",
]

def iter_colors():
    idx = 0
    while True:
        yield (colors[idx].format(alpha=0.2), colors[idx].format(alpha=1))
        idx = (idx + 1) % len(colors)