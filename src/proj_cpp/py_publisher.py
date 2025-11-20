import time
from dataclasses import dataclass
from cyclonedds.domain import DomainParticipant
from cyclonedds.topic import Topic
from cyclonedds.pub import DataWriter
from cyclonedds.idl import IdlStruct
from cyclonedds.idl.types import int32

# --- IDL DEFINITION ---
# typename must be "demo::Counter" to match the C++ compiler output
@dataclass
class Counter(IdlStruct, typename="demo::Counter"):
    value: int32

def main():
    participant = DomainParticipant()
    topic = Topic(participant, "demo/Counter", Counter)
    writer = DataWriter(participant, topic)
    
    print("[PUB] Sending data...")
    
    count = 0
    while True:
        # We create the sample
        sample = Counter(value=count)
        
        writer.write(sample)
        print(f"[PUB] Sent: {count}")
        
        count += 1
        time.sleep(1)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Stopping...")