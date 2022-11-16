'''
Elevator system

'''


class Elevator:
    
    def __init__(self, list_buttons, curr_loc, story):
        self.buttons = list_buttons
        self.curr_loc = curr_loc
        self.story = story
        
    def serve(self):
        
        temp = self.buttons.copy()
        
            
        def quick_sort(sequence):
            length = len(sequence)
            if length <= 1:
                return sequence
            else:
                pivot = sequence.pop()

            items_greater = []
            items_lower = []

            for item in sequence:
                if item >= pivot:
                    items_greater.append(item)
                else:
                    items_lower.append(item)
            return quick_sort(items_lower) + [pivot] + quick_sort(items_greater)
            
        def decide_direction(self):
            self.buttons = quick_sort(self.buttons)
            
            def find_pos(lis, num):
                if num < lis[0]:
                    return 0
                for i in range (len(lis) - 1):
                    if lis[i] < self.curr_loc and num < lis[i+1]:
                        position = i + 1
                        break
                else:
                    position = len(lis)
                return position

            position = find_pos(self.buttons, self.curr_loc)
            self.buttons.append(None)
            i = len(self.buttons) - 1
            while i >= position:
                self.buttons[i] = self.buttons[i-1]
                i = i - 1
            self.buttons[position] = self.curr_loc
            
            index = position
            
            if index < len(self.buttons) - 1 and index != 0: 
                flag_1 = abs(self.buttons[index - 1] - self.curr_loc)
                flag_2 = abs(self.buttons[index + 1] - self.curr_loc)
                
                if flag_1 <= flag_2:
                    delta = -1
                else: delta = 1
            elif index == len(self.buttons) - 1:
                delta = -1
            else: delta = 1
            
            if delta == 1:
                direction = "upward"
            else: direction = "downward"
            
            return direction 
        
        direction = decide_direction(self)
        cur_track, serve_count, distance = 0, 0, 0
        downward = []
        upward = []
        serve_sequence = []
        size = len(temp)
        
        
        if (direction == "downward"):
            downward.append(0)
        elif (direction == "upward"):
            upward.append(self.story - 1)
     
        for i in range(size):
            if (temp[i] < self.curr_loc):
                downward.append(temp[i])
            if (temp[i] > self.curr_loc):
                upward.append(temp[i])
            
        downward = quick_sort(downward)
        upward = quick_sort(upward)
        
        run = 2
        while (run != 0):
            if (direction == "downward"):
                for i in range(len(downward) - 1, -1, -1):
                    cur_track = downward[i]
                    serve_sequence.append(cur_track)
     
                    distance = abs(cur_track - self.curr_loc)
                    serve_count += distance

                    self.curr_loc = cur_track
                 
                direction = "upward"
         
            elif (direction == "upward"):
                for i in range(len(upward)):
                    cur_track = upward[i]
                    serve_sequence.append(cur_track)
                    distance = abs(cur_track - self.curr_loc)
                    serve_count += distance
     
                    self.curr_loc = cur_track
                 
                direction = "downward"
             
            run -= 1
     
        print("The total number of floor traversals is: ",
              serve_count)
     
        print("The Lift's Serving Sequence is:")
     
        for i in range(len(serve_sequence)):
            print("     "*3, "|> Floor ", serve_sequence[i])
        print("The current location of the Lift is at floor: ", self.curr_loc)
        

def main(): 
    List = input("Enter the list(separated by comma) of pressed buttons requesting the lift (e.g. 10,15,4): \n =>")
    List = List.split(',')
    List = list(map(int, List))
    current_location = int(input("Enter the current location(floor) of the Lift: "))
    if current_location in List: 
        raise Exception("The current location(floor level) shoudn't be in the request list")
    N_story = int(input("Enter the total number of floors(story) of the building: "))
    if N_story < max(List):
        raise Exception("The request list contains floors that are out of bound of the building")
    print()
    Elevator(List, current_location, N_story).serve()


if __name__=='__main__':
    main()







        
        
        
