# Instance_Counter
A simple Python OOP project that automatically assigns a unique, incrementing ID to every instance of a class — useful for tracking, debugging, and managing how many objects you have created.

InstanceCounter uses a class-level counter that increments each time a new object is created. Every instance gets a unique ID that follows the order in which it was instantiated. The counter can be reset at any time via a static method.It also includes unit tests to verify correct behaviour.

## Features
- Assigns a unique, automatically incrementing ID to each instance
- Supports resetting the class-level counter to zero
- Demonstrates Object-Oriented Programming (OOP) concept Encapsulation: the counter and ID logic are bundled inside the class, hidden from outside code.
- Demonstrates the difference between class variables (shared across all objects) and instance variables(unique to each object)
- Includes unit tests using Python’s unittest framework
  
## Requirements
- Python 3.x
- No external libraries required (uses Python standard library only)

## Project Structure
```text
instance-counter/
│
├── counter.py              # Main class implementation
├── testcounter.py          # Unit tests
└── README.md               # Project documentation
```
## How It Works

Each time an InstanceCounter object is created, a class-level variable is incremented and assigned to the instance as its unique ID.

## Example Usage

```python
import counter

instance1 = counter.InstanceCounter()
instance2 = counter.InstanceCounter()

print(instance.id)  # 1
print(instance.id)  # 2

counter.InstanceCounter.reset()
instance3 = counter.InstanceCounter()
print(instance3.id)  # 1
```




# How to Run

### 1. Clone the repository

```bash
git clone https://github.com/MakhutsoPoto/Instance_Counter.git
cd instance-counter
```
### 2. Run the program

```bash
python counter.py
```

### 3. Running the Tests
```bash
python test_counter.py
```
## Technologies Used
- Python 3
- Object-Oriented Programming (OOP)
- Unit Testing (unittest)


## Learning Outcomes

This project demonstrates understanding of:
- The difference between class variables and instance variables,when to use each
- Object lifecycle in Python
- Object Oriented Programming principles:Encapsulation 
- Basic unit testing practices with Python's unittest framework
