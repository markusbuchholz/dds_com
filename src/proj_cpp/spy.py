import time
from cyclonedds.domain import DomainParticipant
from cyclonedds.topic import Topic
from cyclonedds.sub import DataReader
from cyclonedds.builtin import BuiltinTopicPublication

def main():
    participant = DomainParticipant()
    
    # Subscribe to the built-in discovery topic
    # This tells us whenever a NEW publisher appears on the network
    topic = Topic(participant, "DCPSPublication", BuiltinTopicPublication)
    reader = DataReader(participant, topic)
    
    print("Spying on network... (Waiting for Publisher announcements)")
    print("Note: If the C++ publisher is already running, restart it so we catch the announcement.")

    for sample in reader.take_iter():
        # We only care about your Counter topic
        if "Counter" in sample.topic_name:
            print("-" * 40)
            print(f"FOUND PUBLISHER:")
            print(f"  Topic Name: '{sample.topic_name}'")
            print(f"  Type Name:  '{sample.type_name}'")
            print("-" * 40)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass