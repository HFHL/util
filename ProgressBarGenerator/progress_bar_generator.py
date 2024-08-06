
def generate_progress_bar_1(total_pages, current_page, bar_length=30):
    # 样式1：基本字符样式
    # 示例: [#######---------------------] 25.00%
    progress = current_page / total_pages
    block = int(round(bar_length * progress))
    progress_bar = f"[{'#' * block}{'-' * (bar_length - block)}] {progress * 100:.2f}%"
    return progress_bar

def generate_progress_bar_2(total_pages, current_page, bar_length=30):
    # 样式2：进度块样式
    # 示例: [███████░░░░░░░░░░░░░░░░░░░] 25.00%
    progress = current_page / total_pages
    block = int(round(bar_length * progress))
    progress_bar = f"[{'█' * block}{'░' * (bar_length - block)}] {progress * 100:.2f}%"
    return progress_bar

def generate_progress_bar_3(total_pages, current_page, bar_length=30):
    # 样式3：带有箭头的样式
    # 示例: [>>>>>>>...................] 25.00%
    progress = current_page / total_pages
    block = int(round(bar_length * progress))
    progress_bar = f"[{'>' * block}{'.' * (bar_length - block)}] {progress * 100:.2f}%"
    return progress_bar

def generate_progress_bar_4(total_pages, current_page, bar_length=10):
    # 样式4：使用Emoji的样式
    # 示例: [📗📗📗📗📗📗📗📖📖📖] 25.00%
    progress = current_page / total_pages
    block = int(round(bar_length * progress))
    progress_bar = f"[{'📗' * block}{'📖' * (bar_length - block)}] {progress * 100:.2f}%"
    return progress_bar

def generate_progress_bar_5(total_pages, current_page, bar_length=10):
    # 样式5：彩虹Emoji样式
    # 示例: [🌈🌈🌈🌈🌈🌈🌈☁️☁️☁️] 25.00%
    progress = current_page / total_pages
    block = int(round(bar_length * progress))
    progress_bar = f"[{'🌈' * block}{'☁️' * (bar_length - block)}] {progress * 100:.2f}%"
    return progress_bar

def main():
    # 输入总页数和当前页数
    total_pages = int(input("请输入全书总页数: "))
    current_page = int(input("请输入当前页数: "))

    # 提供样式选项
    print("请选择进度条样式:")
    print("1. 基本字符样式")
    print("2. 进度块样式")
    print("3. 带有箭头的样式")
    print("4. 使用Emoji的样式")
    print("5. 彩虹Emoji样式")
    
    style_choice = int(input("请输入样式编号 (1-5): "))

    # 根据选择生成进度条
    if style_choice == 1:
        progress_bar = generate_progress_bar_1(total_pages, current_page)
    elif style_choice == 2:
        progress_bar = generate_progress_bar_2(total_pages, current_page)
    elif style_choice == 3:
        progress_bar = generate_progress_bar_3(total_pages, current_page)
    elif style_choice == 4:
        progress_bar = generate_progress_bar_4(total_pages, current_page)
    elif style_choice == 5:
        progress_bar = generate_progress_bar_5(total_pages, current_page)
    else:
        print("无效的选择，请选择 1-5 之间的数字。")
        return

    # 输出进度条
    print("在Markdown中插入以下代码以显示进度条：")
    print(f"```markdown\n{progress_bar}\n```")

if __name__ == "__main__":
    main()
