import pygame
import random
import sys

# Button class
# Button class consists of 2 rectangles, top and bottom, respectively
# With the help of these 2 rectangles an animation is created, by lowering
# the elevation of the top rectangle when clicking on the button
class Button:
    # Constructor for the Button class
    def __init__(self,text,width,height, pos, elevation, fontSize=30):
        self.pressed = False
        self.elevation = elevation
        self.dynamic_elevation = elevation
        self.original_y_pos = pos[1]

        # Top rectangle
        self.top_rect = pygame.Rect(pos, (width,height))
        self.top_color = (213,213,217)

        # Bottom rectangle
        self.bottom_rect = pygame.Rect(pos, (width,height))
        self.bottom_color = (70,70,70)

        # Text
        self.text_surf = pygame.font.Font('Fonts\JetBrainsMonoNL-Light.ttf', fontSize).render(text, True, '#0F1111')
        self.text_rect = self.text_surf.get_rect(center = self.top_rect.center)

    # Drawing the button
    def draw(self):
        # Elevation logic
        self.top_rect.y = self.original_y_pos - self.dynamic_elevation
        self.text_rect.center = self.top_rect.center

        self.bottom_rect.midtop = self.top_rect.midtop
        self.bottom_rect.height = self.top_rect.height + self.dynamic_elevation

        pygame.draw.rect(game.screen, self.bottom_color, self.bottom_rect, border_radius = 7)
        pygame.draw.rect(game.screen, self.top_color, self.top_rect, border_radius= 7)
        game.screen.blit(self.text_surf, self.text_rect)
        self.check_click()

    # Click logic
    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()
        # The next lines make sure that the button is pressed only once and
        # the following code is run only once
        if self.top_rect.collidepoint(mouse_pos):
            self.top_color = (199,199,203)
            if pygame.mouse.get_pressed()[0] and self.pressed == False:
                self.dynamic_elevation = 0
                self.pressed = True
        else:
            self.top_color = (213,213,217)
        
        if pygame.mouse.get_pressed()[0] == False:
            self.dynamic_elevation = self.elevation
            self.pressed = False


