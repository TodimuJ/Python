'''
    Author: Todimu Jenrola
    File name: pageReplacement.py
    Date created: 12/03/2021
    Date last modified: 26/03/2021
    Python Version: 3.6
'''

def belady(frames, stream):
    frame = [None]*frames # initailize frame
    previous = []
    j = 0

    for i in range(len(stream)):
        # user_input = input("")
        # # handle user exit
        # if user_input == "":
        #     print("All done, goodbye!")
        #     break

        # handle the first time when frame is pre-populated
        if j < frames:
            # print number + NF if no page fault
            if not isFault(stream[i], frame):
                print(stream[i] + "NF")
            
            # print fault since frame is empty
            elif isFault(stream[i], frame):
                print(stream[i] + "F")
                frame[j] = stream[i] # add user input to frame

        else:
            # print number + NF if no page fault
            if not isFault(stream[i], frame):
                print(stream[i] + "NF")
            
            # obtain element to evict, insert new value
            elif isFault(stream[i], frame):
                if position(frame) < frames:
                    frame.pop(position(frame))
                    frame.insert(position(frame), stream[i])
                    print(stream[i] + "F")

                # perform cyclic shift operation
                else:
                    index = predict(frame, stream[j:])
                    evicted = frame[index]
                    frame.pop(index)
                    frame.insert(index, stream[i])
                    print(stream[i] + "F" + " E" + evicted)
        
        previous.append(stream[i])
        
        print(frame) # check frame for debugging purposes

        j += 1

    # print("This is the BELADY algorithm with {} frames.".format(frames))
    

def clock(frames):
    frame = [None]*frames
    cache = {}
    j = 0
    previous = []
    temp = 0

    while True:
        user_input = input("")
        # handle user exit
        if user_input == "":
            print("All done, goodbye!")
            break

        # handle the first time when frame is pre-populated
        if j < frames:
            # print number + NF if no page fault
            if not isFault(user_input, frame):
                cache[user_input] = 0
                print(user_input + "NF")
            
            # print fault since frame is empty
            elif isFault(user_input, frame):
                cache[user_input] = 1
                print(user_input + "F")

                temp += 1
                frame[j] = user_input # add user input to frame

        else:
            # print number + NF if no page fault
            if not isFault(user_input, frame):
                cache[user_input] = 0
                print(user_input + "NF")
            
            # obtain element to evict, insert new value
            elif isFault(user_input, frame):
                if position(frame) < frames:
                    frame.pop(position(frame))
                    frame.insert(position(frame), user_input)
                    cache[user_input] = 1
                    print(user_input + "F")

                else:
                    check = []

                    for item in frame:
                        if cache[item] == 1:
                            check.append(True)
                        else:
                            check.append(False)
                            # list(my_dict.keys())[0]
                    
                    if all(check):
                        cache = reset(cache)

                        evicted = frame[0]
                        frame.pop(0)
                        frame.insert(0, user_input)
                        cache[user_input] = 1
                        print(user_input + "F" + " E" + evicted)

                    else:
                        evicted = frame.pop(temp%frames)
                        frame.insert((temp%frames), user_input)
                        cache[user_input] = 1
                        print(user_input + "F" + " E" + str(evicted))

                temp += 1

        previous.append(user_input)
        
        print(frame) # check for debugging purposes

        j += 1

    # print("This is the CLOCK algorithm with {} frames.".format(frames))


