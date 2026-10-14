
def parse_student(line):
    line = line.strip()
    parts = line.split(",")
    if len(parts) != 2:
        raise ValueError("字段数量错误")
    name, score_str = parts
    if len(name.strip()) == 0:
        raise ValueError("姓名为空")
    score = int(score_str)
    if not (0 <= score <= 100):
        raise ValueError("成绩超出0~100范围")
    return {"name":name, "score":score}
