CXX = g++
CXXFLAGS = -std=c++20 -Wall -Wextra -O2
TARGET = bwtsearch
SRCS = main.cpp
HEADERS = index.h support.h occ.h bwt.h
OBJS = $(SRCS:.cpp=.o)

all: $(TARGET)
$(TARGET): $(OBJS)
	$(CXX) $(CXXFLAGS) -o $(TARGET) $(OBJS)

%.o: %.cpp $(HEADERS)
	$(CXX) $(CXXFLAGS) -c $< -o $@

clean:
	rm -f $(TARGET) $(OBJS)

.PHONY: all clean