.PHONY: all clean

CC = gcc
COMPILE_FLAGS = -g -O0 -fno-stack-protector -no-pie # -m32
    # -g: 默认级别的调试信息
    # -O0: 不优化代码
    # -fno-stack-protector: 禁用栈保护（例如 canaries）
    # -no-pie: 禁用位置独立执行 - 禁用相对地址
    # -m32: 以 32 位程序编译

# 各目标文件的列表
TARGETS = adminOverflow betterAdmin tweetTweet itsAlive usingFgets RCE system

# 默认目标
all: $(TARGETS)

# 针对 Apple 环境的目标
apple: $(addsuffix _apple, $(TARGETS))

# 使用模式规则定义通用编译命令
%: %.c
	$(CC) $(COMPILE_FLAGS) -m32 -o ./challenge $<

# 针对 Apple 环境编译目标
%_apple: %.c
	$(CC) $(COMPILE_FLAGS) -o ./challenge $<

# 清理
clean:
	rm -rf ./challenge ./challenge.dSYM