class Game:
    # Constructor for the screen and all the drawing
    def __init__(self):
        pygame.init()
        pygame.font.init()
        self.screen = pygame.display.set_mode((1280, 720))
        self.screen.fill((250,250,250))
        pygame.display.set_caption("Picture Sorter Visualization")
        
        self.clock = pygame.time.Clock()    
        
        self.img = pygame.image.load('Pictures\picture{}.png'.format(random.randint(1, 10)))
        self.listOfBarSizes = []
        self.create_a_list(self.listOfBarSizes)

    # create_a_list creates a list of starting positions of each image
    # Each bar of the image is 2 pixels wide
    def create_a_list(self, lst):
        size = 0
        for i in range(550):
            lst.append(90+size)
            size+=2
        random.shuffle(self.listOfBarSizes)

    # draw_list draws the image on the screen with the help of the previously
    # created list using starting positions of the image
    def draw_list(self):
        size = 0
        for k in range(550):
            self.screen.blit(self.img, [self.listOfBarSizes[k], 200], [size, 0, 2, 500])
            size+=2


    # draw_sorting_process_text draws the text "Sorting..." above the image
    # with the help of class Button and modulo operation
    # Time is tracked each frame and because there are 4 buttons modulo 4 operation
    # is used in order to make a circular drawing process of these 4 buttons
    def draw_sorting_process_text(self):
        pygame.draw.rect(self.screen, (250,250,250), pygame.Rect(0,0,1280,200))
        sortText1 = Button("Sorting", 900, 100, (190,30), 0, 70)
        sortText2 = Button("Sorting.", 900, 100, (190,30), 0, 70)
        sortText3 = Button("Sorting..", 900, 100, (190,30), 0, 70)
        sortText4 = Button("Sorting...", 900, 100, (190,30), 0, 70)
        counter = pygame.time.get_ticks()//1000
        if counter % 4 == 0:
            sortText1.draw()
        elif counter % 4 == 1:
            sortText2.draw()
        elif counter % 4 == 2:
            sortText3.draw()
        elif counter % 4 == 3:
            sortText4.draw()

    # draw_sorting_process is used in every sorting algorithm and is reponsible
    # for the drawing of the sorting process
    def draw_sorting_process(self):
        self.draw_list()
        self.draw_sorting_process_text()
        pygame.event.pump()
        pygame.display.update()
    

    # Here start all the sorting algorithms
    # Bubble sort
    def bubble_sort(self):
        lst = self.listOfBarSizes
        
        for i in range(len(lst) - 1):
            for j in range(len(lst) - 1 - i):
                num1 = lst[j]
                num2 = lst[j+1]

            if num1 > num2:
                lst[j], lst[j+1] = lst[j+1], lst[j]
        
        self.draw_list()

    # Insertion sort
    def insertion_sort(self):
        lst = self.listOfBarSizes

        for i in range(1, len(lst)):
            key = lst[i]
            j = i-1
            while j >= 0 and key < lst[j]:
                lst[j+1] = lst[j]
                j -= 1
            lst[j+1] = key
            self.draw_sorting_process()

    # Selection sort
    def selectionSort(self, array, size):
        for i in range(size):
            min_index = i  
            for j in range(i + 1, size):
                if array[j] < array[min_index]:
                    min_index = j
            (array[i], array[min_index]) = (array[min_index], array[i])
            self.draw_sorting_process()

    # Helper function heapify for Heap sort
    def heapify(self, arr, n, i):
        largest = i  
        l = 2*i+1
        r = 2*i+2

        if l < n and arr[i] < arr[l]:
            largest = l
        
        if r < n and arr[largest] < arr[r]:
            largest = r
        
        if r < n and arr[largest] < arr[r]:
            largest = r
        
        if largest != i:
            (arr[i], arr[largest]) = (arr[largest], arr[i])
            self.heapify(arr, n, largest)
    
    # Heap sort
    def heapSort(self, arr):
        n = len(arr)

        for i in range(n//2 - 1, -1, -1):
            self.heapify(arr, n, i)
            self.draw_sorting_process()
        
        for i in range(n-1, 0, -1):
            (arr[i], arr[0]) = (arr[0], arr[i])
            self.heapify(arr, i, 0)
            self.draw_sorting_process()

    # Helper function partition for Quick sort
    def partition(self, array, low, high):
        pivot = array[high]
        i = low - 1
        
        for j in range(low, high):
            if array[j] <= pivot:
                i=i+1
                (array[i], array[j]) = (array[j], array[i])
        (array[i+1], array[high]) = (array[high], array[i+1])
        
        return i+1
    
    # Quick sort
    def quickSort(self, array, low, high):
        if low < high:
            pi = self.partition(array, low, high)
            self.quickSort(array, low, pi-1)
            self.quickSort(array, pi+1, high)
            self.draw_sorting_process()


    # Run function that draws everything and is responsible for all the events
    def run(self):    
        #Buttons Sort, Reset, Change Picture, Bubble Sort, Insertion Sort
        buttons = [Button('Sort', 200, 40, (300, 30), 5, 21),
                   Button('Reset', 200, 40, (540, 30), 5, 21),
                   Button('Change Picture', 200, 40, (780, 30), 5, 21),
                   Button('Bubble Sort', 200, 40, (40, 120), 5, 21),
                   Button('Insertion Sort', 200, 40, (290, 120), 5, 21),
                   Button('Selection Sort', 200, 40, (540, 120), 5, 21),
                   Button('Heap Sort', 200, 40, (790, 120), 5, 21),
                   Button('Quick Sort', 200, 40, (1040, 120), 5, 21)]
        
        sortingAlg = None

        while True:
            # Drawing white background behind the buttons, each button and the image itself
            pygame.draw.rect(self.screen, (250,250,250), pygame.Rect(0,0,1280,200))
            for button in buttons:
                button.draw()
            self.draw_list()
            
            pygame.display.update()
            self.clock.tick(60)
            
            # Catching all the events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit(0)
                
                elif event.type == pygame.MOUSEBUTTONUP:
                    #Sort Button is being pressed
                    if buttons[0].pressed and sortingAlg == self.bubble_sort:
                        while True:
                            if (self.listOfBarSizes == sorted(self.listOfBarSizes)):
                                break
                            else:
                                self.draw_sorting_process_text()
                                sortingAlg()
                                pygame.event.pump()
                                pygame.display.update()
                        
                    
                    if buttons[0].pressed and sortingAlg == self.insertion_sort:
                        if (self.listOfBarSizes != sorted(self.listOfBarSizes)):
                            sortingAlg()
                    
                    if buttons[0].pressed and sortingAlg == self.selectionSort:
                        if (self.listOfBarSizes != sorted(self.listOfBarSizes)):
                            sortingAlg(self.listOfBarSizes, len(self.listOfBarSizes))
                    
                    if buttons[0].pressed and sortingAlg == self.heapSort:
                       if (self.listOfBarSizes != sorted(self.listOfBarSizes)):
                            sortingAlg(self.listOfBarSizes)
                        
                    if buttons[0].pressed and sortingAlg == self.quickSort:
                        if (self.listOfBarSizes != sorted(self.listOfBarSizes)):
                            sortingAlg(self.listOfBarSizes, 0, len(self.listOfBarSizes)-1)
                            
                    #Reset Button is being pressed
                    if buttons[1].pressed:
                        random.shuffle(self.listOfBarSizes)
                        self.draw_list()
                    
                    #Change Picture Button is being pressed
                    if buttons[2].pressed:
                        random.shuffle(self.listOfBarSizes)
                        self.img = pygame.image.load('Pictures\picture{}.png'.format(random.randint(1, 10)))  
                        self.draw_list() 
                    
                    #Buttons for changing sorting algorithm
                    #Bubble Sort Button
                    if buttons[3].pressed:
                        sortingAlg = self.bubble_sort
                        for button in buttons:
                            button.elevation = 5
                        buttons[3].elevation = 0

                    #Insertion Sort Button
                    if buttons[4].pressed:
                        sortingAlg = self.insertion_sort
                        for button in buttons:
                            button.elevation = 5
                        buttons[4].elevation = 0

                    #Merge Sort Button
                    if buttons[5].pressed:
                        sortingAlg = self.selectionSort
                        for button in buttons:
                            button.elevation = 5
                        buttons[5].elevation = 0

                    #Heap Sort Button
                    if buttons[6].pressed:
                        sortingAlg = self.heapSort
                        for button in buttons:
                            button.elevation = 5
                        buttons[6].elevation = 0
                    
                    #Quick Sort Button
                    if buttons[7].pressed:
                        sortingAlg = self.quickSort
                        for button in buttons:
                            button.elevation = 5
                        buttons[7].elevation = 0

game = Game()
game.run()