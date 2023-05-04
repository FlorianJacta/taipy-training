This code comes from a Taipy project. A lot of small details can be changed to make it better using Taipy GUI an Core at its full potential.

https://github.com/cornelliusyudhawijaya/Taipy_Project/pull/1

-----

# Example of modifications

https://github.com/cornelliusyudhawijaya/Taipy_Project/pull/1

The goal is to use Taipy Core as its fullest. Taipy Core wil handle all your stocks, all your information with automatic storage for your models but also predcitions and so on. I let you see the code by yourself.

Now, scenarios represent a stock and every information should be retrieve from the scenario.

# Configuration:
- A new task to predict
- A new Data node to receive the predictions
- The TOML file is the one being used for Configuration
- The Configuration code can also be found 
- Put all tasks as skippable

# Functions:
- Some changes in the implementation of the clean data function

# test.py
- Another way to retrieve stock info to have more data and better predictions (data from 2015 to today)
- Add `on_init()` function to initialize the application and create 3 scenarios for the 3 stocks (clean, train and predict are done for each one)
- Define different paths to the CSV depending on the scenario to separate it
- Don't use predefined models but models from Taipy with the read() method.

# Markdown in *test.py*
- the selector on the page chooses which scenario/stock to visualize and update the charts accordingly using the Data nodes of the scenario
- Delete unnecessary parts (in layout)
- Add a button 'Reset' to avoid having it in the selector
- Use Python expression for text