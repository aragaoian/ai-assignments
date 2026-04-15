CLASS_MAP = {
    0: "BARBUNYA",
    1: "BOMBAY",
    2: "CALI",
    3: "DERMASON",
    4: "HOROZ",
    5: "SEKER",
    6: "SIRA",
}


def select_class_name(pred_index: int) -> str:
    return CLASS_MAP[pred_index]
