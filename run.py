# -*- coding:utf-8 -*-
from proxypool.scheduler import Scheduler
import io
import sys



sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


def main():
    try:
        # 运行调度器
        s = Scheduler()
        s.run()
    except:
        main()


if __name__ == '__main__':
    main()
