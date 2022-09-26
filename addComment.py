import os

base_path = r"C:\Users\大橘\Desktop\dto"
filenames = os.listdir(base_path)


# 查看时候已经写好注释
def exit_api_common(abs_file_path):
    with open(abs_file_path, 'r', encoding="utf-8") as f:
        annotations = ['ApiModelProperty']
        for line in f:
            for annotation in annotations:
                if annotation in line:
                    return True
    return False


def read_common_data(abs_file_path):
    with open(abs_file_path, 'r', encoding="utf-8") as f:

        line_num = 0
        data = []
        next_line_is_comment = False
        next_line_insert_comment = False
        is_bean_code = False

        for line in f:
            data.append(line)
            if line.find("@Data") != -1:
                is_bean_code = True
                continue
            if is_bean_code:
                # 再bean中找到注释开始位置,下一行就是注释内容
                if line.find("/**") != -1:
                    next_line_is_comment = True
                    continue

                # 提取注释内容
                if next_line_is_comment:
                    line = line.strip()
                    index = line.index("* ")
                    comment = line[index + 2:]
                    next_line_is_comment = False
                    next_line_insert_comment = True
                    continue

                if next_line_insert_comment:
                    # 记录要插入数据的位置
                    insert_index = len(data) - 1

                    # 执行注释插入
                    insert_comment = "    @ApiModelProperty(value = \"%s\")" % comment
                    new_line = line.replace(line, line + insert_comment + "\n")
                    data[insert_index] = new_line
                    next_line_insert_comment = False
                    continue

                line_num += 1

        return data


def write_common_data(abs_file_path, data):
    with open(abs_file_path, "w", encoding="utf-8") as f:
        f.writelines(data)


for filename in filenames:
    abs_file_path = os.path.join(base_path, filename)
    if filename.endswith(".java"):
        if not exit_api_common(abs_file_path):
            data = read_common_data(abs_file_path)
            write_common_data(abs_file_path, data)
            print(f"write {filename} ok !")