def fifo(frames):
    frame = [None]*frames # initailize frame
    temp = 0 # variable for performing cyclic iteration
    j = 0

    while True:
        user_input = input("")
        # handle user exit
        if user_input == "":
            print("All done, goodbye!")
            break

        # handle the first time when frame is pre-populated
        if j < frames:
            # print number + NF if no page fault
            if not isFault(user_input, frame):
                print(user_input + "NF")
            
            # pop appropriate index, insert to frame and print value if page fault
            elif isFault(user_input, frame):
                evicted = frame.pop(temp%frames)
                frame.insert((temp%frames), user_input)
                print(user_input + "F")

                temp += 1
                frame[j] = user_input # add user input to frame

        else:
            # print number + NF if no page fault
            if not isFault(user_input, frame):
                print(user_input + "NF")
            
            # pop appropriate index, insert to frame and print value if page fault
            elif isFault(user_input, frame):
                if position(frame) < frames:
                    frame.pop(position(frame))
                    frame.insert(position(frame), user_input)
                    print(user_input + "F")

                else:
                    evicted = frame.pop(temp%frames)
                    frame.insert((temp%frames), user_input)
                    print(user_input + "F" + " E" + evicted)
                
                temp += 1
                
        print(frame) # check frame for debugging purposes
        
        j += 1
        
    # print("This is the FIFO algorithm with {} frames.".format(frames))


def lru(frames):
    frame = [None]*frames # initailize frame
    previous = []
    j = 0

    while True:
        user_input = input("")
        # handle user exit
        if user_input == "":
            print("All done, goodbye!")
            break

        # handle the first time when frame is pre-populated
        if j < frames:
            # print number + NF if no page fault
            if not isFault(user_input, frame):
                print(user_input + "NF")
            
            # print fault since frame is empty
            elif isFault(user_input, frame):
                print(user_input + "F")
                frame[j] = user_input # add user input to frame

        else:
            # print number + NF if no page fault
            if not isFault(user_input, frame):
                print(user_input + "NF")
            
            # obtain element to evict, insert new value
            elif isFault(user_input, frame):
                if position(frame) < frames:
                    frame.pop(position(frame))
                    frame.insert(position(frame), user_input)
                    print(user_input + "F")

                else:
                    cache = []
                    k = 1

                    # handle when least recently used position is greater then number of frames
                    while len(set(cache)) != frames:
                        cache.append(previous[-(k)])
                        k += 1

                    evicted = cache[-1]
                    index = frame.index(evicted)
                    frame.pop(index)
                    frame.insert(index, user_input)
                    print(user_input + "F" + " E" + evicted)
        
        previous.append(user_input)
        
        print(frame) # check frame for debugging purposes

        j += 1

    # print("This is the LRU algorithm with {} frames.".format(frames))
 
# method to check if frame is full
def position(frame):
    i = 0
    for entry in range(len(frame)):
        if frame[entry] == None:
            break
        i += 1

    return i 

# method to get input stream
def getStream():
    stream = []

    while True:
        user_input = input("")
        if user_input == "":
            break
        stream.append(user_input)

    return stream

# method to check if there is a fault
def isFault(frame, stream):

    return frame not in stream

# method to reset cache
def reset(cache):
    for item in cache:
        cache[item] = 0
    
    return cache

def evict(frame, cache, previous):
    evicted, index = 0, 0

    for item in frame:
        if cache[item] == 0:
            evicted = item
            index = frame.index(item)

            return evicted, index


# method to predict unused page
def predict(frame, stream):
    evicted = []
    for i in range(len(frame)):
        if frame[i] not in stream:
            return frame.index(frame[i])
                
        index = stream.index(frame[i])
        evicted.append(index)
        
    return frame.index(stream[max(evicted)])


if __name__ == "__main__":

# Example: FIFO 3, press enter and input frame entries


    while True:
        prompt = print("Input algorithm type (BELADY, CLOCK, FIFO, LRU) and number of frames: \n")
        algorithms = [belady, clock, lru, fifo]
        selection = input("")
        select = selection.split(" ")

        if selection == "":
            print("Here endeth the program!")
            break
    
        if algorithms[0].__name__ == str(select[0]).lower():
            stream = getStream()
            algorithms[0](int(select[1]), stream)

        else:
            for i in range(1,4):
                if algorithms[i].__name__ == str(select[0]).lower():
                    algorithms[i](int(select[1]))
        
        print("\n")
