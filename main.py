def main():
    pass


if __name__ == '__main__':
    try:
        main()
    except SystemExit:
        pass
    except:
        traceback.print_exc()
        with open(".\\except.txt", 'a') as txt:
            txt.write(time.asctime(time.localtime(time.time())) + '\n' + traceback.format_exc() + '\n')
        pygame.quit()
        print("出现bug，按下任意键退出。" + "\n" + "请打开游戏文件夹下面的except.txt文件，并将其发送给游戏制作者。")
        input()
