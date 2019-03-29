# <center>__Stock Market - Technical Analysis Calculator__ ![alt text](/Images/LogoFinal.png)</center>
</p> The Stock Market Technical Analysis Calculator is a GUI Application for evaluating the Technical Rating of a specific security on the major US Stock Exchanges. The Technical Analysis Calculator is completely dynamic, using real-time data and real-time technical indicators to determine whether the User should Buy, Hold, or Sell an equity stake in a specific security. In order the use the features of the Calculator, the User must input the Ticker Symbol of a specific company. After inputting the Ticker Symbol and clicking "Submit," the Calculator will provide the User with the Company Name and the Current Share Price, along with a Technical Indicator Graph. The Technical Indicator Graph will provide the User with a Chart of the Company's Share Price over Time. The Calculator will also provide the User with an analysis of the following Technical Indicators: 200-DMA, 100-DMA, 50-DMA, RSI, MACD, and VWAP.

## __The Calculator:__

Upon launching the Application, the User will be able to view the Start Page Stock Market Technical Analysis Calculator. The Main Window of the Application parses Data from the [Nasdaq Website](https://www.nasdaq.com/). The Data is constantly updated in Real-Time, providing the User with a dynamic Stock Market interface.

### User Input:

In order to use the Calculator, the User must input the Ticker Symbol of a specific company listed on a United States Stock Exchange. If the User does not know the Ticker Symbols of any companies, the "US Stock Exhanges" Section will provide the User with Tables containing the Ticker Symbols of major companies. The Tables will also provide the User with the following Data in real-time: Market Cap, P/E Ratio, Div Yield, 52-Week High, and 52-Week Low.  
</br>
![alt text](/Images/Picture_1.PNG)

### Company Name and Share Price:

After inputting the Ticker Symbol of a specific company, the GUI Application will present the User with the Technical Data of the Stock on the End Page. The End Page immediately lists the name of the company along with the current share price of the company. All Stock-Related Data is updated in real-time.
</br>

![alt text](/Images/Picture_2.PNG)

### Technical Indicator Chart:

The Technical Indicator Chart provides the User with a Graph of the Stock Price over Time. The User can switch between different Periods of Time by clicking the following Buttons: 3 Month, 6 Month, 9 Month, 1 Year, 3 Year, and 5 Year. The default setting for the Technical Analysis Calculator is "1 Year." The Technical Indicator Graph is separated into three separate plots. The Top Plot graphs the RSI of the Stock over time. The Middle Plot graphs the Price of the Stock over time. The Bottom Plot graphs the MACD of the Stock over time.
</br>

![alt text](/Images/Picture_3.PNG)

### Calculator Rating:

The Calculator Rating analyzes the Technical Indicators of the Stock Graph in order to evaluate the Technical Rating of the Security. The Technical Analysis Calculator provides the User with five different Ratings: Strong Buy, Buy, Hold, Sell, Strong Sell. The Final Rating for the Stock is calculated with a specially-designed algorithm that weighs the technical indicators in a logical and efficient way.
</br>

![alt text](/Images/Picture_4.PNG)

### Main Menu:

In order to return back to the Start Page, the User must navigate through the following Path: (Menu Bar -> File -> Main Menu). Upon returning to the Start Page, the User can enter the Ticker Symbol of a new Stock in order to view a new Technical Rating in real-time.
</br>

![alt text](/Images/Picture_5.png)

## __Technical Indicators:__

### 200-Day Moving Average:
>The 200-day moving average (200 DMA) is considered a key indicator by traders and market analysts for determining the overall long-term market trend. The price level in a market that coincides with the 200-DMA is recognized as a major support level when price is above the 200-DMA or resistance level when price is below the 200-DMA level.

### 100-Day Moving Average:
>The 100-day moving average (100 DMA) is considered a key indicator by traders and market analysts for determining the overall mid-term market trend. The price level in a market that coincides with the 100-DMA is recognized as a major support level when price is above the 100-DMA or resistance level when price is below the 100-DMA level.

### 50-Day Moving Average:
>The 50-day moving average (50 DMA) is considered a key indicator by traders and market analysts for determining the overall short-term market trend. The price level in a market that coincides with the 50-DMA is recognized as a major support level when price is above the 50-DMA or resistance level when price is below the 50-DMA level.

### Relative Strength Index:
>The relative strength index (RSI) is a momentum indicator that measures the magnitude of recent price changes to evaluate overbought or oversold conditions in the price of a stock or other asset. The RSI is displayed as an oscillator (a line graph that moves between two extremes) and can have a reading from 0 to 100. 

### Moving Average Convergence Divergence:
>Moving Average Convergence Divergence (MACD) is a trend-following momentum indicator that shows the relationship between two moving averages of a security’s price. The MACD is calculated by subtracting the 26-period Exponential Moving Average (EMA) from the 12-period EMA. The result of that calculation is the MACD line. A nine-day EMA of the MACD, called the "signal line," is then plotted on top of the MACD line, which can function as a trigger for buy and sell signals. 

### Volume Weighted Average Price:
>The volume weighted average price (VWAP) is a trading benchmark used by traders that gives the average price a security has traded at throughout the day, based on both volume and price. It is important because it provides traders with insight into both the trend and value of a security.

## __References:__
The following References played a major role in the development of the Stock Market Technical Analysis Calculator:
* [Matplotlib Graphing](https://pythonprogramming.net/advanced-matplotlib-graphing-charting-tutorial/)
* [Web Data Parsing](https://www.scrapehero.com/scrape-nasdaq-stock-market-data/)

## __Versions__:
The Stock Market Technical Analysis Calculator uses the following Python Versions:
* Python Version 2.7.15
* IEX Finance 0.4.0
* PyQt4

## __YouTube Video:__
Watch the [YouTube Video](https://www.youtube.com/watch?v=XnHujncigck&t=17s) for an explanation on how to download and use the Stock Market Technical Analysis Calculator.

## __PDF Document:__
Read the [PDF Document](https://github.com/TravisCampos/PIC10C-FinalProject/blob/master/Stock%20Market%20-%20RAII%20Guidelines.pdf) for an explanation on how Qt, PyQt, Qt Designer, and RAII Guidelines influenced the creation of the Stock Market Technical Analysis Calculator. 
