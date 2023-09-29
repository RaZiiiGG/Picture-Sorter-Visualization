<h1 align="center"> 
Picture Sorter Visualization 📶
</h1>
<p align="center"> 
  <img src="gif/logo.png">
</p>
<h2>
  📝 About the project
</h2>
<p>
  This project is a visualization of five different sorting algorithms using different pictures of nature. It shows how five different sorting methods (<b>Bubble Sort</b>, <b>Insertion Sort</b>, <b>Selection Sort</b>, <b>Heap Sort</b>, and <b>Quick Sort</b>) work using pictures. Although this is a more fun way of visualizing sorting algorithms, it is not the best visualization method when it comes to learning. It features 10 pictures of nature that can be sorted by pressing buttons with a desired sorting algorithm.
</p>
<h2>
  🎥 Demo
</h2> 
<p align="center">
  <img src="gif/demoBubbleSort.gif">
</p>
<h2>
  🔑 How it works
</h2>
<p>
  The project is written in Python using pygame library. Firstly, a random image is loaded. In order to cut the image into the bars, function <b>pygame.Surface.blit()</b> is used. Each image is 1100 pixels wide and split into bars that are 2 pixels wide. In order to use the sorting algorithms, first we need a list of numbers. In this case we store starting position of each bar in a list. This way we can easily sort the starting positions of each bar and visualize the process.
</p>
<h2>
  📖 Getting Started
</h2>
<p>
  Requirements: Python and pygame (Python package)
</p>
<p>
  In order to start the program, you have to download the File <b>Picture Sorter Visualization</b>. It is very important that the following files are all in the same directory: <b>main.py</b>, <b>Pictures</b> and <b>Fonts</b>. The easiest method is just to download the File <b>Picture Sorter Visualization</b>.
</p>
<h2>
  🔨 How to use
</h2>
<p>
  After executing the program you will see a window with random unsorted picture of a nature. In order to see the sorting visualization process, you need to press a button selecting your desired sorting algorithm. After that all you need to do is press the button 'Sort' and the sorting process will start. During the sorting process you can not pause it and you need to wait until the end of the process. After that you may reset the image or you can select next random picture of nature to sort.
</p>
<h2>
  📜 Credits
</h2>

In order to get a general idea of how to visualize sorting algorithms in Python I have watched video tutorials from [Tech with Tim](https://www.youtube.com/@TechWithTim). With the help of [Clear Code](https://www.youtube.com/@ClearCode) I have managed to implement animated buttons.

<h2>
  📄 License
</h2>

```
MIT License

Copyright (c) [2023] [Walther Trgovac]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
