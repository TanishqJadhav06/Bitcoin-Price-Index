Bitcoin Price Index

A Python program that calculates the current cost of a specified number of Bitcoins in USD using real-time market data from the CoinCap API.

The program:

Accepts the number of Bitcoins as a command-line argument using sys.argv
Retrieves the latest Bitcoin price from the CoinCap API using the requests library
Parses JSON data returned by the API
Handles invalid or missing user input with exception handling
Calculates the total value of the requested Bitcoins
Formats the output with commas and four decimal places for readability
Concepts Used
Python Libraries
requests
APIs
JSON Parsing
Dictionaries
Command-Line Arguments (sys.argv)
Exception Handling (try / except)
Data Type Conversion
String Formatting

Example
python bitcoin.py 2.5

Output:
Price of 2.5 bitcoins is $167,135.0250

What I Learned

Through this project, I learned how to work with real-world APIs, process JSON data, use command-line arguments, handle errors gracefully, and build programs that interact with live internet data.
