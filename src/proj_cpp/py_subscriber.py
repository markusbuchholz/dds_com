import time
from dataclasses import dataclass
from cyclonedds.domain import DomainParticipant
from cyclonedds.topic import Topic
from cyclonedds.sub import DataReader
from cyclonedds.idl import IdlStruct
from cyclonedds.idl.types import int32

# --- CONFIRMED CONFIGURATION ---
# Matches 'grep' output from your C++ source
@dataclass
class Counter(IdlStruct, typename="demo::Counter"):
    value: int32

def main():
    participant = DomainParticipant()
    topic = Topic(participant, "demo/Counter", Counter)
    reader = DataReader(participant, topic)

    print(f"-------------------------------------------------")
    print(f"[SUB] Topic:    'demo/Counter'")
    print(f"[SUB] TypeName: 'demo::Counter'")
    print(f"[SUB] Status:   Listening for C++ data...")
    print(f"-------------------------------------------------")

    # Simple, robust loop. No experimental attributes.
    for sample in reader.take_iter():
        print(f"✅ [RECEIVED] Value: {sample.value}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Stopping...")