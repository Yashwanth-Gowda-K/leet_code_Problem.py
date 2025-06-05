class Logger:
    def __init__(self):

        self.message_timestamps = {}  

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
      # Case 1: Message has never seen
      if message not in message_timestamps:
        self.message_timestamps[messge] = timestamp
        return True


      # Case 2: Message has been seen before 
      else:
        time = timestame - self.message_timestamps[message]

        if time >= 10:
          self.message_timestamps[message] = timestamp
          return True

        else:
          return False
