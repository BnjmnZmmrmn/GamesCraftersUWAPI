"""
===== STEP 1 ===== 
Create a function that returns AutoGUIv2 Data for your game, given a variant of that game.
Return None if no AutoGUIv2 Data for the given variant.

get_<game>(variant_id) should return JSON of the following form:

    {
        "defaultTheme": <name of default theme>,
        "themes": {
            <name of theme1>: {
                "backgroundGeometry": [<width>, <height>],
                "backgroundImage": <path to background image; if no background image, omit this attribute>,
                "foregroundImage": <path to foreground image; if no foreground image, omit this attribute>,
                "centers": [ [<x0>,<y0>], [<x1>, <y1>], [<x2>, <y2>], [<x3>, <y3>], ... ]
                "pieces": {
                    <char1>: {
                        "image": <path to piece image>, "scale": <image scale>
                    },
                    <char2>: {
                        ...    
                    }
                    ...
                }
            },
            <name of theme2>: {
                ...
            },
            ...
        }
    }

EXAMPLE:

    def get_ttt(variant_id):
        if variant_id == "regular":
            data = {
                "defaultTheme": "simple",
                "themes": {
                    "simple": {
                        "backgroundGeometry": [30, 30], "backgroundImage": "ttt/background.svg", "centers": [ [5, 5], [15, 5], [25, 5], [5, 15], [15, 15], [25, 15], [5, 25], [15, 25], [25, 25] ], "pieces": {
                            "x": {"image": "ttt/x.svg", "scale": 1.0}, "o": {"image": "ttt/x.svg", "scale": 1.0}
                        }
                    }
                }
            }
            return data
        else:
            return None


(Scroll all the way down for Step 2).

"""

def get_lite3(variant_id):
    if variant_id not in ['three-in-a-row', 'surround', 'both']:
        return None
    return {
        "defaultTheme": "regular",
        "themes": {
            "regular": {
                "backgroundGeometry": [30, 30],
                "backgroundImage": "lite3/3x3grid.svg",
                "centers": [
                    [5, 5], [15, 5], [25, 5],
                    [5, 15], [15, 15], [25, 15],
                    [5, 25], [15, 25], [25, 25]
                ],
                "pieces": {
                    "a": {"image": "lite3/o.svg", "scale": 3.0},
                    "b": {"image": "lite3/o.svg", "scale": 6.0},
                    "c": {"image": "lite3/o.svg", "scale": 9.0},
                    "1": {"image": "lite3/x.svg", "scale": 3.0},
                    "2": {"image": "lite3/x.svg", "scale": 6.0},
                    "3": {"image": "lite3/x.svg", "scale": 9.0}
                }
            }
        }
    }

