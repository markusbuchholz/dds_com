#!/usr/bin/env python3
import time, sys
# Make the generated Python package importable
sys.path.insert(0, "./gen_py")

from gen_py import demo  # produced by: idlc -l py hello.idl
from cyclonedds.domain import DomainParticipant
from cyclonedds.topic import Topic
from cyclonedds.sub import Subscriber, DataReader
from cyclonedds.qos import Reliability, ReliabilityPolicy
from cyclonedds.core import Qos

def main():
    dp = DomainParticipant()  # domain 0
    topic = Topic(dp, "demo/Hello", demo.Hello)
    qos = Qos(Reliability(ReliabilityPolicy.Reliable, max_blocking_time=5.0))
    sub = Subscriber(dp)
    reader = DataReader(sub, topic, qos)

    print("[Py ] Waiting for samples on 'demo/Hello' ...")
    received = 0
    while received < 10:
        for data, info in reader.take(10):
            if info.valid_data:
                print(f"[Py ] Received: {data.msg}")
                received += 1
        time.sleep(0.1)

if __name__ == "__main__":
    main()
