import sys

class Fib():

    def __init__(self,chars,wordwise=True):
        if wordwise:
            self.chars = chars.split()
        else:
            self.chars = chars
        self.current_fib = 0
        self.next_fib = 1
    
    def _increment_ptr(self):
        self.ptr +=1
    
    def _increment_fib(self):
        temp = self.current_fib + self.next_fib
        self.current_fib = self.next_fib
        self.next_fib = temp
    
    def fibo_read(self):
        while self.current_fib < (len(self.chars) -2):
            print(self.chars[self.current_fib])
            self._increment_fib()

if __name__ == "__main__":
    print(sys.argv)
    with open(sys.argv[1], "r") as file:
        program = file.read()
        print(program)
        fibonacci = Fib(program,wordwise=True) 
        fibonacci.fibo_read()   