def get_baghchal(variant_id):
    return {
        "regular": {
            "defaultTheme": "stolen_art",
            "themes": {
                "stolen_art": {
                    "backgroundGeometry": [5, 6],
                    "backgroundImage": "baghchal/grid5Diag.svg",
                    "arrowThickness": 0.05,
                    "centers": [[0.5 + (i % 5), 0.5 + (i // 5)] for i in range(25)] + [[3.75,5.2], [3.95,5.2], [-1,-1], [3.75,5.55], [3.95,5.55]],
                    "pieces": {
                        "G": {
                            "image": "baghchal/G.png", "scale": 0.75
                        }, "T": {
                            "image": "baghchal/T.png", "scale": 0.75
                        }, "0": {
                            "image": "general/0.svg", "scale": 1.2
                        }, "1": {
                            "image": "general/1.svg", "scale": 1.2
                        }, "2": {
                            "image": "general/2.svg", "scale": 1.2
                        }, "3": {
                            "image": "general/3.svg", "scale": 1.2
                        }, "4": {
                            "image": "general/4.svg", "scale": 1.2
                        }, "5": {
                            "image": "general/5.svg", "scale": 1.2
                        }, "6": {
                            "image": "general/6.svg", "scale": 1.2
                        }, "7": {
                            "image": "general/7.svg", "scale": 1.2
                        }, "8": {
                            "image": "general/8.svg", "scale": 1.2
                        }, "9": {
                            "image": "general/9.svg", "scale": 1.2
                        }
                    }
                }
            }
        }
    }.get(variant_id, None)

def get_3spot(variant_id):
    return {
        "regular": {
            "defaultTheme": "standard",
            "themes": {
                "standard": {
                    "backgroundGeometry": [
                        3, 4
                    ],
                    "backgroundImage": "3spot/grid.svg",
                    "centers": [
                        [0.5, 0.5], [1, 0.5], [1.5, 0.5], [2, 0.5], [2.5, 0.5], 
                        [0.5, 1], [1, 1], [1.5, 1], [2, 1], [2.5, 1], 
                        [0.5, 1.5], [1, 1.5], [1.5, 1.5], [2, 1.5], [2.5, 1.5], 
                        [0.5, 2.0], [1, 2.0], [1.5, 2.0], [2, 2.0], [2.5, 2.0], 
                        [0.5, 2.5], [1, 2.5], [1.5, 2.5], [2, 2.5], [2.5, 2.5], 
                        [0.3, 3.5], [0.7, 3.5], [-1, -1], [2.3, 3.5], [2.7, 3.5]
                    ],
                    "pieces": {
                        "R": {
                            "image": "3spot/R.svg", "scale": 1.0
                        }, "W": {
                            "image": "3spot/W.svg", "scale": 1.0
                        }, "B": {
                            "image": "3spot/B.svg", "scale": 1.0
                        }, "h": {
                            "image": "3spot/h.svg", "scale": 0.3
                        }, "v": {
                            "image": "3spot/v.svg", "scale": 0.3
                        }, "0": {
                            "image": "general/0.svg", "scale": 2.0
                        }, "1": {
                            "image": "general/1.svg", "scale": 2.0
                        }, "2": {
                            "image": "general/2.svg", "scale": 2.0
                        }, "3": {
                            "image": "general/3.svg", "scale": 2.0
                        }, "4": {
                            "image": "general/4.svg", "scale": 2.0
                        }, "5": {
                            "image": "general/5.svg", "scale": 2.0
                        }, "6": {
                            "image": "general/6.svg", "scale": 2.0
                        }, "7": {
                            "image": "general/7.svg", "scale": 2.0
                        }, "8": {
                            "image": "general/8.svg", "scale": 2.0
                        }, "9": {
                            "image": "general/9.svg", "scale": 2.0
                        }
                    }
                }
            }
        }
    }.get(variant_id, None)

def get_369mm(variant_id):
    return {
        "regular": {
            "defaultTheme": "wikipedia",
            "themes": {
                "wikipedia": {
                    "backgroundGeometry": [
                        300, 300
                    ],
                    "backgroundImage": "369mm/board.svg",
                    "arrowThickness": 5,
                    "centers": [
                        [145, 140], [99, 99], [99, 99], [99, 99], [99, 99], [99, 99], 
                        [175, 140], [40, 20], [99, 99], [99, 99], [160, 20], [99, 99], 
                        [99, 99], [280, 20], [99, 99], [80, 60], [99, 99], [160, 60], 
                        [99, 99], [240, 60], [99, 99], [99, 99], [99, 99], [120, 100], 
                        [160, 100], [200, 100], [99, 99], [99, 99], [40, 140], 
                        [80, 140], [120, 140], [99, 99], [200, 140], [240, 140], 
                        [280, 140], [99, 99], [99, 99], [120, 180], [160, 180], 
                        [200, 180], [99, 99], [99, 99], [99, 99], [80, 220], [99, 99], 
                        [160, 220], [99, 99], [240, 220], [99, 99], [40, 260], [99, 99], 
                        [99, 99], [160, 260], [99, 99], [99, 99], [280, 260]
                    ],
                    "pieces": {
                        "0": {
                            "image": "general/0.svg", "scale": 100.0
                        }, "1": {
                            "image": "general/1.svg", "scale": 100.0
                        }, "2": {
                            "image": "general/2.svg", "scale": 100.0
                        }, "3": {
                            "image": "general/3.svg", "scale": 100.0
                        }, "4": {
                            "image": "general/4.svg", "scale": 100.0
                        }, "5": {
                            "image": "general/5.svg", "scale": 100.0
                        }, "6": {
                            "image": "general/6.svg", "scale": 100.0
                        }, "7": {
                            "image": "general/7.svg", "scale": 100.0
                        }, "8": {
                            "image": "general/8.svg", "scale": 100.0
                        }, "9": {
                            "image": "general/9.svg", "scale": 100.0
                        }, "B": {
                            "image": "369mm/X.svg", "scale": 28.6
                        }, "W": {
                            "image": "369mm/O.svg", "scale": 28.6
                        }
                    }
                }
            }
        }
    }.get(variant_id, None)

def get_topitop(variant_id):
    return {
        "regular": {
            "defaultTheme": "beach",
            "themes": {
                "beach": {
                    "backgroundGeometry": [
                        3, 4
                    ],
                    "backgroundImage": "topitop/grid.svg",
                    "centers": [
                        [99, 99], [99, 99], [99, 99], [99, 99], [99, 99], [99, 99], 
                        [0.5, 0.5], [1.5, 0.5], [2.5, 0.5], [99, 99], [99, 99], 
                        [0.5, 1.5], [1.5, 1.5], [2.5, 1.5], [99, 99], [99, 99], 
                        [0.5, 2.5], [1.5, 2.5], [2.5, 2.5], [99, 99], [99, 99], 
                        [99, 99], [1.5, 3.85], [99, 99], [99, 99], [0.25, 3.15], 
                        [0.25, 3.85], [99, 99], [0.8, 3.15], [0.8, 3.85], 
                        [1.5, 3.15], [1.5, 3.85], [99, 99], [2.4, 3.15], 
                        [2.4, 3.85], [99, 99], [99, 99], [99, 99], [99, 99], [99, 99]
                    ],
                    "pieces": {
                        "0": {
                            "image": "general/0.svg", "scale": 1.0
                        }, "1": {
                            "image": "general/1.svg", "scale": 1.0
                        }, "2": {
                            "image": "general/2.svg", "scale": 1.0
                        }, "3": {
                            "image": "general/3.svg", "scale": 1.0
                        }, "4": {
                            "image": "general/4.svg", "scale": 1.0
                        }, "B": {
                            "image": "topitop/B.svg", "scale": 1.0
                        }, "R": {
                            "image": "topitop/R.svg", "scale": 1.0
                        }, "S": {
                            "image": "topitop/S.svg", "scale": 1.0
                        }, "L": {
                            "image": "topitop/L.svg", "scale": 1.0
                        }, "X": {
                            "image": "topitop/X.svg", "scale": 1.0
                        }, "O": {
                            "image": "topitop/O.svg", "scale": 1.0
                        }, "C": {
                            "image": "topitop/C.svg", "scale": 1.0
                        }, "P": {
                            "image": "topitop/P.svg", "scale": 1.0
                        }, "Q": {
                            "image": "topitop/Q.svg", "scale": 1.0
                        }, "b": {
                            "image": "topitop/bb.svg", "scale": 1.0
                        }, "r": {
                            "image": "topitop/rr.svg", "scale": 1.0
                        }, "s": {
                            "image": "topitop/ss.svg", "scale": 1.0
                        }, "l": {
                            "image": "topitop/ll.svg", "scale": 1.0
                        }
                    }
                }
            }
        }
    }.get(variant_id, None)

def get_Lgame(variant_id):
    return {
        "regular": {
            "defaultTheme": "regular",
            "themes": {
                "regular": {
                    "backgroundGeometry": [
                        4, 4
                    ],
                    "backgroundImage": "Lgame/grid.svg",
                    "centers": [
                        [99, 99], [99, 99], [99, 99], [99, 99], [0.5, 0.5], 
                        [1.5, 0.5], [2.5, 0.5], [3.5, 0.5], [99, 99], 
                        [99, 99], [99, 99], [99, 99], [99, 99], [99, 99], 
                        [99, 99], [99, 99], [0.5, 1.5], [1.5, 1.5], 
                        [2.5, 1.5], [3.5, 1.5], [99, 99], [99, 99], 
                        [99, 99], [99, 99], [99, 99], [99, 99], [99, 99], 
                        [99, 99], [0.5, 2.5], [1.5, 2.5], [2.5, 2.5], 
                        [3.5, 2.5], [99, 99], [99, 99], [99, 99], [99, 99], 
                        [99, 99], [99, 99], [99, 99], [99, 99], [0.5, 3.5], 
                        [1.5, 3.5], [2.5, 3.5], [3.5, 3.5], [99, 99], 
                        [99, 99], [99, 99], [99, 99], [0.15, 0.15], [1.15, 0.15], 
                        [2.15, 0.15], [0.15, 1.15], [1.15, 1.15], [2.15, 1.15], 
                        [1.85, 0.15], [2.85, 0.15], [3.85, 0.15], [1.85, 1.15], 
                        [2.85, 1.15], [3.85, 1.15], [3.85, 0.75], [3.85, 1.75], 
                        [3.85, 2.15], [2.85, 0.75], [2.85, 1.75], [2.85, 2.15], 
                        [3.375, 1.85], [3.375, 2.85], [3.375, 3.85], [2.375, 1.85], 
                        [2.375, 2.25], [2.85, 3.25], [3.85, 3.85], [2.85, 3.85], 
                        [1.85, 3.85], [3.85, 2.85], [2.85, 2.85], [1.85, 2.85], 
                        [2.15, 3.85], [1.15, 3.85], [0.15, 3.85], [2.15, 2.85], 
                        [1.15, 2.85], [0.15, 2.85], [0.625, 3.85], [0.625, 2.85], 
                        [0.625, 1.85], [1.15, 3.25], [1.625, 2.25], [1.625, 1.85], 
                        [0.15, 2.15], [0.15, 1.75], [0.15, 0.75], [1.15, 2.15], 
                        [1.15, 1.75], [1.15, 0.75]
                    ],
                    "pieces": {
                        "B": {
                            "image": "Lgame/B.svg", "scale": 1.0
                        }, "R": {
                            "image": "Lgame/R.svg", "scale": 1.0
                        }, "W": {
                            "image": "Lgame/S1.svg", "scale": 1.0
                        }, "G": {
                            "image": "Lgame/S2.svg", "scale": 1.0
                        }, "1": {
                            "image": "Lgame/L1.svg", "scale": 0.6
                        }, "2": {
                            "image": "Lgame/L2.svg", "scale": 0.6
                        }, "3": {
                            "image": "Lgame/L3.svg", "scale": 0.6
                        }, "4": {
                            "image": "Lgame/L4.svg", "scale": 0.6
                        }, "5": {
                            "image": "Lgame/L5.svg", "scale": 0.6
                        }, "6": {
                            "image": "Lgame/L6.svg", "scale": 0.6
                        }, "7": {
                            "image": "Lgame/L7.svg", "scale": 0.6
                        }, "8": {
                            "image": "Lgame/L8.svg", "scale": 0.6
                        }
                    }
                }
            }
        }
    }.get(variant_id, None)

def get_dodgem(variant_id):
    return {
        "regular": {
            "defaultTheme": "regular",
            "themes": {
                "regular": {
                    "backgroundGeometry": [
                        4, 4
                    ],
                    "piecesOverArrows": True,
                    "backgroundImage": "dodgem/grid.svg",
                    "centers": [
                        [0.5, 0.5], [1.5, 0.5], [2.5, 0.5], [3.5, 0.5], 
                        [0.5, 1.5], [1.5, 1.5], [2.5, 1.5], [3.5, 1.5], 
                        [0.5, 2.5], [1.5, 2.5], [2.5, 2.5], [3.5, 2.5], 
                        [0.5, 3.5], [1.5, 3.5], [2.5, 3.5], [3.5, 3.5]
                    ],
                    "pieces": {
                        "x": {
                            "image": "dodgem/x.svg", "scale": 1
                        }, "o": {
                            "image": "dodgem/o.svg", "scale": 1
                        }
                    }
                }
            }
        }
    }.get(variant_id, None)

def get_tttwo(variant_id):
    return {
        "regular": {
            "defaultTheme": "regular",
            "themes": {
                "regular": {
                    "backgroundGeometry": [
                        104, 124
                    ],
                    "backgroundImage": "tttwo/grid.svg",
                    "centers": [
                        [12, 12], [32, 12], [52, 12], [72, 12], [92, 12], 
                        [12, 32], [32, 32], [52, 32], [72, 32], [92, 32], 
                        [12, 52], [32, 52], [52, 52], [72, 52], [92, 52], 
                        [12, 72], [32, 72], [52, 72], [72, 72], [92, 72], 
                        [12, 92], [32, 92], [52, 92], [72, 92], [92, 92], 
                        [12, 112], [92, 112], [999, 999], [999, 999], [52, 112]
                    ],
                    "pieces": {
                        "x": {
                            "image": "tttwo/a.svg", "scale": 56.0
                        }, "o": {
                            "image": "tttwo/b.svg", "scale": 56.0
                        }, "s": {
                            "image": "tttwo/s.svg", "scale": 56.0
                        }, "X": {
                            "image": "tttwo/X.svg", "scale": 16.0
                        }, "O": {
                            "image": "tttwo/O.svg", "scale": 16.0
                        }, "G": {
                            "image": "tttwo/s.svg", "scale": 16.0
                        }, "0": {
                            "image": "general/0.svg", "scale": 50.0
                        }, "1": {
                            "image": "general/1.svg", "scale": 50.0
                        }, "2": {
                            "image": "general/2.svg", "scale": 50.0
                        }, "3": {
                            "image": "general/3.svg", "scale": 50.0
                        }, "4": {
                            "image": "general/4.svg", "scale": 50.0
                        }
                    }
                }
            }
        }
    }.get(variant_id, None)

def get_stt(variant_id):
    return {
        "default": {
            "defaultTheme": "regular",
            "themes": {
                "regular": {
                    "backgroundGeometry": [
                        9, 6
                    ],
                    "arrowThickness": 0.15,
                    "foregroundImage": "stt/foreground.svg",
                    "centers": [
                        [3.5, 0.5], [4.5, 0.5], [5.5, 0.5], 
                        [3.5, 1.5], [4.5, 1.5], [5.5, 1.5], 
                        [0, 2.5], [1, 2.5], [2, 2.5], 
                        [2.5, 2.5], [3.5, 2.5], [4.5, 2.5], 
                        [5.5, 2.5], [6.5, 2.5], [7, 2.5], 
                        [8, 2.5], [9, 2.5], [0, 3.5], 
                        [1, 3.5], [2, 3.5], [2.5, 3.5], 
                        [3.5, 3.5], [4.5, 3.5], [5.5, 3.5], 
                        [6.5, 3.5], [7, 3.5], [8, 3.5], 
                        [9, 3.5], [0, 4.5], [1, 4.5], 
                        [2, 4.5], [2.5, 4.5], [3.5, 4.5], 
                        [4.5, 4.5], [5.5, 4.5], [6.5, 4.5], 
                        [7, 4.5], [8, 4.5], [9, 4.5], 
                        [2.5, 5.5], [6.5, 5.5], [3.5, 2.5], 
                        [4.5, 2.5], [5.5, 2.5], [3.5, 3.5], 
                        [4.5, 3.5], [5.5, 3.5], [3.5, 4.5], 
                        [4.5, 4.5], [5.5, 4.5]
                    ],
                    "pieces": {
                        "S": {
                            "image": "stt/S.svg", "scale": 5.0
                        }, "x": {
                            "image": "stt/x.svg", "scale": 1.0
                        }, "o": {
                            "image": "stt/o.svg", "scale": 1.0
                        }
                    }
                }
            }
        }
    }.get(variant_id, None)

def get_tootnottopy(variant_id):
    return {
        "6": {
            "defaultTheme": "dan",
            "themes": {
                "dan": {
                    "backgroundGeometry": [
                        120, 70
                    ],
                    "backgroundImage": "tootnotto/board.svg",
                    "centers": [
                        [99, 99], [99, 99], [99, 99], 
                        [35, 5], [45, 5], [55, 5], 
                        [65, 5], [75, 5], [85, 5], 
                        [99, 99], [99, 99], [99, 99], 
                        [5, 15], [15, 15], [99, 99], 
                        [35, 15], [45, 15], [55, 15], 
                        [65, 15], [75, 15], [85, 15], 
                        [99, 99], [105, 15], [115, 15], 
                        [5, 25], [15, 25], [99, 99], 
                        [99, 99], [99, 99], [99, 99], 
                        [99, 99], [99, 99], [99, 99], 
                        [99, 99], [105, 25], [115, 25], 
                        [5, 35], [15, 35], [99, 99], 
                        [35, 35], [45, 35], [55, 35], 
                        [65, 35], [75, 35], [85, 35], 
                        [99, 99], [105, 35], [115, 35], 
                        [5, 45], [15, 45], [99, 99], 
                        [35, 45], [45, 45], [55, 45], 
                        [65, 45], [75, 45], [85, 45], 
                        [99, 99], [105, 45], [115, 45], 
                        [5, 55], [15, 55], [99, 99], 
                        [35, 55], [45, 55], [55, 55], 
                        [65, 55], [75, 55], [85, 55], 
                        [99, 99], [105, 55], [115, 55], 
                        [5, 65], [15, 65], [99, 99], 
                        [35, 65], [45, 65], [55, 65], 
                        [65, 65], [75, 65], [85, 65], 
                        [99, 99], [105, 65], [115, 65]
                    ],
                    "pieces": {
                        "T": {
                            "image": "tootnotto/T.svg", "scale": 10.0
                        }, "t": {
                            "image": "tootnotto/tt.svg", "scale": 10.0
                        }, "O": {
                            "image": "tootnotto/O.svg", "scale": 10.0
                        }, "o": {
                            "image": "tootnotto/oo.svg", "scale": 10.0
                        }
                    }
                }
            }
        }
    }.get(variant_id, None)

def get_ctoi(variant_id):
    return {
        "regular": {
            "defaultTheme": "regular",
            "themes": {
                "regular": {
                    "backgroundGeometry": [
                        3, 4
                    ],
                    "backgroundImage": "ctoi/grid.svg",
                    "centers": [
                        [0.5, 0.5], [1.5, 0.5], [2.5, 0.5], 
                        [0.5, 1.5], [1.5, 1.5], [2.5, 1.5], 
                        [0.5, 2.5], [1.5, 2.5], [2.5, 2.5], 
                        [99, 99], [99, 99], [99, 99], 
                        [1, 3.4], [2, 3.4], [99, 99], 
                        [1, 3.8], [2, 3.8], [99, 99]
                    ],
                    "pieces": {
                        "R": {
                            "image": "ctoi/R.svg", "scale": 1.0
                        }, "W": {
                            "image": "ctoi/W.svg", "scale": 1.0
                        }, "T": {
                            "image": "ctoi/T.svg", "scale": 1.0
                        }, "X": {
                            "image": "ctoi/X.svg", "scale": 1.0
                        }, "t": {
                            "image": "ctoi/tt.svg", "scale": 1.0
                        }, "x": {
                            "image": "ctoi/xx.svg", "scale": 1.0
                        }, "Y": {
                            "image": "ctoi/X.svg", "scale": 0.6
                        }, "Z": {
                            "image": "ctoi/T.svg", "scale": 0.6
                        }, "y": {
                            "image": "ctoi/xx.svg", "scale": 0.6
                        }, "z": {
                            "image": "ctoi/tt.svg", "scale": 0.6
                        }
                    }
                }
            }
        }
    }.get(variant_id, None)

def get_chomp(variant_id):
    return {
        "3x2": {
            "defaultTheme": "choco",
            "themes": {
                "choco": {
                    "backgroundGeometry": [2, 3],
                    "centers": [
                        [0.5, 0.5], [1.5, 0.5], [0.5, 1.5], 
                        [1.5, 1.5], [0.5, 2.5], [1.5, 2.5]
                    ],
                    "pieces": {
                        "x" : {
                            "image": "chomp/x.svg", "scale": 1.0
                        }
                    }
                }
            }
        },
        "4x7": {
            "defaultTheme": "choco",
            "themes": {
                "choco": {
                    "backgroundGeometry": [7, 4],
                    "centers": [
                        [0.5, 0.5], [1.5, 0.5], [2.5, 0.5], [3.5, 0.5], 
                        [4.5, 0.5], [5.5, 0.5], [6.5, 0.5], 
                        [0.5, 1.5], [1.5, 1.5], [2.5, 1.5], [3.5, 1.5], 
                        [4.5, 1.5], [5.5, 1.5], [6.5, 1.5], 
                        [0.5, 2.5], [1.5, 2.5], [2.5, 2.5], [3.5, 2.5], 
                        [4.5, 2.5], [5.5, 2.5], [6.5, 2.5], 
                        [0.5, 3.5], [1.5, 3.5], [2.5, 3.5], [3.5, 3.5], 
                        [4.5, 3.5], [5.5, 3.5], [6.5, 3.5]
                    ],
                    "pieces": {
                        "x" : {
                            "image": "chomp/x.svg", "scale": 1.0
                        }
                    }
                }
            }
        }
    }.get(variant_id, None)

def get_dawsonschess(variant_id):
    size = int(variant_id)
    return {
        "defaultTheme": "kings",
        "themes": {
            "kings": {
                "backgroundGeometry": [size, 1],
                "centers": [[0.5 + i, 0.5] for i in range(size)],
                "pieces": {
                    "b": {
                        "image": "dawsonschess/b.svg", "scale": 1
                    },
                    "x": {
                        "image": "dawsonschess/x.svg", "scale": 1
                    },
                    "o": {
                        "image": "dawsonschess/o.svg", "scale": 1
                    }
                }
            }
        }
    }

def get_chess(variant_id):
    if variant_id != '7-man':
        return None
    pieces = {
                "K": "K", "Q": "Q", "R": "R", "B": "B", "N": "N", 
                "P": "P", "k": "kk", "q": "qq", "r": "rr", 
                "b": "bb", "n": "nn", "p": "pp"
            }
    return {
            "defaultTheme": "wikipedia",
            "themes": {
                "wikipedia": {
                    "backgroundGeometry": [8, 8],
                    "arrowThickness": 0.1,
                    "backgroundImage": "chess/wikipedia/grid.svg",
                    "centers": [[0.5 + (i % 8), 0.5 + (i // 8)] for i in range(64)],
                    "pieces": {k: {"image": "chess/wikipedia/{}.svg".format(v), "scale": 1} for (k, v) in pieces.items()}
                },
                "lichess": {
                    "backgroundGeometry": [8, 8],
                    "arrowThickness": 0.1,
                    "backgroundImage": "chess/lichess/grid.svg",
                    "centers": [[0.5 + (i % 8), 0.5 + (i // 8)] for i in range(64)],
                    "pieces": {k: {"image": "chess/lichess/{}.svg".format(v), "scale": 1} for (k, v) in pieces.items()}
                }
            }
        }

def get_snake(variant_id):
    if variant_id != "regular":
        return None
    return {
        "defaultTheme": "slither",
        "themes": {
            "slither": {
                "backgroundGeometry": [4, 4],
                "piecesOverArrows": True,
                "backgroundImage": "snake/background.svg",
                "centers": [[0.5 + i % 4, 0.5 + i // 4] for i in range(16)],
                "pieces": {
                    "b": {
                        "image": "snake/b.svg", "scale": 1.0
                    },
                    "h": {
                        "image": "snake/h.svg", "scale": 1.0
                    },
                    "t": {
                        "image": "snake/t.svg", "scale": 1.0
                    }
                }
            }
        }
    }
    
def get_quickcross(variant_id):
    if variant_id != "regular": # 4x4 variant (option-9)
        return None
    #48.75,141.25,233.75,326.25
    center_maps = [
            [48.75, 48.75], #0
            [141.25, 48.75],#1
            [233.75, 48.75], #2
            [326.25, 48.75], #3
            [48.75, 141.25], #4
            [141.25, 141.25],#5
            [233.75, 141.25], #6
            [326.25, 141.25], #7
            [48.75, 233.75], #8
            [141.25, 233.75], #9
            [233.75, 233.75],#10
            [326.25, 233.75], #11
            [48.75, 326.25], #12
            [141.25, 326.25], #13
            [233.75, 326.25], #14
            [326.25, 326.25], #15
        ]
    width = 27.5
    left_cross = [[center_maps[i][0] - width, center_maps[i][1]] for i in range(len(center_maps))]
    right_cross = [[center_maps[i][0] + width, center_maps[i][1]] for i in range(len(center_maps))]
    top_cross = [[center_maps[i][0], center_maps[i][1] - width] for i in range(len(center_maps))]
    bottom_cross = [[center_maps[i][0], center_maps[i][1] + width] for i in range(len(center_maps))]
    mapping_list = center_maps + left_cross + right_cross + top_cross + bottom_cross

    return {
        "defaultTheme": "moffitt", #because Cameron and Arihant worked in Moffitt
        "themes": {
            "moffitt": {
                "backgroundGeometry": [375, 375],
                "backgroundImage": "quickcross/background.svg",
                #centers contains mappings to points in the background svg that point to the following:
                #centers[0->15]: centers, [16->31]: left coordinate for horizontal piece
                #centers[32->47]: right coordinate for horizontal piece
                #centers[48->63]: top coordinate for vertical piece
                #centers[64->79]: bottom coordinate for vertical piece.
                "centers": mapping_list,
                "pieces": {
                    "v": {
                        "image": "quickcross/V.svg", "scale": 70.0
                    },
                    "h": {
                        "image": "quickcross/H.svg", "scale": 70.0
                    },
                    "r": {
                        "image": "quickcross/rotate.svg", "scale": 30.0
                    }
                }
            }
        }
    }



def get_haregame(variant_id):
    if variant_id == 's-hounds-first' or variant_id == "s-hare-first":
        return {
            "defaultTheme": "regular",
            "themes": {
                "regular": {
                    "backgroundGeometry": [180, 100],
                    "piecesOverArrows": True,
                    "arrowThickness": 2,
                    "backgroundImage": "haregame/boardsmall.svg",
                    "centers": [[10, 50]] + [[40*i + 50, 40*j + 10] for i in range(3) for j in range(3)] + [[170, 50]],
                    "pieces": {
                        "d": {
                            "image": "haregame/d.svg", "scale": 20
                        }, "r": {
                            "image": "haregame/r.svg", "scale": 20
                        }
                    }
                }
            }
        }
    elif variant_id == 'm-hounds-first' or variant_id == "m-hare-first":
        return {
            "defaultTheme": "regular",
            "themes": {
                "regular": {
                    "backgroundGeometry": [260, 100],
                    "piecesOverArrows": True,
                    "arrowThickness": 2,
                    "backgroundImage": "haregame/boardmedium.svg",
                    "centers": [[10, 50]] + [[40*i + 50, 40*j + 10] for i in range(5) for j in range(3)] + [[250, 50]],
                    "pieces": {
                        "d": {
                            "image": "haregame/d.svg", "scale": 20
                        }, "r": {
                            "image": "haregame/r.svg", "scale": 20
                        }
                    }
                }
            }
        }
    elif variant_id == 'l-hounds-first' or variant_id == "l-hare-first":
        return {
            "defaultTheme": "regular",
            "themes": {
                "regular": {
                    "backgroundGeometry": [340, 100],
                    "piecesOverArrows": True,
                    "arrowThickness": 2,
                    "backgroundImage": "haregame/boardlarge.svg",
                    "centers": [[10, 50]] + [[40*i + 50, 40*j + 10] for i in range(7) for j in range(3)] + [[330, 50]],
                    "pieces": {
                        "d": {
                            "image": "haregame/d.svg", "scale": 20
                        }, "r": {
                            "image": "haregame/r.svg", "scale": 20
                        }
                    }
                }
            }
        }
    return None

def get_connect4c(variant_id):
    if variant_id == '6x6':
        return {
            "defaultTheme": "normal",
            "themes": {
                "normal": {
                    "backgroundGeometry": [6, 7],
                    "foregroundImage": "connect4/foreground6x6.svg",
                    "centers": [[0.5 + i // 6, 1.5 + i % 6] for i in range(36)] + [[0.5 + i, 0.5] for i in range(6)],
                    "pieces": {
                        "X": {
                            "image": "connect4/X.svg", "scale": 1.0
                        }, "O": {
                            "image": "connect4/O.svg", "scale": 1.0
                        }, "a": {
                            "image": "connect4/a.svg", "scale": 0.8
                        }
                    }
                }
            }
        }
    elif variant_id == '6x7':
        return {
            "defaultTheme": "normal",
            "themes": {
                "normal": {
                    "backgroundGeometry": [7, 7],
                    "foregroundImage": "connect4/foreground6x7.svg",
                    "centers": [[0.5 + i // 6, 1.5 + i % 6] for i in range(42)] + [[0.5 + i, 0.5] for i in range(7)],
                    "pieces": {
                        "X": {
                            "image": "connect4/X.svg", "scale": 1.0
                        }, "O": {
                            "image": "connect4/O.svg", "scale": 1.0
                        }, "a": {
                            "image": "connect4/a.svg", "scale": 0.8
                        }
                    }
                }
            }
        } 
    return None

def get_mutorere(variant_id):
    if variant_id not in ('regular', 'misere'):
        return None
    return {
        "defaultTheme": "octagon",
        "themes": {
            "octagon": {
                "backgroundGeometry": [100, 100],
                "piecesOverArrows": True,
                "backgroundImage": "mutorere/board.svg",
                "centers": [
                    [50 + 17 * x, 50 + 17 * y] for x, y in 
                    [[0, 0], [-1, -2.41421], [-2.41421, -1], [-2.41421, 1], [-1, 2.41421],
                     [1, 2.41421], [2.41421, 1], [2.41421, -1], [1, -2.41421]]
                ],
                "pieces": {
                    "x": {
                        "image": "general/blue_circle.svg", "scale": 10
                    },
                    "o": {
                        "image": "general/red_circle.svg", "scale": 10
                    }
                }
            }
        }
    }
    
def get_achi(variant_id):
    return {
        "defaultTheme": "basic",
        "themes": {
            "basic": {
                "backgroundGeometry": [100, 100],
                "backgroundImage": "achi/achiboard.svg",
                "piecesOverArrows": True,
                "arrowThickness": 4,
                "defaultMoveTokenRadius": 6.5,
                "centers": [
                    [10, 10],
                    [50, 10],
                    [90, 10],
                    [10, 50],
                    [50, 50],
                    [90, 50],
                    [10, 90],
                    [50, 90],
                    [90, 90],
                ],
                "pieces": {
                    "x": {
                        "image": "369mm/X.svg", "scale": 15
                    },
                    "o": {
                        "image": "369mm/O.svg", "scale": 15
                    }
                }
            }
        }
    }

def get_dinododgem(variant_id):
    return {
        "regular": {
            "defaultTheme": "regular",
            "themes": {
                "regular": {
                    "backgroundGeometry": [
                        6, 6
                    ],
                    "piecesOverArrows": True,
                    "arrowThickness": 0.09,
                    "backgroundImage": "dinododgem/new_grid.svg",
                    "centers": [
                        [0.5, 5.5], [0.5, 4.5], [0.5, 3.5], [0.5, 2.5], [0.5, 1.5], 
                        [1.5, 5.5], [1.5, 4.5], [1.5, 3.5], [1.5, 2.5], [1.5, 1.5], 
                        [2.5, 5.5], [2.5, 4.5], [2.5, 3.5], [2.5, 2.5], [2.5, 1.5], 
                        [3.5, 5.5], [3.5, 4.5], [3.5, 3.5], [3.5, 2.5], [3.5, 1.5], 
                        [4.5, 5.5], [4.5, 4.5], [4.5, 3.5], [4.5, 2.5], [4.5, 1.5], 
                        [1.5, 0.5], [2.5, 0.5], [3.5, 0.5], [4.5, 0.5], [5.5, 1.5], 
                        [5.5, 2.5], [5.5, 3.5], [5.5, 4.5]
                    ],
                    "pieces": {
                        "x": {
                            "image": "dinododgem/hadrosaur.svg", "scale": 1.0
                        }, "o": {
                            "image": "dinododgem/triceratops.svg", "scale": 1.0
                        }
                    }
                }
            }
        }
    }.get(variant_id, None)
    
def get_quickchess(variant_id):
    return {
        "regular": {
            "defaultTheme": "regular",
            "themes": {
                "regular": {
                    "backgroundGeometry": [
                        4, 3
                    ],
                    "backgroundImage": "quickchess/grid.svg",
                    "centers": [
                        [0.5, 0.5], [0.5, 1.5], [0.5, 2.5], 
                        [1.5, 0.5], [1.5, 1.5], [1.5, 2.5], 
                        [2.5, 0.5], [2.5, 1.5], [2.5, 2.5], 
                        [3.5, 0.5], [3.5, 1.5], [3.5, 2.5],
                    ],
                    "pieces": {
                        "Q": {
                            "image": "chess/wikipedia/Q.svg", "scale": 1.0
                        }, "R": {
                            "image": "chess/wikipedia/R.svg", "scale": 1.0
                        }, "K": {
                            "image": "chess/wikipedia/K.svg", "scale": 1.0
                        }, "q": {
                            "image": "chess/wikipedia/qq.svg", "scale": 1.0
                        }, "r": {
                            "image": "chess/wikipedia/rr.svg", "scale": 1.0
                        }, "k": {
                            "image": "chess/wikipedia/kk.svg", "scale": 1.0
                        }
                    }
                }
            }
        }
    }.get(variant_id, None)

def get_tactix(variant_id):
    if variant_id != 'regular':
        return None
    return {
        "defaultTheme": "basic",
        "themes": {
            "basic": {
                "backgroundGeometry": [4, 4],
                "backgroundImage": "snake/background.svg",
                "centers": [[0.5, 0.5], [1.5, 0.5], [2.5, 0.5], [3.5, 0.5], 
                            [0.5, 1.5], [1.5, 1.5], [2.5, 1.5], [3.5, 1.5], 
                            [0.5, 2.5], [1.5, 2.5], [2.5, 2.5], [3.5, 2.5], 
                            [0.5, 3.5], [1.5, 3.5], [2.5, 3.5], [3.5, 3.5], 
                            [0.05, 0.08000000000000002], [1.95, 0.08000000000000002], 
                            [1.05, 0.4], [2.95, 0.4], [2.05, 0.08000000000000002], 
                            [3.95, 0.08000000000000002], [0.05, 0.16000000000000003], 
                            [2.95, 0.16000000000000003], [1.05, 0.32], [3.95, 0.32], 
                            [0.05, 0.24000000000000002], [3.95, 0.24000000000000002], 
                            [0.05, 1.0799999999999998], [1.95, 1.0799999999999998], 
                            [1.05, 1.4], [2.95, 1.4], [2.05, 1.0799999999999998], 
                            [3.95, 1.0799999999999998], [0.05, 1.16], [2.95, 1.16], 
                            [1.05, 1.3199999999999998], [3.95, 1.3199999999999998], 
                            [0.05, 1.24], [3.95, 1.24], [0.05, 2.08], [1.95, 2.08], 
                            [1.05, 2.4], [2.95, 2.4], [2.05, 2.08], [3.95, 2.08], 
                            [0.05, 2.16], [2.95, 2.16], [1.05, 2.32], [3.95, 2.32], 
                            [0.05, 2.2399999999999998], [3.95, 2.2399999999999998], 
                            [0.05, 3.08], [1.95, 3.08], [1.05, 3.4], [2.95, 3.4], 
                            [2.05, 3.08], [3.95, 3.08], [0.05, 3.16], [2.95, 3.16], 
                            [1.05, 3.32], [3.95, 3.32], [0.05, 3.2399999999999998], 
                            [3.95, 3.2399999999999998], [0.08000000000000002, 0.05], 
                            [0.08000000000000002, 1.95], [0.4, 1.05], [0.4, 2.95], 
                            [0.08000000000000002, 2.05], [0.08000000000000002, 3.95], 
                            [0.16000000000000003, 0.05], [0.16000000000000003, 2.95], 
                            [0.32, 1.05], [0.32, 3.95], [0.24000000000000002, 0.05], 
                            [0.24000000000000002, 3.95], [1.0799999999999998, 0.05], 
                            [1.0799999999999998, 1.95], [1.4, 1.05], [1.4, 2.95], 
                            [1.0799999999999998, 2.05], [1.0799999999999998, 3.95], 
                            [1.16, 0.05], [1.16, 2.95], [1.3199999999999998, 1.05], 
                            [1.3199999999999998, 3.95], [1.24, 0.05], [1.24, 3.95], 
                            [2.08, 0.05], [2.08, 1.95], [2.4, 1.05], [2.4, 2.95], 
                            [2.08, 2.05], [2.08, 3.95], [2.16, 0.05], [2.16, 2.95], 
                            [2.32, 1.05], [2.32, 3.95], [2.2399999999999998, 0.05], 
                            [2.2399999999999998, 3.95], [3.08, 0.05], [3.08, 1.95], 
                            [3.4, 1.05], [3.4, 2.95], [3.08, 2.05], [3.08, 3.95], 
                            [3.16, 0.05], [3.16, 2.95], [3.32, 1.05], [3.32, 3.95], 
                            [3.2399999999999998, 0.05], [3.2399999999999998, 3.95]],
                "pieces": {
                    "O": {
                        "image": "Lgame/S2.svg", "scale": 1
                    }
                }
            }
        }
    }

def get_othello(variant_id):
    return {
        "defaultTheme": "regular",
        "themes": {
            "regular": {
                "backgroundGeometry": [40, 50],
                "backgroundImage": "othello/grid.svg",
                "defaultMoveTokenRadius": 1.5,
                "centers": [[5, 5], [15, 5], [25, 5], [35, 5], 
                            [5, 15], [15, 15], [25, 15], [35, 15], 
                            [5, 25], [15, 25], [25, 25], [35, 25], 
                            [5, 35], [15, 35], [25, 35], [35, 35], 
                            [8, 45], [12, 45], 
                            [-1, -1], 
                            [28, 45], [32, 45]],
                "pieces": {
                    "B": {
                        "image": "othello/B.svg", "scale": 9
                    },
                    "W": {
                        "image": "othello/W.svg", "scale": 9
                    },
                    "0": {
                        "image": "general/0.svg", "scale": 20.0
                    },
                    "1": {
                        "image": "general/1.svg", "scale": 20.0
                    },
                    "2": {
                        "image": "general/2.svg", "scale": 20.0
                    },
                    "3": {
                        "image": "general/3.svg", "scale": 20.0
                    },
                    "4": {
                        "image": "general/4.svg", "scale": 20.0
                    },
                    "5": {
                        "image": "general/5.svg", "scale": 20.0
                    },
                    "6": {
                        "image": "general/6.svg", "scale": 20.0
                    },
                    "7": {
                        "image": "general/7.svg", "scale": 20.0
                    },
                    "8": {
                        "image": "general/8.svg", "scale": 20.0
                    },
                    "9": {
                        "image": "general/9.svg", "scale": 20.0
                    }
                }
            }
        }
    }
    
def get_gameofy(variant_id):
    if variant_id == "dim4" or variant_id == "dim4-misere":
        return {
            "defaultTheme": "basic",
            "themes": {
                "basic": {
                    "backgroundGeometry": [8, 6],
                    "backgroundImage": "gameofy/dim4.svg",
                    # "foregroundImage": <path to foreground image; if no foreground image, omit this attribute>,
                    "centers": [
                        [4, 1.2], [3.47, 2.1], [4.53, 2.1], [2.97, 3], 
                        [4, 3], [5.03, 3], [2.44, 3.9], [3.47, 3.9], 
                        [4.53, 3.9], [5.56, 3.9]
                    ],
                    "pieces": {
                        "W": {
                            "image": "gameofy/blue_circle.svg", "scale": 0.8
                        }, "B": {
                            "image": "gameofy/red_circle.svg", "scale": 0.8
                        }
                    }
                },
            }
        }
    elif variant_id == "dim5" or variant_id == "dim5-misere":
        return {
            "defaultTheme": "basic",
            "themes": {
                "basic": {
                    "backgroundGeometry": [8, 6],
                    "backgroundImage": "gameofy/dim5.svg",
                    # "foregroundImage": <path to foreground image; if no foreground image, omit this attribute>,
                    "centers": [
                        [4, 1.2], 
                        [3.47, 2.1], 
                        [4.53, 2.1], 
                        [2.97, 3], 
                        [4, 3], 
                        [5.03, 3], 
                        [2.44, 3.9], 
                        [3.47, 3.9], 
                        [4.53, 3.9], 
                        [5.56, 3.9], 
                        [1.91, 4.8], 
                        [2.97, 4.8], 
                        [4.00, 4.8], 
                        [5.03, 4.8], 
                        [6.09, 4.8], 
                        [6.62, 4.8], 
                    ],
                    "pieces": {
                        "W": {
                            "image": "gameofy/blue_circle.svg", "scale": 0.8
                        }, "B": {
                            "image": "gameofy/red_circle.svg", "scale": 0.8
                        }
                    }
                },
            }
        }
    
def get_notakto(variant_id):
    if variant_id == "regular":
        return {
            "defaultTheme": "basic",
            "themes": {
                "basic": {
                    "backgroundGeometry": [3, 3],
                    "backgroundImage": "notakto/grid1.svg",
                    # "foregroundImage": <path to foreground image; if no foreground image, omit this attribute>,
                    "centers": [
                        [0.5, 0.5], [1.5, 0.5], [2.5, 0.5],
                        [0.5, 1.5], [1.5, 1.5], [2.5, 1.5],
                        [0.5, 2.5], [1.5, 2.5], [2.5, 2.5]
                    ],
                    "pieces": {
                        "X": {
                            "image": "notakto/x.svg", "scale": 1
                        },
                    }
                },
            }
        }
    elif variant_id == "board2":
        return {
            "defaultTheme": "basic",
            "themes": {
                "basic": {
                    "backgroundGeometry": [6, 3],
                    "backgroundImage": "notakto/grid2.svg",
                    # "foregroundImage": <path to foreground image; if no foreground image, omit this attribute>,
                    "centers": [
                        [0.45, 0.5], [1.45, 0.5], [2.45, 0.5],
                        [0.45, 1.5], [1.45, 1.5], [2.45, 1.5],
                        [0.45, 2.5], [1.45, 2.5], [2.45, 2.5],
                        
                        [3.55, 0.5], [4.55, 0.5], [5.55, 0.5],
                        [3.55, 1.5], [4.55, 1.5], [5.55, 1.5],
                        [3.55, 2.5], [4.55, 2.5], [5.55, 2.5]
                    ],
                    "pieces": {
                        "X": {
                            "image": "notakto/x.svg", "scale": 1
                        },
                    }
                },
            }
        }
    elif variant_id == "board3":
        return {
            "defaultTheme": "basic",
            "themes": {
                "basic": {
                    "backgroundGeometry": [6, 6],
                    "backgroundImage": "notakto/grid3.svg",
                    # "foregroundImage": <path to foreground image; if no foreground image, omit this attribute>,
                    "centers": [
                        [0.45, 0.5], [1.45, 0.5], [2.45, 0.5],
                        [0.45, 1.5], [1.45, 1.5], [2.45, 1.5],
                        [0.45, 2.5], [1.45, 2.5], [2.45, 2.5],
                        
                        [3.55, 0.5], [4.55, 0.5], [5.55, 0.5],
                        [3.55, 1.5], [4.55, 1.5], [5.55, 1.5],
                        [3.55, 2.5], [4.55, 2.5], [5.55, 2.5],

                        [2.0, 3.55], [3.0, 3.55], [4.0, 3.55],
                        [2.0, 4.55], [3.0, 4.55], [4.0, 4.55],
                        [2.0, 5.55], [3.0, 5.55], [4.0, 5.55]
                    ],
                    "pieces": {
                        "X": {
                            "image": "notakto/x.svg", "scale": 1
                        },
                    }
                },
            }
        }

def get_beeline(variant_id):
    return {
        "defaultTheme": "basic",
        "themes": {
            "basic": {
                "backgroundGeometry": [10, 8],
                "backgroundImage": "beeline/board.svg",
                "arrowThickness": 0.1,
                "piecesOverArrows": True,
                # "foregroundImage": <path to foreground image; if no foreground image, omit this attribute>,
                "centers": [
                    [1.25, 4.75], # 0
                    [2.5, 4.05], # 1
                    [3.75, 3.3], # 2
                    [5.00, 2.6], # 3
                    [2.5, 5.5], # 4
                    [3.76, 4.75], # 5
                    [5.00, 4.05], # 6
                    [6.25, 3.3], # 7
                    [3.75, 6.2], # 8
                    [5, 5.5], # 9
                    [6.25, 4.75], # 10
                    [7.5, 4.05], # 11
                    [5.00, 6.95], # 12
                    [6.25, 6.2], # 13
                    [7.5, 5.5], # 14
                    [8.75, 4.75], # 15
                ],
                "pieces": {
                    "W": {
                        "image": "beeline/yellow_bee.svg", "scale": 1.4
                    },
                    "B": {
                        "image": "beeline/red_bee.svg", "scale": 1.4
                    }
                }
            },
        }
    }

def get_1dchess(variant_id):
    return {
        "defaultTheme": "basic",
        "themes": {
            "basic": {
                "backgroundGeometry": [8, 1],
                "backgroundImage": "1dchess/grid.svg",
                "piecesOverArrows": False,
                # "foregroundImage": <path to foreground image; if no foreground image, omit this attribute>,
                "centers": [
                    [0.5, 0.5],
                    [1.5, 0.5],
                    [2.5, 0.5],
                    [3.5, 0.5],
                    [4.5, 0.5],
                    [5.5, 0.5],
                    [6.5, 0.5],
                    [7.5, 0.5]
                ],
                "pieces": {
                    "K": {
                        "image": "1dchess/nn.svg", "scale": 1
                    },
                    "k": {
                        "image": "1dchess/N.svg", "scale": 1
                    },
                    "T": {
                        "image": "1dchess/kk.svg", "scale": 1
                    },
                    "t": {
                        "image": "1dchess/K.svg", "scale": 1
                    },
                    "R": {
                        "image": "1dchess/rr.svg", "scale": 1
                    },
                    "r": {
                        "image": "1dchess/R.svg", "scale": 1
                    },
                }
            },
        }
    }

def get_chinesechess(variant_id):
    pieces = {
        "K": "general_r", "A": "advisor_r", "R": "chariot_r", "B": "elephant_r", 
        "N": "horse_r", "P": "soldier_r", "Q": "soldier_r", "C":"cannon_r", 
        "k": "general_b", "a": "advisor_b", "r": "chariot_b", "b": "elephant_b", 
        "n": "horse_b", "p": "soldier_b", "q": "soldier_b", "c":"cannon_b"
    }
    
    return {
        "defaultTheme": "regular",
        "themes": {
            "regular": {
                "backgroundGeometry": [9, 10],
                "arrowThickness": 0.1,
                "backgroundImage": "chinesechess/board.svg",
                "centers": [[0.5 + (i % 9), 0.5 + (i // 9)] for i in range(90)],
                "pieces": {k: {"image": "chinesechess/regular/{}.svg".format(v), "scale": 1} for (k, v) in pieces.items()}
            },
            "graphical": {
                "backgroundGeometry": [9, 10],
                "arrowThickness": 0.1,
                "backgroundImage": "chinesechess/board.svg",
                "centers": [[0.5 + (i % 9), 0.5 + (i // 9)] for i in range(90)],
                "pieces": {k: {"image": "chinesechess/graphical/{}.svg".format(v), "scale": 1} for (k, v) in pieces.items()}
            }
        }
    }

def get_dao(variant_id):    
    return {
        "defaultTheme": "basic",
        "themes": {
            "basic": {
                "backgroundGeometry": [4, 4],
                "backgroundImage": "dao/grid.svg",
                "arrowThickness": 0.1,
                "piecesOverArrows": True,
                # "foregroundImage": <path to foreground image; if no foreground image, omit this attribute>,
                "centers": [
                    [0.5, 0.5], [1.5, 0.5], [2.5, 0.5], [3.5, 0.5],
                    [0.5, 1.5], [1.5, 1.5], [2.5, 1.5], [3.5, 1.5],
                    [0.5, 2.5], [1.5, 2.5], [2.5, 2.5], [3.5, 2.5],
                    [0.5, 3.5], [1.5, 3.5], [2.5, 3.5], [3.5, 3.5],
                ],
                "pieces": {
                    "O": {
                        "image": "dao/W.svg", "scale": 1
                    },
                    "X": {
                        "image": "dao/B.svg", "scale": 1
                    }
                }
            },
        }
    }

def get_change(variant_id):
    return {
        "defaultTheme": "basic",
        "themes": {
            "basic": {
                "backgroundGeometry": [80, 80],
                "backgroundImage": "change/graph.svg",
                "arrowThickness": 1,
                "piecesOverArrows": True,
                "centers": [
                    [70, 26], [70, 44], [70, 62],
                    [50, 17], [50, 35], [50, 53], [50, 71],
                    [30, 8], [30, 26], [30, 44], [30, 62],
                    [10, 17], [10, 35], [10, 53]
                ],
                "pieces": {
                    "o": {
                        "image": "general/red_circle.svg", "scale": 10
                    },
                    "x": {
                        "image": "general/blue_circle.svg", "scale": 10
                    }
                }
            },
        }
    }
    
def get_fivefieldkono(variant_id):
    if variant_id not in ["regular", "delta", "omega"]:
        return None
    return {
        variant_id: {
            "defaultTheme": variant_id,
            "themes": {
                variant_id: {
                    "backgroundGeometry": [
                        200, 200
                    ],
                    "backgroundImage": "fivefieldkono/board.svg",
                    "piecesOverArrows": True,
                    "arrowThickness": 5,
                    "centers": [[20 + 40 * i, 20 + 40 * j] for j in range(0,5) for i in range(0,5)],
                    "pieces": {
                        "x": {
                            # White pieces for X
                            "image": "369mm/O.svg", "scale": 25.0
                        }, "o": {
                            # Black pieces for O
                            "image": "369mm/X.svg", "scale": 25.0
                        }
                    }
                }
            }
        }
    }.get(variant_id, None)

"""
===== STEP 2 ===== 
Add your function to the autoGUIv2DataFuncs dict.
"""

autoGUIv2DataFuncs = {
    "quickcross": get_quickcross,
    "baghchal": get_baghchal,
    "3spot": get_3spot,
    "369mm": get_369mm,
    "topitop": get_topitop,
    "Lgame": get_Lgame,
    "dodgem": get_dodgem,
    "tttwo": get_tttwo,
    "stt": get_stt,
    "tootnottopy": get_tootnottopy,
    "ctoi": get_ctoi,
    "chomp": get_chomp,
    "dawsonschess": get_dawsonschess,
    "chess": get_chess,
    "snake": get_snake,
    "connect4c": get_connect4c,
    "lite3": get_lite3,
    "mutorere": get_mutorere,
    "achi": get_achi,
    "dinododgem": get_dinododgem,
    "tactix": get_tactix,
    "quickchess": get_quickchess,
    "haregame": get_haregame,
    "othello": get_othello,
    "gameofy": get_gameofy,
    "beeline": get_beeline,
    "1dchess": get_1dchess,
    "chinesechess": get_chinesechess,
    "notakto": get_notakto,
    "dao": get_dao,
    "change": get_change,
    "fivefieldkono": get_fivefieldkono
}

def get_autoguiV2Data(game_id, variant_id):
    if game_id in autoGUIv2DataFuncs:
        return autoGUIv2DataFuncs[game_id](variant_id)
    return None
