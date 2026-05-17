# Instance_Counter
A simple Python OOP project that automatically assigns a unique, incrementing ID to every instance of a class — useful for tracking, debugging, and managing how many objects you have created.

InstanceCounter uses a class-level counter that increments each time a new object is created. Every instance gets a unique ID that follows the order in which it was instantiated. The counter can be reset at any time via a static method.It also includes unit tests to verify correct behaviour.

## Features
- Assigns a unique, automatically incrementing ID to each instance
- Supports resetting the class-level counter to zero
- Demonstrates Object-Oriented Programming (OOP) concept Encapsulation: the counter and ID logic are bundled inside the class, hidden from outside code.
- Demonstrates the difference between class variables (shared across all objects) and instance variables(unique to each object)
- Includes unit tests using Python’s unittest framework
- Supports Docker containerization  
- Includes automated Docker build and run script  

## Requirements
- Python 3.x
- Docker Desktop
- Bash-compatible terminal (Git Bash, WSL, or Linux terminal)
- No external libraries required (uses Python standard library only)

## Project Structure
```text
instance-counter/
│
├── counter.py            # Main class implementation
├── testcounter.py        # Unit tests
├── Dockerfile            # Docker container configuration
├── build.sh              # Automated Docker build and run script
├── requirements.txt      # Project requirements
└── README.md             # Project documentation            
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

## Docker Support

This project can be built and executed inside a Docker container.

### Build Docker image

```bash
docker build -t instance-counter .
```

### Run Docker container

```bash
docker run --rm instance-counter
```

---

## Build Script

The project employs shell script to automate the Docker build and execution process.

### Run build script

```bash
./build.sh
```

The script:
- builds the Docker image
- runs the container
- removes the container after execution

## Technologies Used
- Python 3
- Object-Oriented Programming (OOP)
- Unit Testing (unittest)
- Docker 
- Bash Scripting


## Learning Outcomes

This project demonstrates understanding of:
- The difference between class variables and instance variables,when to use each
- Object lifecycle in Python
- Object Oriented Programming principles:Encapsulation 
- Basic unit testing practices with Python's unittest framework
- Docker containerization fundamentals  
- Basic automation using Bash scripting  
