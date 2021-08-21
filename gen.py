import os


def write_file_index(path, filename, base_path):
    """
    将文件写入目录
    """
    space = "  " * (len(path.split("/")) - len(base_path.split("/")) + 1)
    line = "{}- [{}]({}/{})\n".format(
        space, filename.split(".md")[0], path, filename
    ).replace("docs/", "")
    with open(f"{base_path}/_sidebar.md", "a+") as f:
        f.write(line)


def write_dir_index(path, filename, base_path):
    """
    将文件夹写入目录
    """
    space = "  " * (len(path.split("/")) - 1)
    dirname = path.split("/")[-1]
    line = "{}- [{}]({}/{})\n".format(space, dirname, path, "README.md").replace(
        "docs/", ""
    )
    with open(f"{base_path}/_sidebar.md", "a+") as f:
        f.write(line)


def is_in_ingnore_dirs(path):
    """
    是否包含忽略的文件夹,如果包含则返回 True
    """
    for dirname in ingnore_dirs:
        if path.find(f"docs/{dirname}") != -1:
            return True
    return False


def gen_index(start_path):
    """
    自动化生成博客目录
    """
    base_path = start_path
    current_path = start_path
    if os.path.exists(f"{current_path}/_sidebar.md"):
        os.remove(f"{current_path}/_sidebar.md")
    for path, dir_list, file_list in os.walk(current_path):
        file_list.sort(key=lambda parameter_list: parameter_list[0:1])
        for filename in file_list:
            if (
                filename.endswith(".md")
                and not filename.startswith("_")
                and filename not in ("README.md")
                and not is_in_ingnore_dirs(path)
            ):
                if current_path != path:  # 当进入了新的文件夹路径
                    # 1. 把dirname名称作为目录名称
                    write_dir_index(path, filename, base_path)
                    # 2. 写 第一个 filename
                    write_file_index(path, filename, base_path)
                    current_path = path
                else:
                    # 写 其他的 filename
                    write_file_index(path, filename, base_path)


def get_dirs():
    """
    获得要gen的目录
    """
    dirs = []
    for path, dir_list, file_list in os.walk("docs"):
        if path.find("_") == -1 and path != "docs":
            dirs.append(path)
    return dirs


if __name__ == "__main__":
    ingnore_dirs = ["weidian"]
    gen_index("docs")
    ingnore_dirs = []
    dirs = get_dirs()
    for start_path in get_dirs():
        gen_index(start_path)
