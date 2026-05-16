# Instance_Counter
A simple Python OOP project that automatically assigns a unique, incrementing ID to every instance of a class — useful for tracking, debugging, and managing how many objects you have created.

InstanceCounter uses a class-level counter that increments each time a new object is created. Every instance gets a unique ID that follows the order in which it was instantiated. The counter can be reset at any time via a static method.It also includes unit tests to verify correct behaviour.

## Features
- Assigns a unique, automatically incrementing ID to each instance
- Supports resetting the class-level counter to zero
- Demonstrates Object-Oriented Programming (OOP) concept Encapsulation: the counter and ID logic are bundled inside the class, hidden from outside code.
- Demonstrates the difference between class variables (shared across all objects) and instance variables(unique to each object)
- Includes unit tests using Python’s unittest framework

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

obj1 = counter.InstanceCounter()
obj2 = counter.InstanceCounter()

print(obj1.id)  # 1
print(obj2.id)  # 2

counter.InstanceCounter.reset()

obj3 = counter.InstanceCounter()
print(obj3.id)  # 1

# How to Run

### 1. Clone the repository
```bash
git clone https://github.com/your-username/instance-counter.git
cd instance-counter

###2.Run the program
```bash
python counter.py

