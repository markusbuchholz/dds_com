FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive

# 1. Install all build dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    cmake \
    pkg-config \
    python3 \
    python3-pip \
    python3-dev \
    git \
    libssl-dev \
    wget \
    && rm -rf /var/lib/apt/lists/*

RUN apt-get update && apt-get install -y python3-pip && rm -rf /var/lib/apt/lists/*

RUN pip install cyclonedds

# Set a directory for building
WORKDIR /tmp/build

# 2. Build and install the CycloneDDS C/C++ library
RUN git clone https://github.com/eclipse-cyclonedds/cyclonedds.git && \
    cd cyclonedds && \
    mkdir build && \
    cd build && \
    cmake .. && \
    make && \
    make install



# 4. Clean up the build files to save space
RUN rm -rf /tmp/build

# 5. Set the final working directory for your projects
WORKDIR /workspace

CMD ["bash"]